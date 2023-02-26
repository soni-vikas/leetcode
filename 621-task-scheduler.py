from typing import List


class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Case 1: find the idle time. [A, A, A, B, B, C], n = 2
            3A, 2B, 1C
    
            Arrange max elements n distance apart. 
            A . . A . . A
            
            Try to arrange non-max-element in the void space. 
            if there is less non-max-elements than free space, CPU would remain idle (#) in those time unit.   
            A B C A B # A 
            
            return length of the sequence. 
        
        Case 2: if there are more than one max_count_task. i.e. [A A A B B B C], n = 2
            Arrange max elements such that same tasks are n distance apart. 
            A B . A B . A B
            
            Fill the remaining spaces with non-max-elements & idle (#). 
            A B C A B # A B
            return length of the sequence.
            
        Case 3: non-max-elements are greater than free space. [A A A B C D E F], n = 2
            Arrange max elements such that same tasks are n distance apart.
            A . . A . . A
            
            Fill the remaining spaces with non-max-elements & idle (#). 
            A B C A D E A
            
            F is the remaining element
            return length of the sequence. + count of remaining element. 
        
        
        """
        count_map = {}
        for t in tasks:
            count_map[t] = count_map.get(t, 0) + 1

        max_count = 0
        max_count_tasks = []
        for k, v in count_map.items():
            if v > max_count:
                max_count = v
                max_count_tasks = [k]

            elif v == max_count:
                max_count_tasks.append(k)

        partitions = max_count - 1
        free_space = partitions * (n - (len(max_count_tasks) - 1))
        non_max_count = len(tasks) - len(max_count_tasks) * max_count
        return (n + 1) * partitions + len(max_count_tasks) + max(0, non_max_count - free_space)
