from flask import Flask, render_template
app = Flask(__name__)

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

@app.route("/", methods=['GET', 'POST'])
def hello():
    name = "Ximul Debian"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run()
