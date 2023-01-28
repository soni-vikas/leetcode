class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        """
        A.............B...............Destination

        explaination: x..........y...........z........destination
        if y can catch-up z and x can catch-up y, then x must catch-up z.
        push z onto the stack
        if y can cross the z, ignore y putting into the stack since it is making a car fleet at z. 
        perform the same logic for x.......................z........destination.
        if x can't cross z, put x also in the stack. 
        """

        z = sorted([(p, s) for p, s in zip(position, speed)], reverse=True)

        stack = []
        for p, s in z:
            if not stack:
                stack.append((p, s))
            else:
                a_time_to_reach_destination = (target - p) / s
                b_time_to_reach_destination = (target - stack[-1][0]) / stack[-1][1]
                if b_time_to_reach_destination < a_time_to_reach_destination:
                    stack.append((p, s))

        return len(stack)
