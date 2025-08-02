import unittest
import os
from core.manager import NoteManager

class TestNoteManager(unittest.TestCase):
    def setUp(self):
        self.manager = NoteManager()
        self.test_title = "Test Note"
        self.test_content = "This is a test content"
        self.path = self.manager.get_note_path(self.test_title)
        
        if self.path.exists():
            self.path.unlink()
            
    def test_add_note(self):
        self.manager.add_note(self.test_title,self.test_content)
        self.assertTrue(self.path.exists())
        
    def test_view_note(self):
        self.manager.add_note(self.test_title,self.test_content)
        try:
            self.manager.view_note(self.test_title)
        except Exception as e:
            self.fail(f"view_note() raised Exception unexpectedly: {e}")
            
    def test_delete_note(self):
       self.manager.add_note(self.test_title,self.test_content)
       self.manager.delete_note(self.test_title)
       self.assertFalse(self.path.exists())
       
    def tearDown(self):
        if self.path.exists():
            self.path.unlink()
            

if __name__ == "__main__":
    unittest.main()
        