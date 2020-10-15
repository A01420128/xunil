import math
PROCESOS= {
    "A": {
        "Duracion": 400,
        "Bloqueos": 2,
        "Inicio_ejecucion": 3000 
    },
    "B": {
        "Duracion": 300,
        "Bloqueos": 2,
        "Inicio_ejecucion": 0 
    },
    "C": {
        "Duracion": 50,
        "Bloqueos": 2,
        "Inicio_ejecucion": 3000 
    },
    "D": {
        "Duracion": 100,
        "Bloqueos": 2,
        "Inicio_ejecucion": 0 
    },
    "E": {
        "Duracion": 1000,
        "Bloqueos": 5,
        "Inicio_ejecucion": 3000
    },
    "F": {
        "Duracion": 500,
        "Bloqueos": 3,
        "Inicio_ejecucion": 0 
    },
    "G": {
        "Duracion": 10,
        "Bloqueos": 2,
        "Inicio_ejecucion": 3000 
    },
    "H": {
        "Duracion": 700,
        "Bloqueos": 4,
        "Inicio_ejecucion": 0 
    },
    "I": {
        "Duracion": 450,
        "Bloqueos": 3,
        "Inicio_ejecucion": 3000 
    },
    "J": {
        "Duracion": 300,
        "Bloqueos": 2,
        "Inicio_ejecucion": 1500 
    },
    "K": {
        "Duracion": 100,
        "Bloqueos": 2,
        "Inicio_ejecucion": 4000 
    },
    "L": {
        "Duracion": 3000,
        "Bloqueos": 5,
        "Inicio_ejecucion": 1500 
    },
    "M": {
        "Duracion": 80,
        "Bloqueos": 2,
        "Inicio_ejecucion": 4000 
    },
    "N": {
        "Duracion": 50,
        "Bloqueos": 2,
        "Inicio_ejecucion": 1500 
    },
    "Ñ": {
        "Duracion": 500,
        "Bloqueos": 3,
        "Inicio_ejecucion": 8000 
    },
    "O": {
        "Duracion": 600,
        "Bloqueos": 3,
        "Inicio_ejecucion": 1500 
    },
    "P": {
        "Duracion": 800,
        "Bloqueos": 4,
        "Inicio_ejecucion": 4000 
    }
}
orden_Procesos= ["B","D","F","H","J","L","N","O","A","C","E","G","I","K","M","P","Ñ"]


def crear_Procesadores(numMicros:int = 1):
    """
    Creates a dictionary containing all microprocessors
    and their tables of execution
    Returns: dictionary of all microprocessors
    """
    micros={ }
    for i in range(numMicros):
        micros["Micro"+str(i+1)]= [ ["ALPHA",-1,0,0,0,0,0,0] ]
    return micros

def despachador(micros, current_process):
    masChico="Micro1"
    tiempoMasChico=10000000000000000
    inicio_exe= PROCESOS[current_process]["Inicio_ejecucion"]
    for key,value in micros.items():
        if(inicio_exe>value[-1][7]):
            micros[key].append(["PAUSA", -1,0,0,0,0,value[-1][7],inicio_exe])
            print(masChico+ "")
            if(inicio_exe<tiempoMasChico):
                masChico=key
        if(value[-1][7]<tiempoMasChico):
            masChico=key
            tiempoMasChico=value[-1][7]
    tcc_anterior=micros[masChico][-1][1]
    tf_anterior=micros[masChico][-1][7]
    
    if(tcc_anterior!=-1):
        tcc_actual=cambioContexto
    else: tcc_actual=0
    tvc_actual= ((math.ceil((PROCESOS[current_process]["Duracion"])/quantum))-1) * cambioContexto
    te_actual= PROCESOS[current_process]["Duracion"]
    tb_actual= PROCESOS[current_process]["Bloqueos"] * tiempoBloqueo
    tt_actual= tcc_actual+te_actual+tvc_actual+tb_actual
    ti_actual= tf_anterior
    tf_actual= ti_actual+tt_actual
    micros[masChico].append(
        [current_process,                          #Proceso
        tcc_actual,                               #Cambio de contexto TCC
        te_actual,                                #TE
        tvc_actual,                                #TVC
        tb_actual,
        tt_actual,
        ti_actual,
        tf_actual
        ]
    )

##DATOS VARIABLES POR USUARIO
cambioContexto=15
tiempoBloqueo=15
numeroMicros=2
quantum=3000
##################################

def printTabla(micros):
    for key,values in micros.items():
        print(key)
        for row in values:
            print(row)
        


def main():
    micros= crear_Procesadores(numeroMicros)
    for proceso in orden_Procesos:
        despachador(micros, proceso)
    printTabla(micros)
    return micros
main()