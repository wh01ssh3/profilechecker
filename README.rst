Profilechecker
##############

To run this project you need to install docker-machine `Docker`_ from stable channel

.. _Docker: https://download.docker.com/win/stable/InstallDocker.msi

Also you need to install python3 and pip

Install docker-compose:
.. code-block::bash

    pip install docker-compose

Then


.. code-block::bash

    docker-compose build


After successful build you have to run


.. code-block::bash

    docker-compose up postgres

And wait while postgres DB will be initialized

Then run ``docker-compose up web`` and go to http://localhost:8000
