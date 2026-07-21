from rest_framework import serializers
from .models import InstituteProfile

# Create your tests here.


class InstituteSerializer(serializers.ModelSerializer):
    class Meta:
        model = InstituteProfile
        fields = '__all__'