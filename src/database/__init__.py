import sqlite3
from src.echo_bot.models.users import User
from src.echo_bot.models.quote import Quote

class Database:
    def __init__(self, db_name="database.db"):
        self.db_name = db_name
        self.conn = sqlite3.connect(db_name)
    
    def add_user(self, user: User):
        raise NotImplementedError
    
    def get_user(self, user_id: int) -> User:
        raise NotImplementedError
    
    def add_quote(self, quote: Quote):
        raise NotImplementedError
    
    def get_quote(self, quote_id: str) -> Quote:
        raise NotImplementedError