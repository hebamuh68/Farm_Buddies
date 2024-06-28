from django.db import models
from .choices import age_CHOICES, gender_CHOICES, governorate_CHOICES, cs_CHOICES, experience_CHOICES, \
    buddy_gender_CHOICES, buddy_age_CHOICES, buddy_governorate_CHOICES

class UserModel(models.Model):

    name = models.CharField(max_length=100, blank=False, null=False)

    email = models.EmailField(max_length=320, primary_key=True, unique=True, blank=False, null=False )

    age = models.CharField(max_length=100, choices=age_CHOICES, default='18-25', blank=False, null=False)

    gender = models.CharField(max_length=100, choices=gender_CHOICES, default='Female', blank=False, null=False)

    governorate = models.CharField(max_length=100, choices=governorate_CHOICES, default='Alexandria', blank=False,
                                   null=False)

    cs_field = models.CharField(max_length=100, choices=cs_CHOICES, default='UI/UX', blank=False, null=False)

    experience_levels = models.CharField(max_length=100, choices=experience_CHOICES, default='Junior', blank=False,
                                         null=False)

    twitter_link = models.URLField(max_length=500, blank=False, null=False)

    github_link = models.URLField(max_length=500, blank=False, null=False)


    # Farm Buddy =================================================================

    buddy_age = models.CharField(max_length=100, choices=buddy_age_CHOICES, default='18-25', blank=False, null=False)

    buddy_gender = models.CharField(max_length=100, choices=buddy_gender_CHOICES, default='Female', blank=False,
                                    null=False)

    buddy_governorate = models.CharField(max_length=100, choices=buddy_governorate_CHOICES, default='Alexandria', blank=False,
                                         null=False)