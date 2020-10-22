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
        micros["Micro"+str(i+1)]= [ ["VACIO",-1,0,0,0,0,0,0] ]
    return micros

def despachador(micros, current_process, cambioContexto, tiempoBloqueo, quantum):
    masChico="Micro1"
    tiempoMasChico=10000000000000000
    inicio_exe= PROCESOS[current_process]["Inicio_ejecucion"]
    for key,value in micros.items():
        anterior_final = inicio_exe if inicio_exe > value[-1][7] else value[-1][7]
        if (anterior_final < tiempoMasChico):
            masChico=key
            tiempoMasChico = anterior_final
    tf_anterior=micros[masChico][-1][7]
    if (tf_anterior < inicio_exe):
        micros[masChico].append(["VACIO", 0,0,0,0,0,tf_anterior,inicio_exe])
        tf_anterior = inicio_exe
    tcc_actual = 0 if micros[masChico][-1][0] == "VACIO" else cambioContexto
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

def printTabla(micros):
    for key,values in micros.items():
        print(key)
        for row in values:
            print(row)
        


def main(cambioContexto, tiempoBloqueo, numeroMicros, quantum):
    micros= crear_Procesadores(numeroMicros)
    for proceso in orden_Procesos:
        despachador(micros, proceso, cambioContexto, tiempoBloqueo, quantum)
    for key, value in micros.items():
        del value[0]
    printTabla(micros)
    return micros


main(15,15,2,3000)
