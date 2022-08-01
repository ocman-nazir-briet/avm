from django.contrib import admin
# Register your models here.

from .models import Contact
admin.site.register(Contact)

from .models import stats
@admin.register(stats)
class statsAdmin(admin.ModelAdmin):
    list_display = ['id', 'year', 'month', 'sale']

from .models import plots
@admin.register(plots)
class plotAdmin(admin.ModelAdmin):
    list_display=['id', 'description', 'city', 'price', 'bath', 'bed', 'area', 'date', 'picture']

from .models import agents
@admin.register(agents)
class agentAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'picture']



from .models import clients
@admin.register(clients)
class clientAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'type', 'description', 'picture']

from .models import blogs
@admin.register(blogs)
class clientAdmin(admin.ModelAdmin):
    list_display=['id', 'name', 'description', 'date', 'picture']
