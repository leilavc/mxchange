from flask_wtf import FlaskForm
from wtforms import TextField, DateField, SelectField
from wtforms.validators import DataRequired


class StartMealExchangeForm(FlaskForm):
    guest = TextField('guest', validators=[DataRequired()])
    date = DateField(validators=[DataRequired()])
    meal = SelectField(u'Meal', choices=[(
        'breakfast', 'Breakfast'), ('lunch', 'Lunch'), ('dinner', 'Dinner')])


class EndMealExchangeForm(FlaskForm):
    date = DateField(validators=[DataRequired()])
