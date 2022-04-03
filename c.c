#include <stdio.h>
#include <stdlib.h>
typedef struct Cell Cell;

struct Cell
{
    int x;
    int y;

    int custo_destino;
    int custo_start;
    int custo_total;

    Cell* origin;
    Cell* up;
    Cell* bt;
    Cell* left;
    Cell* right;

};

//Atraves do origin eu consigo saber o custo_start
Cell* createCell(Cell* origin)
{
    Cell* new_cell = (Cell*)malloc(sizeof(Cell));
    return new_cell;
}

void setValue(Cell* cell, int x, int y, int custo_start, int custo_destino)
{
    cell->x = x;
    cell->y = y;
    cell-> custo_start = custo_start;
    cell->custo_destino = custo_destino;
}


//Necessario? Nao sei
void setNext(Cell* cell, Cell* up, Cell* bt, Cell *left, Cell* right)
{
    cell->up = up;
    cell->bt = bt;
    cell-> left = left;
    cell->right = right;
}

//Alterar tipo e retorno
int read_grid(char *path_grid)
{
    FILE *arquivo;
    arquivo = fopen(path_grid, "r");
    if(arquivo)
    {

    }
    return 1;
}

void print_grid(int grid[5][6], int lin, int col)
{
    for(int i = 0; i < lin; i++)
    {
        for(int j = 0; j < col; j++)
        {
            printf("%d ", grid[i][j]);
        }
        printf("\n");
    }
    printf("\n");
}


int main()
{

    //Grid de teste
    int grid[5][6] = {{0, 1, 0, 0, 0, 0},
                      {0, 1, 0, 0, 0, 0},
                      {0, 1, 0, 0, 0, 0},
                      {0, 1, 0, 0, 0, 0},
                      {0, 0, 0, 0, 1, 0}};

    print_grid(grid, 5, 6);

    Cell* cabCell = createCell();
    return 0;
}