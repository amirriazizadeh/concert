from django import forms

class searchForm(forms.Form):
    searchConcert=forms.CharField(max_length=100,label="نام کنسرت",required=False)
