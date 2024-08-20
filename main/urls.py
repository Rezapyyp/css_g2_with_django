from django.urls import path
from . import views

app_name = "main"


urlpatterns = [
    path("" , views.BASE_DIR_apps_and_dirs , name="apps_and_dirs" ) ,
    path("apps/<str:app_name>/" , views.app_detail , name="app_detail" ) ,
    path("temp/" , views.Temp.as_view() , name="temp"  )
]


generators = [
    # Folders
    path("list_folders/" , views.list_folders , name="list_folders"),
    path("create_folder/" , views.create_folder , name="create_folder"),
    path("delete_folder/<int:folder_id>/" , views.delete_folder , name="delete_folder"),

    # Files
    path("files_of_folder/<slug:folder_name>/" , views.files_of_folder , name="files_of_folder"),
    path("create_html_file/<slug:folder_name>/",views.create_html_file , name="create_html_file"),
    path("create_css_file/<slug:folder_name>/",views.create_css_file , name="create_css_file"),
    path("delete_html_file/<slug:folder_name>/<int:file_id>/",views.delete_html_file , name="delete_html_file"),
    path("delete_css_file/<slug:folder_name>/<int:file_id>/" , views.delete_css_file , name="delete_css_file"),


    
]


urlpatterns += generators


