# -*- coding: utf-8 -*-
__author__ = 'sandlbn'
from django.db import models
from django.utils.translation import ugettext as _


class CalendarEvent(models.Model):
    """
    Calendar Events
    """
    CSS_CLASS_CHOICES = (
        ('', _('Normal')),
        ('event-warning', _('Warning')),
        ('event-info', _('Info')),
        ('event-success', _('Success')),
        ('event-inverse', _('Inverse')),
        ('event-special', _('Special')),
        ('event-important', _('Important')),
    )
    title = models.CharField(max_length=255, verbose_name=_('Title'))
    url = models.URLField(verbose_name=_('URL'))
    css_class = models.CharField(max_length=20, verbose_name=_('CSS Class'))
    start = models.DateTimeField(verbose_name=_('Start Date'))
    end = models.DateTimeField(verbose_name=_('End Date'), blank=True)

    def __unicode__(self):
        return self.title
