from rest_framework import status
from rest_framework.response import Response
from rest_framework.request import Request
from rest_framework.decorators import api_view
from drf_yasg.utils import swagger_auto_schema

from .models import Home
from .serializers import HomeSerializer


@swagger_auto_schema(methods=['post'], request_body=HomeSerializer, operation_description='Create new home')
@swagger_auto_schema(methods=['get'], operation_description='List all homes')
@api_view(['GET', 'POST'])
def homes(request: Request) -> Response:
    if request.method == 'GET':
        res = HomeSerializer(Home.objects.all(), many=True)
        return Response(res.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        new_home = HomeSerializer(data=request.data)
        if new_home.is_valid():
            new_home.save()
            return Response(new_home.data, status=status.HTTP_201_CREATED)
        else:
            return Response(new_home.errors, status=status.HTTP_400_BAD_REQUEST)


@swagger_auto_schema(methods=['put'], request_body=HomeSerializer, operation_description='Update home data')
@swagger_auto_schema(methods=['get'], operation_description='Fetch home data')
@swagger_auto_schema(methods=['delete'], operation_description='Remove a home from the system')
@api_view(['GET', 'PUT', 'DELETE'])
def home_by_id(request: Request, home_id: int) -> Response:
    try:
        home = Home.objects.get(id=home_id)
    except Home.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        res = HomeSerializer(home)
        return Response(res.data)
    elif request.method == 'PUT':
        new_home_data = HomeSerializer(home, data=request.data)
        if new_home_data.is_valid():
            new_home_data.save()
            return Response(new_home_data.data, status=status.HTTP_200_OK)
        else:
            return Response(new_home_data.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        home.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
