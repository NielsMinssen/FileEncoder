from django import forms


class FileUploadForm(forms.Form):
    file = forms.FileField()
    encoding = forms.ChoiceField(choices=[('utf-8', 'UTF-8'), ('iso-8859-1', 'ISO-8859-1')])  # Add more encodings as needed
