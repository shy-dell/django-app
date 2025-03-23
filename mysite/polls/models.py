from django.db import models

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #CharField has required arguments i.e., max length
    pub_date = models.DateTimeField("date published") #these will be the columns in our db

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #when a row in the parent table is deleted, all associated values in the child table(s) with the same foreign key will be deleted (CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)


