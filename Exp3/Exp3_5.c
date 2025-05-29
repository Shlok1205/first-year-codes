/*WAP using ternary operator, the user should input the length and breadth of a rectangle, one 
has to find out which rectangle has the highest perimeter. The minimum number of rectangles 
should be three.*/

#include <stdio.h>
int main() 
{
    float l1, b1, l2, b2, l3, b3, p1, p2, p3;

    printf("Enter length and breadth of rectangle 1: ");
    scanf("%f %f", &l1, &b1);
    
    printf("Enter length and breadth of rectangle 2: ");
    scanf("%f %f", &l2, &b2);
    
    printf("Enter length and breadth of rectangle 3: ");
    scanf("%f %f", &l3, &b3);

    p1 = 2 * (l1 + b1);
    p2 = 2 * (l2 + b2);
    p3 = 2 * (l3 + b3);

    (p1 > p2 && p1 > p3)?printf("\nRectangle 1 has the highest perimeter: %.2f", p1) :
    (p2 > p3)?printf("\nRectangle 2 has the highest perimeter: %.2f", p2) :
    printf("\nRectangle 3 has the highest perimeter: %.2f", p3);

    return 0;
}

/*Enter length and breadth of rectangle 1: 4 9
Enter length and breadth of rectangle 2: 8 2
Enter length and breadth of rectangle 3: 7 6

Rectangle 3 has the highest perimeter: 26.00*/