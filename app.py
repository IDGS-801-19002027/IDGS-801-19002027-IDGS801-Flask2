from flask import Flask, render_template
from flask import request
import forms

app = Flask(__name__)

@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cajasDinamicas",methods=['GET', 'POST'])
def cajasDinamicas():
    reg_cajas = forms.BoxForm(request.form)
    num = 0
    if request.method == 'POST':
        # Con la propiedad data se obtiene el valor del campo
        num = reg_cajas.numero.data

    return render_template("cajasDinamicas.html", form=reg_cajas, num = num)

@app.route("/resultados",methods=['GET','POST'])
def resultados():
    prom = 0
    min = 0
    max = 0
    if request.method == 'POST':
        
        print(prom)
        print(min)  
        n1 = request.form['cajasVacias']

        
    return render_template("resultados.html", prom = prom, max = max, min = min)



@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method == 'POST':
        # Con la propiedad data se obtiene el valor del campo
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data
    return render_template('Alumnos.html', form=reg_alum, mat=mat, nom=nom)

if __name__ == "__main__":
    app.run(debug = True, port = 3000)
