from rest_framework import serializers
from .models import SearchBox, ValueSearch

class SearchBoxSerializer(serializers.ModelSerializer):
    class Meta:
        model = SearchBox
        fields = ('Text_box',)

class ValueSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = ValueSearch
        fields = ('title', 'titles', 'urls', 'price')

        def create(self, validated_data):
            return ValueSearch.objects.create(**validated_data)