from fastapi import APIRouter, Request, Form, Response, status
from fastapi.responses import RedirectResponse
from fastapi.templating import Jinja2Templates

from src.db.history import HistoryService, History
from sqlalchemy import text

router = APIRouter(tags=["Main"])

templates = Jinja2Templates(directory="src/templates")


@router.get("/")
async def main_page(request: Request):
    return templates.TemplateResponse("calculator.html", {"request": request})


@router.get("/history")
async def history_page(request: Request, username: str = None, operation: str = None):
    history = HistoryService.get_all_history()
    conditions = []
    if username:
        conditions.append(f"username ILIKE '%{username}%'")
    if operation:
        conditions.append(f"expression LIKE '%{operation}%'")
    if conditions:
        query = " WHERE " + " AND ".join(conditions)
        history = HistoryService.get_any_history(query)
    return templates.TemplateResponse("history.html", {"request": request, "history": history})


@router.post("/add")
async def add_to_db(request: Request):
    request_data = await request.json()
    history = History(username=request_data["username"], expression=request_data["expression"],
                      result=request_data["result"])
    HistoryService.add_history(history)
