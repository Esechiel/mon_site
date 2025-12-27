from django.contrib import admin
from django.utils.html import format_html
from .models import (
    Project,
    ProjectImage,
    Contact,
    Blog,
    Service,
    Profile,
    Apropos,
    Competence,
    InformationsPersonnelles
)

class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 1

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image_preview', 'date')
    inlines = [ProjectImageInline]

    def image_preview(self, obj):
        if obj.image:
            return format_html(
                '<img src="{}" width="60" />',
                obj.image.url
            )
        return "-"


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image_preview', 'published', 'date')
    prepopulated_fields = {'slug': ('titre',)}

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60"/>', obj.image.url)
        return "-"

@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ('titre', 'image_preview')

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60"/>', obj.image.url)
        return "-"

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ('nom', 'photo_preview', 'cv_preview')

    def photo_preview(self, obj):
        if obj.photo:
            return format_html('<img src="{}" width="60"/>', obj.photo.url)
        return "-"

    def cv_preview(self, obj):
        if obj.cv:
            return format_html(
                '<a href="{}" target="_blank">Voir CV</a>',
                obj.cv.url
            )
        return "-"

@admin.register(Apropos)
class AproposAdmin(admin.ModelAdmin):
    list_display = ("titre", "image_preview")

    def image_preview(self, obj):
        if obj.image:
            return format_html('<img src="{}" width="60"/>', obj.image.url)
        return "-"


@admin.register(Competence)
class CompetenceAdmin(admin.ModelAdmin):
    list_display = ("nom", "niveau", "icone_preview")

    def icone_preview(self, obj):
        if obj.icone:
            return format_html('<img src="{}" width="40"/>', obj.icone.url)
        return "-"
    
@admin.register(InformationsPersonnelles)
class InformationsPersonnellesAdmin(admin.ModelAdmin):
    list_display = (
        "telephone",
        "email",
        "lieu_naissance"
    )

@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ("nom", "email", "date")
    list_filter = ("date",)
    search_fields = ("nom", "email", "message")
    ordering = ("-date",)
