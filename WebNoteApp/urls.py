from django.urls import path
from . import views
urlpatterns = [
    path('notes',views.getRoute,name="routes"),
    path('get-notes',views.getNotes,name="get_notes"),
    path('get-notes/<int:id>/',views.getNote,name="get_note"),
]