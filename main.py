from pydoc import plain
import seaborn as sns
import pandas as pd
from pydantic import BaseModel
from fastapi import FastAPI,Request,Form
from fastapi.templating import Jinja2Templates
from fastapi.responses import HTMLResponse
from sklearn.ensemble import RandomForestClassifier

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


@app.post("/predict",status_code=200)
def get_predict(request:Request,pclass:int=Form(),sibsp:int=Form(),parch:int=Form(),sex:str=Form()):
    sex_female = 1 if sex == 'female' else 0
    sex_male = 1 if sex == 'male' else 0
    row = pd.DataFrame({"pclass":[pclass],"sibsp" :[sibsp], "parch" :[parch], "sex_female" :[sex_female], "sex_male":[sex_male]})
    model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
    model.fit(X, y)
    prediction = model.predict(row)
    status = 'survived' if prediction[0] == 1 else 'death'
    return template.TemplateResponse('prediction.html',{'request':request,'pclass':pclass,'sibsp':sibsp,'parch':parch,'sex':sex,'prediction':status})