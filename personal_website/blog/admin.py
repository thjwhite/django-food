from django.contrib import admin

from .models import BlogEntry, Section, Part


class PartInline(admin.TabularInline):
    model = Part
    extra = 1


class SectionInline(admin.TabularInline):
    model = Section
    extra = 1


class BlogEntryAdmin(admin.ModelAdmin):
    inlines = [SectionInline]


class SectionAdmin(admin.ModelAdmin):
    inlines = [PartInline]


admin.site.register(BlogEntry, BlogEntryAdmin)
admin.site.register(Section, SectionAdmin)
