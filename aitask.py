
class AITask:
    def __init__(self, user: str, prompt: str, tasktype: str) -> None:
        self.user = user
        self.prompt = prompt
        self.tasktype = tasktype

    def process(self) -> dict:
        # LLM action can be added here later
        return {
            "user": self.user,
            "prompt": self.prompt,
            "task_type": self.tasktype,
            "status": "completed",
            "message": f"Task received: {self.prompt}"
        }

    def __str__(self) -> str:
        return f"{self.user}, {self.tasktype}"
