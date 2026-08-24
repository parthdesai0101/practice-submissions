from sortedcontainers import SortedList
from collections import defaultdict

class TodoList:
    def __init__(self):
        self.i = 1
        self.tasks = defaultdict(SortedList) #hashset with sortedlist as values
    
    def addTask(self, userId: int, taskDescription: str, dueDate: int, tags: List[str]) -> int:
        taskId = self.i
        self.i += 1
        self.tasks[userId].add([dueDate, taskDescription, set(tags), taskId, False])
        return taskId
    def getAllTasks(self, userId: int) -> List[str]:
        return [x[1] for x in self.tasks[userId] if not x[4]]
    def getTasksForTags(self, userId: int, tag: str) -> List[str]:
        tag_tasks = []
        for task in self.tasks[userId]:
            if tag in task[2] and not task[4]:
                tag_tasks.append(task[1])
        return tag_tasks
    def completeTask(self, userId: int, taskId: int) -> None:
        for task in self.tasks[userId]:
            if task[3] == taskId:
                task[4] = True
                break
            
