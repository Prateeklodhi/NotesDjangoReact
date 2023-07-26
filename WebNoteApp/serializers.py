from rest_framework.serializers import ModelSerializer
from .models import NoteModel

class NoteSerializers(ModelSerializer):
    class Meta:
        model = NoteModel
        fields = '__all__'
