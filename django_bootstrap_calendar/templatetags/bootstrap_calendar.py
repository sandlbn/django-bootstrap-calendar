# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django import template
from django.template.loader import render_to_string

register = template.Library()


@register.simple_tag
def bootstrap_calendar(css_classes):
    """
    return a calendar div if none push empty ""
    """
    return render_to_string(
        'partial/calendar.html',
        {'css_classes': css_classes}
    )


@register.simple_tag
def bootstrap_controls(css_classes):
    """
    return a calendar controls div if none push empty ""
    """
    return render_to_string(
        'partial/calendar_controls.html',
        {'css_classes': css_classes}
    )


@register.simple_tag
def bootstrap_calendar_js(*args):
    """
    return a boostrap calendar tag java script files
    """
    return render_to_string(
        'partial/calendar_js.html'
    )


@register.simple_tag
def bootstrap_calendar_css(*args):
    """
    return a boostrap calendar tag css files
    """
    return render_to_string(
        'partial/calendar_css.html'
    )
