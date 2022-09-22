
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

template = Jinja2Templates(directory='templates')

@app.get("/",response_class=HTMLResponse)
def get_homepage(request:Request):
    return template.TemplateResponse('index.html',{"request":request})
