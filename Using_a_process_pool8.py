import time
from fastapi import FastAPI, APIRouter
import multiprocessing
from pydantic import BaseModel
from typing import List


router = APIRouter()



#این همون خروجی رو میده بهمون

class ResultModel(BaseModel):
    results: List[int]

def function_square(data):
    result = data * data
    return result

def calculate_squares(inputs):
    with multiprocessing.Pool(processes=4) as pool:
        pool_outputs = pool.map(function_square, inputs)
    return pool_outputs

@router.post("/scenario2_8_1", response_model=ResultModel)
def get_squares():
    inputs = list(range(0, 100))  # List of integers from 0 to 99
    results = calculate_squares(inputs)
    return {"results": results}





#توی این کد من اومدم ورودی هارو به توان رسوندم که مجموع مربعات رو بهم بده

class ResultModel(BaseModel):
    results: List[int]

def function_cube(data):
    result = data ** 3
    return result

def calculate_results(inputs, func):
    with multiprocessing.Pool(processes=4) as pool:
        pool_outputs = pool.map(func, inputs)
    return pool_outputs

@router.post("/scenario2_8_2", response_model=ResultModel)
def get_results():
    inputs = list(range(0, 100))  # List of integers from 0 to 99
    results = calculate_results(inputs, function_cube)  # Use the function_cube here
    return {"results": results}



#اینجا اومدم اول اعداد رو ضرب کردم بعد با همون ورودی جمع کردم و بازه رو هم از 100 به 50 تغیر دادم

class ResultModel(BaseModel):
    results: List[int]

def function_square(data):
    result = data * data + data
    return result

def calculate_results(inputs, func):
    with multiprocessing.Pool(processes=4) as pool:
        pool_outputs = pool.map(func, inputs)
    return pool_outputs

@router.post("/scenario2_8_3", response_model=ResultModel)
def get_results():
    inputs = list(range(0, 50))
    results = calculate_results(inputs, function_square)  # Use the modified function_square here
    return {"results": results}









#
# def function_square(data):
#     result = data * data
#     return result
#
# def calculate_squares(inputs):
#     pool = multiprocessing.Pool(processes=4)
#     pool_outputs = pool.map(function_square, inputs)
#     pool.close()
#     pool.join()
#     return pool_outputs
#
# @router.post("/calculate_squares")
# def get_squares():
#     inputs = list(range(0, 100))
#     results = calculate_squares(inputs)
#     return {"results": results}
#
