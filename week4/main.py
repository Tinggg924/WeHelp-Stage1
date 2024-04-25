import os
from fastapi import FastAPI, Request, Form, HTTPException, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from pydantic import BaseModel
from typing import Optional

current_dir = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "templates")), name="static")
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

class User(BaseModel):
    username: Optional[str] = None
    password: Optional[str] = None

#定義登錄狀態
sign_in_state = False

#設置登錄狀態
def set_sign_in_state(state: bool):
    global sign_in_state
    sign_in_state = state

#獲取登錄狀態
def get_sign_in_state() -> bool:
    return sign_in_state

@app.get("/", response_class=HTMLResponse)
async def read_root(request: Request):
    return templates.TemplateResponse("Week4.html", {"request": request})

@app.post("/signin")
async def signin(request: Request, username: str = Form(None), password: str = Form(None)):
    if username is None or password is None:
        return RedirectResponse(url="/error?message=請輸入帳號或密碼", status_code=status.HTTP_303_SEE_OTHER)
    if username == "test" and password == "test":
        set_sign_in_state(True)
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    if not get_sign_in_state():
        return RedirectResponse(url="/")
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/signout")
async def signout(request: Request):
    set_sign_in_state(False)
    return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = None):
    if message:
        return templates.TemplateResponse("error.html", {"request": request, "message": message})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "message": "未知錯誤"})