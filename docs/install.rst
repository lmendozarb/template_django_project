Installation
=============

Download the source code
------------------------

Download the main repo:

- git clone https://gitlab.com/lmendozamb/ecommerce-web.git

Run
---

Execute the next command to start web and database service::

    docker-compose up --build


Connect to Docker Container::

    docker-compose exec web bash

Run Management Command::

    docker-compose run web python3 ./manage.py <command>


Stop
----

In the project root, execute the next command::

    docker-compose down
