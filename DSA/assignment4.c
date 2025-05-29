#include <stdio.h>
#include <stdlib.h>
#include <string.h>

#define SIZE 10

typedef struct {
    int jobId;
    char user[30];
} PrintJob;

PrintJob queue[SIZE];
int front = -1, rear = -1;

void addJob(int jobId, char user[]) {
    if (rear == SIZE - 1) {
        printf("Print Queue is Full\n");
        return;
    }
    if (front == -1) front = 0;
    rear++;
    queue[rear].jobId = jobId;
    strcpy(queue[rear].user, user);
    printf("Added Job %d by %s\n", jobId, user);
}

void processJob() {
    if (front == -1 || front > rear) {
        printf("Print Queue is Empty\n");
        return;
    }
    printf("Processing Job %d by %s\n", queue[front].jobId, queue[front].user);
    front++;
}

int main() {
    int choice, jobId;
    char user[30];

    while (1) {
        printf("\n1. Add Print Job\n2. Process Job\n3. Exit\nEnter your choice: ");
        scanf("%d", &choice);
        switch (choice) {
            case 1:
                printf("Enter Job ID: ");
                scanf("%d", &jobId);
                printf("Enter User Name: ");
                scanf("%s", user);
                addJob(jobId, user);
                break;
            case 2:
                processJob();
                break;
            case 3:
                exit(0);
            default:
                printf("Invalid Choice\n");
        }
    }
    return 0;
}

// 1. Add Print Job
// 2. Process Job
// 3. Exit
// Enter your choice: 1
// Enter Job ID: 101
// Enter User Name: Madan
// Added Job 101 by Madan

// 1. Add Print Job
// 2. Process Job
// 3. Exit
// Enter your choice: 3