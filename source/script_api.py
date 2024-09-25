from typing import Union
from fastapi import FastAPI 
import requests

app = FastAPI()

@app.get("/")
def get_data_gouv():
    url = "https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets"
    
    response = requests.get(url)
    
    if response.status_code == 200:
        return response.json()
    else:
        return {"erreur": "marche pas"}


@app.get("/telecharge")
def download_data():
    url = "https://data.culture.gouv.fr/api/explore/v2.1/catalog/datasets"
    
    data = requests.get(url)
    data_dict.json.loads(data)
    pd.dataframe(c)
    
