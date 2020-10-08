from flask import Flask, redirect, render_template, request, url_for
app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
def index(name='no'):
    if request.method == 'POST':
        numProc = request.form['numProc']
        tamQuan = request.form['tamQuan']
        tiemCC = request.form['tiemCC']
        tiemBloq = request.form['tiemBloq']
        return redirect(url_for('index', name=tiemCC))
    name = "Ximul Debian"
    return render_template('index.html', name=name)

if __name__ == "__main__":
    app.run()
