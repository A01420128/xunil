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
    tablas={ }
    for i in range(numMicros):
        tablas.update({
            "Micro"+str(i+1): [["PROCESO"],["TCC"],["TE"],["TVC"],["TB"],["TT"],["TI"],["TF"]]
        })
    return tablas

def temp(tablas, orden_Procesos):
    current_process= str(orden_Procesos.pop(0))
    tablas["Micro1"].append([
        [current_process],                      #Nombre del proceso
        [0],                                    #Cambio de contexto
        [PROCESOS[current_process]["Duracion"]],#Tiempo de ejecución
        [0],                                    #Vencimiento de Quantum
        [PROCESOS[current_process]["Bloqueos"]],#Tiempo de bloqueos

    ]
    )

def main():
    tablas= crear_Procesadores()
    temp(tablas, orden_Procesos)

    
main()