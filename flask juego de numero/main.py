from flask import Flask
from flask import render_template
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('main.html')
@app.route('/cal')
def cal(name=None):
	return render_template('cal.html', name=name)
@app.route('/sud')
def sud():
	cuadros = [5,15,25,35]
	return render_template('sud.html',cuadros=cuadros)
@app.route('/acierta', methods=['GET', 'POST'])
def acierta():
    mensaje = "Introduce un numero ya!";
    global hidden
    print hidden
    if request.method == "POST":
        numero = request.form["numero"]
        numero = int(numero)
        if hidden == numero:
            mensage = 'Numero acertado'
            hidden = randrange(1,99)
            print hidden
        else:
            if(hidden>numero):
                mensaje = 'Numero por encima'
            else:
                mensaje
                 = 'Numero por debajo'
    
    return render_template('endevina.html', mensaje = msg)

if __name__ == "__main__":
    app.run()