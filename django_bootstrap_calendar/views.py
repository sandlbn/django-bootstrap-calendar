# -*- coding: utf-8 -*-
__author__ = 'sandlbn'

from django.views.generic import ListView, TemplateView
from models import CalendarEvent
from serializers import event_serializer
from utils import timestamp_to_datetime


class CalendarJsonListView(ListView):

    template_name = 'django_bootstrap_calendar/calendar_events.html'

    def get_queryset(self):
        queryset = CalendarEvent.objects.filter()
        from_date = self.request.GET.get('from', False)
        to_date = self.request.GET.get('to', False)

        if from_date:
            queryset = queryset.filter(
                start__gte=timestamp_to_datetime(from_date)
            )
        if to_date:
            queryset = queryset.filter(
                end__lte=timestamp_to_datetime(to_date)
            )

        return event_serializer(queryset)


class CalendarView(TemplateView):

    template_name = 'django_bootstrap_calendar/calendar.html'
