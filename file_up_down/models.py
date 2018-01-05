from django.db import models

# Create your models here.
class courseware_db(models.Model):
    content = models.FileField(upload_to='uploadfile/')

    def __unicode__(self):
        return self.filename 
