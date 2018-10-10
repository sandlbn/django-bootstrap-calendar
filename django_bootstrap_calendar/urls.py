# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.conf.urls import url
from views import CalendarJsonListView, CalendarView

urlpatterns = [
    url(
        r'^json/$',
        CalendarJsonListView.as_view(),
        name='calendar_json'
    ),
    url(
        r'^$',
        CalendarView.as_view(),
        name='calendar'
    ),
]
