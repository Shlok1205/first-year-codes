#include <stdio.h>
#include <stdlib.h>

struct Node {
    int data;
    struct Node* next;
};

int main() {
    struct Node* node1 = (struct Node*)malloc(sizeof(struct Node));
    struct Node* node2 = (struct Node*)malloc(sizeof(struct Node));
    struct Node* node3 = (struct Node*)malloc(sizeof(struct Node));
    struct Node* node4 = (struct Node*)malloc(sizeof(struct Node));

    node1->data = 12;
    node1->next = node2;
    node2->data = 16;
    node2->next = node3;
    node3->data = 17;
    node3->next = node4;
    node4->data = 8;
    node4->next = NULL;

    struct Node* currentNode = node1;
    while (currentNode != NULL) {
        printf("%d -> ", currentNode->data);
        currentNode = currentNode->next;
    }
    printf("null\n");

    free(node1);
    free(node2);
    free(node3);
    free(node4);

    return 0;
}