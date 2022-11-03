from rest_framework.response import Response
from rest_framework.decorators import APIView
from REST.models import Song
from .serializers import ArtisteSerializers, SongSerializers, LyricsSerializers
from rest_framework import status


# This class is for creating an Artiste
class CreateArtise(APIView):
    serializer_class = ArtisteSerializers

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        print(request.data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Artiste Created Successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class is for creating a song  and fetching all songs from the SQLite Database
class Create_and_get_all_Song(APIView):

    serializer_class = SongSerializers

# getting all songs from the SQLite Database
    def get(self, request):
        songs = Song.objects.all()
        serializer = self.serializer_class(songs, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

# creating (inserting) a song in the SQLite database
    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Song Created Successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class is for Updating, Reading and Deleting Song from the SQLite Database
class Update_read_del(APIView):
    serializer_class = SongSerializers

# To get a single song based on its ID
    def get(self, request, pk):
        song = Song.objects.get(id=pk)
        serializer = self.serializer_class(song)
        return Response(serializer.data, status=status.HTTP_200_OK)
# To delete a  song based on its ID

    def delete(self, request, pk):
        song = Song.objects.get(id=pk)
        song.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
# To update a song based on its ID

    def post(self, request, pk):
        song = Song.objects.get(id=pk)
        serializer = self.serializer_class(data=request.data, instance=song)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Song Updated successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# This class is for creating lyrics
class CreateLyrics(APIView):

    serializer_class = LyricsSerializers

    def post(self, request):
        data = request.data
        serializer = self.serializer_class(data=data)
        if serializer.is_valid():
            serializer.save()
            response = {
                "message": "Lyrics Created Successfully",
                'data': serializer.data
            }
            return Response(data=response, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
