# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django import template
from datetime import datetime
from time import mktime
from jsmin import jsmin


def timestamp_to_datetime(timestamp):
    """
    Converts string timestamp to datetime
    with json fix
    """
    if isinstance(timestamp, (str, unicode)):

        if len(timestamp) == 13:
            timestamp = int(timestamp) / 1000

        return datetime.fromtimestamp(timestamp)
    else:
        return ""


def datetime_to_timestamp(date):
    """
    Converts datetime to timestamp
    with json fix
    """
    if isinstance(date, datetime):

        timestamp = mktime(date.timetuple())
        json_timestamp = int(timestamp) * 1000

        return '{0}'.format(json_timestamp)
    else:
        return ""


class MinifyJs(template.Node):

    def __init__(self, nodelist):
        self.nodelist = nodelist

    def render(self, context):
        return jsmin(self.nodelist.render(context))
