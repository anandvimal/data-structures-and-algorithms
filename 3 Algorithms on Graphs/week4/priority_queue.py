import heapq

# Heap and a mapping for priorities
heap = []
priorities = {}

def add_task(priority, task):
    heapq.heappush(heap, (priority, task))
    priorities[task] = priority

def update_priority(task, new_priority):
    global heap
    if task in priorities:
        del priorities[task]
        heap = [(p, t) for p, t in heap if t != task]
        heapq.heapify(heap)
    add_task(new_priority, task)

add_task(5, 'task1')
add_task(2, 'task2')
add_task(8, 'task3')

update_priority('task1', 1)

print(heap)

