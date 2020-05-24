# python3

from collections import namedtuple
import numpy as np


AssignedJob = namedtuple("AssignedJob", ["worker", "started_at"])


def assign_jobs(n_workers, jobs):
    # TODO: replace this code with a faster algorithm.
    result = []
    next_free_time = [0] * n_workers
    for job in jobs:
        next_worker = min(range(n_workers), key=lambda w: next_free_time[w])
        result.append(AssignedJob(next_worker, next_free_time[next_worker]))
        next_free_time[next_worker] += job

    return result


def assign_jobs_(n_workers, jobs):
    #TODO use min-heap
    #this is not a priority queue implementation but it's valid if n_workers is small which is a practical case
    result = []
    workers = [None] * len(jobs)
    start_times = [None] * len(jobs)
    next_free_time = [0] * n_workers
    for i in range(len(jobs)):
      next_worker = 0
      for j in range(n_workers):
        if next_free_time[j] < next_free_time[next_worker]:
          next_worker = j
      workers[i] = next_worker
      start_times[i] = next_free_time[next_worker]
      next_free_time[next_worker] += jobs[i]
      result.append(AssignedJob(workers[i], start_times[i]))
    return result



def parent(i):
    return (i-1)//2

def right_child(i):
    return 2*i+2

def left_child(i):
    return 2*i+1

def compare_workers(worker1, worker2):
    if worker1[1] != worker2[1]:
        return worker1[1] < worker2[1]
    else:
        return worker1[0] < worker2[0]

def sift_down(i):
    min_index = i
    left = left_child(i)
    if left < n_workers_ and compare_workers(next_free_time[left], next_free_time[min_index]):
        min_index = left
    right = right_child(i)
    if right < n_workers_ and compare_workers(next_free_time[right], next_free_time[min_index]):
        min_index = right
    if i != min_index:
        next_free_time[i], next_free_time[min_index] = next_free_time[min_index], next_free_time[i]
        sift_down(min_index)

def assign_jobs_heap(n_workers, jobs):
    result = []
    global next_free_time
    global n_workers_
    n_workers_ = n_workers
    next_free_time = [[i, 0] for i in range(n_workers)]
    for i in range(len(jobs)):
      result.append(AssignedJob(next_free_time[0][0], next_free_time[0][1]))
      next_free_time[0][1] += jobs[i]
      sift_down(0)
    return result


def main():
    n_workers, n_jobs = map(int, input().split())
    jobs = list(map(int, input().split()))
    assert len(jobs) == n_jobs

    assigned_jobs = assign_jobs_heap(n_workers, jobs)

    for job in assigned_jobs:
        print(job.worker, job.started_at)


if __name__ == "__main__":
    main()
