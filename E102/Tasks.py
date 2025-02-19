
class Tasks:
    def __init__(self):
        self.task_list = []

    def get_item(self, index):
        return self.task_list[index]

    def add(self, task):
        self.task_list.append(task)

    def add_all(self, tasks):
        for task in tasks:
            self.add(task)

    def get_index(self, task):
        return self.task_list.index(task)

    def update(self, index, task):
        self.task_list[index] = task
        return self.task_list[index]

    def remove_by_index(self, index):
        return self.task_list.pop(index)

    def remove_by_item(self, item):
        self.task_list.remove(item)

    def clear(self):
        self.task_list.clear()

    def size(self):
        return len(self.task_list)
