from rest_framework import serializers
from .models import User, UserProfile, ClothingItem, Outfit

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'

class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserProfile
        fields = '__all__'

class ClothingItemSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')

    class Meta:
        model = ClothingItem
        fields = '__all__'

class OutfitSerializer(serializers.ModelSerializer):
    owner = serializers.ReadOnlyField(source='owner.username')
    clothing_items = ClothingItemSerializer(many=True)

    class Meta:
        model = Outfit
        fields = '__all__'
