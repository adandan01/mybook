Django formset tutorial
==================

This is a simple django app that will demonstrate how to use django formset. I recently wanted to use the formset in my work but i couldn't find any good working example. 
I ended doing a lot of trial and error and looked at the django source code. At tne end, I really enjoyed using this feature but wish the documentation would be better now. This is my small attempt to make it better for someone else. 

I will use a simple django app called mybook to demostrate the different usages of formset. The model and the scenario is faily simple. 

Mybook is a social network app. In the app, you can edit your social profile. One section of the profile is about your family. 
You can add as family member as you like. For each family member, you need to specify family member's relationship with you.  
   

useful documenations:
----
* https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-display/
* https://docs.djangoproject.com/en/1.10/topics/class-based-views/generic-editing/
* https://docs.djangoproject.com/en/1.10/ref/class-based-views/generic-editing/

