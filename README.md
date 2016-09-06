Video Recipes React-Native Application

Rest Framework
http://www.django-rest-framework.org/

# Video Recipes Mobile Application (in React Native)
Video browser for short (~1 minute) recipe videos on Facebook.

## Installation

### Requirements

* Homebrew
* Virtualenv - Packaged with Python if installed with `brew`

### Development

1. Clone repo `git clone git@...`
2. Make virtual environment in new directory and activate `cd videorecipes && virtualenv venv && . venv/bin/activate`
3. Install Python dependencies `pip install -r requirements.txt`.

   You may need to to `export CFLAGS=-Qunused-arguments && export CPPFLAGS=-Qunused-arguments`
   if there is a `clang` error


## Running

### Development

1. Start RabbitMQ service with `rabbitmq-server`
2. Start Redis server with `redis-server`
3. Start Celery workers with `./start_celery.sh`
4. Run server with `./run.sh`

#### Updating Code

Django will automatically reload after a code change, but Celery will not.
This means you need to stop the Celery worker and restart it when the code is
changed.
