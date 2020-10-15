# TODO: Add placeholders of values
# TODO: Eliminar pauasa
# TODO: Pausa to vacio
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

import utils


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numProc = int(request.form['numProc'])
        tamQuan = int(request.form['tamQuan'])
        tiemCC = int(request.form['tiemCC'])
        tiemBloq = int(request.form['tiemBloq'])
        micros = utils.main(tiemCC, tiemBloq, numProc, tamQuan)
        placeholders = { "numProc": numProc, "tamQuan": tamQuan, "tiemCC": tiemCC, "tiemBloq": tiemBloq }
        return render_template('index.html', micros=micros, placeholder=placeholders)
    return render_template('index.html', micros={}, placeholder={})

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
