#include<stdio.h>
#include<string.h>

struct student {
    int rollno;
    char name[10];
};

int main() {
    int i;
    struct student st[5];

    printf("Enter Records of 5 students:\n");
    for(i = 0; i < 5; i++) {
        printf("Enter Roll No: ");
        scanf("%d", &st[i].rollno);
        printf("Enter Name: ");
        scanf("%s", st[i].name);
    }

    printf("\nStudent Information List:\n");
    for(i = 0; i < 5; i++) {
        printf("\nRoll No: %d, Name: %s", st[i].rollno, st[i].name);
    }

    return 0;
}
