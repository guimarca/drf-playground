from django.urls import path
from rest_framework import routers

from .views import StuffViewset, StuffScoreView

router = routers.SimpleRouter()
router.register(r"", StuffViewset)

urlpatterns = [path("<score>/list", StuffScoreView.as_view())]

urlpatterns += router.urls
