from fastapi import FastAPI,Path
from pydantic import BaseModel

app=FastAPI()

class Employee(BaseModel):
    name:str
    role:str

employee = {
    1:{
        "name": "Ganesh",
        "role": "Tester"
    },
    2:{
        "name": "Mani",
        "role": "Tester"
    }
}
@app.get("/test/{employe_id}")
def test(employe_id:int =  Path(description = "ID is required", gt=0 , le=3)):
    if employe_id in employee:
        return employee[employe_id]
    return {"Data":"Not found"}

@app.get("/query/{employe_id}")
def get_by_query(employe_id:int, name:str):
    for employe_id in employee:
        if employee[employe_id]["name"] == name:
            return employee[employe_id]
        return {"name": "Not Found"}
    return {"Data":"Not found"}

@app.post("/post/{employe_id}")
def create(employe_id:int, employe:Employee):
    if employe_id in employee:
        return {"Employee":"ID already exsists"}
    employee[employe_id] = employe
    return employee[employe_id]

@app.put("/update/{employe_id}")
def update(employe_id:int, employe:Employee):
    if employe_id not in employee:
        return {"Employee":"NOt exsists"}
    return employee[employe_id]
@app.delete("/delete/{employe_id}")
def delete_employee(employe_id:int):
    if employe_id not in employee:
        return {"Error":"Student doesn't exists"}
    del employee[employe_id]
    return {"Employee":"Deleted"}





