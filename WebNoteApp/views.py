from django.shortcuts import render
from rest_framework.response import Response
from .models import NoteModel
from rest_framework.decorators import api_view
from .serializers import NoteSerializers
# Create your views here.
@api_view(['GET'])
def getRoute(request):
    routes = [
        {
            'Endpoint':'/noteapp/get-notes',
            'Method':'GET',
            'Parameter':'None',
            'Description':'This will return all the notes form the list',
        },
        {
            'Endpoint':'/noteapp/get-note',
            'Method':'GET',
            'Parameter':'note-id',
            'Description':'This will return single note detail',
        },
        {
            'Endpoint':'/noteapp/create-note',
            'Method':'POST',
            'Parameter':"body",
            'Description':'This will create a new node',
        },
        {
            'Endpoint':'/noteapp/update-note/<id>',
            'Method':'POST',
            'Parameter':"body,id",
            'Description':'This will return all the notes form the list',
        },
        {
            'Endpoint':'/noteapp/delete-note/<id>',
            'Method':'POST',
            'Parameter':"body,id",
            'Description':'This will return all the notes form the list',
        },
    ]
    return Response(routes)

@api_view(['GET',])
def getNotes(request):
    notes = NoteModel.objects.all()
    serializer = NoteSerializers(notes, many = True)
    return Response(serializer.data)


@api_view(['GET','POST'])
def getNote(request,id):
    note = NoteModel.objects.get(id=id)
    serializer = NoteSerializers(note,many=False)
    return Response(serializer.data)