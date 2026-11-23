"""
Code to fill the database with sample data.
Run once on an empty database: python fill_data.py
"""

from database import init_db, session

# Initialize our database
init_db()