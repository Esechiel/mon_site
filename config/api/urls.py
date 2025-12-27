from rest_framework.routers import DefaultRouter
from .views import (
    ProfileViewSet,
    ProjectViewSet,
    ServiceViewSet,
    ContactViewSet,
    BlogViewSet,
    AproposViewSet,
    CompetenceViewSet,
    InformationsPersonnellesViewSet
)

router = DefaultRouter()
router.register('profile', ProfileViewSet)
router.register('projects', ProjectViewSet)
router.register('services', ServiceViewSet)
router.register('contact', ContactViewSet)
router.register('blog', BlogViewSet)
router.register("apropos", AproposViewSet)
router.register("competences", CompetenceViewSet)
router.register("informations-personnelles", InformationsPersonnellesViewSet)


urlpatterns = router.urls
