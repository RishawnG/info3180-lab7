from flask_wtf import Form,TextAreaField,DataRequired
from flask_wtf.file import FileField,FileRequired,FileAllowed
from werkzeug import secure_filename

class UploadForm(Form):
    description=TextAreaField('description',validators=[DataRequired()])
    fileupload=FileField(validators=[FileRequired(),FileAllowed(['jpg', 'png', 'Images only!'])])
    