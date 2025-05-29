#include <stdio.h>
#include <stdlib.h>

// Define the Node structure
struct Node {
    int data;
    struct Node* next;
    struct Node* prev;
};

// Function to create a new node
struct Node* createNode(int data) {
    struct Node* newNode = (struct Node*)malloc(sizeof(struct Node));
    newNode->data = data;
    newNode->next = NULL;
    newNode->prev = NULL;
    return newNode;
}

// Function to print the list forward
void traverseForward(struct Node* head) {
    struct Node* currentNode = head;
    printf("\nTraversing forward:\n");
    while (currentNode != NULL) {
        printf("%d -> ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("null\n");
}

// Function to print the list backward
void traverseBackward(struct Node* tail) {
    struct Node* currentNode = tail;
    printf("\nTraversing backward:\n");
    while (currentNode != NULL) {
        printf("%d -> ", currentNode->data);
        currentNode = currentNode->prev;
    }
    printf("null\n");
}

int main() {
    // Create nodes
    struct Node* node1 = createNode(12);
    struct Node* node2 = createNode(16);
    struct Node* node3 = createNode(8);
    struct Node* node4 = createNode(17);

    // Link nodes
    node1->next = node2;

    node2->prev = node1;
    node2->next = node3;

    node3->prev = node2;
    node3->next = node4;

    node4->prev = node3;

    // Traverse the list forward
    traverseForward(node1);

    // Traverse the list backward
    traverseBackward(node4);

    // Free allocated memory
    free(node1);
    free(node2);
    free(node3);
    free(node4);

    return 0;
}