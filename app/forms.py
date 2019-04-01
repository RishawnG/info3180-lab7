from flask_wtf import FlaskForm
from flask_wtf.file import FileField, FileAllowed, FileRequired
from wtforms import TextAreaField
from wtforms.validators import InputRequired
from werkzeug import secure_filename

class UploadForm(FlaskForm):
    description=TextAreaField('description',validators=[InputRequired()])
    photo=FileField('fileupload',validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    