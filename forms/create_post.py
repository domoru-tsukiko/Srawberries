from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, TextAreaField, SubmitField, EmailField, FileField
from wtforms.validators import DataRequired


class CreatePost(FlaskForm):
    title = StringField("Название", validators=[DataRequired()])
    text = TextAreaField('Текст записи', validators=[DataRequired()])
    img = FileField('Изображение')
    submit = SubmitField('Создать')

