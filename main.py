import seaborn as sns
import pandas as pd
from fastapi import FastAPI,Request
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse


app = FastAPI()

template = Jinja2Templates(directory='templates')

df = sns.load_dataset('titanic')
y = df["survived"]
features = ["pclass", "sex", "sibsp", "parch"]
X = pd.get_dummies(df[features])

@app.get("/",response_class=HTMLResponse)
def get_homepage(request:Request):
    return template.TemplateResponse('index.html',{"request":request})

@app.get("/values")
def get_values():
    values = {}
    for column in  X.columns:
        values.update({column:set(X[column].to_list())})
    return values
        
    