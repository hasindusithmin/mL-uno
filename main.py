
import seaborn as sns
import pandas as pd
from sklearn.ensemble import RandomForestClassifier

df = sns.load_dataset('titanic')

y = df["survived"]
features = ["pclass", "sex", "sibsp", "parch"]
X = pd.get_dummies(df[features])

row = pd.DataFrame({"pclass":[3],"sibsp" :[1], "parch" :[0], "sex_female" :[1], "sex_male":[0]})

model = RandomForestClassifier(n_estimators=100, max_depth=5, random_state=1)
model.fit(X, y)
predictions = model.predict(row)
print(predictions)