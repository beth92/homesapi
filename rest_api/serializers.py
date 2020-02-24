from rest_framework import serializers
from .models import Home


class HomeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Home
        fields = [
            'id',
            'home_type',
            'address',
            'city',
            'state',
            'zipcode',
            'price',
            'rent_price',
            'bedrooms',
            'bathrooms',
            'area_unit',
            'home_size',
            'property_size',
            'year_built',
            'zillow_id',
            'link',
            'zestimate_amount',
            'zestimate_last_updated',
            'rentzestimate_amount',
            'rentzestimate_last_updated',
            'tax_year',
            'tax_value',
            'last_sold_date',
            'last_sold_price',
        ]
