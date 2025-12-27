from rest_framework import serializers
from core.models import Profile, Project, Service, Contact, Blog, Apropos, Competence, InformationsPersonnelles

class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = '__all__'

class ProjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Project
        fields = '__all__'


class ServiceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Service
        fields = '__all__'


class ContactSerializer(serializers.ModelSerializer):
    class Meta:
        model = Contact
        fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'

class AproposSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apropos
        fields = "__all__"


class CompetenceSerializer(serializers.ModelSerializer):
    icone = serializers.ImageField(use_url=True)

    class Meta:
        model = Competence
        fields = "__all__"

class InformationsPersonnellesSerializer(serializers.ModelSerializer):
    class Meta:
        model = InformationsPersonnelles
        fields = "__all__"
