from django.db import models

class Profile(models.Model):
    nom = models.CharField(max_length=100)
    titre = models.CharField(max_length=150)
    bio = models.TextField()
    email = models.EmailField()
    photo = models.ImageField(upload_to='profile/', blank=True, null=True)
    cv = models.FileField(upload_to='cv/', blank=True, null=True)
    github = models.URLField(blank=True)
    linkedin = models.URLField(blank=True)

    def __str__(self):
        return self.nom


class Project(models.Model):
    titre = models.CharField(max_length=200)
    description = models.TextField()
    technologies = models.CharField(max_length=200)
    image = models.ImageField(
        upload_to='projects/',
        blank=True,
        null=True
    )
    lien = models.URLField(blank=True)
    date = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.titre

class ProjectImage(models.Model):
    project = models.ForeignKey(
        Project,
        related_name='gallery',
        on_delete=models.CASCADE
    )
    image = models.ImageField(upload_to='projects/gallery/')

    def __str__(self):
        return f"Image - {self.project.titre}"



class Service(models.Model):
    titre = models.CharField(max_length=150)
    description = models.TextField()
    icone = models.CharField(max_length=50, blank=True)
    image = models.ImageField(upload_to='services/', blank=True, null=True)


    def __str__(self):
        return self.titre


class Contact(models.Model):
    nom = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nom


class Blog(models.Model):
    titre = models.CharField(max_length=200)
    slug = models.SlugField(unique=True)
    contenu = models.TextField()
    image = models.ImageField(upload_to='blog/', blank=True, null=True)
    date = models.DateTimeField(auto_now_add=True)
    published = models.BooleanField(default=True)

    def __str__(self):
        return self.titre

class Apropos(models.Model):
    titre = models.CharField(max_length=200)
    contenu = models.TextField()
    image = models.ImageField(upload_to="apropos/", blank=True, null=True)

    def __str__(self):
        return self.titre


class Competence(models.Model):
    nom = models.TextField()
    niveau = models.PositiveIntegerField(help_text="0 à 100")
    icone = models.ImageField(upload_to="competences/", blank=True, null=True)

    def __str__(self):
        return self.nom



class InformationsPersonnelles(models.Model):
    date_naissance = models.DateField(null=True, blank=True)
    lieu_naissance = models.CharField(max_length=255, blank=True)
    email = models.EmailField(blank=True)
    telephone = models.CharField(max_length=30, blank=True)
    adresse = models.TextField(blank=True)
    pays = models.CharField(max_length=100, blank=True)

    class Meta:
        verbose_name = "Informations personnelles"
        verbose_name_plural = "Informations personnelles"
