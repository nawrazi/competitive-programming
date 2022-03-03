# https://leetcode.com/problems/employee-importance/submissions/

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emp_map = {}
        for employee in employees:
            emp_map[employee.id] = employee

        def totalImportance(employee):
            importance = employee.importance
            for sub_id in employee.subordinates:
                importance += totalImportance(emp_map[sub_id])
            return importance

        return totalImportance(emp_map[id])
