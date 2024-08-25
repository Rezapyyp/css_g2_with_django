from django.shortcuts import render



def edit_html_file(request,file_id):
    return render(request , "html/html_editor.html")




def edit_css_file(request,file_id):
    return render(request , "css/css_editor.html")