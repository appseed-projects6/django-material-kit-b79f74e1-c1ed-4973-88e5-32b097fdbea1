# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import gettext_lazy as _

# Create your models here.

class UserProfile(models.Model):

    user = models.OneToOneField(User, on_delete=models.CASCADE)

    #__PROFILE_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    phone = models.CharField(max_length=255, null=True, blank=True)
    bio = models.CharField(max_length=255, null=True, blank=True)

    #__PROFILE_FIELDS__END

    def __str__(self):
        return self.user.username
    
    class Meta:
        verbose_name        = _("UserProfile")
        verbose_name_plural = _("UserProfile")

#__MODELS__
class User(models.Model):

    #__User_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    admin = models.CharField(max_length=255, null=True, blank=True)
    user_profile = models.CharField(max_length=255, null=True, blank=True)
    first_name = models.CharField(max_length=255, null=True, blank=True)
    last_name = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=255, null=True, blank=True)
    staff = models.CharField(max_length=255, null=True, blank=True)

    #__User_FIELDS__END

    class Meta:
        verbose_name        = _("User")
        verbose_name_plural = _("User")


class Booking(models.Model):

    #__Booking_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    user = models.CharField(max_length=255, null=True, blank=True)
    start_date = models.CharField(max_length=255, null=True, blank=True)
    end_date = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)

    #__Booking_FIELDS__END

    class Meta:
        verbose_name        = _("Booking")
        verbose_name_plural = _("Booking")


class Amenity(models.Model):

    #__Amenity_FIELDS__
    name = models.CharField(max_length=255, null=True, blank=True)
    icon = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=255, null=True, blank=True)
    created_at = models.CharField(max_length=255, null=True, blank=True)

    #__Amenity_FIELDS__END

    class Meta:
        verbose_name        = _("Amenity")
        verbose_name_plural = _("Amenity")


class Stay(models.Model):

    #__Stay_FIELDS__
    id = models.CharField(max_length=255, null=True, blank=True)
    title = models.CharField(max_length=255, null=True, blank=True)
    host = models.CharField(max_length=255, null=True, blank=True)
    city = models.CharField(max_length=255, null=True, blank=True)
    state = models.CharField(max_length=255, null=True, blank=True)
    country = models.CharField(max_length=255, null=True, blank=True)
    guest = models.CharField(max_length=255, null=True, blank=True)
    bedroom = models.CharField(max_length=255, null=True, blank=True)
    price = models.CharField(max_length=255, null=True, blank=True)
    check_in = models.CharField(max_length=255, null=True, blank=True)
    description = models.CharField(max_length=255, null=True, blank=True)
    bookings = models.CharField(max_length=255, null=True, blank=True)
    main_image = models.CharField(max_length=255, null=True, blank=True)
    active = models.CharField(max_length=255, null=True, blank=True)

    #__Stay_FIELDS__END

    class Meta:
        verbose_name        = _("Stay")
        verbose_name_plural = _("Stay")



#__MODELS__END
