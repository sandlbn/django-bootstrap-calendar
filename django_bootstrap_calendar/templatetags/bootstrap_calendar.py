# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django import template
from django.template.loader import render_to_string
from django_bootstrap_calendar.utils import MinifyJs

register = template.Library()


@register.simple_tag
def bootstrap_calendar(css_classes):
    """
    return a calendar div if none push empty ""
    """
    return render_to_string(
        'django_bootstrap_calendar/partial/calendar.html',
        {'css_classes': css_classes}
    )


@register.simple_tag
def bootstrap_controls(css_classes):
    """
    return a calendar controls div if none push empty ""
    """
    return render_to_string(
        'django_bootstrap_calendar/partial/calendar_controls.html',
        {'css_classes': css_classes}
    )


@register.simple_tag
def bootstrap_calendar_js(*args, **kwargs):
    """
    return a boostrap calendar tag java script files
    """

    options = {}

    try:
        options["language"] = kwargs["language"]
    except KeyError:
        pass

    return render_to_string(
        'django_bootstrap_calendar/partial/calendar_js.html',
        options
    )


@register.simple_tag
def bootstrap_calendar_css(*args):
    """
    return a boostrap calendar tag css files
    """
    return render_to_string(
        'django_bootstrap_calendar/partial/calendar_css.html'
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
        options["language"] = kwargs["language"]
    except KeyError:
        options["language"] = 'en'

    try:
        options["first_day"] = kwargs["first_day"]
    except KeyError:
        options["first_day"] = 1

    try:
        options["width"] = kwargs["width"]
    except KeyError:
        options["width"] = '100%'

    return render_to_string('django_bootstrap_calendar/partial/calendar_init.html', options)


@register.tag
def minifyjs(parser, token):
    nodelist = parser.parse(('endminifyjs',))
    parser.delete_first_token()
    return MinifyJs(nodelist)

