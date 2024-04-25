import os
from fastapi import FastAPI, Request, Form, status
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
from starlette.applications import Starlette
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

current_dir = os.path.dirname(os.path.realpath(__file__))

app = FastAPI()

app.add_middleware(SessionMiddleware, secret_key="my_secret_key")
app.mount("/static", StaticFiles(directory=os.path.join(current_dir, "templates")), name="static")
templates = Jinja2Templates(directory=os.path.join(current_dir, "templates"))

# 定義登錄狀態
sign_in_state = False

# 設置登錄狀態
def set_sign_in_state(state: bool):
    global sign_in_state
    sign_in_state = state

# 獲取登錄狀態
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
        request.session["sign_in"] = True
        return RedirectResponse(url="/member", status_code=status.HTTP_303_SEE_OTHER)
    else:
        return RedirectResponse(url="/error?message=帳號或密碼輸入錯誤", status_code=status.HTTP_303_SEE_OTHER)

@app.get("/member", response_class=HTMLResponse)
async def member(request: Request):
    sign_in = request.session.get("sign_in", False)
    if not sign_in:
        return RedirectResponse(url="/", status_code=status.HTTP_303_SEE_OTHER)
    return templates.TemplateResponse("member.html", {"request": request})

@app.get("/signout")
async def signout(request: Request):
    request.session["sign_in"] = False
    return RedirectResponse(url="/", status_code=status.HTTP_307_TEMPORARY_REDIRECT)

@app.get("/error", response_class=HTMLResponse)
async def error(request: Request, message: str = None):
    if message:
        return templates.TemplateResponse("error.html", {"request": request, "message": message})
    else:
        return templates.TemplateResponse("error.html", {"request": request, "message": "未知錯誤"})