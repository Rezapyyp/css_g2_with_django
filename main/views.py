from django.shortcuts import render , redirect
from config.settings import BASE_DIR
from os import listdir, system , chdir 
from django.apps import apps
from .models import Folder
from .forms import CreateFolderForm
from django.contrib import messages
from django.views.generic import TemplateView


class Temp(TemplateView):
    template_name = "main/generator/temp/temp.html"





# def list_files(request):  
    
#     context = {
#     }
#     return render(request,"",context)

# def delete_file(request,folder_id):
    
#     context = {
#     }
#     return render(request,"",context)

# def create_file(request):
    
#     context = {
#     }
#     return render(request,"",context)
    


####################################################################


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
    
    messages.warning(request, "folder dont... craeted ...")
    return redirect("main:list_folders")

# def workspace(request,folder_id):
#     ...
#     return render(request)

####################################################################

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


