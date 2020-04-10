# QASO: Question Answer From StackOverflow
![Language](https://img.shields.io/badge/language-Python-blue.svg) [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

Question answering system for programming related issues mainly (for now only) extracted from StackOverflow (SO). This application is mainly to better understand the working of docker but not limited.



## Setting up with `Docker`

 * Pull the project and change the working directory to the project i.e. directory of this README.md file.

 * Install Docker (how to work with docker please read [here](https://comingup.soon)).

 * Pull the publicly available image from [docker-hub](https://hub.docker.com/) with `docker pull voyager2020/qaso_web:latest` (no need of account to pull the image) **OR** 
 	* execute `docker-compose up` to first build the image from the Dockerfile(s) and launch the server.

 * Open `127.0.0.1:8000` or `localhost:8000` to use the application. 



## Setting up with `requirements.txt`

 * Pull the project and change the working directory to it i.e. directory of this README.md file.

 * Create a new environment using `conda create --name <env-name>` and activate with `source activate <the-new-env-name>`.

 * Run `pip install -r requirements.txt` from the terminal to install all the dependencies.

 * Finally to start the server with `python manage.py runserver` or `python -m manage runserver`

 * Open `127.0.0.1:8000` or `localhost:8000` to use the application 



## Using the application 

 * To use application and open the page `127.0.0.1:8000` or `localhost:8000` in your favourite browser.

 * This page presents text-area where one can write a question for an answer.

 * Once requested for an answer- the page loads two sections
   * The complete question and answers- accepted and most-voted, scrapped from SO page and suggested answer(s) for the question. 
      


## Further Improvements

  * Use docker to launch multiple microservices for better learning, and maybe also experiment with [Kubernetes](https://containerjournal.com/topics/container-ecosystems/kubernetes-vs-docker-a-primer/). 

  * Extend beyond SO page for searches such as Reddit, Quora, etc.

  * Use natural language processing to parse the question and make this application a single page application for getting most relevant solution rather than navigating multiple sites.  




