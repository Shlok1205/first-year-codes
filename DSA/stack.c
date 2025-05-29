#include <stdio.h>
#include <stdlib.h>

#define SIZE 5  // Stack size

int stack[SIZE], top = -1;

// Function to check if the stack is full
int isFull() 
{
    return top == SIZE - 1;
}

// Function to check if the stack is empty
int isEmpty() 
{
    return top == -1;
}

// Function to push an element onto the stack
void push(int value) 
{
    if (isFull()) 
    {
        printf("Stack Overflow! Cannot push %d\n", value);
    } 
    else 
    {
        stack[++top] = value;
        printf("%d pushed onto stack\n", value);
    }
}

// Function to pop an element from the stack
void pop() 
{
    if (isEmpty()) 
    {
        printf("Stack Underflow! Nothing to pop\n");
    } 
    else 
    {
        printf("%d popped from stack\n", stack[top--]);
    }
}

// Function to display the stack
void display() 
{
    if (isEmpty()) 
    {
        printf("\nStack is empty\n");
    } 
    else 
    {
        printf("\nStack elements: ");
        for (int i = top; i >= 0; i--) 
        {
            printf("%d ", stack[i]);
        }
        printf("\n");
    }
}

// Function to initialize the stack with initial data
void initialize_stack() 
{
    int n, value;
    printf("Enter the number of initial elements (max %d): ", SIZE);
    scanf("%d", &n);

    for (int i = 0; i < n; i++) 
    {
        if (isFull()) 
        {
            printf("Stack Overflow! Cannot push more elements\n");
            break;
        }
        printf("Enter value %d: \n", i + 1);
        scanf("%d", &value);
        stack[++top] = value;
    }
}

void main() 
{
    int choice, value;
    initialize_stack(); 
    
    while (1) 
    {
        printf("\nStack Operations: \n");
        printf("1. Push\n");
        printf("2. Pop\n");
        printf("3. Display\n");
        printf("4. Exit\n");
        printf("Enter your choice: ");
        scanf("%d", &choice);
        
        switch (choice) 
        {
            case 1:
                printf("\nEnter the value to push: ");
                scanf("%d", &value);
                push(value);
                break;
            case 2:
                pop();
                break;
            case 3:
                display();
                break;
            case 4:
                exit(0);
            default:
                printf("\nInvalid choice! Please enter a valid option.\n");
        }
    }
}

