# Pilhas em Python
import gc

class Node:
    def __init__(self, _data):
        self.data = _data
        self.nxt = None
    
    
    def to_string(self):
        info = f'Nó: {self}\nValor: {self.data}\nPróximo: '
        
        if self.nxt != None:
            info += f'{self.nxt.data}\n'
        else:
            info += 'None\n'
        
        return info


class Stack:
    def __init__(self, _capacity):
        self.head = None
        self.capacity = _capacity
        self.size = 0
    
    
    def push(self, _data):
        new = Node(_data)
        
        if self.size == self.capacity:
            print("Stack overflow!\n")
        else:
            if self.head == None:
                self.head = new
            else:
                new.nxt = self.head
                self.head = new
            
            self.size += 1
    
    
    def pop(self):
        if self.head == None:
            return None
        
        popped = self.head
        self.head = self.head.nxt
        popped.nxt = None
        
        return popped.to_string() + '\n-----------------'
    
    
    def peek(self):
        if self.head == None:
            return 'None\n'
        
        input("\nENTER para avançar\n")
        return f'{self.head.to_string()}\n-----------------'
    
    
    def display(self):
        aux = self.head
        stack_info = ""
        
        if self.head == None:
            print("Stack underflow...\n")
            return
        
        while aux:
            print(aux.to_string())
            stack_info += f'{aux.data} -> '
            
            aux = aux.nxt
        
        stack_info += '\n'
        print(stack_info)


stack1 = Stack(10)
stack1.display()
print(stack1.peek())

stack1.push(65)
stack1.display()
print(stack1.peek())

stack1.push(71)
stack1.display()
print(stack1.peek())

stack1.push(26)
stack1.display()
print(stack1.peek())

stack1.push(84)
stack1.display()
print(stack1.peek())

stack1.push(12)
stack1.display()
print(stack1.peek())

stack1.push(90)
stack1.display()
print(stack1.peek())

stack1.push(36)
stack1.display()
print(stack1.peek())

stack1.push(47)
stack1.display()
print(stack1.peek())

stack1.push(58)
stack1.display()
print(stack1.peek())

stack1.push(31)
stack1.display()
print(stack1.peek())

stack1.push(111)
stack1.display()
print(stack1.peek())

print(stack1.pop())
gc.collect()
stack1.display()
print(stack1.peek())
