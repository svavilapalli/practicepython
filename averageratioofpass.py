# There is a school that has classes of students and each class will be having a final exam. You are given a 2D integer array classes, where classes[i] = [passi, totali]. You know beforehand that in the ith class, there are totali total students, but only passi number of students will pass the exam.
# You are also given an integer extraStudents. There are another extraStudents brilliant students that are guaranteed to pass the exam of any class they are assigned to. You want to assign each of the extraStudents students to a class in a way that maximizes the average pass ratio across all the classes.
# The pass ratio of a class is equal to the number of students of the class that will pass the exam divided by the total number of students of the class. The average pass ratio is the sum of pass ratios of all the classes divided by the number of the classes.
# Return the maximum possible average pass ratio after assigning the extraStudents students. Answers within 10-5 of the actual answer will be accepted.


class Solution:
    def maxAverageRatio(self, classes: List[List[int]], extraStudents: int) -> float:
        classheap = [ ((p/t)-((p+1)/(t+1)),p,t) for p,t in classes]
        heapq.heapify(classheap)
        for v in range(extraStudents):
            r, p, t = heapq.heappop(classheap)
            ch = ((p+1)/(t+1))-((p+2)/(t+2))
            heapq.heappush(classheap,(ch,p+1, t+1))
        tr = 0
        for r,p,t in classheap:
            tr += (p/t)
        return tr/len(classes)

  if __name__ == "__main__":
      s = Solution()
      classes = [[1,2],[3,5],[2,2]]
      extraStudents = 2
      print("Expected Output: 0.78333")
      print("Actual Output:", s.maxAverageRatio(classes, extraStudents))
