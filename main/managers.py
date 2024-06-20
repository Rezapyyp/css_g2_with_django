from django.db import models
from json import dumps , loads 
from .generators import dict_to_html




class HtmlManager(models.Manager):


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


class FolderManager(models.Manager):
    ...
    # def delete(self,*args,**kwargs):
    #     print("\n")
    #     print("DELETED")
    #     print("\n")
    #     return super().delete(*args,**kwargs)






