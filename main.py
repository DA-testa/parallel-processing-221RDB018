# python3
import heapq

def main():

    n, m = map(int, input().split()) 
    processing_times = list(map(int, input().split()))

    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)

    start_times = []

    for i in range(m):
        free_time, thread_idx = heapq.heappop(threads)   
        start_times.append((thread_idx, free_time))
        free_time += processing_times[i]
        heapq.heappush(threads, (free_time, thread_idx))

    for thread_idx, start_time in start_times:
        print(thread_idx, start_time)


if __name__ == "__main__":
    main()





# def parallel_processing(n, m, data):
#     output = []
#     # TODO: write the function for simulating parallel tasks, 
#     # create the output pairs

#     return output

# def main():
#     # TODO: create input from keyboard
#     # input consists of two lines
#     # first line - n and m
#     # n - thread count 
#     # m - job count
#     n = 0
#     m = 0

#     # second line - data 
#     # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
#     data = []

#     # TODO: create the function
#     result = parallel_processing(n,m,data)
    
#     # TODO: print out the results, each pair in it's own line



# if __name__ == "__main__":
#     main()
