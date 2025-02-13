#working solution for paralleel processing problem.
import heapq

class Node:
    def __init__(self, thread, time):
        self.thread = thread
        self.time = time
    
class ThreadNode(Node):
    def __lt__(self, other):
        return self.thread < other.thread
    
class JobNode(Node):
    def __lt__(self, other):
        return self.time < other.time
    
threadHeap = []
jobHeap = []
job_start_record = []

thread_details = list(map(int, input().split()))
no_of_threads = thread_details[0]
no_of_jobs = thread_details[1]
all_jobs = list(map(int, input().split()))

for i in range(0,no_of_threads):
    heapq.heappush(threadHeap, ThreadNode(thread=i, time=0))

current_time = 0
while len(all_jobs)>0 or len(jobHeap)>0 :

    while len(threadHeap) > 0 and len(all_jobs) >0:
            thread_instance = heapq.heappop(threadHeap)
            heapq.heappush(jobHeap, JobNode(thread=thread_instance.thread, time=current_time+all_jobs.pop(0)))
            print(f"{thread_instance.thread} {current_time}")

    if len(jobHeap) > 0: 
        current_time = jobHeap[0].time

    if len(jobHeap) > 0:
        while jobHeap[0].time == current_time:
            job_instance = heapq.heappop(jobHeap)
            heapq.heappush(threadHeap, ThreadNode(thread=job_instance.thread, time=current_time)) 
            if len(jobHeap) == 0:
                break

