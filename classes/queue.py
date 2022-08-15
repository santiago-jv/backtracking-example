class Queue:
    queue = []

    def __init__(self, array):

        if not isinstance(array, list):

            raise Exception('The data must be a list of python.')

        self.queue = array
    
    def push(self, value):
        self.queue.append(value)   
         
    def pop(self):
        return self.queue.pop(0)
        
    def get_size(self):
        return len(self.queue)
    
    def get_list(self):
        return self.queue
    
    def get_index(self, value):
        return self.queue.index(value)
    
    def get(self, index):
        return self.queue[index]
        
    
