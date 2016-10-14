# Django

In **MVC** we need to separate **Model** from **Controller** and
**View** to make it reusable.

A single **News Article** can be **Model** itself. It can have methods:
`.publish()`, `.render()`, `.show_comments()` and so on. Thus **Model**
can be very flexible: we can show news in HTML, XML, RSS or just in
plain text.

#### MVC Components

* **Router** - chooses a particular **Controller** based on URI
* **Model** - all App's business logic
* **Controller** - works w/ HTTP (gets all headers, cookies & data from
  user), connects to DB (using Model), renders reply w/ **View**
* **View** - generates HTML or another view

#### Django Project Files

|     File      | Description                                       |
|:-------------:|:--------------------------------------------------|
|  `manage.py`  | Auto generated file that manages our project      |
| `settings.py` | All settings                                      |
|   `urls.py`   | Router                                            |
|   `wsgi.py`   | Entry point (called by gunicorn for each request) |

#### Django Commands

| Command                                 | Action                |
|:----------------------------------------|:----------------------|
| `django-admin.py startproject app_name` | Create new project    |
| `./manage.py startapp app_name`         | Create new Django App |

#### Django Settings

`url(r'^admin/', admin.site.urls)` - we always omit 1st / in RegExp.

`Django Apps` - Way to distribute code in Django All logic like **news**, **comments**, **texts** or 

