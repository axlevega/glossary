from django.contrib import admin
from .models import Project, Term

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('name', 'user', 'created_at')
    search_fields = ('name', 'user__username')

@admin.register(Term)
class TermAdmin(admin.ModelAdmin):
    list_display = ('word', 'project', 'created_at', 'updated_at')
    search_fields = ('word', 'project__name')
