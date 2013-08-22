# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from datetime import datetime
from time import mktime


def timestamp_to_datetime(timestamp):
    """
    Converts string timestamp to datetime
    with json fix
    """
    if isinstance(timestamp, (str, unicode)):
        if len(timestamp) == 13:
            timestamp = timestamp[:10]
        return datetime.fromtimestamp(float(timestamp))
    else:
        return ""


def datetime_to_timestamp(date):
    """
    Converts datetime to timestamp
    with json fix
    """
    if isinstance(date, datetime):
        timestamp = mktime(date.timetuple())
        return '{0}000'.format(long(timestamp))
    else:
        return ""
