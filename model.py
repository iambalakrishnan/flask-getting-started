"""
model.py
---------
Implements the model for our website by simulating a database.

Note: Although this is nice as a simple, don't do this in a real-world production settings.
Having a global object for application data is asking for trouble.
Instead, use a real database layer, like https://flask-sqlalchemy.palletsprojects.com/en/2.x/
"""

import json


def load_db():
    with open("flashcards_db.json") as f:
        return json.load(f)


def save_db():
    with open("flashcards_db.json", 'w') as f:
        return json.dump(db, f)


db = load_db()
