/*WAP to take check if the triangle is valid or not. If the validity is established, do check if the 
triangle is isosceles, equilateral, right angle, or scalene. Take sides of the triangle as input 
from a user.*/


#include<stdio.h>
int main()
{
int a,b,c;
printf("\nEnter the three sides of the triangle:");
scanf("%d %d %d",&a,&b,&c);
if(a + b > c && a + c > b && b + c > a) 
{
printf("\nThe triangle is valid.");
}
if (a == b && b == c && c==a) 
{
printf("\nThe triangle is equilateral.");
}
else if (a == b || b == c || a == c) 
{
printf("The triangle is isosceles.\n");
}
else if ((a*a==b*b+c*c)||
         (b*b==a*a+c*c)||
         (c*c==a*a+b*b))
         {
printf("\nThe triangle is right-angled.");
}
else if (a!=b!=c)
{
printf("\nThe triangle is scalene.");
}
else
{
printf("\nThe triangle is not valid.");
}
return 0;
}

/*Enter the three sides of the triangle:3 4 4
The triangle is valid.The triangle is isosceles.*/

/*Enter the three sides of the triangle:6 6 6 
The triangle is valid.
The triangle is equilateral.*/

/*Enter the three sides of the triangle:2 4 8
The triangle is scalene.*/

/*The triangle is valid.
The triangle is right-angled.*/