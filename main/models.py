from django.db import models
from config.settings import BASE_DIR
from os import listdir , mkdir , chdir
from django.core.exceptions import ValidationError
from .managers import HtmlManager #, FolderManager


class Folder(models.Model):
    # objects = FolderManager()

    PATH  =  BASE_DIR / "templates" / "generated"
    name = models.CharField(max_length=120, unique=True)

    def save(self,*args, **kwargs):
        if self.name in listdir(self.PATH):
            ValidationError("You can't use this name to create a folder ... E):#main.Folde")
        else :
            path =  self.PATH / self.name
            print(f"{path = }")
            mkdir(path)
            print(self.name)
        super().save(*args, **kwargs)




class Html(models.Model):
    objects = HtmlManager()

    name = models.CharField(max_length=120, unique=True)
    json = models.TextField(default=None , blank=True , null=True)
    dict = models.TextField(default=None , blank=True , null=True)
    str = models.TextField(default=None  , blank=True , null=True)

    folder = models.ForeignKey(Folder , on_delete=models.DO_NOTHING)

    

    def save(self, *args , **kwargs):
        super().save(*args , **kwargs)
        if self.str :
            path = BASE_DIR / "templates" / "generated" / self.folder.name
            chdir(path)
            file_name = self.name + ".html"
            with open(file_name,"w") as f:
                f.write("<!DOCTYPE html>\n")
                f.write(self.str)


class Css(models.Model):
    # objects = CssManager()

    name = models.CharField(max_length=120, unique=True)
    json = models.TextField(default=None , blank=True , null=True)
    dict = models.TextField(default=None , blank=True , null=True)
    str = models.TextField(default=None  , blank=True , null=True)

    folder = models.ForeignKey(Folder , on_delete=models.DO_NOTHING)

    

    def save(self, *args , **kwargs):
        super().save(*args , **kwargs)
        if self.str :
            path = BASE_DIR / "templates" / "generated" / self.folder.name
            chdir(path)
            file_name = self.name + ".css"
            with open(file_name,"w") as f:
                f.write("<!DOCTYPE html>\n")
                f.write(self.str)




