from rest_framework import serializers
from .models import Artiste, Song, Lyrics


#  Create simple basic serializers to handle validations of incoming data
class ArtisteSerializers(serializers.ModelSerializer):
    class Meta:
        model = Artiste
        fields = '__all__'


class SongSerializers(serializers.ModelSerializer):
    class Meta:
        model = Song
        fields = '__all__'


class LyricsSerializers(serializers.ModelSerializer):
    class Meta:
        model = Lyrics
        fields = '__all__'
