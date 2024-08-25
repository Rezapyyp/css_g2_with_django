from django.contrib import admin
from .models import Css , Html , Folder , SimpleFile

admin.site.register(Html)
admin.site.register(Css)
admin.site.register(Folder)
admin.site.register(SimpleFile)


