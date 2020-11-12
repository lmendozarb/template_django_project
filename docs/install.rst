Installation
=============

Download the source code
------------------------

Download the main repo:

- git clone https://gitlab.com/lmendozamb/ecommerce-web.git

Run
---

Execute the next command to start web and database service::

    docker-compose -f local.yml build
    docker-compose -f local.yml up


Connect to Docker Container::

    docker-compose exec django bash

Run Management Command::

    docker-compose -f local.yml run --rm django python3 manage.py <command>


Stop
----

In the project root, execute the next command::

    docker-compose down

Pre commit
---
Execute the next commad the first time to install pre commit::
    pre-commit install

Later , the next comment::

    pre-commit run --all-files