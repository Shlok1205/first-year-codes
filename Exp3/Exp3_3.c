/*WAPto check if three points (x1,y1), (x2,y2) and (x3,y3) are collinear or not.*/


#include<stdio.h>
#include<math.h>
int main()
{
    int x1, y1, x2, y2, x3, y3;
    int lhs;
    printf("Enter the points (x1 y1 x2 y2 x3 y3): ");
    scanf("%d %d %d %d %d %d", &x1, &y1, &x2, &y2, &x3, &y3);
    lhs = x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2);
    if (lhs == 0)
    {
        printf("\nPoints are collinear.");
    }
    else
    {
        printf("\nPoints are not collinear");
    }
    return 0;
}
/*Enter the points (x1 y1 x2 y2 x3 y3): 3 4 5 6 6 6
Points are not collinear*/

/*Enter the points (x1 y1 x2 y2 x3 y3): 3 3 3 3 3 3 
Points are collinear.*/