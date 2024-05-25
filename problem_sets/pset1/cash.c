#include <stdio.h>

int main(void) 
{
    int change = 0, quarters = 0, dimes = 0, nickels = 0, pennies = 0;
    int quarterValue = 25, dimeValue = 10, nickelValue = 5, penneValue = 1;
    int totalCoins = 0;
    printf("Change owned: ");
    scanf("%d", &change);
    while (change - quarterValue >= 0)
    {
        change -= quarterValue;
        quarters += 1;
    }
    while (change - dimeValue >= 0)
    {
        change -= dimeValue;
        dimes += 1;
    }
    while (change - nickelValue >= 0)
    {
        change -= nickelValue;
        nickels += 1;
    }
    while (change - penneValue >= 0)
    {
        change -= penneValue;
        nickels += 1;
    }
    totalCoins = quarters + dimes + nickels + pennies;
    printf("Quarters: %d\n", quarters);
    printf("Dimes: %d\n", dimes);
    printf("Nickels: %d\n", nickels);
    printf("Pennies: %d\n", pennies);
    printf("Coins qty.: %d\n", totalCoins);
}