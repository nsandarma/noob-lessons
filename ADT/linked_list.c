#include <stdio.h>
#include <stdlib.h>

struct node_s{
  int value;
  struct node_s *next;
};

typedef struct node_s Node;


void is_empty(Node *head){
  if (head == NULL){
    printf("List of Empty\n");
    exit(EXIT_FAILURE);
  }
}

void print(Node *head){
  while(head != NULL){
    printf("%d -> ",head->value);
    head = head->next;
  }
  printf("NULL\n");
}

Node *createNode(int value){
  Node *newNode = malloc(sizeof(Node));
  newNode->value = value;
  newNode->next = NULL;
  return newNode;
}

void insertAtFirst(Node** head, int value){
  Node* newNode = createNode(value);
  if (*head != NULL){
    newNode->next = *head;
  }
  *head = newNode;
}

void insertAtEnd(Node** head, int value){
  Node* newNode = createNode(value);
  if(*head == NULL){
    *head = newNode;
    return;
  }
  Node *temp = *head;
  while(temp->next != NULL) temp = temp->next;
  temp->next = newNode;
}

void insertAtPosition(Node** head,int value, int position){
  if (position == 0 ){
    insertAtFirst(head, value);
    return;
  }
  Node* newNode = createNode(value);
  Node* temp = *head;
  for(int i = 0 ; temp != NULL && i < position - 1 ; i++){
    temp = temp->next;
  }
  if (temp == NULL){
    printf("Position out of range\n");
    free(newNode);
    exit(EXIT_FAILURE);
  }
  newNode->next = temp->next;
  temp->next = newNode;
}

void deleteFromFirst(Node** head){
  is_empty(*head);
  Node* temp = *head;
  *head = temp->next;
  free(temp);
}

void deleteFromEnd(Node** head){
  is_empty(*head);
  Node* temp = *head;
  if(temp->next == NULL){
    free(temp);
    *head = NULL;
    return;
  }
  while(temp->next->next != NULL){
    temp = temp->next;
  }
  free(temp->next);
  temp->next = NULL;
}

void deleteFromPosition(Node** head,int position){
  is_empty(*head);
  if (position == 0 ){
    deleteFromFirst(head);
    return;
  }
  Node* temp = *head;
  for(int i = 0; temp != NULL && i < position - 1 ;i++){
    temp = temp->next;
  }
  if(temp == NULL || temp->next == NULL){
    printf("position out of range\n");
    return;
  }
  Node* next = temp->next->next;
  free(temp->next);
  temp->next = next;
}

void free_node(Node *head){
  while(head != NULL){
    Node *next = head->next;
    free(head);
    head = next;
  }
}

void generateArange(Node** head,int start , int end){
  if (start >= end){
    printf("start > end\n");
    return;
  }
  for(;start < end;start++ ){
    insertAtFirst(head,start);
  }
}

void generateArangeQue(Node** head, int start, int end){
  if (start >= end){
    printf("start > end\n");
    return;
  }
  for(;start < end;start++ ){
    insertAtEnd(head,start);
  }
}

/*
   kalo mau menggunakan stack, insertAtFirst() sebagai push , dan deleteFromFirst() sebagai pop;
   kalo mau menggunakan queue, insertAtEnd() sebagai Enqueue, dan deleteFromFirst() sebagai Dequeue
*/

void useStack(){
  Node *head = NULL;
  generateArange(&head, 1, 11);

  printf("top -> %d\n",head->value);
  deleteFromFirst(&head); // pop
  printf("top -> %d\n",head->value);
  deleteFromFirst(&head); // pop
  printf("top -> %d\n",head->value);
  deleteFromFirst(&head); // pop
  printf("top -> %d\n",head->value);
  insertAtFirst(&head,123); // push
  print(head);
  free_node(head);
}

void useQueue(){
  Node *head = NULL;
  generateArangeQue(&head,1, 11);
  printf("Peek -> %d\n",head->value);
  insertAtEnd(&head, 12); // Enqueue
  print(head);
  deleteFromFirst(&head); // Dequeue
  printf("Peek -> %d\n",head->value);
  print(head);
  free_node(head);
}


int main(){
  // useStack();
  useQueue();
  return 0;
}

