from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializers import ItemSerializer
from .serializers  import blogSerializer
from .serializers import messageSerializer
from base.models import Item 
from base.models import blog
from base.models import message


@api_view(['GET'])
def getData(request):
    items  = Item.objects.all()
    serializer = ItemSerializer(items,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def addItem(request):
    serializer = ItemSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getblog(request):
    blogs = blog.objects.all()
    serializer = blogSerializer(blogs,many=True)
    return Response(serializer.data)

@api_view(['POST'])
def addblog(request):
    serializer = blogSerializer(data=request.data)
    if serializer.is_valid():
        serializer.save()
    return Response(serializer.data)


@api_view(['GET'])
def getmessage(request):
    messages = message.objects.all()
    serializer = messageSerializer(messages,many=True)
    return Response(serializer.data)


@api_view(['POST'])
def postmessage(request):
    message = messageSerializer(data=request.data)
    if message.is_valid():
        message.save()
    return Response(message.data)

