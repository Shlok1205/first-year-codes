/*According to the gregorian calendar, it was Monday on the date 01/01/01. If Any year is input 
through the keyboard write a program to find out what is the day on 1st January of this year.*/


#include<stdio.h>
int main()
{
 int year, day;
    printf("Enter the year: ");
    scanf("%d", &year);
    int yearsPassed = year-1; 
    int leapYears = yearsPassed/4 - yearsPassed/100 + yearsPassed/400; 
    int normalYears = yearsPassed - leapYears; 
    int totalDays = normalYears*365 + leapYears*366;
    day = totalDays %7;
    switch (day) 
    {
        case 0: 
        printf("\nThe day on 1st January of %d was Monday.",year); 
        break;
        
        case 1: 
        printf("\nThe day on 1st January of %d was Tuesday.",year); 
        break;
       
        case 2: 
        printf("\nThe day on 1st January of %d was Wednesday.",year); 
        break;
        
        case 3: 
        printf("\nThe day on 1st January of %d was Thursday.",year); 
        break;
        
        case 4: 
        printf("\nThe day on 1st January of %d was Friday.",year); 
        break;
       
        case 5: 
        printf("\nThe day on 1st January of %d was Saturday.",year); 
        break;
       
        case 6: 
        printf("\nThe day on 1st January of %d was Sunday.",year); 
        break;
    }

    return 0;   
}

/*Enter the year: 2007
The day on 1st January of 2007 was Monday.*/

/*Enter the year: 2008
The day on 1st January of 2008 was Tuesday.*/

/*Enter the year: 2014
The day on 1st January of 2014 was Wednesday.*/

/*Enter the year: 2009
The day on 1st January of 2009 was Thursday*/

/*Enter the year: 2010
The day on 1st January of 2010 was Friday.*/

/*Enter the year: 2005
The day on 1st January of 2005 was Saturday.*/

/*Enter the year: 2006
The day on 1st January of 2006 was Sunday.*/