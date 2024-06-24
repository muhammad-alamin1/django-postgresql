from rest_framework import serializers
from .models import OrmTestModel, Author

class AuthorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Author
        fields = '__all__'

class OrmTestModelSerializer(serializers.ModelSerializer):
    author = AuthorSerializer()
    
    class Meta:
        model = OrmTestModel
        fields = '__all__'