# python3
import math

class Node:
    def __init__(self, id: int) -> None:
       self.id: int = id
       self.process_timer: int = 0

    def process(self, job: int) -> None:
       self.process_timer += job

    def get_id(self) -> None:
       return self.id
    
    def get_current_timer(self) -> None:
       return self.process_timer
    
    def __repr__(self) -> str:
       return f"ID = {self.id}, Timer = {self.process_timer}"

class JobQueue:
    def read_data(self):
        self.num_workers, m = map(int, input().split())
        self.jobs = list(map(int, input().split()))
        self.assigned_workers = [None] * len(self.jobs)
        self.start_times = [None] * len(self.jobs)
        self.max_size_idx = self.num_workers - 1
        assert m == len(self.jobs)

    def write_response(self):
        for i in range(len(self.jobs)):
            print(self.assigned_workers[i], self.start_times[i]) 
    
    def parent(self, i):
        return math.floor((i - 1)/2)
    
    def left_child(self, i):
        return 2*i + 1
    
    def right_child(self, i):
        return 2*i + 2
    
    def sift_down(self, i):
        max_idx = i
        left = self.left_child(i)
        if left <= self.max_size_idx:
            if self.nodes[left].process_timer < self.nodes[max_idx].process_timer:
                max_idx = left
            elif self.nodes[left].process_timer == self.nodes[max_idx].process_timer:
                if self.nodes[left].id < self.nodes[max_idx].id:
                    max_idx = left
        right = self.right_child(i)
        if right <= self.max_size_idx:
            if self.nodes[right].process_timer < self.nodes[max_idx].process_timer:
                max_idx = right
            elif self.nodes[right].process_timer == self.nodes[max_idx].process_timer:
                if self.nodes[right].id < self.nodes[max_idx].id:
                    max_idx = right
        if i != max_idx:
            self.nodes[max_idx], self.nodes[i] = self.nodes[i], self.nodes[max_idx]
            self.sift_down(max_idx)
    
    def assign_jobs(self):
        self.nodes = [Node(id=x) for x in range(self.num_workers)]
        for i in range(len(self.jobs)):
            self.assigned_workers[i] = self.nodes[0].id
            self.start_times[i] = self.nodes[0].process_timer
            self.nodes[0].process_timer += self.jobs[i]
            self.sift_down(0)

    def solve(self):
        self.read_data()
        self.assign_jobs()
        self.write_response()

if __name__ == '__main__':
    job_queue = JobQueue()
    job_queue.solve()