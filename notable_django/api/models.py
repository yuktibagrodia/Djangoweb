from django.db import models

# Create your models here.
class Note(models.Model):
    question = models.CharField(max_length=200)
    option1 = models.CharField(max_length=200)
    option2 = models.CharField(max_length=200)
    option3 = models.CharField(max_length=200)
    answer = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return '%s %s %s %s %s' % (self.question, self.option1,self.option2,self.option3,self.answer)
    pass
        

    