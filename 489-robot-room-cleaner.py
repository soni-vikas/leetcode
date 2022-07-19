# https://leetcode.com/problems/robot-room-cleaner/

# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
# class Robot:
#    def move(self):
#        """
#        Returns true if the cell in front is open and robot moves into the cell.
#        Returns false if the cell in front is blocked and robot stays in the current cell.
#        :rtype bool
#        """
#
#    def turnLeft(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def turnRight(self):
#        """
#        Robot will stay in the same cell after calling turnLeft/turnRight.
#        Each turn will be 90 degrees.
#        :rtype void
#        """
#
#    def clean(self):
#        """
#        Clean the current cell.
#        :rtype void
#        """


class Solution:
    # assigning an index to each direction
    dir_index = {
        "U": 0,
        "L": 1,
        "D": 2,
        "R": 3,
    }

    def cleanRoom(self, robot, i=0, j=0, visited=None, direction=None):
        """
        :type robot: Robot
        :rtype: None
        """
        if visited is None:
            visited = set()
            direction = {"dir": 0}

        if (i, j) in visited:
            return

        visited.add((i, j))
        robot.clean()

        if self.moveUp(robot, direction):
            self.cleanRoom(robot, i - 1, j, visited, direction)
            self.moveDown(robot, direction)

        if self.moveLeft(robot, direction):
            self.cleanRoom(robot, i, j - 1, visited, direction)
            self.moveRight(robot, direction)

        if self.moveDown(robot, direction):
            self.cleanRoom(robot, i + 1, j, visited, direction)
            self.moveUp(robot, direction)

        if self.moveRight(robot, direction):
            self.cleanRoom(robot, i, j + 1, visited, direction)
            self.moveLeft(robot, direction)

    def moveUp(self, robot, direction):
        return self.updateDirectionAndMove(robot, direction, "U")

    def moveDown(self, robot, direction):
        return self.updateDirectionAndMove(robot, direction, "D")

    def moveLeft(self, robot, direction):
        return self.updateDirectionAndMove(robot, direction, "L")

    def moveRight(self, robot, direction):
        return self.updateDirectionAndMove(robot, direction, "R")

    def updateDirectionAndMove(self, robot, direction, target_direction):
        # finding minimum rotation needed for bot to be on target direction
        rotate_count = (direction["dir"] - self.dir_index[target_direction]) % 4
        for _ in range(rotate_count):
            robot.turnRight()

        direction["dir"] = self.dir_index[target_direction]
        return robot.move()
