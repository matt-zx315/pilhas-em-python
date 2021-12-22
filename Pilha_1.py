# Implementar uma pilha com uma função para sempre retornar o menor valor
# Não é permitido usar outra estrutura de dados além da pilha
# É necessário que a operação tenha complexidade de tempo (O)1
# A nova classe pilha deve ter todos os métodos de uma pilha comum

import gc

class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
    
    
    def to_string(self):
        info = f'Nó: {self}\nValor: {self.data}\nPróximo: '
        
        if self.nxt != None:
            info += f'{self.nxt.data}'
        else:
            info += 'None\n'
        
        return info


class Stack:
    def __init__(self, _size):
        self.head = None
        self.size = _size
        self.top = -1
    
    
    def is_full(self):
        if self.top == self.size - 1:
            return True
        return False
    
    
    def is_empty(self):
        if self.top == -1:
            return True
        return False
    
    
    def push(self, _data):
        new = Node(_data)
        
        if self.is_full():
            print("Stack overflow!\n")
        else:
            if self.head == None:
                self.head = new
            else:
                new.nxt = self.head
                self.head = new
            
            self.top += 1
    
    
    def pop(self):
        if self.head == None:
            return None
        
        popped = self.head
        self.head = self.head.nxt
        popped.nxt = None
        
        return popped.data
    
    
    def peek(self):
        if self.head == None:
            return 'None\n'
        return f'{self.head.to_string()}\n-----------------'
    
    
    def display(self):
        aux = self.head
        stack_info = ""
        
        if self.is_empty():
            print("Stack underflow...\n")
            return
        
        while aux:
            print(aux.to_string() + '\n')
            stack_info += f'{aux.data} -> '
            
            aux = aux.nxt
        
        stack_info += '\n'
        print(stack_info)
    
    
class Special_Stack(Stack):
    def __init__(self, _size):
        super().__init__(_size)
        self.min_stack = Stack(_size)
    
    
    def push(self, _data):
        if self.is_empty():
            super().push(_data)
            self.min_stack.push(_data)
        else:
            super().push(_data)
            last = self.min_stack.pop()
            self.min_stack.push(last)
            
            if _data < last:
                self.min_stack.push(_data)
            else:
                self.min_stack.push(last)
    
    
    def pop(self):
        x = super().pop()
        self.min_stack.pop()
        return x
    
    
    def get_min(self):
        print(f'-----------------\n{self.min_stack.peek()}\n')


stack1 = Special_Stack(100)
stack1.push(20)
stack1.display()

stack1.push(25)
stack1.display()
stack1.get_min()

stack1.push(15)
stack1.display()
stack1.get_min()

stack1.push(18)
stack1.display()
stack1.get_min()

stack1.push(17)
stack1.display()
stack1.get_min()

stack1.push(12)
stack1.display()
stack1.get_min()

stack1.pop()
stack1.display()
stack1.get_min()
