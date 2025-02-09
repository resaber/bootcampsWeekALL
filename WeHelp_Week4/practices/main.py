from fastapi import FastAPI,Body,Path,Query
# 載入typing模組的Anotated工具進行資料驗證 Annotated[資料型態,資料驗證]Annotated標註
from typing import Annotated
#預設是由JSONResponse回應
from fastapi.responses import JSONResponse
#回應純文字物件字串
from fastapi.responses import PlainTextResponse
#回應HTML格式
from fastapi.responses import HTMLResponse
#回應file格式和Redirect
from fastapi.responses import FileResponse,RedirectResponse
#處理static files靜態檔案處理方式
from fastapi.staticfiles import StaticFiles
import json
app = FastAPI()#FastAPI物件
# 建立網站首頁
# 利用路由設定，處理路徑 /
# @app.get("/")
# def index():
#     #return JSONResponse物件
#     return  JSONResponse("Hello FastAPI")
# 利用路由設定，處理get方法的路徑 /data
# 處理非靜態檔案擺在上方
@app.get("/data")
def getData():
    return {"data":[1,2,3],"method":"GET"}
#處理post方法的路徑 /data
@app.post("/data")
def postData(body = Body(None)):
    # 後端機會收到前端傳過來的請求文本
    # body = body.decode("utf-8")
    # 將接受到的前端資料再轉換成字典形式出來
    data = json.loads(body)
    # print這邊代表可以先在後端這邊先印出來
    print(data)
    # 回傳給前端的資料包含data["x"]key裡面的value
    return {"data": 0 ,"method":"POST","result":data["x"]}
@app.post("/add")
def postAdd(body = Body(None)):
    # 後端機會收到前端傳過來的請求文本
    # 將接受到的前端資料再轉換成字典形式出來
    data = json.loads(body)
    # print這邊代表可以先在後端這邊先印出來
    # 取兩key的value data["n1"]+data["n2"]
    result = data["n1"]+data["n2"]
    print(data)
    # 回傳給前端的資料包含data["x"]key裡面的value
    return {"data": 0 ,"method":"POST","result":result}

#前端透過網址輸入一個數字，後端把輸入的數字平方，回應給前端
#動態路由，使用路徑參數，處理有相同的前綴字 /square/ 任意整數的路徑
@app.get("/square")
def square(num:Annotated[int,None]):
    #把輸入的字串型態調整成整數
    result = num*num
    return{"data": result}
#處理要求字串的內容參數 /hello?name=名字
@app.get("/hello")
def hello(name):
    message = "Hello,"+name
    return {"message:" : message}
#處理要求字串的參數路徑乘法 /multiply?n1=數字&n2=數字
@app.get("/multiply")
def multiply(n1:Annotated[int,None],n2:Annotated[int,None]):
    result = n1 * n2
    return {"data" : result}

#輸入資料驗證 Path代表隊路徑參數進行資料驗證
@app.get("/square2/{number}")
def square2(
    number:Annotated[int,Path(gt=1,lt=10)]
):
    #把輸入的字串型態調整成整數
    number = int(number)
    return {"result": number*number}

# 輸入資料驗證要求字串Query 乘法 /multiply?n1=數字&n2=數字
@app.get("/multiply2")
def multiply2(
    n1:Annotated[int,Query(ge=1,le=10)],
    n2:Annotated[int,Query(ge=-10,le=10)]
):
    n1 = int(n1)
    n2 = int(n2)
    result = n1 * n2
    return {"result" : result}
#輸入資料驗證 Path代表隊路徑參數進行資料驗證
@app.get("/user2/{account}")
def user2(
    #做事串長度的驗證
    account:Annotated[str,Path(min_length=2,max_length=8)]
):
   
    return {"message": "Hello,"+account}
#處理要求字串資料驗證 /user3?account=帳號
@app.get("/user3")
def user3(
    #做字串長度的驗證
    account:Annotated[str,Query(min_length=2,max_length=8)]
):
    return {"message": "Hello,"+account}
#回應純文字物件字串
@app.get("/text")
def text():
    return PlainTextResponse("Hello FastAPI")
#回應HTML物件
@app.get("/html")
def html():
    #三個###可以寫多行程式碼
    return HTMLResponse("""
        <h2>Hello FastAPI</h2>
        <div>這是一個HTML文件</div>
        <a href="https://www.google.com">Google</a>            
     """)

#回傳RedirectResponse物件，導回到首頁
@app.get("/redirect")
def redirect():
    return RedirectResponse("/")

# static files靜態檔案處理方式 統一大量靜態檔案處理放在最下方以免影響其他路由 FileResponse物件統整免得一個一個要單獨處理
# app.mount("網址路徑前綴",StaticFiles(directory=="靜態檔案路徑(子資料夾名稱)"))所以要的檔案其實是在www資料夾裡面
# html = True抓首頁，會自動對應index.html 非常重要
app.mount("/",StaticFiles(directory="www",html = True))
    