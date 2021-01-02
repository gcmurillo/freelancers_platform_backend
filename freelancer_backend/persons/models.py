from django.db import models
from django.contrib.auth.models import User
from django_countries.fields import CountryField
from multiselectfield import MultiSelectField

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    country = CountryField()
    is_freelancer = models.BooleanField(null=True, blank=True)
    is_entrepreneur = models.BooleanField(null=True, blank=True)
    years_of_experience = models.IntegerField(null=True, blank=True)
    joined_at = models.DateField()


class ExperienceItem(models.Model):
    TECHS_ENUM = (
        ("PYT", "Python"),
        ("DJA", "Django"),
        ("NOD", "Node"),
        ("ANG", "Angular"),
        ("REA", "React"),
        ("VUE", "Vue"),
        ("KER", "Keras"),
        ("TEN", "TensorFlow"),
        ("JUP", "Jupyter"),
        ("ION", "Ionic"),
        ("AND", "Android"),
        ("IOS", "iOS"),
        ("UNI", "Unity"),
        ("UNE", "Unreal Engine"),
        ("FLA", "Flask"),
        ("NET", ".Net/C#"),
        ("AWS", "AWS"),
        ("AZU", "Azure"),
        ("GCP", "GCP"),
        ("CCC", "C"),
        ("SQL", "SQL"),
        ("JAV", "Java"),
        ("KOT", "Kotlin"),
        ("LAR", "Laravel"),
    )

    techs_used = MultiSelectField(choices=TECHS_ENUM, null=False, blank=False)
    description = models.TextField(max_length=1000, blank=True)
    since = models.DateField(null=False, blank=False)
    to = models.DateField(null=True)
    company = models.CharField(max_length=30, null=False, blank=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
