from django.shortcuts import get_object_or_404, render
from .serializers import *
from .models import Cartochka
from rest_framework .views import APIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.permissions import AllowAny


class EventsView(APIView):
    serializer_class = SubjectSerializer
    permission_classes = [AllowAny]  # Разрешает доступ всем пользователям
    queryset = Cartochka.objects.all()


    def get(self, request, pk=None):
        if pk:
            person = get_object_or_404(Cartochka, pk=pk)
            serializer = SubjectSerializer(person, context={"request": request})
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            events = Cartochka.objects.all()
            serializer = SubjectSerializer(events, many=True, context={'request': request})
            return Response(serializer.data, status=status.HTTP_200_OK)

    def post(self, request, *args, **kwargs):
      serializer = SubjectSerializer(data=request.data, many=True)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put (self, request, *args, **kwargs):
      pk = kwargs.get('pk', None)
      if not pk:
        return Response({'error': 'Missing primary key'}, status=status.HTTP_400_BAD_REQUEST)
    
      try:
        instance = Cartochka.objects.get(pk=pk)
      except: 
        return Response({'error': 'Cartochka not found'}, status=status.HTTP_404_NOT_FOUND)
    
      serializers = SubjectSerializer(data = request.data, instance=instance)
      serializers.is_valid(raise_exception=True)
      serializers.save()
      return Response({'post': serializers.data})
    

    def delete(self, request, pk, *args, **kwargs):
        person = get_object_or_404(Cartochka, pk=pk)
        person.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

    


