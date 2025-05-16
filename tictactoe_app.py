import streamlit as st
from PIL import Image

def ij_to_num(i, j):
    return ((i * 3 + j) + 1)

def num_to_ij(num):
    return (num - 1) // 3, (num - 1) % 3

def auswerten(felder):
    win = [[1,2,3],[4,5,6],[7,8,9],
           [1,4,7],[2,5,8],[3,6,9],
           [1,5,9],[3,5,7]]
    for kombi in win:
        if set(kombi).issubset(felder):
            return kombi
    return None

def bewertung(x, o):
    if auswerten(x):
        return -1
    elif auswerten(o):
        return 1
    return 0

def minimax(x, o, frei, ist_max):
    score = bewertung(x, o)
    if score != 0 or not frei:
        return score
    if ist_max:
        return max(minimax(x, o+[f], [z for z in frei if z != f], False) for f in frei)
    else:
        return min(minimax(x+[f], o, [z for z in frei if z != f], True) for f in frei)

def comp_setzen():
    beste_score = -float("inf")
    bester_zug = None
    for feld in st.session_state["freie"]:
        score = minimax(
            st.session_state["x"],
            st.session_state["o"] + [feld],
            [f for f in st.session_state["freie"] if f != feld],
            False
        )
        if score > beste_score:
            beste_score = score
            bester_zug = feld
    if bester_zug:
        st.session_state["o"].append(bester_zug)
        st.session_state["freie"].remove(bester_zug)

def neues_spiel():
    st.session_state["x"] = []
    st.session_state["o"] = []
    st.session_state["freie"] = list(range(1,10))
    st.session_state["msg"] = ""
    st.session_state["letzter_zug"] = None

if "spielgestartet" not in st.session_state:
    st.session_state["spielgestartet"] = False

if "x" not in st.session_state:
    neues_spiel()
    st.session_state["punkte_spieler"] = 0
    st.session_state["punkte_computer"] = 0

if not st.session_state["spielgestartet"]:
    titelbild = Image.open("Titelbild.jpg").resize((120, 180))
    st.image(titelbild)
    st.title("🎮 Bernds TicTacToe")
    st.markdown("Ein klassisches Spiel gegen den Computer mit Minimax-Logik.")

    if st.button("🎲 Spiel starten"):
        st.session_state["spielgestartet"] = True
        st.rerun()
    st.stop()  # Alles andere wird nicht geladen

# Bilder laden
img_X = Image.open("Spieler_01.jpg").resize((80, 80))
img_O = Image.open("Spieler_02.jpg").resize((80, 80))
img_blank = Image.open("Button.jpg").resize((80, 80))

st.title("🧠 Tic Tac Toe – Spieler vs. Computer")
st.caption("Du bist **Blaues Shirt**, der Computer ist **Rosa Shirt**.")

col1, col2 = st.columns(2)
col1.metric("Deine Punkte", st.session_state["punkte_spieler"])
col2.metric("Computer", st.session_state["punkte_computer"])

# Spielfeld anzeigen (Bild + Button bleibt, Button ggf. deaktiviert)
for i in range(3):
    cols = st.columns(3)
    for j in range(3):
        feld = ij_to_num(i, j)
        if feld in st.session_state["x"]:
            cols[j].image(img_X)
        elif feld in st.session_state["o"]:
            cols[j].image(img_O)
        else:
            cols[j].image(img_blank)

        # Button bleibt, aber wird deaktiviert wenn Feld belegt
        if feld in st.session_state["freie"]:
            if cols[j].button(" ", key=f"{i}-{j}"):
                st.session_state["letzter_zug"] = feld
                st.rerun()
        else:
            cols[j].button(" ", key=f"{i}-{j}", disabled=True)

# Nach dem Klick: Zug verarbeiten
if st.session_state["letzter_zug"] is not None:
    feld = st.session_state["letzter_zug"]
    if feld in st.session_state["freie"]:
        st.session_state["x"].append(feld)
        st.session_state["freie"].remove(feld)

        if auswerten(st.session_state["x"]):
            st.session_state["punkte_spieler"] += 1
            st.session_state["msg"] = "🎉 Du hast gewonnen!"
        elif not st.session_state["freie"]:
            st.session_state["msg"] = "🤝 Unentschieden!"
        else:
            comp_setzen()
            if auswerten(st.session_state["o"]):
                st.session_state["punkte_computer"] += 1
                st.session_state["msg"] = "💻 Der Computer hat gewonnen!"

    st.session_state["letzter_zug"] = None
    st.rerun()

# Spielende Nachricht
if st.session_state["msg"]:
    st.subheader(st.session_state["msg"])
    col3, col4 = st.columns(2)
    if col3.button("🔄 Neues Spiel"):
        neues_spiel()
        st.rerun()
    if col4.button("❌ Spiel Beenden"):
        st.stop()
