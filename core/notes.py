from datetime import datetime

class Note:
    def __init__(self,title: str,content: str):
        self.title = title
        self.content = content
        self.created_at = datetime.now()
    
    def display(self) -> str:
        return (
            f"Title: {self.title}",
            f"Date created: {self.created_at.strftime('%Y-%m-%d %H:%M')}\n",
            f"Content: {self.content}"
        ) # type: ignore