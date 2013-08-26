=============================
django-bootstrap-calendar
=============================

simple calendar based on the bootstrap calendar from http://bootstrap-calendar.azurewebsites.net/

.. image:: https://raw.github.com/sandlbn/django-bootstrap-calendar/master/screenshot.png

Requirements
------------

- Python 2.6, 2.7
- Django (1.4.3+)
- jsmin (2.0.3+)

Instalation
----------

Django:

settings.py::

    INSTALLED_APPS = (
    ...
    'django_bootstrap_calendar',
    ...
    )

urls.py::

    urlpatterns = patterns('',
    ...
    (r'^calendar/', include('django_bootstrap_calendar.urls')),
    ...
    )

Load templatetags::

    {% load bootstrap_calendar %}

In your template file::

    Calendar controls :

    {% bootstrap_controls 'optional-css-classes' %}
    
    Calendar:

    {% bootstrap_calendar 'optional-css-classes' %}

In your base.html file css section::

    {% bootstrap_calendar_css %}

In your base.html file javascript section::

    {% bootstrap_calendar_js language="lang-code" %} 
    {% bootstrap_calendar_init language="lang-code" %} 


