from django import forms

class UploadFileForm(forms.From):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
