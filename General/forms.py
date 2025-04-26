from django import forms

class contactForm(forms.Form):
    name=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Name','required':'','name':'name'}))
    mob = forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Mobile','name':'mob','required':''}))
    email=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Email','required':'','name':'email'}))
    subj=forms.CharField(widget=forms.TextInput(attrs={'placeholder':'Subject','required':'','name':'subj'}))
    msg=forms.CharField(widget=forms.Textarea(attrs={'placeholder':'Message','required':'','name':'msg'}))

class aloginForm(forms.Form):
    username=forms.EmailField(label="Enter Your name")
    password=forms.IntegerField(widget=forms.IntegerField)




