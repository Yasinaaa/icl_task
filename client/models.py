from django.db import models
import os
from .validators import validate_file_extension

def get_path(instance, filename):
    return os.path.join('excel', filename)

class ClientFileModel(models.Model):
    class Meta:
        db_table = "graphs_table"

    title = models.CharField(max_length=256, unique=True)
    path_to_file = models.FileField(blank=True, upload_to=get_path,validators=[validate_file_extension])

    def __unicode__(self):
        return "%s" % (self.title)

    def json(self):
        return dict(
            id = self.id,
            title = self.title)

