from django import forms

class EpisodeForm(forms.Form):
#    number = forms.IntegerField(required=True)
    title = forms.CharField(required=True)
    agenda = forms.CharField(required=True)
    person = forms.CharField(required=True)
    shownote = forms.CharField()
