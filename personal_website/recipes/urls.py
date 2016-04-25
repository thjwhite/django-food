from django.conf.urls import url

from . import views

app_name = 'recipes'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^(?P<recipe_name>[\w\d]+)/$', views.recipe_details, name='recipe_details'),
]
