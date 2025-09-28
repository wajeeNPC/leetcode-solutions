
- Each folder represents a single LeetCode problem.  
- Folder names include the **problem number and title**.  
- `solution.py` contains the solution in Python.  

---

## How to Run

1. Open the folder in **VS Code** or any Python IDE.  
2. Run the solution by creating an instance of the `Solution` class and calling the method:

```python
from solution import Solution

nums = [2, 7, 11, 15]
target = 9
solution = Solution()
print(solution.twoSum(nums, target))  # Output: [0, 1]
