class Stack:
    stack = []
    
    def __init__(self, array = []):
        if not isinstance(array, list):
            raise Exception('The data must be a list of python.')
        self.stack = array
    
    def push(self, value):
        self.stack.append(value)   
         
    def pop(self):
        return self.stack.pop()
        
    def get_size(self):
        return len(self.stack)
    
    def get_list(self):
        return self.stack
        
    def get_index(self, value):
        return self.stack.index(value)
    
    def get(self, index):
        return self.stack[index]