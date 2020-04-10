# Specify the base Image
FROM python:3-slim 

# Maintainer
LABEL maintainer="prem4708@gmail.com"

# Update
RUN apt-get update \
     && apt-get install -y \
        libgl1-mesa-glx \
        libx11-xcb1 \
     && apt-get clean all \
     && rm -r /var/lib/apt/lists/*


# Set working directory
WORKDIR /qaso


# First copy and install requirements so further cache can be used
COPY ./requirements.txt ./requirements.txt


# Install the project dependency listed in requirements.txt
RUN pip install --default-timeout=10000 -r requirements.txt


# Copy the current directory contents into the container at /<app_name>
COPY . /qaso/


# EXPOSE port 8000 to allow communication to/from server
# EXPOSE 8000 # if this was used run `docker run -it -p 8000:8000 qarc:latest python manage.py runserver`

# EXPOSE 8000
# CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

# Promp messge for successful run
CMD ["echo", "Web server running @ http://127.0.0.1:8000/"]

