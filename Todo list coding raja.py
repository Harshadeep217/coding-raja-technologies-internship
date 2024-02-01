import datetime


class Task:
    def __init__(self, description, priority, due_date):
        self.description = description
        self.priority = priority
        self.due_date = due_date
        self.is_done = False

    def __str__(self):
        return f"{self.description} ({self.priority}, due: {self.due_date})"


class ToDoList:
    def __init__(self, filename):
        self.filename = filename
        self.tasks = self._load_tasks()

    def _load_tasks(self):
        tasks = []
        try:
            with open(self.filename, "r") as f:
                for line in f:
                    description, priority, due_date_str = line.strip().split(",")
                    due_date = datetime.datetime.strptime(due_date_str, "%Y-%m-%d").date()
                    task = Task(description, priority, due_date)
                    tasks.append(task)
        except FileNotFoundError:
            pass
        return tasks

    def _save_tasks(self):
        with open(self.filename, "w") as f:
            for task in self.tasks:
                line = f"{task.description},{task.priority},{task.due_date.strftime('%Y-%m-%d')}\n"
                f.write(line)

    def add_task(self, description, priority, due_date):
        task = Task(description, priority, due_date)
        self.tasks.append(task)
        self._save_tasks()

    def remove_task(self, description):
        for task in self.tasks:
            if task.description == description:
                self.tasks.remove(task)
                self._save_tasks()
                return

        print(f"Task '{description}' not found.")

    def mark_done(self, description):
        for task in self.tasks:
            if task.description == description:
                task.is_done = True
                self._save_tasks()
                return

        print(f"Task '{description}' not found.")

    def list_tasks(self):
        print("To-Do List:")
        for task in self.tasks:
            done_str = "Done" if task.is_done else "Pending"
            print(f"- {task} ({done_str})")



