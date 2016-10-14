# Django

In **MVC** we need to separate **Model** from **Controller** and **View** to make it reusable.

A single **News Article** can be **Model** itself. It can have methods: `.publish()`, `.render()`, `.show_comments()` and so on. Thus **Model** can be very flexible: we can show news in HTML, XML, RSS or just in plain text.

#### MVC Components

* **Router** - chooses a particular **Controller** based on URI
* **Model** - app's business logic
* **Controller** - works w/ HTTP (gets all headers, cookies & data from user), connects to DB (using Model), renders reply w/ **View**
* **View** - generates HTML or another view


