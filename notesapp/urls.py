from django.urls import path

from .views import NotesListView,NotesCreateView,NotesDeleteView,NotesUpdateView



urlpatterns = [
    path("",NotesListView.as_view(),name = "notes-list"),
    path('add/',NotesCreateView.as_view(),name="note-create"),
    path('update/<int:pk>/',NotesUpdateView.as_view(),name="note-update"),
    path("delete/<int:pk>/",NotesDeleteView.as_view(),name="note-delete"),

]

