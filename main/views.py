from django.shortcuts import render , redirect
from config.settings import BASE_DIR
from os import listdir, system , chdir 
from django.apps import apps
from .models import Folder , Html , Css
from .forms import CreateFolderForm , CreateHtmlFileForm ,CreateCssFileForm
from django.contrib import messages
from django.views.generic import TemplateView


class Temp(TemplateView):
    template_name = "main/generator/temp/temp.html"




def list_folders(request):
    folders = Folder.objects.all()
    form = CreateFolderForm
    context = {
        "folders" : folders ,
        "create_folder_form" : form ,
    }
    return render(request,"main/generator/folders/list.html",context)

def delete_folder(request,folder_id):
    folder = Folder.objects.get(id=folder_id)
    path = folder.PATH / folder.name
    system(f"rm -rf {path}")
    folder.delete()
    messages.success(request,"Folder Deleted successfully")
    return redirect("main:list_folders")

def create_folder(request):
    form = CreateFolderForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        folder = Folder.objects.create(name=cd["name"])
        folder.save()
        messages.success(request, "folder craeted successfully ...")
        return redirect("main:list_folders")
    
    messages.error(request, "folder dont... craeted ...")
    return redirect("main:list_folders")

# def rename_folder()
#    coming soon



def files_of_folder(request,folder_name):
    html_files = Html.objects.filter(folder__name=folder_name)
    css_files = Css.objects.filter(folder__name=folder_name)

    create_html_form = CreateHtmlFileForm
    create_css_form = CreateCssFileForm

    context = {
        "html_files" : html_files ,
        "css_files" : css_files ,
        "create_html_form" : create_html_form ,
        "create_css_form" : create_css_form ,
        "folder_name" : folder_name ,
    }
    return render(request,"main/generator/files/list.html",context)

def delete_html_file(request,folder_name,file_id):
    file = Html.objects.get(id=file_id)
    folder = Folder.objects.get(name=folder_name)
    path = folder.PATH / folder.name / file.name
    system(f"rm -rf {path}")
    file.delete()
    messages.success(request,"Html file Deleted successfully")
    return redirect("main:files_of_folder", folder.name)

def delete_css_file(request,folder_name,file_id):
    file = Css.objects.get(id=file_id)
    folder = Folder.objects.get(name=folder_name)
    path = folder.PATH / folder.name / file.name
    system(f"rm -rf {path}")
    file.delete()
    messages.success(request,"Css file Deleted successfully")
    return redirect("main:files_of_folder", folder.name)


def create_html_file(request,folder_name):
    form = CreateHtmlFileForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        folder = Folder.objects.get(name=folder_name)
        html_file = Html.objects.create(name=cd["name"],folder=folder)
        html_file.save()
        
        messages.success(request, "Html file craeted successfully ...")
        return redirect("main:files_of_folder",folder_name)

    messages.error(request, "Html file dont... craeted ...")
    return redirect("main:files_of_folder",folder_name)

def create_css_file(request,folder_name):
    form = CreateCssFileForm(request.POST)
    if form.is_valid():
        cd = form.cleaned_data
        folder = Folder.objects.get(name=folder_name)
        html_file = Css.objects.create(name=cd["name"],folder=folder)
        html_file.save()
        
        messages.success(request, "Css file craeted successfully ...")
        return redirect("main:files_of_folder",folder_name)

    messages.error(request, "Css file dont... craeted ...")
    return redirect("main:files_of_folder",folder_name)












































def BASE_DIR_apps_and_dirs(request):
    lis = []
    installed_dirs = []

    for dir in listdir(BASE_DIR):
        if not ("." in dir) and dir!="templates" and dir!="config":
            if apps.is_installed(dir): 
                installed_dirs.append(dir)
            else :
                lis.append(dir)

    context = {
        "installed_dirs": installed_dirs ,
        "BASE_DIR" : BASE_DIR ,
        "dirs" : lis ,
    }
    return render(request,"main/apps_and_dirs.html",context)


def app_detail(request,app_name):
    files = []
    for file in listdir(BASE_DIR/app_name):
        if  ("." in file) and file != "__pycache__" and file != "__init__.py" :
            files.append(file)
    context = {
        "app_name" : app_name ,
        'files' : files
    }
    return render(request,"main/app_detail.html", context)


