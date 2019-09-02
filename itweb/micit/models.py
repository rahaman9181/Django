from django.db import models
from django.utils.timezone import datetime
from django.db.models.fields import Field
from django.contrib.auth.models import User
from django.conf import settings
from django.contrib.auth import get_user_model

class IT_Posts(models.Model):
    name=models.CharField(max_length=100)
    description=models.CharField(max_length=250,blank=True)
    pdf=models.FileField(upload_to='posts/pdfs/')
    date = models.DateTimeField(auto_now=True)
    posted=models.ForeignKey(User,default=None,on_delete=models.CASCADE)
    def __str__(self):
        return self.name

    def delete(self, *args, **kwargs):
        self.pdf.delete()
        super().delete(*args, **kwargs)
# datetime.now
