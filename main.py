from typing import List

from fastapi import FastAPI

from App import create_app_list
from LearningRes import learning_resources, LearningRes

app = FastAPI()


@app.get("/app-list")
def read_root():
    return {"apps": create_app_list()}


@app.get("/learning_resources", response_model=List[LearningRes])
def get_learning_resources():
    return learning_resources
