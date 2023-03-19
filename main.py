import heapq
def parallel_processing(n, m, data):
    output = []
    # TODO: write the function for simulating parallel tasks, 
    # create the output pairs
    threads = [(0, i) for i in range(n)]
    heapq.heapify(threads)
    for i in range(m):
        free_time, thread_idx = heapq.heappop(threads)   
        output.append((thread_idx, free_time))
        free_time += data[i]
        heapq.heappush(threads, (free_time, thread_idx))

    return output

def main():
    n, m = map(int, input().split()) 

    # second line - data 
    # data - contains m integers t(i) - the times in seconds it takes any thread to process i-th job
    data = list(map(int, input().split()))

    # TODO: create the function
    result = parallel_processing(n,m,data)
    
    # TODO: print out the results, each pair in it's own line
    for thread_idx, start_time in result:
        print(thread_idx, start_time)



if __name__ == "__main__":
    main()
