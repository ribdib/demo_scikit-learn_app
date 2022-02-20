from wtforms import Form, DecimalField, IntegerField, SubmitField, validators

class ProductForm(Form):
    color  = IntegerField('Color',  [validators.InputRequired(), validators.NumberRange(min=1, max=10)])
    weight = DecimalField('Weight', [validators.InputRequired(), validators.NumberRange(min=0, max=100)])
    rating = IntegerField('Rating', [validators.InputRequired(), validators.NumberRange(min=1, max=5)])
    submit = SubmitField('Submit')