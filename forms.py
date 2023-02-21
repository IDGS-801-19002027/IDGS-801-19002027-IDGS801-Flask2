from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, PasswordField, TextAreaField, RadioField, IntegerField
from wtforms import validators

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message="El campo es requerido."),
        validators.length(min=4, max=10, message="La matrícula debe ser de 4 a 10 caracteres.")
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField('Amaterno')
    apaterno = StringField('Apaterno')
    email = EmailField('Correo')

class BoxForm(Form):
    numero = IntegerField('Número')
    cajasVacias = StringField('Número')
