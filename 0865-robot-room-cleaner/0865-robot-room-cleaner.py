# """
# This is the robot's control interface.
# You should not implement it, or speculate about its implementation
# """
#class Robot:
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
    def cleanRoom(self, robot):
        """
        :type robot: Robot
        :rtype: None
        """
        # counter-clockwise
        directions = [(-1, 0), (0, -1), (1, 0), (0, 1)]
        visit = set()
        def go_back():
            robot.turnLeft()
            robot.turnLeft()
            # move to the cell behind
            robot.move()
            robot.turnLeft()
            robot.turnLeft()
        def backtrack(r, c, direction):
            visit.add((r, c))
            robot.clean()

            for i in range(4):
                new_direction = (i + direction) % 4
                new_r = r + directions[new_direction][0]
                new_c = c + directions[new_direction][1]

                if (new_r, new_c) not in visit and robot.move():
                    backtrack(new_r, new_c, new_direction)
                    go_back()
                
                robot.turnLeft()
        backtrack(0, 0, 0)