from ninja import Schema
from datetime import datetime


class MemoRequest(Schema):
    title: str
    content: str


class MemoResponse(MemoRequest):
    id: int
    created_at: datetime


