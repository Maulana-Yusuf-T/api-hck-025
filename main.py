from fastapi import FastAPI
import pandas as pd

# create API object
app = FastAPI()

# read data
data = pd.read_csv('data.csv')

# coba membuat root home API (GET)
@app.get("/")
def root():
    return {'message':'Hello World!'}

#endpoint sapaan
@app.get("/name/{name}")
def greet(name):
    return {'message': f'Hai {name}, how are you?'}

# 127.0.0.1:8000/name/yusuf

# endpoint return data
@app.get("/data")
def get_data():
    return data.to_dict(orient='records')

# 127.0.0.1:8000/data # ini muncul error karena harus pakai orient

# get data by id
@app.get("/data/{id}")
def search_data(id:int): # harus bentuknya integer
    result = data[data['id']==id]
    return {'result': result.to_dict(orient='records')}

# http://127.0.0.1:8000/data/3
# http://127.0.0.1:8000/data/docs

# # Menambahkan data
# @app.post("/data/{new_data}")
# def add_data(new_data:str):
#     new_data = new_data.split('-')
#     new_row = {'id':new_data[0],
#                'nama': new_data[1],
#                'age': new_data[2],
#                'job': new_data[3]}
    
#     new_row = pd.DataFrame(new_data)
#     data = pd.concat(data, new_row, ignore_index=True)

#     return {'message':data.to_dict(orient='records'}

# menambahkan data
@app.post("/data/add")
def add_data(new_data:dict):
    global data
    
    new_row = pd.DataFrame([new_data])
    data = pd.concat([data, new_row], ignore_index=True)

    return {'message':data.to_dict(orient='records')}