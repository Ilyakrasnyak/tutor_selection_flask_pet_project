from flask_wtf import FlaskForm
from wtforms import StringField, HiddenField
from wtforms.validators import DataRequired, Length


class BookingForm(FlaskForm):
    name = StringField('Вас зовут', validators=[DataRequired()])
    phone = StringField('Ваш телефон', validators=[DataRequired(), Length(11)])
    teacher_id = HiddenField('teacher_id')
    weekday = HiddenField('weekday')
    time = HiddenField('time')
