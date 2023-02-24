from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, PasswordField, TextAreaField, RadioField, IntegerField
from wtforms import validators

def mi_validacion(form,field):
    if len(field.data) == 0:
        raise validators.ValidationError('El campo no tiene datos.')

class UserForm(Form):
    matricula = StringField('Matricula', [
        validators.DataRequired(message="El campo es requerido."),
        validators.length(min=4, max=10, message="La matrícula debe ser de 4 a 10 caracteres.")
    ])
    nombre = StringField('Nombre', [
        validators.DataRequired(message="El campo es requerido")
    ])
    amaterno = StringField('Amaterno', [mi_validacion])
    apaterno = StringField('Apaterno', [mi_validacion])
    email = EmailField('Correo')

class BoxForm(Form):
    numero = IntegerField('Número')
    cajasVacias = StringField('Número')

class LoginForm(Form):
    username = StringField('Usuario', [
        validators.DataRequired(message="El campo es requerido."),
        validators.length(min=4, max=10, message="El nombre de usuario debe contener de 4 a 10 caracteres.")
    ])
    password = StringField('Password', [
        validators.DataRequired(message="El campo es requerido."),
        validators.length(min=4, max=10, message="La contraseña debe contener de 4 a 10 caracteres.")
    ])