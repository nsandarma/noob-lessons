#include <stdio.h>
#include <stdlib.h>
#include <stdbool.h>

#define MAX 100

typedef struct {
  int data[MAX];
  int top;
}Stack;

void init(Stack * stack){
  stack->top = -1;
}
bool is_empty(Stack *stack){
  return stack->top == -1;
}

bool is_full(Stack *stack){
  return stack->top == MAX - 1;
}

void push(Stack *stack,int value){
  if (is_full(stack)){
    printf("Stack overflow\n");
    return;
  }
  stack->data[++stack->top] = value;
}

int pop(Stack *stack){
  if (is_empty(stack)){
    printf("stack underflow\n");
    exit(EXIT_FAILURE);
  }
  // printf("Popped %d from the stack\n",stack->data[stack->top]);
  return stack->data[stack->top--];
}

int peek(Stack *stack){
  if (is_empty(stack)){
    printf("Stack is empty\n");
    exit(EXIT_FAILURE);
  }
  return stack->data[stack->top];
}

void printStack(Stack *stack){
  if(is_empty(stack)){
    printf("Stack is empty\n");
    return;
  }
  printf("current Stack : ");
  for(int i = 0 ; i <= stack->top ; i ++){
    printf("%d ",stack->data[i]);
  }
  printf("\n");
}

int main(){
  Stack stack;
  init (&stack);
  push(&stack,10);
  printStack(&stack);
  printf("%d\n",peek(&stack));

  printf("Top: %d\n",peek(&stack));
  return 0;

}
