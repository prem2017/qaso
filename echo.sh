echo "Web server running @ http://127.0.0.1:8000/"


version: '3'
services:
  web:
    build: .
    command: python manage.py runserver 0.0.0.0:8000
    volumes:
      - .:/qaso
    ports:
      - "8000:8000"


      Hub: 415f41507569


      created: 752da093d617