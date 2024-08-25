from . import views 
from django.urls import path 

app_name = "editor"


urlpatterns = [
    path("edit_html_file/<int:file_id>/", views.edit_html_file, name="edit_html_file" ),
    path("edit_css_file/<int:file_id>/", views.edit_css_file , name="edit_css_file" ),
]

