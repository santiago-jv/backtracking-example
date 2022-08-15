from classes.queue import  Queue
from classes.stack import  Stack
import coloring

initial_state = Queue([
    coloring.colorize('Y', 'yellow'),
    coloring.colorize('B', 'blue'),
    coloring.colorize('R', 'red'),
])
result = Stack()
length_data = initial_state.get_size()


def show_result(result:Stack):
    print(*result.get_list(), sep = " ")

def back(depth:int, length_data:int, current_state:Queue, result:Stack):
    if(depth == length_data):
        show_result(Stack(result.get_list()))    
    else:
        for index in range(depth, length_data):
            result.push(current_state.pop())
            back(depth+1,length_data, current_state, result)
            current_state.push(result.pop())


back(0,length_data, initial_state, result)
