from django import forms

class UploadFileForm(forms.Form):
    title = forms.ImageField()
