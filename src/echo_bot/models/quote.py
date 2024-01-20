from dataclasses import dataclass

@dataclass
class Quote:
    id: int
    quote_text: str
    user_id: int
    timestamp: int