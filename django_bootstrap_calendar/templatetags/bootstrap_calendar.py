# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django import template
from jsmin import jsmin
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


@register.simple_tag
def bootstrap_calendar_init(*args, **kwargs):
    """
    """
    options = {}

    try:
        options["events_url"] = kwargs["events_url"]
    except KeyError:
        options["events_url"] = '/calendar/json/'

    try:
        options["view"] = kwargs["view"]
    except KeyError:
        options["view"] = 'month'

    try:
        options["first_day"] = kwargs["first_day"]
    except KeyError:
        options["first_day"] = 1

    return render_to_string('partial/calendar_init.html', options)
