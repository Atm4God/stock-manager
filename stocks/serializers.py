from abc import ABC

from rest_framework import serializers

from .models import Stock


class StockSerializer(serializers.HyperlinkedModelSerializer):
    url = serializers.HyperlinkedRelatedField(read_only=True, view_name='stocks:stock-detail')
    owner = serializers.HyperlinkedRelatedField(read_only=True, view_name='accounts:account-detail')

    class Meta:
        model = Stock
        fields = ('id', 'url', 'owner', 'name', 'symbol', 'unit_price', 'shares', 'total_price')


class StockSearchSerializer(serializers.Serializer):
    price = serializers.CharField()
    company_name = serializers.CharField()

    def create(self, validated_data):
        return Stock(**validated_data)
