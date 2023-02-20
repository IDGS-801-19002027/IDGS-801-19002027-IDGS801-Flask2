from flask import Flask, render_template
from flask import request
import forms

app = Flask(__name__)

@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cajasDinamicas",methods=['GET', 'POST'])
def cajasDinamicas():
    #reg_cajas = forms.BoxForm(request.form)
    num = 0
    if request.method == 'POST':
        # Con la propiedad data se obtiene el valor del campo num = reg_cajas.numero.data
        num = int(request.form.get('numero'))

    return render_template("cajasDinamicas.html", num = num)

@app.route("/resultados", methods=['GET','POST'])
def resultados():
    
    numeros = []
    numRepetidos = []
    cantNumeros = []
    st = ""
    suma= 0
    # Mostrar la lista de todos los números
    for num in request.form:
            numeros.append(int(request.form.get(num)))

    # Promedio
    for num in numeros:
        suma = suma + num
    
    totalNumeros = len(numeros)
    promedio = suma / totalNumeros
    # Números repetidos
    for i in numeros:
        veces = int(numeros.count(i))
        if veces > 1:  
            if i not in numRepetidos:
                numRepetidos.append(i)
                cantNumeros.append(veces)
                st += str(i)+"-->"+str(veces)+" veces"
    
    
    return render_template("resultados.html", numeros = numeros, st=st, promedio = promedio, minNum=min(numeros), maxNum=max(numeros))

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
