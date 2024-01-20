from dataclasses import dataclass

@dataclass
class quote:
    id: int
    quote_text: str
    user_id: int
    timestamp: int