from rest_framework import serializers
from base.models import Item
from base.models import blog
from base.models import message

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

    
class blogSerializer(serializers.ModelSerializer):
    class Meta:
        model =  blog
        fields = '__all__'


class messageSerializer(serializers.ModelSerializer):
    class Meta:
        model = message
        fields = '__all__'