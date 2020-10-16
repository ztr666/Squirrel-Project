from django.db import models
from django.utils.translation import gettext as _


class Squirrel(models.Model):
    Latitude = models.FloatField(
        help_text=_('Latitude for squirrel'),
    )

    Longitude = models.FloatField(
        help_text=_('Longitude for squirrel'),
    )

    Unique_Squirrel_ID = models.CharField(
        max_length=100,
        help_text=_('Identification tag for each squirrel sightings'),
    )
    
    AM = 'AM'
    PM = 'PM'

    SHIFT_CHOICES = [
            (AM, _('AM')),
            (PM, _('PM')),
    ]

    Shift = models.CharField(
        help_text=_('Morning or evening'),
        max_length=100,
        blank=True,
        choices=SHIFT_CHOICES,
    )

    Date = models.CharField(
        max_length=100,
        blank=True,
    )

    ADULT = 'Adult'
    JUVENILE = 'Juvenile'
    OTHER = '?'

    AGE_CHOICES = [
            (ADULT, _('Adult')),
            (JUVENILE, _('Juvenile')),
            (None,_('')),
            (OTHER,_('?')),
    ]

    Age = models.CharField(
        help_text=_('Age of squirrel'),
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
            (None,_('')),
    ]

    Primary_Fur_Color = models.CharField(
        help_text=_('Primary fur color of squirrel'),
        max_length=100,
        blank=True,
        choices=FUR_CHOICES,
    )
    
    GROUND = 'Ground Plane'
    ABOVE = 'Above Ground'

    LOCATION_CHOICES = [
            (GROUND, _('Ground Plane')),
            (ABOVE, _('Above Ground')),
            (None,_('')),
    ]

    Location = models.CharField(
        help_text=_('Location of squirrel'),
        max_length=100, 
        blank=True,
        choices=LOCATION_CHOICES,
    )
    
    Specific_Location = models.CharField(
        help_text=_('Specific location of squirrel'),
        max_length=100, 
        blank=True,
    )
    
    Running = models.BooleanField(
        help_text=_('Whether or not squirrel is running'),
        blank=True,
    )
    
    Chasing = models.BooleanField(
        help_text=_('Whether or not squirrel is chasing'),
        blank=True,
    )
    
    Climbing = models.BooleanField(
        help_text=_('Whether or not squirrel is climbing'),
        blank=True,
    )
    
    Eating = models.BooleanField(
        help_text=_('Whether or not squirrel is eating'),
        blank=True,
    )
    
    Foraging = models.BooleanField(
        help_text=_('Whether or not squirrel is foraging'),
        blank=True,
    )
    
    Other_Activities = models.CharField(
        help_text=_('Other activities of squirrel'),
        max_length=100,
        blank=True,
    )
    
    Kuks = models.BooleanField(
        help_text=_('Whether or not squirrel kuks'),
        blank=True,
    )
    
    Quaas = models.BooleanField(
        help_text=_('Whether or not squirrel quaas'),
        blank=True,
    )
    
    Moans = models.BooleanField(
        help_text=_('Whether or not squirrel moans'),
        blank=True,
    )
    
    Tail_Flags = models.BooleanField(
        help_text=_('Whether or not squirrel tail flags'),
        blank=True,
    )
    
    Tail_Twitches = models.BooleanField(
        help_text=_('Whether or not squirrel tail twitches'),
        blank=True,
    )
    
    Approaches = models.BooleanField(
        help_text=_('Whether or not squirrel approaches'),
        blank=True,
    )
    
    Indifferent = models.BooleanField(
        help_text=_('Whether or not squirrel is indifferent'),
        blank=True,
    )
    
    Runs_From = models.BooleanField(
        help_text=_('Whether or not squirrel runs from'),
        blank=True,
    )

    def __str__(self):
        return self.Unique_Squirrel_ID
