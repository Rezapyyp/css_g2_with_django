import re

my_tag = """
<tagName pn key2 = "val2" key3="val3"key4="val4"  
    key1="val1"    
    key   =    "val"    
    keynn  =  'ok'
    style   =  ""
    style   =  "color :;#red "   
   
p1 p2 p3 ></tagName>'
"""


def get_attrs_of_tag(tag):
    attrs = {}
    attr_reg = r""" {0}(\w{0,}) {0,}= {0,}[\"\']([\w\s]{0,}|.{0,})[\"\'] {0,1}"""
    result = re.findall(attr_reg,tag)
    for i in result :
        attrs[i[0]] = i[1]
    
    return attrs


get_tag_name = """[<] {0,}(\w{1,}) {0,}"""










