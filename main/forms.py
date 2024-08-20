from django import forms
from .models import Folder , Html , Css



class CreateFolderForm(forms.ModelForm):
    class Meta :
        model = Folder
        fields = ("name" ,)



class CreateHtmlFileForm(forms.ModelForm):
    class Meta :
        model = Html
        fields = ("name",)


class CreateCssFileForm(forms.ModelForm):
    class Meta :
        model = Css
        fields = ("name",)
