from rest_framework import serializers
from .models import *

class Bookserializers(serializers.ModelSerializer):
    class Meta:
        model=Book
        fields='__all__'