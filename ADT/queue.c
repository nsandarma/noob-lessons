#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>
#define MAX_SIZE 100

typedef struct {
  int data[MAX_SIZE];
  int front; // head
  int rear; // tail/back
}Queue;

void init(Queue* q){
  q->front = -1;
  q->rear = 0;
}

bool isEmpty(Queue* q){ return (q->front == q->rear -1);}

bool isFull(Queue* q){return (q->rear == MAX_SIZE);}

void enqueue(Queue* q,int value){
  if(isFull(q)){
    printf("Queue is full\n");
    return;
  }
  q->data[q->rear] = value;
  q->rear++;
}

void dequeue(Queue* q){
  if (isEmpty(q)){
    printf("Queue is empty\n");
    return;
  }
  q->front++;
}

int peek(Queue *q){
  if (isEmpty(q)){
    printf("Queue is empty\n");
    exit(EXIT_FAILURE);
  }
  return q->data[q->front + 1];
}

void printQueue(Queue* q){
  if (isEmpty(q)){
    printf("Queue is empty\n");
    return;
  }
  printf("Current Queue: ");
  for (int i = q->front + 1; i < q->rear; i ++){
    printf("%d ",q->data[i]);
  }
  printf("\n");
}

void arange(Queue* q,int start, int end){
  if(start >= end){
    printf("start > end\n");
    exit(EXIT_FAILURE);
  }
  for (;start < end;start++){
    enqueue(q, start);
  }
}


int main(){
  Queue q;
  init(&q);
  arange(&q,1,11);
  printQueue(&q);
  printf("front : %d\n",peek(&q));
  dequeue(&q);
  printQueue(&q);
  printf("front : %d\n",peek(&q));
  return 0;
}



