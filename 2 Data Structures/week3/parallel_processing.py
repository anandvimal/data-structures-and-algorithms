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
# heapq.heappush(threadHeap, ThreadNode(thread=0,time=0))
# heapq.heappush(threadHeap, ThreadNode(thread=1,time=0))
# heapq.heappush(threadHeap, ThreadNode(thread=2,time=0))

#obj = heapq.heappop(threadHeap)
#print(f"obj : obj.thread:{obj.thread} obj.time:{obj.time}")

thread_details = list(map(int, input().split()))
no_of_threads = thread_details[0]
no_of_jobs = thread_details[1]
all_jobs = list(map(int, input().split()))
print(f"threads : {no_of_threads}")
print(f"# of jobs : {no_of_jobs}")
print(f"all jobs : {all_jobs}")

for i in range(0,no_of_threads):
    heapq.heappush(threadHeap, ThreadNode(thread=i, time=0))

current_time = 0
while len(all_jobs)>0 or len(jobHeap)>0 :
    print(f"no of threads: {len(threadHeap)}")
    print(f"no of jobs running: {len(jobHeap)}")
    while len(threadHeap) > 0 and len(all_jobs) >0:
            thread_instance = heapq.heappop(threadHeap)
            heapq.heappush(jobHeap, JobNode(thread=thread_instance.thread, time=current_time+all_jobs.pop(0)))
            job_start_record.append(f"thread:{thread_instance.thread} at time:{current_time}")
    #now we check the time left in jobs:
    print("-------------------------------------")
    print(f"no of free threads: {len(threadHeap)}")
    print(f"no of running jobs with threads: {len(jobHeap)}")
    current_time = current_time + 1

    if len(jobHeap) > 0:
        while jobHeap[0].time == current_time:
            job_instance = heapq.heappop(jobHeap)
            heapq.heappush(threadHeap, ThreadNode(thread=job_instance.thread, time=current_time)) 
            if len(jobHeap) == 0:
                break

    #break
print(job_start_record)