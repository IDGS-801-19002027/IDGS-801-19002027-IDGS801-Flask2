from flask import Flask, render_template
from flask import request
import forms
from flask import make_response
from flask import flash
from flask_wtf import CSRFProtect

app = Flask(__name__)
app.config['SECRET_KEY']="Esta es la clave encriptada"
csrf= CSRFProtect()

@app.route("/calcular",methods=['GET'])
def calcular():
    return render_template("calcular.html")

@app.route("/cookie", methods=['GET', 'POST'])
def cookie():
    reg_user = forms.LoginForm(request.form)

    if request.method == 'POST' and reg_user.validate():
        user=reg_user.username.data
        password = reg_user.password.data
        datos=user+"@"+password
        # Creación del mensaje de bienvenida
        success_message = 'Bienvenido {}'.format(user)
        response.set_cookie('datos_user', datos)
        flash(success_message)
        #print(user+ ' '+ password)
    response = make_response(render_template('cookie.html', form = reg_user))
    
    return response

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
                st += str(i)+"-->"+str(veces)+" veces, "
    
    
    return render_template("resultados.html", numeros = numeros, st=st, promedio = promedio, minNum=min(numeros), maxNum=max(numeros))

@app.route("/Alumnos", methods=['GET', 'POST'])
def alumnos():
    reg_alum = forms.UserForm(request.form)
    mat = ''
    nom = ''
    if request.method == 'POST' and reg_alum.validate():
        # Con la propiedad data se obtiene el valor del campo
        mat = reg_alum.matricula.data
        nom = reg_alum.nombre.data
    return render_template('Alumnos.html', form=reg_alum, mat=mat, nom=nom)

@app.route("/Traductor", methods=['GET', 'POST'])
def traductor():
    if request.method == 'POST':
        ing = request.form.get('ing')
        esp = request.form.get('esp')
        # Agregar palabras al archivo.txt
        file = open('diccionario.txt', 'a')
        file.write(ing.lower()+" "+esp.lower()+"\n")
        file.close()

    #print(ing, esp)
    return render_template('traductor.html')

@app.route("/buscarPalabras", methods=['GET', 'POST'])
def buscarPalabra():
    if request.method == 'POST':
        word = ''
        opcion = request.form['opcion']
        palabra = request.form.get('word').lower()
        
        if opcion == 'espR':
            result = buscar(palabra)
            if(result):
                result = result.split()
                word = result[1]
            else:
                word = 'No hay resultados'
                success_message = 'La palabra aún no esta en el diccionario.'
                flash(success_message)
        
        elif opcion == 'ingR':
            result = buscar(palabra)
            if(result):
                result = result.split()
                word = result[0]
            else:
                word = 'No hay resultados'
                success_message = 'La palabra aún no esta en el diccionario.'
                flash(success_message)

    return render_template('traductor.html', word = word)

def buscar(parametro):
    with open('diccionario.txt', 'r') as f:
        lineas = f.readlines()
        for linea in lineas:
            datos = linea.split()
            if datos[0] == parametro:
                return linea.strip()
            elif datos[1] == parametro:
                return linea.strip()

if __name__ == "__main__":
    #csrf.init_app(app)
    app.run(debug = True, port = 3000)
