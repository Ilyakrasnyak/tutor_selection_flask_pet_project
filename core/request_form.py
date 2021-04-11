from flask_wtf import FlaskForm
from wtforms import StringField, RadioField
from wtforms.validators import DataRequired, Length


class RequestForm(FlaskForm):
    goal = RadioField('Какая цель занятий?', choices=[('Для путешествий', 'Для путешествий'),
                                                      ('Для школы', 'Для школы'),
                                                      ('Для работы', 'Для работы'),
                                                      ('Для переезда', 'Для переезда')
                                                      ])
    load = RadioField('Сколько времени есть?', choices=[('1-2 часа в неделю', '1-2 часа в неделю'),
                                                        ('3-5 часов в неделю', '3-5 часов в неделю'),
                                                        ('5-7 часов в неделю', '5-7 часов в неделю'),
                                                        ('7-10 часов в неделю', '7-10 часов в неделю')
                                                        ])
    name = StringField('Вас зовут', validators=[DataRequired()])
    phone = StringField('Ваш телефон', validators=[DataRequired(), Length(11)])
