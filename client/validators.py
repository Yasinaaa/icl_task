from django.core.exceptions import ValidationError
import os

__author__ = 'yasina'

def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.xlsx', '.xls']
    if not ext in valid_extensions:
        raise ValidationError(u'Unsupported file extension.')