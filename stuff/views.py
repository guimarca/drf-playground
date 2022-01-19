from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.generics import ListAPIView
from rest_framework.response import Response

from stuff.models import Stuff
from stuff.serializers import StuffSerializer


class StuffViewset(viewsets.ModelViewSet):
    queryset = Stuff.objects.all()
    serializer_class = StuffSerializer

    @action(detail=True, methods=["post"])
    def foo(self, request, pk=None):
        return Response({"pk": pk})


class StuffScoreView(ListAPIView):
    serializer_class = StuffSerializer
    queryset = Stuff.objects.all()

    def get_queryset(self):
        return super().get_queryset().filter(score=self.kwargs.get("score"))
