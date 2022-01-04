# Implementar uma pilha de pilhas (spoilers: fica feio pra um cacete!)

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
    
    
    def find_stack(self, _index):
        aux = self.top
        stack = self.head
        
        while aux != _index and stack != None:
            aux -= 1
            stack = stack.nxt
        
        if stack != None:
            return stack
        
        print("Índice inválido!")
    
    
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
            # print(aux.to_string() + '\n')
            stack_info += f'{aux.data} -> '
            
            aux = aux.nxt
        
        stack_info += '\n'
        print(stack_info)


kstacks = Stack(10)  # Instanciando a pilha de pilhas

kstacks.push(Stack(10))  # Inserindo uma pilha
kstacks.find_stack(0).data.push(65)
print(kstacks.find_stack(0).data.peek()) # Eu sei... Isso é FEIO PRA CARALHO!

# Para acessar uma pilha dentro de kstacks, é preciso acessar o atributo data (usar get e set)
kstacks.find_stack(0).data.push(71)
print(kstacks.find_stack(0).data.peek())

kstacks.push(Stack(10))
kstacks.find_stack(1).data.push(26)
print(kstacks.find_stack(0).data.peek())
print(kstacks.find_stack(1).data.peek())
kstacks.find_stack(0).data.display()
kstacks.find_stack(1).data.display()
