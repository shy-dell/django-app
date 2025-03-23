import datetime
from django.db import models
from django.utils import timezone

# Create your models here.
class Question(models.Model):
    question_text = models.CharField(max_length=200) #CharField has required arguments i.e., max length
    pub_date = models.DateTimeField("date published") #these will be the columns in our db
    
    def __str__(self):
        return self.question_text
    
    def was_published_recently(self):
        now = timezone.now()
        return now - datetime.timedelta(days=1) <= self.pub_date <= now
        #the above equation ensures that pub date is now greater than today (i.e., in the future) AND checks if it was created in the last day ("recently")

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    #when a row in the parent table is deleted, all associated values in the child table(s) with the same foreign key will be deleted (CASCADE)
    choice_text = models.CharField(max_length=200)
    votes = models.IntegerField(default=0)
    def __str__(self):
        return self.choice_text


