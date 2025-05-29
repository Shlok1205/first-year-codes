#include<stdio.h>
#include<stdlib.h>
void bubbleSort(int *arr,int n);
{
     for (int i = 0; i < n - 1; i++) 
     {
        for (int j = 0; j < n - i - 1; j++) 
        {
            if (*(arr + j) > *(arr + j + 1)) 
            {
                int temp = *(arr + j);
                *(arr + j) = *(arr + j + 1);
                *(arr + j + 1) = temp;
            }
        }
    }
}
int main()
{
int n;
printf("\nEnter the number of elements: ",n);
scanf("%d",&n);
int *arr = (int *)malloc(n * sizeof(int));
    if (arr == NULL) 
        printf("\nMemory allocation failed.");
       return 1;
}