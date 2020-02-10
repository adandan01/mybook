Django inline formset example
==================

This is a simple django app that demonstrates how to use inline formset.

Mybook is a social networking app. In the app, you can edit your social profile. One section of the profile is about your family member.
You can add as many family member as you like. For each family member, you need to specify family member's relationship with you.

Quick start
-----------
1. (optional) create virtual env ex. mkvirtualenv mybook_env
2. pip install -r requirements.txt
3. (optional) source export_django_setting.py
4. python manage.py migrate
5. python manage.py runserver

Load Sample Data
---------------- 
`$: python manage.py loaddata profile.json`
`$: python manage.py loaddata family_member.json`

Useful references:
-----------
* https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-display/
* https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/
* https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-editing/
* https://docs.djangoproject.com/en/1.10/ref/class-based-views/flattened-index/
* https://docs.djangoproject.com/en/1.10/topics/forms/modelforms/#inline-formsets
* http://whoisnicoleharris.com/2015/01/06/implementing-django-formsets.html
* https://github.com/elo80ka/django-dynamic-formset
* https://gist.github.com/neara/6209563
* http://stackoverflow.com/questions/27876644/django-class-based-createview-and-updateview-with-multiple-inline-formsets
* https://github.com/AndrewIngram/django-extra-views
* http://ruddra.com/2015/09/18/working-with-formset/


