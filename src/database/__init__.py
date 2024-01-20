import sqlite3

class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
    
    def add_user(self, user_id, user):
        raise NotImplementedError
    
    def get_user(self, user_id) -> :
        raise NotImplementedError
    
    def add_quote(self, quote: str):
        raise NotImplementedError
    
    def get_quote(self, quote_id: str):
        raise NotImplementedError