EX_css_structure = {
    "selector1":{
        "property11" : "value11",
        "property12" : "value12",
        "property13" : "value13",
        "property14" : "value14",
    },
    "selector2":{
        "property21" : "value21",
        "property22" : "value22",
        "property23" : "value23",
        "property24" : "value24",
    },
    "selector3":{
        "property31" : "value31",
        "property32" : "value32",
        "property33" : "value33",
        "property34" : "value34",
    }
}



def dict_to_css(dict_css) -> str:
    css_string = ""
    for selector , propertys in dict_css.items() :
        css_string += selector + "{\n"
        for k , v in propertys.items() :
            css_string += "    " + k + " : " + v + " ;" + "\n"
        css_string += "}\n\n"
    
    return css_string



# print(dict_to_css(EX_css_structure))






















EX_html_structure = {
    "tagName": "html",
    "attrs": {"lang":"en"},
    "children": [
        {
            "tagName": "img",
            "attrs": {"src":"surec/path" , "alt":"an_image"},
        },
        {
            "tagName": "head",
            "attrs": {},
            "children": [
                {
                    "tagName": "title",
                    "attrs": {},
                    "content": "Page Title",
                    "children": []
                }
            ]
        },
        {
            "tagName": "body",
            "attrs": {},
            "children": [
                {
                    "tagName": "header",
                    "attrs": {},
                    "children": [
                        {
                            "tagName": "h1",
                            "attrs": {},
                            "content": "Welcome to My Website",
                            "children": []
                        }
                    ]
                },
                {
                    "tagName": "main",
                    "attrs": {},
                    "children": [
                        {
                            "tagName": "article",
                            "attrs": {},
                            "children": [
                                {
                                    "tagName": "h2",
                                    "attrs": {},
                                    "content": "Article Title",
                                    "children": []
                                },
                                {
                                    "tagName": "p",
                                    "attrs": {},
                                    "content": "This is a paragraph in the article.",
                                    "children": []
                                }
                            ]
                        },
                        {
                            "tagName": "section",
                            "attrs": {},
                            "children": [
                                {
                                    "tagName": "h2",
                                    "attrs": {},
                                    "content": "Section Title",
                                    "children": []
                                },
                                {
                                    "tagName": "p",
                                    "attrs": {},
                                    "content": "This is a paragraph in the section.",
                                    "children": []
                                }
                            ]
                        }
                    ]
                },
                {
                    "tagName": "footer",
                    "attrs": {},
                    "children": [
                        {
                            "tagName": "p",
                            "attrs": {},
                            "content": "Footer information here.",
                            "children": []
                        }
                    ]
                }
            ]
        }
    ]
}


BLOCKED_TAGS = ("img", "link" , "br" , "hr","meta" , "source" , "command" , "param" ,)



def dict_to_html(tag_dict):
    
    is_blocked_tag = tag_dict['tagName'] in BLOCKED_TAGS
    html_str = ""
    html_str += f"<{tag_dict['tagName']}"

    attrs = tag_dict.get('attrs', {})
    for attr, value in attrs.items():
        html_str += f" {attr}='{value}'"
    html_str += ">\n"

    # if is_blocked_tag :
    #     html_str += ""

    content = tag_dict.get('content')
    if content:
        html_str += content
        html_str += "\n"

    # Recursively add children
    children = tag_dict.get('children', [])
    loop_counter = 0
    for child in children:
        # tab = "    " * loop_counter
        html_str += dict_to_html(child) 
        loop_counter += 1

    # Close the main tag
    if not is_blocked_tag :
        html_str += f"</{tag_dict['tagName']}>\n"

    return html_str

