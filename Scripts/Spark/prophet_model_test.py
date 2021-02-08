from pymongo import MongoClient
from fbprophet import Prophet
import pandas as pd

client = MongoClient('localhost', 27017)
db = client['Bitcoin']
df = pd.DataFrame(db.data.find())
df = df[["timestamp", "price_usd"]][:50]
df.rename(columns={'timestamp': 'ds', 'price_usd': 'y'}, inplace=True)

model = Prophet()
model.fit(df)

future_pd = model.make_future_dataframe(periods=1, freq='T')
forecast_pd = model.predict(future_pd)

f_pd = forecast_pd[['ds', 'yhat', 'yhat_upper', 'yhat_lower']].set_index('ds')
b_pd = df[['ds', 'y']].set_index('ds')

results_pd = f_pd.join(b_pd, how='left')
results_pd.reset_index(level=0, inplace=True)

print(results_pd[['ds', 'y', 'yhat', 'yhat_upper', 'yhat_lower']])