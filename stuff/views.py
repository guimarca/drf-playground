from rest_framework import viewsets
from rest_framework.generics import ListAPIView

from stuff.models import Stuff
from stuff.serializers import StuffSerializer


class StuffViewset(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer


class StuffScoreView(ListAPIView):
    serializer_class = StuffSerializer
    queryset = Stuff.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(score=self.kwargs.get("score"))
