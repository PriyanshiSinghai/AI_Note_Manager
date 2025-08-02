from pathlib import Path
from core.notes import Note
import requests
import os
import logging
from functools import wraps
from dotenv import load_dotenv
load_dotenv()

logging.basicConfig(
    filename="/Users/psinghai/Dream_AI/Projects/AI_note_manager/data/notes/activity.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def log_action(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        logging.info(f"Called {func.__name__} with args {args[1:]}, kwargs:{kwargs}")
        return func(*args,**kwargs)
    return wrapper
    
class NoteManager:
    def __init__(self):
        self.notes_dir = Path("/Users/psinghai/Dream_AI/Projects/AI_note_manager/data/notes")
        self.notes_dir.mkdir(parents=True,exist_ok=True)

    def get_note_path(self,title: str):
        safe_title = title.replace(" ","_").lower()
        return self.notes_dir / f"{safe_title}.txt"
    
    @log_action
    def add_note(self,title: str, content: str):
        note = Note(title,content) 
        note_path = self.get_note_path(title)
        with open(note_path,"w") as f:
            f.write(note.content)
        print(f"Note {title} saved.")
    
    @log_action    
    def view_note(self,title: str):
        note_path = self.get_note_path(title) 
        if not note_path.exists():
            print(f"Note {title} not found.")
            return
        with open(note_path,"r") as f:
            content = f.read()
        note = Note(title,content) 
        print(note.display()) 
    
    @log_action
    def delete_note(self,title):
        note_path = self.get_note_path(title)
        if note_path.exists():
            note_path.unlink()
            print(f"Note {title} deleted")
        else:
            print(f"Note {title} not found")
    
    @log_action    
    def list_note(self):
        notes = list(self.notes_dir.glob("*.txt"))
        if not notes:
            print("No notes found.")
            return
        print("Youre notes: ")
        for note_file in notes:
            print("-", note_file.stem.replace("_"," "))
    
    @log_action        
    def summarize_note(self,title):
        note_path = self.get_note_path(title)
        if not note_path.exists():
            print(f"Note {title} not found")
            return
        with open(note_path,"r") as f:
            content = f.read()
            
        hf_api_keys = os.getenv("HF_API_KEY")
        headers = {
            "Authorization": f"Bearer {hf_api_keys}",
            "Content-Type": "application/json"
        }
        
        data = {"inputs": content}
        url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
        
        try:
            response = requests.post(url,headers=headers,json=data,timeout=60)
            response.raise_for_status()
            summary = response.json()[0]["summary_text"]
            print("Summary")
            print(summary)
        except Exception as e:
            print(f"failed to summarise: {e}")
            logging.error(f"Error summarizing note '{title}': {e}")
        