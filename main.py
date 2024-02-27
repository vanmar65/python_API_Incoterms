# if you want to run this API first start the local server with
# >pip install "fastapi[all]"

# this next command starts the server
# >uvicorn main:app --reload

# some ideas to improve
# todo add table with risks
# todo ad info over changes between 2010 and 2020
# todo publish this on external website
from Data import *
from fastapi import FastAPI

app = FastAPI()

# example of request with variable
# http://127.0.0.1:8000/random/402?query_param=EXW
@app.get('/random/{limit}')
async def get_random(limit: int, query_param: str = None):
    rn: int = limit
    command: str = query_param
    if command == 'EXW':
        print(I_EXW)
    else:
        print("No value")
    return{'limit' : rn, 'command': command}

@app.get('/rand/{nr}')
async def get_rand(nr: int, qu: str = None):
    if qu == 'Intro':
        inco: str = I_Intro
    elif qu == 'EXW':
        inco = I_EXW
    elif qu == 'FCA':
        inco = I_FCA
    elif qu == 'CPT':
        inco = I_CPT
    elif qu == 'CIP':
        inco = I_CIP
    elif qu == 'DPU':
        inco = I_DPU
    elif qu == 'DAP':
        inco = I_DAP
    elif qu == 'DDP':
        inco = I_DDP
    else:
        inco = "No valid value, use Intro/EXW/FCA/CPT/CIP/DPU/DAP/DDP instead"
    return{'limit' : nr, 'command': qu, "Incoterm": inco}



@app.get('/')
async def root():
   return{'Incoterms': "2020", 'Intro': I_Intro}

@app.get('/ALL')
async def ALL():
    return{"Incoterms": "2020","Intro": I_Intro,"EXW": I_EXW, 'FCA': I_FCA, "CPT": I_CPT,
           "CIP": I_CIP, "DPU": I_DPU, "DAP": I_DAP, "DDP": I_DDP}

@app.get('/EXW')
async def EXW():
    return{'Incoterms': "2020",'EXW': I_EXW, "mode":"all"}

@app.get('/FCA')
async def FCA():
    return{'Incoterms': "2020",'FCA': I_FCA, "mode":"all"}

@app.get('/CPT')
async def CPT():
    return{'Incoterms': "2020",'CPT': I_CPT, "mode":"all"}

@app.get('/CIP')
async def CIP():
    return{'Incoterms': "2020",'CIP': I_CIP, "mode":"all"}

@app.get('/DPU')
async def DPU():
    return{'Incoterms': "2020",'DPU': I_DPU, "mode":"all"}

@app.get('/DAP')
async def DAP():
    return{'Incoterms': "2020",'DAP': I_DAP, "mode":"all"}

@app.get('/DDP')
async def DDP():
    return{'Incoterms': "2020",'DDP': I_DDP, "mode":"all"}
