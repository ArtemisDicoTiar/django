## MODEL HOW TO USE: https://brownbears.tistory.com/63

from django.db import models
from django import setup
from datetime import datetime

# Create your models here.
class Feedback(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    comment = models.TextField()
    createDate = models.DateTimeField()

''' //  DELETE  // '''
# fb = Feedback.objects.all()
# fb.delete()
# Feedback.objects.filter(id=2).delete()

''' //  SELECT  // '''
# s = ''
# for f in Feedback.objects.all():
#     s += str(f.id) + ' : ' + f.name + '\n'
#
#

''' //  INSERT  // '''
# fb = Feedback(name='KIM', email='kim@test.com', comment='Hi', createDate=datetime.now())
# fb.save()

''' //  UPDATE  // '''
# fbb = Feedback.objects.get(pk=1)
# fbb.name = 'Park'
# fbb.save()

