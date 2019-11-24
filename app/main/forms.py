from flask_wtf import FlaskForm
from wtforms import StringField,TextAreaField,SubmitField,SelectField
from wtforms.validators import Required

class PitchForm(FlaskForm):
    """docstring for PitchForm."""

    title = StringField('Pitch title', validators = [Required()])
    text = TextAreaField('Text', validators = [Required()])
    carrtegory = SelectField('Type', choices = [('pickup_pitches','Pickup-line pitch'),('interview','Interview pitch'),('product','Product pitch'),('promotion','Promotion pitch')], validators = [Required()])
    submit = SubmitField('Submit')

class UpdateProfile(FlaskForm):
    """docstring for UpdateProfile. for updating user profiles"""

    bio = TextAreaField('Bio', validators = [Required()])
    submit = SubmitField('Submmit')

class CommentForm(FlaskForm):
    """docstring for CommentForm."""

    text = TextAreaField('Leave a Comment:', validators = [Required()])
    submit = SubmitField('Submit')
