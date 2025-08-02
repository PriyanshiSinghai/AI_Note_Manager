from core.manager import NoteManager

manager = NoteManager()

# Add a note
title = "Quarterly Review Notes"

content = "In the 2025 quarterly review, we discussed goals, performance metrics, and key KPIs for the product team." 
"The meeting included an analysis of team performance, productivity evaluation, customer feedback, and a review of the competitive landscape."
                 
manager.add_note(title, content)

# View it
manager.view_note(title)

#cList all notes
manager.list_note()

# Summarize it (make sure your HF_API_KEY is set in .env)
manager.summarize_note(title)

# Delete it
# manager.delete_note(title)
