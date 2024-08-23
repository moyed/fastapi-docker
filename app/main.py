# main.py
from fastapi import FastAPI
#import databases
#import sqlalchemy

#DATABASE_URL = "postgresql://postgres:postgres@db:5432/mydatabase"

#database = databases.Database(DATABASE_URL)
#metadata = sqlalchemy.MetaData()

app = FastAPI()

#@app.on_event("startup")
#async def startup():
#    await database.connect()

#@app.on_event("shutdown")
#async def shutdown():
#    await database.disconnect()

@app.get("/")
async def read_root():
    return {"Hello": "World"}