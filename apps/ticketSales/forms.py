from django import forms
from .models import concertModel
class searchForm(forms.Form):
    searchConcert=forms.CharField(max_length=100,label="نام کنسرت",required=False)


class ConcertForm(forms.ModelForm):
    class Meta:
        model=concertModel
        fields="__all__"