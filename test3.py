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


html_code = dict_to_html(html_structure)



with open("ok.html","w") as f:
    f.write("<!DOCTYPE html>\n")
    f.write(html_code)
    











# from config.settings import BASE_DIR
# from os import listdir , mkdir
# ID = "2"
# print(BASE_DIR/"templates"/"generated"/ID)

# with open("id")


# PATH  =  BASE_DIR / "templates" / "generated"

# print(listdir(PATH))

# name= "ok"
# path = BASE_DIR / "templates" / "generated" / name
# mkdir(path)