from django.test import TestCase
from main.models import Folder , Html
from json import  dumps

class MyTestCase(TestCase):
    _dict = {
            "tag": "html",
            "attributes": {"lang":"en"},
            "children": [
                {
                    "tag": "img",
                    "attributes": {"src":"surec/path" , "alt":"an_image"},
                },
                {
                    "tag": "head",
                    "attributes": {},
                    "children": [
                        {
                            "tag": "title",
                            "attributes": {},
                            "content": "Page Title",
                            "children": []
                        }
                    ]
                },
                {
                    "tag": "body",
                    "attributes": {},
                    "children": [
                        {
                            "tag": "header",
                            "attributes": {},
                            "children": [
                                {
                                    "tag": "h1",
                                    "attributes": {},
                                    "content": "Welcome to My Website",
                                    "children": []
                                }
                            ]
                        },
                        {
                            "tag": "main",
                            "attributes": {},
                            "children": [
                                {
                                    "tag": "article",
                                    "attributes": {},
                                    "children": [
                                        {
                                            "tag": "h2",
                                            "attributes": {},
                                            "content": "Article Title",
                                            "children": []
                                        },
                                        {
                                            "tag": "p",
                                            "attributes": {},
                                            "content": "This is a paragraph in the article.",
                                            "children": []
                                        }
                                    ]
                                },
                                {
                                    "tag": "section",
                                    "attributes": {},
                                    "children": [
                                        {
                                            "tag": "h2",
                                            "attributes": {},
                                            "content": "Section Title",
                                            "children": []
                                        },
                                        {
                                            "tag": "p",
                                            "attributes": {},
                                            "content": "This is a paragraph in the section.",
                                            "children": []
                                        }
                                    ]
                                }
                            ]
                        },
                        {
                            "tag": "footer",
                            "attributes": {},
                            "children": [
                                {
                                    "tag": "p",
                                    "attributes": {},
                                    "content": "Footer information here.",
                                    "children": []
                                }
                            ]
                        }
                    ]
                }
            ]
        }
        
    def test_folder_on_craete(self):
        obj = Folder.objects.create(name="test_folder_on_craete")
        obj.save()
    

    def test_insert_dict(self):
        folder = Folder.objects.create(name="test_dict")
        folder.save()
        obj = Html.objects.insert_dict(name="test_dict",folder=folder,dict_data=self._dict )

        obj.save()
    
    def test_insert_json(self):
        folder = Folder.objects.create(name="test_json")
        folder.save()
        json_str = dumps(self._dict)
        obj = Html.objects.insert_json(name="test_json",folder=folder,json_str=json_str )
        obj.save()
    
    
