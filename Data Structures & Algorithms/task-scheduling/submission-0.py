from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        given a list of tasks and n
        intuitively
        we want to queue the tasks with more duplicates earlier 

        so our first scan through we collate frequencies of tasks with O(n) time in a hashmap

        then we can use a maxheap to push the tasks

        once pushed, we reappend with the prev freq - 1 to the minheap

        but how do we ensure that it doesnt get executed, and this insertion doesnt block subsequent insertions?

        we can use a queue datastructure with (time, new_freqm data) and globally track time, appending when our time is matched
        if our min heap is empty, we keep adding time until time matches queue and push in min heap again until botht min heap and queue are empty to get time
        """

        task_freq = {}

        #collate frequencies of each task
        for task in tasks:
            task_freq[task] = task_freq.get(task, 0) + 1

        #push these tasks into the initial max_heap in structure (-freq, data)
        heap_task = []
        for task, freq in task_freq.items():
            heap_task.append((-1 * freq, task))
        
        #initialize heap and cooldown queue
        heapq.heapify(heap_task)
        cooldown = deque([])

        #push tasks from maxheap until none remain
        #dequeu elements are saved in (release_time, freq, task)
        time = 0
        while heap_task or cooldown:
            if cooldown:
                #check if heap is empty. if it is, we skip time to next release time
                release_time = cooldown[0][0]

                if not heap_task:
                    time = release_time
                if release_time == time:
                    release_time, freq, task = cooldown.popleft()
                    heapq.heappush(heap_task, (freq, task))

            #pop the highest freq element in the heap
            freq, task = heapq.heappop(heap_task)
            freq += 1

            #push into cooldown queue if still exists
            if freq < 0:
                cooldown.append((time + n + 1, freq, task))
            
            time += 1

        return time
