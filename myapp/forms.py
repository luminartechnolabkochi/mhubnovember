from django import forms

class MovieForm(forms.Form):

    title=forms.CharField()

    year=forms.CharField()

    director=forms.CharField()

    run_time=forms.IntegerField()

    language=forms.CharField()

    genre=forms.CharField()

    producer=forms.CharField()














