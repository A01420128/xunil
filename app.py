from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        numProc = request.form['numProc']
        tamQuan = request.form['tamQuan']
        tiemCC = request.form['tiemCC']
        tiemBloq = request.form['tiemBloq']
        return render_template('index.html', name=tiemCC)
    return render_template('index.html', name='Xinul')

if __name__ == "__main__":
    app.run(port = 5000, debug = True)
