from .models import Memo
from ninja import NinjaAPI
from django.shortcuts import get_object_or_404

from .schema import MemoResponse, MemoRequest

api = NinjaAPI()


@api.get("/memos", response=list[MemoResponse])
def list_memos(request):
    memos = Memo.objects.all()
    return memos


@api.post("/memos", response=MemoResponse)
def create_memo(request, payload: MemoRequest):
    memo = Memo.objects.create(**payload.dict())
    return memo


@api.get("/memos/{memo_id}", response=MemoResponse)
def get_memo(request, memo_id: int):
    memo = get_object_or_404(Memo, id=memo_id)
    return memo


@api.put("/memos/{memo_id}", response=MemoResponse)
def update_memo(request, memo_id: int, payload: MemoRequest):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.title = payload.title
    memo.content = payload.content
    memo.save()
    return memo


@api.delete("/memos/{memo_id}")
def delete_memo(request, memo_id: int):
    memo = get_object_or_404(Memo, id=memo_id)
    memo.delete()
    return {"success": True}
