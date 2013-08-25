============
Installation
============

At the command line::

    $ git clone https://github.com/sandlbn/django-bootstrap-calendar.git 
    $ cd django-bootstrap-calendar
    $ python setup.py install

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

    {% bootstrap_calendar_js %} 

