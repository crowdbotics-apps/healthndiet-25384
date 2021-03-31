from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .viewsets import ChoiceViewSet, QuestionViewSet, StepViewSet

router = DefaultRouter()
router.register("step", StepViewSet)
router.register("choice", ChoiceViewSet)
router.register("question", QuestionViewSet)

urlpatterns = [
    path("", include(router.urls)),
]
