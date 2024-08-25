from django.db import models
from config.settings import BASE_DIR
from os import listdir , mkdir , chdir
from django.core.exceptions import ValidationError
from .managers import HtmlManager , CssManager


def folder_name_validator(folder_name):
    PATH  =  BASE_DIR / "templates" / "generated"
    if " " in folder_name:
        raise ValidationError("Folder_name can`t have a space !!! ")    
    return folder_name

def file_name_validator(value):
    if " " in value :
        raise ValidationError("Error")
    return value


class Folder(models.Model):
    # objects = FolderManager()

    PATH  =  BASE_DIR / "templates" / "generated"
    name = models.SlugField(max_length=120, unique=True,validators=[folder_name_validator])

    def get_path(self):
        path =  self.PATH / self.name
        return path
    
    def save(self,*args, **kwargs):
        if self.name in listdir(self.PATH):
            ValidationError("You can't use this name to create a folder ... E):#main.Folde")
        else :
            path =  self.PATH / self.name
            mkdir(path)
        super().save(*args, **kwargs)


class File(models.Model):
    name = models.SlugField(max_length=120, unique=True , validators=[file_name_validator])
    folder = models.ForeignKey(Folder , on_delete=models.DO_NOTHING)

    def get_path(self):
        PATH  =  BASE_DIR / "templates" / "generated" / self.folder.name / self.name
        return PATH
    
    def is_html_file(self):
        ...
    
    def is_css_file(self):
        ...

    def save(self, *args , **kwargs):
        super().save(*args , **kwargs)
        if self.str :
            path = BASE_DIR / "templates" / "generated" / self.folder.name
            chdir(path)
            # file_name = self.name + ".html"
            with open(self.name,"w") as f:
                # f.write("<!DOCTYPE html>\n")
                f.write(self.str)


class Html(File):
    objects = HtmlManager()

    json = models.TextField(default=None , blank=True , null=True)
    dict = models.TextField(default=None , blank=True , null=True)


class Css(File):
    objects = CssManager()

    json = models.TextField(default=None , blank=True , null=True)
    dict = models.TextField(default=None , blank=True , null=True)






