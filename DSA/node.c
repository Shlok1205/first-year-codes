#include<stdio.h>
#include<stdlib.h>
//structure of a node
struct node{
    int data;
    struct node* next;
}*head;
//functions to create and display list
void create_list(int n);
void traverse_list();

void main()
{
    int n;
    printf("\nEnter the total number of nodes= ");
    scanf("%d",&n);

    create_list(n);
    printf("\nData in list");

    traverse_list();
}

//create a list of n nodes
void create_list(int n)
{
    struct node *new node,*temp;
    int data,i;

    head=(struct node*)malloc(sizeof(struct node));

    if(head==NULL)
    {
        printf("\nMemory not allocated");
    
    }
    else
    //input data of node from the user
    {
        printf("\nEnter the data of node 1: ");
        scanf("%d",&data);

        head->data=data;
        head->next=NULL;
        //create n-1 nodes and add to the list

        temp=head;

        for(i=2;i<=n;i++)
        {
            new_node=(struct node*)malloc(sizeof(struct node));
            if(new node==null);
            printf("\nMemory not allocated");
            
            else
            {
                printf("\nEnter the data of node: ");
                scanf("%d",&data);

                new_node->data=data;
                 new_node->next=NULL;

                 temp->next=new_node;
                 temp=temp->next;
            }

        }
    }
}
void traverse_list()
{
    struct node *temp=head;
    //traversing the list
    while(temp!=NULL)
    printf("\t%d",temp->data);
    temp=temp->next;
}