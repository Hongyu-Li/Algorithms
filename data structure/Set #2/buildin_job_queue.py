# python3
import heapq

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
          print(self.assigned_workers[i], self.start_times[i]) 

    def assign_jobs(self):
        self.start_times=[]
        self.assigned_workers=[0]*len(self.jobs)
        self.d2=[]
        self.next_value=[0,0]
        self.ind=[i for i in range(1,self.num_workers)]
        for i in range(len(self.jobs)):
            self.assigned_workers[i]=self.next_value[1]
            self.start_times.append(self.next_value[0])
            self.next_value=[self.start_times[i]+self.jobs[i],self.assigned_workers[i]]
            heapq.heappush(self.d2,list(self.next_value))
            if self.next_value[0]!=0 and len(self.d2) < self.num_workers:
                self.next_value[1]=int(self.ind.pop(0))
                self.next_value[0]=0
            elif self.next_value[0]==0 and len(self.d2) < self.num_workers:
                self.d2.pop(0)
            elif self.next_value[0]!=0 and len(self.d2) >= self.num_workers:
                self.next_value=heapq.heappop(self.d2)
            elif self.next_value[0]==0 and len(self.d2) >= self.num_workers:
                self.d2.pop(0)
            
     
    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()
