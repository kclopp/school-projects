#include <stdio.h>
#include <cs50.h>
#include <math.h>


// greedy.c to calculate the samllest amount of coins returned
int main(void)

{

    float changeBack;
    int money;
    
    
    // do loop to get postive change needed   
    do
    {
        printf("Please enter cange needed ");
        changeBack = GetFloat();
    }
    while (changeBack < 0);
    
    // int var for each coint type
    int qtr = 0;
    int dime = 0;
    int nickel = 0;
    
    
    // change the float 'changeBack' to it's int form stored in money
    money = (int) (round(changeBack * 100));
    
    // series of if statments do weed out the coins
    // quarters
    if (money >= 25)
    {
        qtr = money / 25;
        money = money - (qtr * 25);
    }
      // dimes
    if (money >= 10)
    {
        dime = money / 10;
        money = money - (dime * 10);
    }
      // nickles  
    if (money >= 5)
    {
        nickel = money / 5;
        // what is left in var money is equal to the pennies
        money = money - (nickel * 5);
    }
    
    // totals up coins
    printf("%d\n", qtr + dime + nickel + money);
    

}
