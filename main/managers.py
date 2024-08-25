from typing import Any
from django.db import models
from json import dumps , loads 
from .generators import dict_to_html
from config.settings import BASE_DIR
from os import system



class HtmlManager(models.Manager):

    def create_file(self, name , folder):
        path = BASE_DIR / "templates" / "generated" / folder.name / f"{name}.html" 
        system(f"touch {path}")
        obj = self.model(name=name,folder=folder)
        return obj
    
    def delete_file(self, name , folder):
        path = BASE_DIR / "templates" / "generated" / folder.name / f"{name}.html" 
        system(f"touch {path}")
        obj = self.model(name=name,folder=folder)
        return obj
    

    def insert_json(self,json_str,**extra_fields):
        _dict = loads(json_str)
        _html = dict_to_html(_dict)
        obj = self.model(json=json_str,dict=_dict,str=_html,**extra_fields)
        return obj
    

    def insert_dict(self,dict_data,**extra_fields):
        _json = dumps(dict_data)
        _html = dict_to_html(dict_data)

        obj = self.model(dict=dict_data,json=_json,str=_html,**extra_fields)
        return obj


class CssManager(models.Manager):

    def create_file(self, name , folder):
        path = BASE_DIR / "templates" / "generated" / folder.name / f"{name}.css" 
        system(f"touch {path}")
        obj = self.model(name=name,folder=folder)
        return obj



