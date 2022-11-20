# -*- coding: utf-8 -*-

import os
import time
import json

def fnComando(prComando:str)->None:
    os.system(prComando)
    time.sleep(0.5)

def fnEjecutar(prTools:dict):
    print(f"""
        #################informacion###############
        {prTools["info"]}
        comando : {prTools["comando"]}
    """)
    strOpt = input("Quiere ejecutar [Y/n]")

    if strOpt.upper() == 'Y' : fnComando(prTools['comando'])

def fnMenu()->print():
    listCerrar = ["99","x"]
    strf = open('herramientas.json')
    dicTools = json.load(strf)
    strf.close()
   
    for intIndex in range(len(dicTools)):
        print(f"-> {intIndex}  {dicTools[str(intIndex)]['nombre']}")
        time.sleep(0.3)
   
    print(f"-> {listCerrar[0]} cerrar")
    strOpt = input('Que funcion quiere ejecutar \n->')
    fnEjecutar(dicTools[strOpt])

fnMenu()