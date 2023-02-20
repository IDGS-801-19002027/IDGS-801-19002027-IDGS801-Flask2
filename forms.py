from wtforms import Form
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField, FieldList, FormField, SelectField

from wtforms.fields import EmailField, PasswordField, TextAreaField, RadioField, IntegerField

class UserForm(Form):
    matricula = StringField('Matricula')
    nombre = StringField('Nombre')
    amaterno = StringField('Amaterno')
    apaterno = StringField('Apaterno')
    email = EmailField('Correo')

class BoxForm(Form):
    numero = IntegerField('Número')
    cajasVacias = StringField('Número')
