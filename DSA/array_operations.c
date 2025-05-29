#include <stdio.h>
#include <stdlib.h>
void traverse(int n, int a[n]) 
{
    printf("Current Array: ");
    for (int i = 0; i < n; i++) 
    {
        printf("%d ", a[i]);
    }
    printf("\n");
}

void insert(int n, int a[n], int l, int e) 
{
    printf("Inserting %d at position %d...\n", e, l);
    for (int i = n; i >= l; i--) 
    {
        a[i] = a[i - 1];
    }
    a[l - 1] = e;
    n++;
    traverse(n, a);
}

void delete(int n, int a[n], int l) 
{
    printf("Removing element at position %d...\n", l);
    for (int i = l - 1; i < n - 1; i++) 
    {
        a[i] = a[i + 1];
    }
    n--;
    traverse(n, a);
}

void search(int n, int a[n], int e, int method) 
{
    if (method == 1)// Linear Search
    { 
        printf("Searching %d using Linear Search...\n", e);
        for (int i = 0; i < n; i++) 
        {
            if (a[i] == e) 
            {
                printf("Element %d found at position %d\n", e, i + 1);
                return;
            }
        }
        printf("Element %d not found.\n", e);
    } 
    else if (method == 2)// Binary Search
    {
        printf("Searching %d using Binary Search...\n", e);
        int start = 0, end = n - 1, mid;
        while (start <= end) 
        {
            mid = (start + end) / 2;
            if (a[mid] == e) 
            {
                printf("Element %d found at position %d\n", e, mid + 1);
                return;
            } 
            else if (a[mid] < e) 
            {
                start = mid + 1;
            } 
            else 
            {
                end = mid - 1;
            }
        }
        printf("Element %d not found.\n", e);
    } 
    else 
    {
        printf("Invalid search method. Use 1 for Linear or 2 for Binary.\n");
    }
}

int main() 
{
    int a[20] = {10, 20, 30, 40, 50};
    int n = 5, choice, l, e, method;

    printf("Welcome! Here's the initial array:\n");
    traverse(n, a);

    printf("\nChoose an option:\n");
    printf("1. Show Array (Traversal)\n");
    printf("2. Add an Element (Insertion)\n");
    printf("3. Remove an Element (Deletion)\n");
    printf("4. Find an Element (Search)\n");
    printf("Your choice: ");
    scanf("%d", &choice);

    switch (choice) 
    {
        case 1:
            traverse(n, a);
            break;

        case 2:
            printf("Enter position to insert (1 to %d): ", n + 1);
            scanf("%d", &l);
            if (l <= 0 || l > n + 1) 
            {
                printf("Invalid position! Please enter between 1 and %d.\n", n + 1);
                break;
            }
            printf("Enter the value to insert: ");
            scanf("%d", &e);
            insert(n, a, l, e);
            n++;
            break;

        case 3:
            printf("Enter position to delete (1 to %d): ", n);
            scanf("%d", &l);
            if (l <= 0 || l > n) 
            {
                printf("Invalid position! Please enter between 1 and %d.\n", n);
                break;
            }
            delete(n, a, l);
            n--;
            break;

        case 4:
            printf("Enter the value to search: ");
            scanf("%d", &e);
            printf("Choose search method:\n");
            printf("1. Linear Search\n");
            printf("2. Binary Search\n");
            printf("Your choice: ");
            scanf("%d", &method);
            search(n, a, e, method);
            break;

        default:
            printf("Invalid option! Please choose a number between 1 and 4.\n");
            break;
    }
    return 0;
}