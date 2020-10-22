# TODO: Add placeholders of values
# TODO: Eliminar pauasa
# TODO: Pausa to vacio
from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)

import utils


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try: 
            numProc = int(request.form['numProc'])
            tamQuan = int(request.form['tamQuan'])
            tiemCC = int(request.form['tiemCC'])
            tiemBloq = int(request.form['tiemBloq'])
            placeholders = { "numProc": numProc, "tamQuan": tamQuan, "tiemCC": tiemCC, "tiemBloq": tiemBloq }
            if numProc <= 0 or tamQuan <= 0 or tiemCC < 0 or tiemBloq < 0:
                return render_template('index.html', micros={}, placeholder=placeholders, msg="Ocurrio un error")
            else:
                micros = utils.main(tiemCC, tiemBloq, numProc, tamQuan)
                return render_template('index.html', micros=micros, placeholder=placeholders, msg="")
        except:
            return render_template('index.html', micros={}, placeholder={}, msg="Ocurrio un error")
    return render_template('index.html', micros={}, placeholder={}, msg="")

if __name__ == "__main__":
    app.run(port = 5000, debug = False)
