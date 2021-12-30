from rest_framework import serializers

from stuff.models import Stuff


class StuffSerializer(serializers.ModelSerializer):
    class Meta:
        model = Stuff
        fields = "__all__"
