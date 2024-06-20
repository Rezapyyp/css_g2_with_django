from pprint import pprint
html_structure = {
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



BLOCKED_TAGS = "img", "link" , "br" , "hr","meta" , "source" , "command" , "param"
def dict_to_html(tag_dict):

    is_blocked_tag = tag_dict["tag"] in BLOCKED_TAGS
    html_str = ""
    html_str += f"<{tag_dict['tag']}"

    attributes = tag_dict.get('attributes', {})
    for attr, value in attributes.items():
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
        html_str += f"</{tag_dict['tag']}>\n"

    return html_str

# Example usage with the provided dictionary
html_code = dict_to_html(html_structure)
print(html_code)

































# def dict_to_html(tag_dict):
#     # Start with an empty string to accumulate HTML
#     html_str = ""

#     # Open the main tag
#     html_str += f"<{tag_dict['tag']}"

#     # Add attributes if there are any
#     attributes = tag_dict.get('attributes', {})
#     for attr, value in attributes.items():
#         html_str += f" {attr}='{value}'"

#     # Close the opening tag
#     html_str += ">"

#     # Check if there is content to add
#     content = tag_dict.get('content')
#     if content:
#         html_str += content

#     # Recursively add children
#     children = tag_dict.get('children', [])
#     for child in children:
#         html_str += dict_to_html(child)

#     # Close the main tag
#     html_str += f"</{tag_dict['tag']}>"

#     return html_str

# # Example usage with the provided dictionary
# html_code = dict_to_html(html_structure)
# pprint(html_code)




##############################################################################################
# from bs4 import BeautifulSoup

# def html_to_dict(html_code):
#     # Parse the HTML code using Beautiful Soup
#     soup = BeautifulSoup(html_code, 'html.parser')

#     # Define a recursive function to convert BeautifulSoup Tag to dictionary
#     def tag_to_dict(tag):
#         tag_dict = {
#             "tag": tag.name,
#             "attributes": dict(tag.attrs),
#             "children": []
#         }

#         # Add content if the tag has any
#         if tag.string:
#             tag_dict["content"] = tag.string.strip()

#         # Recursively add children
#         for child in tag.children:
#             if isinstance(child, BeautifulSoup.Tag):
#                 tag_dict["children"].append(tag_to_dict(child))

#         return tag_dict

#     # Start conversion from the top-level tags
#     dict_structure = []
#     for child in soup.children:
#         if isinstance(child, BeautifulSoup.Tag):
#             dict_structure.append(tag_to_dict(child))

#     return dict_structure

# # Example HTML code
# html_code = """
# <html>
# <head>
#     <title>Sample Page</title>
# </head>
# <body>
#     <header>
#         <h1>Welcome to My Website</h1>
#     </header>
#     <main>
#         <article>
#             <h2>Article Title</h2>
#             <p>This is a paragraph in the article.</p>
#         </article>
#         <section>
#             <h2>Section Title</h2>
#             <p>This is a paragraph in the section.</p>
#         </section>
#     </main>
#     <footer>
#         <p>Footer information here.</p>
#     </footer>
# </body>
# </html>
# """

# # Convert HTML to dictionary structure
# html_dict = html_to_dict(html_code)
# import json
# pprint(json.dumps(html_dict, indent=2))


















































###################################################################################################################################
# from pprint import pprint
# "attrs" : {"lang": "en"} ,
# "propertyes" : [] ,
# "content" : None ,
# "content_before_children" : None ,
# "content_after_children" : None ,
# tag = {
#     "name" : "html" ,
#     "children" : [
#         {
#             "name" : "head" ,
#             "children" : [
#                 {
#                     "name" : "title" ,
#                     "content" : "Web Title" ,
#                     "children" : [] ,
#                 },
#             ]
#         },
#         {
#             "name" : "body" ,
#             "children" : [
#                 {
#                     "name" : "nav" ,
#                     "children" : [
#                         {
#                             "name" : "ul" ,
#                             "content" : "content of (ul >>> nav >>> body)" ,
#                             "children" : []
#                         },
#                     ]
#                 },
#                 {
#                     "name" : "main" ,
#                     "children" : [
#                         {
#                             "name" : "div1" ,
#                             "content" : "content of (div1 >>> main >>> body)" ,
#                             "children" : []

#                         },
#                         {
#                             "name" : "div2" ,
#                             "content" : "content of (div2 >>> main >>> body)" ,
#                             "children" : []

#                         },
#                     ]
#                 },
#                 {
#                     "name" : "footer" ,
#                     "content" : "content of (footer >>> body)" ,
#                     "children" : []
#                 },
#             ]
#         },
#     ]
# }








# def MAKE_CHILDREN_ROW(tag):
#     tagName = tag.get("name")             # TYPE : STR
#     children = tag.get("children")        # TYPE : LIST OF TAGS
#     content = tag.get("content","null")   # TYPE : STR

    

    # print(content)
    # content_row = f"{tagName} :"
    # if children :
    #     for child in children :
    #         content_row += "-" + tagName
    #         MAKE_CHILDREN_ROW(child)
    # else :
    #     content_of_tagName = tag.get('content')
    #     content_row = f"c_of({tagName}): {content_of_tagName} "
    # print(content_row)



# MAKE_CHILDREN_ROW(tag)

















# def MAKE_CHILDREN_ROW(tag):
#     parent = tag.get("name")
#     children = tag.get("children")
#     content_row = f"{parent} :"
#     if children :
#         for child in children :
#             content_row += "-" + parent
#             MAKE_CHILDREN_ROW(child)
#     else :
#         content_of_parent = tag.get('content')
#         content_row = f"c_of({parent}): {content_of_parent} "
#     print(content_row)



# MAKE_CHILDREN_ROW(tag)




























# def MAKE_CHILDREN_ROW2(tag):
#     parent = tag.get("name")
#     children = tag.get("children")
#     children_row = f"{parent} :"
#     if children :
#         for child in children :
#             parent_to_send = child.get('name')
#             children_to_send = child.get('children')
#             children_row += "-" + parent_to_send
#             # MAKE_CHILDREN_ROW3(tag)
#     else :
#         content_of_parent = tag.get('content')
#         children_row = f"c_of({parent}): {content_of_parent} "
#     print(children_row)


# def MAKE_CHILDREN_ROW1(tag):
#     parent = tag.get("name")
#     children = tag.get("children")
#     children_row = f"{parent} :"
#     if children :
#         for child in children :
#             parent_to_send = child.get('name')
#             children_to_send = child.get('children')
#             children_row += "-" + parent_to_send
#             MAKE_CHILDREN_ROW2(child)
#     else :
#         content_of_parent = tag.get('content')
#         children_row = f"c_of({parent}): {content_of_parent} "
#     print(children_row)

# def MAKE_CHILDREN_ROW0(tag):
#     parent = tag.get("name")
#     children = tag.get("children")
#     children_row = f"{parent} :"
#     if children :
#         for child in children :
#             parent_to_send = child.get('name')
#             children_to_send = child.get('children')
#             children_row += "-" + parent_to_send
#             MAKE_CHILDREN_ROW1(child)
#     else :
#         content_of_parent = tag.get('content')
#         children_row = f"c_of({parent}): {content_of_parent} "
#     print(children_row)



# MAKE_CHILDREN_ROW0(tag)


































































# print("0")
# print(tag["name"])
# MAKE_CHILDREN_ROW0(tag)
# for tag0 in tag["children"]:
#     print(tag0["name"])
#     MAKE_CHILDREN_ROW0(tag0.get('children'))
#     for tag1 in tag0["children"] :
#         print(tag1["name"])
#         MAKE_CHILDREN_ROW0(tag1.get('children'))
#         for tag2 in tag1["children"] :
#             print(tag2["name"])
#             MAKE_CHILDREN_ROW0(tag2.get('children'))






















































# class NodeStracture :

#     def __init__(self,tag):
#         self.tag = tag
#         self.children_row = ""
    
#     def FOR_LOOP(self):
#         print(f"{self.tag.get('name')}")
#         for tag in self.tag["children"]:

#             self.FOR_LOOP()


# NodeStracture(tag).FOR_LOOP()







































































# out_counter = 0
# def FOR_LOOP(tag,children_row="",in_counter=0):
#     global out_counter
#     out_counter += 1
#     print(f"{tag.get('name')}-{in_counter}") #-{out_counter}
#     in_counter = 0
#     for tag in tag["children"]:
#         in_counter += 1
#         FOR_LOOP(tag,children_row,in_counter)
    

    
        



# FOR_LOOP(tag)
            

























# def FOR_LOOP(tag,children_row=""):

#     for child0 in tag["children"]:
#         formated_children = '<{child_name}">{content}</{child_name}>'.format_map({"child_name":child0.get("name"),"content":None})
#         children_row += formated_children 
#         FOR_LOOP(child0,children_row)
        
#     formated_tag = '<{tag_name}">{children_row}</{tag_name}>'.format_map({"tag_name":tag.get("name"),"children_row":children_row})




