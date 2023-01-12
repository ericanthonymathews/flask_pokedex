from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, FloatField, BooleanField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, NumberRange 


'''
• imageUrl has a getter method we need to look at 
• moves validation think

'''

types = [
  "fire",
  "electric",
  "normal",
  "ghost",
  "psychic",
  "water",
  "bug",
  "dragon",
  "grass",
  "fighting",
  "ice",
  "flying",
  "poison",
  "ground",
  "rock",
  "steel",
]

class CreatePokemonForm(FlaskForm): 
  number = IntegerField("Number", validators=[DataRequired(), NumberRange(min=1)])
  attack = IntegerField("Attack", validators=[DataRequired(), NumberRange(min=0, max=100, message=f"Must be an integer between {min} and {max}")])
  defense = IntegerField("Defense", validators=[DataRequired(), NumberRange(min=0, max=100, message=f"Must be an integer between {min} and {max}")])
  image_url = StringField("Image URL", validators=[DataRequired()])
  name = StringField("Name", validators=[DataRequired(), Length(min=3, max=255, message=f"Must be between {min} and {max} characters")])
  type = SelectField("Type", choices=(types))
  moves = StringField("Moves", validators=[DataRequired(), Length(max=255, message=f"Must be no greater than {max}")])
  encounter_rate = FloatField("Encounter Rate", validators=[DataRequired(), NumberRange(min=0, max=100, message=f"Must be an integer between {min} and {max}")])
  catch_rate = FloatField("Catch Rate", validators=[DataRequired(), NumberRange(min=0, max=100, message=f"Must be an integer between {min} and {max}")])
  captured = BooleanField("Captured")
  submit = SubmitField("Submit")
  









