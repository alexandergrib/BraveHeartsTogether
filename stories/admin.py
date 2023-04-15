from django.contrib import admin
from stories.models import Story


class StoriesAdmin(admin.ModelAdmin):
    model = Story


admin.site.register(Story, StoriesAdmin)