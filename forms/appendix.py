from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField
from wtforms.validators import DataRequired


class SearchForm(FlaskForm):
    title = StringField("Текст поиска", validators=[DataRequired()])
    submit = SubmitField("Поиск")
