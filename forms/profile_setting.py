from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, EmailField
from wtforms.validators import DataRequired


class SettingForm(FlaskForm):
    email = EmailField('Почта', validators=[DataRequired()])
    name = StringField('Имя пользователя', validators=[DataRequired()])
    about = TextAreaField("Немного о себе")
    submit = SubmitField('Сохранить изменения')
