from rest_framework import serializers
from .models import ConnectDB


class ConnectDBSerializers(serializers.ModelSerializer):
    class Meta:
        model = ConnectDB
        fields = "__all__"