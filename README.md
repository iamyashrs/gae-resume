gae-resume
========

> **gae-resume** is a boilerplate to make custom online résumé (rez-u-may) on Google App Engine using Python, Django, AngularJS, Bootstrap and other technologies.


A demonstration of GAE-Resume is online:
[https://gae-resume.appspot.com](https://gae-resume.appspot.com)

Requirements
------------

  - [Google App Engine SDK for Python][]
  - [pip][], [virtualenv][], [perl][]
  - [OS X][] or [Linux][] or [Windows][]



Initializing
-----------------------------------
To get started:

 - Clone this repo (don't forget to change the origin to your own repo!)
 - Run `./install_deps` (this will pip install requirements, and download the App Engine SDK)
 - `python manage.py runserver`


To test it visit `http://localhost:8080/` in your browser.


Customizing
------------------------------------

To customize the your resume, you can either create a new template or you can edit the values in `gae_resume/views.py` for default template provided:

```
context = {
  'title': 'GAE - Resume',
  'count': models.get_kudos(),
  'author': 'Yash Raj Singh',
  'why': '',
  'who': '',
  'primary_color_hex': '#FFF',
  'company': '',
  'company_url': 'http://yashrajsingh.net/',
  'work_desc': '',
}
```


Deploying on Google App Engine
------------------------------

Create a Google App Engine project. Edit `app.yaml` and change `application: gae-resume` to `application: your-app-id`. Then, if you're in the `gae-resume` directory, run:

    $ appcfg.py update ./

If you have two-factor authentication enabled in your Google account, run:

    $ appcfg.py --oauth2 update ./


Tech Stack & Credits
----------

  - [Google App Engine][], [NDB][]
  - [Django][], [AngularJS][],
  - [Bootstrap][], [jQuery][], 
  - [angular-kudos][], [ngStorage][], 
  - [Python 2.7][], [pip][], [virtualenv][]

Help & Support
----------
  - [Author][]

[bootstrap]: http://getbootstrap.com/
[google app engine sdk for python]: https://developers.google.com/appengine/downloads
[google app engine]: https://developers.google.com/appengine/
[jquery]: https://jquery.com/
[linux]: http://www.ubuntu.com
[ndb]: https://developers.google.com/appengine/docs/python/ndb/
[os x]: http://www.apple.com/osx/
[pip]: http://www.pip-installer.org/
[python 2.7]: https://developers.google.com/appengine/docs/python/python27/using27
[virtualenv]: http://www.virtualenv.org/
[windows]: http://windows.microsoft.com/
[perl]: https://www.perl.org/
[Django]: https://www.djangoproject.com/
[Djangae]: https://github.com/potatolondon/djangae
[AngularJS]: https://angularjs.org/
[angular-kudos]: https://github.com/oojr/inspiration
[ngStorage]: https://github.com/gsklee/ngStorage
[Author]: http://yashrajsingh.net/
