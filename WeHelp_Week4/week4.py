from fastapi import FastAPI, Form,Request
from fastapi.responses import HTMLResponse,RedirectResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates
# 載入typing模組的Anotated工具進行資料驗證 Annotated[資料型態,資料驗證]Annotated標註
from typing import Annotated
# 從 Starlette 匯入應用程式相關的模組，用來處理 請求 (Request) 
# 和 Session (會話) 中介軟體 (Middleware)處理使用者狀態（如登入狀態）
# 登入狀態正確時才會顯示會員頁面
from starlette.applications import Starlette
from starlette.requests import Request
from starlette.middleware import Middleware
from starlette.middleware.sessions import SessionMiddleware

app=FastAPI()
app.add_middleware(SessionMiddleware,secret_key="my_secrect_key")




templates = Jinja2Templates(directory="templates")
@app.get("/")
async def read_homepage(request: Request):
    return templates.TemplateResponse("index.html",{"request":request})

@app.post("/signin")
async def signin(member :Annotated[str,Form()],password : Annotated[str,Form()], request:Request):
    
   # form()是表單的資料驗證，傳送參數進來時要括號
    if not member or not password:
    # ture == not null 
       return RedirectResponse("/error?message=請輸入帳號密碼",status_code=303)
    if member != "test" or password != "test":
       return RedirectResponse("/error?message=帳號、或密碼輸入錯誤",status_code=303)
     # 登入成功後，儲存帳號資訊到 Session（確保有使用者狀態也就是說使用者狀態不為空值）
     # request.session.["member"] 有值並將其儲存到這裡面member key裡面
    request.session["member"] = member
    return RedirectResponse("/member" ,status_code=303)

   
@app.get("/member")
async def read_memberPage(request: Request):
    member =request.session.get("member")
    # 檢查是否有登入，Session 中是否有 'member'這個key裡面是否有值
    # 空值情況下將其重新導向回首頁
    if not member:
        return RedirectResponse("/")
    # 有值的情況下則可正常進入member.html並將此回傳給前端
    return templates.TemplateResponse("member.html", {"request": request})


@app.get("/error")
async def read_memberPage(request: Request , message:str):
    # 將錯誤的要求字串內容在後端列印出來
    print(message)
    return templates.TemplateResponse("error.html",{"request":request , "message":message})

@app.get("/signout")
async def signout(request:Request):
    # 清除session裡面暫存資料把登入狀態清除，也可以理解request.session["member"]裡面為空值
    request.session.clear()
    return RedirectResponse("/" ,status_code=303)

app.mount("/static", StaticFiles(directory="static"), name="static")

# 待完成-計算正整數平方
# @app.get("/square/{number}")
# async def calculate(number):
#     result = number*number
#     return {result}

