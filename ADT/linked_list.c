#include <assert.h>
#include <stdio.h>
#include <stdlib.h>


typedef struct Node{
  int data;
  int size;
  struct Node* next;
}Node;


Node* init(int value){
  Node *n = malloc(sizeof(Node));
  n->data = value;
  n->size = 1;
  n->next = NULL;
  return n;
}

void push(Node **node,int value){
  Node *n = malloc(sizeof(Node));
  n->data = value;
  n->next = *node;
  n->size = (*node)->size+1;
  *node = n;
}

// return is node->value
int get_value(Node* node, int idx){
  int size = node->size;
  assert(idx < size && "idx out of range !");
  while(node != NULL){
    if (node->size == idx+1) return node->data;
    node = node->next;
  }
  return 0;
}

// return is pointer node
Node* get(Node* node,int idx){
  int size = node->size;
  assert(idx < size && "idx out of range !");
  while(node != NULL){
    if (node->size == idx+1) return node;
    node = node->next;
  }
  return NULL;

}

// print the last node at the beginning
void print_node(Node *node){
  while(node != NULL){
    printf("%d ",node->data);
    node = node->next;
  }
  printf("\n");
}

// print the last node at the end
void print_nodev2(Node *node){
  for(int i = 0 ; i < node->size ; i ++){
    printf("%d ",get_value(node,i));
  }
  printf("\n");
}

void free_node(Node *node){
  Node *current = node;
  while(current != NULL){
    Node* next = current->next;
    free(current);
    current = next;
  }
}

void delete(Node *node,int idx){
  assert((node->size >= idx && idx >= 0 ) && "idx out of range !");
  Node* temp = get(node,idx);
  if (node->size-1 == idx){
    Node* current = get(node,idx-1);
    temp->data = current->data;
    temp->next = current->next;
    free(current);

  }else{
    Node* current = get(node,idx+1);
    current->next = get(node,idx-1);
    free(temp);
  }
  node->size = node->size-1;
}

void arange(Node** node,int start ,int end){
  assert((start < end) && "start > end");
  for (int i = start; i < end; i++){
    push(node,i);
  }
}


int main(){
  Node *n = init(1);
  arange(&n,2,11);
  push(&n,11);
  push(&n,12);
  push(&n,13);
  push(&n,15);

  printf("%d\n",n->size);

  print_node(n);
  delete(n,10);
  delete(n,10);
  print_node(n);

  printf("%d\n",n->size);

  free_node(n);

  return 0;
}

