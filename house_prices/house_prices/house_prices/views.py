from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework import status


class MainView(ListAPIView):
    def get(self, request, *args, **kwargs):
        return Response("Hello World", status=status.HTTP_200_OK)
