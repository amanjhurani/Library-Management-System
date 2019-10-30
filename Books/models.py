from django.db import models

# Create your models here.
import datetime
from django.utils import timezone
from django.utils.timezone import now


class Book(models.Model):
    BookISBN = models.IntegerField(primary_key=True)
    BookTitle = models.CharField(max_length=150)
    BookAuthor = models.CharField(max_length=100)


class Issued(models.Model):
    BookISBN = models.ForeignKey('Book',on_delete=models.CASCADE)
    StudentRoll = models.IntegerField()
    IssueDate = models.DateField(default=datetime.datetime.now().date())
    DueDate = models.DateField(default=datetime.datetime.now().date() + datetime.timedelta(days=15))



