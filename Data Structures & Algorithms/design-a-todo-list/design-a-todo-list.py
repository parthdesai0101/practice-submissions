from sortedcontainers import SortedList
from collections import defaultdict
from typing import List

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


class TodoList:
    """A todo list where each task can be nested beneath another task.

    `self.tasks[userId]` stores that user's *root* tasks.  Every task is a
    dictionary with its own sorted `children` list, so together they form a
    forest (a collection of task trees).
    """

    def __init__(self):
        self.next_task_id = 1
        self.tasks = defaultdict(self._new_task_list)

    @staticmethod
    def _new_task_list() -> SortedList:
        # Due date is the main ordering; task ID safely breaks date ties.
        return SortedList(key=lambda task: (task["due_date"], task["task_id"]))

    def addTask(self, userId: int, taskDescription: str, dueDate: int,
                tags: List[str]) -> int:
        task_id = self.next_task_id
        self.next_task_id += 1

        task = {
            "task_id": task_id,
            "description": taskDescription,
            "due_date": dueDate,
            "tags": set(tags),
            "completed": False,
            "parent_id": None,
            "children": self._new_task_list(),
        }
        self.tasks[userId].add(task)
        return task_id

    def _find_task_dfs(self, userId: int, taskId: int):
        """Find a task anywhere in a user's task trees with depth-first search."""
        stack = list(reversed(self.tasks[userId]))

        while stack:
            task = stack.pop()
            if task["task_id"] == taskId:
                return task

            # Reverse before pushing so DFS visits children in due-date order.
            stack.extend(reversed(task["children"]))

        return None

    def _walk_tasks_dfs(self, userId: int):
        """Yield every task in parent-before-child (preorder DFS) order."""
        stack = list(reversed(self.tasks[userId]))

        while stack:
            task = stack.pop()
            yield task
            stack.extend(reversed(task["children"]))

    @staticmethod
    def _contains_task(root, taskId: int) -> bool:
        """Return whether taskId occurs in root's subtree."""
        stack = [root]
        while stack:
            task = stack.pop()
            if task["task_id"] == taskId:
                return True
            stack.extend(task["children"])
        return False

    def setTaskChildren(self, userId: int, taskId: int,
                        childTaskIds: List[int]) -> None:
        """Make `childTaskIds` the direct children of `taskId`.

        A child is removed from its old parent (or from the root list) first.
        Old children of taskId become root tasks.  A task cannot become its own
        child or be placed under one of its descendants, because that would
        create a cycle.
        """
        parent = self._find_task_dfs(userId, taskId)
        if parent is None:
            raise ValueError("Parent task does not exist for this user")
        if len(childTaskIds) != len(set(childTaskIds)):
            raise ValueError("A child task can be listed only once")

        children = []
        for child_id in childTaskIds:
            child = self._find_task_dfs(userId, child_id)
            if child is None:
                raise ValueError("Child task does not exist for this user")
            if child_id == taskId or self._contains_task(child, taskId):
                raise ValueError("Cannot create a cycle in the task tree")
            children.append(child)

        # Children no longer assigned to this parent become root tasks.
        for old_child in list(parent["children"]):
            old_child["parent_id"] = None
            self.tasks[userId].add(old_child)
        parent["children"].clear()

        for child in children:
            old_parent_id = child["parent_id"]
            if old_parent_id is None:
                self.tasks[userId].remove(child)
            elif old_parent_id != taskId:
                old_parent = self._find_task_dfs(userId, old_parent_id)
                old_parent["children"].remove(child)

            child["parent_id"] = taskId
            parent["children"].add(child)

    def getAllTasks(self, userId: int) -> List[str]:
        return [task["description"] for task in self._walk_tasks_dfs(userId)
                if not task["completed"]]

    def getTasksForTags(self, userId: int, tag: str) -> List[str]:
        return [task["description"] for task in self._walk_tasks_dfs(userId)
                if tag in task["tags"] and not task["completed"]]

    def completeTask(self, userId: int, taskId: int) -> None:
        task = self._find_task_dfs(userId, taskId)
        if task is not None:
            task["completed"] = True
