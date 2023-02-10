#include <stdio.h>
#include <stdlib.h>

void SpielfeldMalen(char board[9]); //Initieren der Hilfsfunktion um das Spielfeld zu malen

void SpielfeldMalen(char board[9]) //Hilfsfunktion um das Spielfeld zu malen
{
    system("cls"); //löscht die Konsole (unter Windows zumindest)
    printf("  _______         ______              ______\n");
    printf(" /_  __(_)____   /_  __/___  _____   /_  __/___  ___*/\\*\n");
    printf("  / / / / ___/    / / / __ `/ ___/    / / / __ \\/ _ \\\n");
    printf(" / / / / /__     / / / /_/ / /__     / / / /_/ /  __/\n");
    printf("/_/ /_/\\___/    /_/  \\__,_/\\___/    /_/  \\____/\\___/\n");
    printf("\n   */\\proudly/\\presented/\\by/\\sharpnail=games/\\*\n\n\n");
    //printf("-----------\n");
    printf("      %c | %c | %c\n", board[0], board[1], board[2]);
    printf("     ---+---+---\n");
    printf("      %c | %c | %c\n", board[3], board[4], board[5]);
    printf("     ---+---+---\n");
    printf("      %c | %c | %c\n\n", board[6], board[7], board[8]);
}

int SpielfeldEingabeWennFrei (char board[9], int i)
{
    char board_alle[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};
    if (board[i-1] == board_alle[i-1])
    {
        return 1;
    }
    else
    {
        return 0;
    }
}

int GewinnCheck (char board[9])
{
    if (board[0] == board[1] && board[1] == board[2]) return 1;
    else if (board[3] == board[4] && board[4] == board[5]) return 1;
    else if (board[6] == board[7] && board[7] == board[8]) return 1;
    else if (board[0] == board[4] && board[4] == board[8]) return 1;
    else if (board[2] == board[4] && board[4] == board[6]) return 1;
    else if (board[0] == board[3] && board[3] == board[6]) return 1;
    else if (board[1] == board[4] && board[4] == board[7]) return 1;
    else if (board[2] == board[5] && board[5] == board[8]) return 1;
    else if (board[0] != '1' && board[1] != '2' && board[2] != '3' && board[3] != '4'
             && board[4] != '5' && board[5] != '6' && board[6] != '7' && board[7] != '8'
             && board[8] != '9') return 0;
    else return -1;
}
int main()
{
    int MyPos = 0;
    int check = 0;
    int gcheck = -1;

    char MyBoard[9] = {'1', '2', '3', '4', '5', '6', '7', '8', '9'};

    SpielfeldMalen(MyBoard);

    while (gcheck == -1)
    {
        while (check == 0)
        {
            printf("Spieler 1 (X),\ngib die Nummer an, die du Befuellen moechtest: ");
            scanf("%d",&MyPos);
            //printf("%d", SpielfeldEingabeWennFrei(MyBoard, MyPos));
            if (SpielfeldEingabeWennFrei(MyBoard, MyPos) == 1)
            {
                MyBoard[MyPos-1] = 'X';
                check = 1;
            }
            else
            {
                printf("Falsche Nummer oder Feld ist schon besetzt - Bitte nochmals versuchen");
            }
        }
        check = 0;
        SpielfeldMalen(MyBoard);
        if (GewinnCheck(MyBoard) == 1)
        {
            printf("*** Gewinner ist Spieler 1 mit X ***");
            scanf("%d");
            break;
        }
        else if (GewinnCheck(MyBoard) == 0)
        {
            printf("UNENTSCHIEDEN - Kein Gewinner");
            scanf("%d");
            break;
        }

        while (check == 0)
        {
            printf("Spieler 2 (O),\ngib die Nummer an, die du Befuellen moechtest: ");
            scanf("%d",&MyPos);
            //printf("%d", SpielfeldEingabeWennFrei(MyBoard, MyPos));
            if (SpielfeldEingabeWennFrei(MyBoard, MyPos) == 1)
            {
                MyBoard[MyPos-1] = 'O';
                check = 1;
            }
            else
            {
                printf("Falsche Nummer oder Feld ist schon besetzt - Bitte nochmals versuchen");
            }
        }
        check = 0;
        SpielfeldMalen(MyBoard);
        if (GewinnCheck(MyBoard) == 1)
        {
            printf("*** Gewinner ist Spieler 2 mit O ***");
            scanf("%d");
            break;
        }
        else if (GewinnCheck(MyBoard) == 0)
        {
            printf("UNENTSCHIEDEN - Kein Gewinner");
            scanf("%d");
            break;
        }
    }
    return 0;
}
