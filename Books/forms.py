from django import forms
from .models import *

class BookAddForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['BookISBN','BookTitle','BookAuthor']

class BookIssueForm(forms.ModelForm):
    class Meta:
        model = Issued
        fields = ['BookISBN','StudentRoll','IssueDate','DueDate']
