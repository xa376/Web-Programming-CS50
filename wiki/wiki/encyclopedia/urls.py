from django.urls import path

from . import util

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("entry", views.entry, name="entry")
]
for entry in util.list_entries():
    urlpatterns.append(path(entry, views.entry, name=entry))
