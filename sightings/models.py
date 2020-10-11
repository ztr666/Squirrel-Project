from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    Latitude = models.FloatField(
        help_text=_('Latitude for the squirrel'),
        blank=False,
    )

    Longitude = models.FloatField(
        help_text=_('Longitude for the squirrel'),
        blank=False,
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text=_('Identification tag for each squirrel sightings'),
        unique=True,
        blank=False,
    )
    
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),
    ]

    Shift = models.CharField(
        max_length=100,
        blank=False,
        choices=SHIFT_CHOICES,
    )

    Date = models.CharField(
        max_length=100,
        blank=False,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'

    AGE_CHOICES = [
            (ADULT, _('Adult')),
            (JUVENILE, _('Juvenile')),
    ]

    Age = models.CharField(
        max_length=100,
        blank=True,
        choices=AGE_CHOICES,
    )

    GRAY = 'Gray'
    CINNAMON = 'Cinnamon'
    BLACK = 'Black'

    FUR_CHOICES = [
            (GRAY, _('Gray')),
            (CINNAMON, _('Cinnamon')),
            (BLACK, _('Black')),
    ]

    Primary_Fur_Color = models.CharField(
        max_length=100,
        blank=True,
        choices=FUR_CHOICES,
    )
    
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    LOCATION_CHOICES = [
            (GROUND, _('Ground Plane')),
            (ABOVE, _('Above Ground')),
    ]

    Location = models.CharField(
        max_length=100, 
        blank=True,
        choices=LOCATION_CHOICES,
    )
    
    Specific_Location = models.CharField(
        max_length=100, 
        blank=True,
    )
    
    Running = models.BooleanField(
        blank=True,
    )
    
    Chasing = models.BooleanField(
        blank=True,
    )
    
    Climbing = models.BooleanField(
        blank=True,
    )
    
    Eating = models.BooleanField(
        blank=True,
    )
    
    Foraging = models.BooleanField(
        blank=True,
    )
    
    Other_Activities = models.CharField(
        max_length=100,
        blank=True,
    )
    
    Kuks = models.BooleanField(
        blank=True,
    )
    
    Quaas = models.BooleanField(
        blank=True,
    )
    
    Moans = models.BooleanField(
        blank=True,
    )
    
    Tail_Flags = models.BooleanField(
        blank=True,
    )
    
    Tail_Twitches = models.BooleanField(
        blank=True,
    )
    
    Approaches = models.BooleanField(
        blank=True,
    )
    
    Indifferent = models.BooleanField(
        blank=True,
    )
    
    Runs_From = models.BooleanField(
        blank=True,
    )
