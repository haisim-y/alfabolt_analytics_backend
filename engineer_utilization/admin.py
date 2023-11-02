from django.contrib import admin
from .models import Resource,Project,ProjectResource,Technology,ResourceTechnology,Level,Status,Designation
# Register your models here.
admin.site.register(Resource)
admin.site.register(Project)
admin.site.register(ProjectResource)
admin.site.register(Technology)
admin.site.register(ResourceTechnology)
admin.site.register(Level)
admin.site.register(Status)
admin.site.register(Designation)