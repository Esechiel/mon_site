from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from django.core.mail import send_mail
from django.conf import settings
from rest_framework.permissions import AllowAny
from .permissions import IsAdminOrReadOnly

from core.models import (
    Profile, Project, Service, Contact,
    Blog, Apropos, Competence, InformationsPersonnelles
)
from .serializers import (
    ProfileSerializer, ProjectSerializer, ServiceSerializer,
    ContactSerializer, BlogSerializer, AproposSerializer,
    CompetenceSerializer, InformationsPersonnellesSerializer
)

class ProfileViewSet(viewsets.ModelViewSet):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    permission_classes = [IsAdminOrReadOnly]


class ProjectViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectSerializer
    permission_classes = [IsAdminOrReadOnly]


class ServiceViewSet(viewsets.ModelViewSet):
    queryset = Service.objects.all()
    serializer_class = ServiceSerializer
    permission_classes = [IsAdminOrReadOnly]


class BlogViewSet(viewsets.ModelViewSet):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    permission_classes = [IsAdminOrReadOnly]


class AproposViewSet(viewsets.ModelViewSet):
    queryset = Apropos.objects.all()
    serializer_class = AproposSerializer
    permission_classes = [IsAdminOrReadOnly]


class CompetenceViewSet(viewsets.ModelViewSet):
    queryset = Competence.objects.all()
    serializer_class = CompetenceSerializer
    permission_classes = [IsAdminOrReadOnly]


class InformationsPersonnellesViewSet(viewsets.ModelViewSet):
    queryset = InformationsPersonnelles.objects.all()
    serializer_class = InformationsPersonnellesSerializer
    permission_classes = [IsAdminOrReadOnly]


# Cas spécial : Contact (formulaire public)
class ContactViewSet(viewsets.ModelViewSet):
    queryset = Contact.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]


@api_view(['POST'])
def contact_view(request):
    serializer = ContactSerializer(data=request.data)

    if serializer.is_valid():
        contact = serializer.save()

        # 📧 Envoi de l’email
        subject = f"Nouveau message de {contact.nom}"
        message = f"""
Nom : {contact.nom}
Email : {contact.email}

Message :
{contact.message}
"""

        send_mail(
            subject,
            message,
            settings.DEFAULT_FROM_EMAIL,
            [settings.CONTACT_RECEIVER_EMAIL],
            fail_silently=False,
        )

        return Response(
            {"message": "Message envoyé avec succès"},
            status=status.HTTP_201_CREATED
        )

    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)