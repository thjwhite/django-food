from django.contrib import admin
from .models import Recipe, IngredientRequirement, Ingredient

admin.site.site_header = 'TJ White\'s website admin panel'
admin.site.site_title = 'TJ White\'s personal website'
admin.site.index_title = 'Administration'


class IngredientRequirementInline(admin.TabularInline):
    model = IngredientRequirement
    extra = 1


class RecipeAdmin(admin.ModelAdmin):
    fieldsets = [
        ('General Information', {'fields': ['name', 'title']}),
        ('Publishing Information', {'fields': ['date_published']})
    ]
    inlines =[IngredientRequirementInline]
    search_fields = ['title']


admin.site.register(Recipe, RecipeAdmin)
admin.site.register(Ingredient)
