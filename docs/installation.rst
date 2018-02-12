============
Installation
============

At the command line::

    $ git clone https://github.com/sandlbn/django-bootstrap-calendar.git 
    $ cd django-bootstrap-calendar
    $ python setup.py install
Another Method of Installation:
    Simply add this -- "git+git://github.com/sandlbn/django-bootstrap-calendar.git@86c87c98380fc98b1d2d32d225f9a8dbd38e07a6#egg=django-bootstrap-calendar" to your requirement.txt file (reflecting the latest github commit as of July 7, 2016; simply switch out the numbers "86c87c98380fc98b1d2d32d225f9a8dbd38e07a6" with the latest commit numbers if needed). 
    You can now run the installation command -- "pip install -r requirement.txt" in the command line. This should be a cleaner method of importing the app to your current project without any python path issue provided that you follow the rest of the instructions below.
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

