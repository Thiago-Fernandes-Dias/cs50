#include <stdio.h>

void iterative(int);
void recursive(int);
void recursiveHelper(int, int);

int main(void)
{
    int height = -1;
    while (height < 0)
    {
        printf("Height: ");
        scanf("%d", &height);
    }
    printf("Iterative: \n");
    iterative(height);
    printf("Recursive:");
    recursive(height);
    return 0;
}

void iterative(int height)
{
    for (int i = 0, k = height - 1; k >= 0; k--, i++)
    {
        for (int j = 0; j < k; j++)
            printf(" ");
        for (int j = i; j >= 0; j--)
            printf("#");
        printf(" ");
        for (int j = i; j >= 0; j--)
            printf("#");
        for (int j = 0; j < k; j++)
            printf(" ");
        printf("\n");
    }
}

void recursive(int height)
{
    recursiveHelper(height, 0);
}

void recursiveHelper(int height, int spaces)
{
    if (height > 0)
        recursiveHelper(height - 1, spaces + 1);
    for (int j = 0; j < spaces; j++)
        printf(" ");
    for (int j = height; j > 0; j--)
        printf("#");
    printf(" ");
    for (int j = height; j > 0; j--)
        printf("#");
    for (int j = 0; j < spaces; j++)
        printf(" ");
    printf("\n");
}
