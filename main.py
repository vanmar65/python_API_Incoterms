# if you want to run this API first start the local server with
# >pip install "fastapi[all]"

# this next command starts the server
# >uvicorn main:app --reload

# some ideas to improve
# add shipping method as parameter
# add table with risks
# add variable parameter

# ad info over changes between 2010 and 2020
# publish thi on external website
from Data import *
from fastapi import FastAPI

app = FastAPI()

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
