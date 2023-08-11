# The website by design presentations 
[![Workflow](https://github.com/EvgVol/website-by-designer/actions/workflows/main.yml/badge.svg?branch=main)](https://github.com/EvgVol/website-by-designer/actions/workflows/main.yml) [![Python Version](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/downloads/release/python-3110/) [![Django Version](https://img.shields.io/badge/django-v4.2-green)](https://docs.djangoproject.com/en/4.2/) [![Nginx](https://img.shields.io/badge/-NGINX-464646?style=flat-square&logo=NGINX)](https://nginx.org/ru/) [![Docker](https://img.shields.io/badge/-Docker-464646?style=flat-square&logo=docker)](https://www.docker.com/) [![Yandex.Cloud](https://img.shields.io/badge/-Yandex.Cloud-464646?style=flat-square&logo=Yandex.Cloud)](https://cloud.yandex.ru/) [![Certbot](https://img.shields.io/badge/-Certbot-003A6E?style=flat&logo=letsencrypt&logoColor=white)](https://certbot.eff.org/) [![PostgreSQL](https://img.shields.io/badge/PostgreSQL-13.0-336791?logo=postgresql&logoColor=white)](https://www.postgresql.org/)  [![Bootstrap Version](https://img.shields.io/badge/bootstrap-v4.3-orange)](https://getbootstrap.com/docs/4.3/getting-started/introduction/) [![HTML](https://img.shields.io/badge/HTML-v5-red)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) [![CSS](https://img.shields.io/badge/CSS-v3-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)



## Description

This is a website for a designer that specializes in creating presentations. The website showcases the designer's portfolio, skills, and services. Visitors can view the designer's previous work and can contact them for potential collaborations.

## Features

Portfolio showcasing previous work
About the designer section
Advantages
Contact form for potential collaborations

## Technologies Used
* Django
* Docker
* Nginx
* Yandex.Cloud
* Bootstrap framework
* HTML
* CSS

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository using:
```bash
git clone https://github.com/evgvol/website-by-designer.git
```
2. Create a .env file in the root directory of the project.

3. Add the following environment variables to the .env file:
```bash
SECRET_KEY='django-insecure-+%_0#njq$hkob)bx)les6ta6vh!@9=d5%mz3j#rvfcj%2)k4-u'
DEBUG=False
ALLOWED_HOSTS=127.0.0.1, localhost
EMAIL_HOST_USER='your-email@yandex.ru'
EMAIL_HOST_PASSWORD='your-password'
EMAIL_ADMIN='your-email@yandex.ru'
TELEGRAM_TOKEN='your-telegram-token'
TELEGRAM_CHAT_ID='your-telegram-id'
```

4. Navigate to the project directory using:
```bash
cd website-by-designer/website
```

5. Install the dependencies using the following command: 
```bash
pip install -r requirements.txt
```

6. Start the Django development server using the following command:
```bash
python manage.py runserver
```

7. Open your web browser and navigate to http://localhost:8000 to view the application.
[![example](https://raw.githubusercontent.com/EvgVol/website-by-designer/main/example.gif)]()

We will perform all actions in Docker, docker-compose both on the local machine and on VM server.
We will pre-install the necessary components for work on the VM in the cloud:

*0. Add the following environment variables to Github Actions:
```bash
SECRET_KEY='django-insecure-+%_0#njq$hkob)bx)les6ta6vh!@9=d5%mz3j#rvfcj%2)k4-u'
DEBUG=False
ALLOWED_HOSTS=127.0.0.1, localhost
EMAIL_HOST_USER='your-email@yandex.ru'
EMAIL_HOST_PASSWORD='your-password'
EMAIL_ADMIN='your-email@yandex.ru'
HOST=011.222.333.444
USER='your-username'
PASSWORD='your-password'
SSH_KEY='your-keys'
DOCKER_USERNAME='login-by-dockerhub'
DOCKER_PASSWORD='password-by-dockerhub'
TELEGRAM_TOKEN='your-telegram-token'
TELEGRAM_CHAT_ID='your-telegram-id'
```

*1. Connect to your server*

```bash
ssh admin@011.222.333.444
# admin: the name of the user under which the connection to the server will be made
# 011.222.333.444: Server IP address
```

*2. First update the existing package list:*

```bash
sudo apt update
```

*3. Now update the packages installed in the system and install security updates: the system was installed on your server from the internal repository of Yandex.Cloud, and it is unknown when it was updated. Trust, but update:*

```bash
sudo apt upgrade -y
```

*3. Install Docker on your server:*

```bash
sudo apt install docker.io
```

*4. The following command downloads version 1.26.0 and saves the executable file in the /usr/local/bin/docker-compose directory, as a result of which this software will be globally available under the name docker-compose:*

```bash
sudo curl -L "https://github.com/docker/compose/releases/download/1.26.0/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose
```

*5. Then you need to set the correct permissions to make the docker-compose command executable:*
```bash
sudo chmod +x /usr/local/bin/docker-compose
```

*6. To check the success of the installation, run the following command:*

```bash
docker-compose --version
# The output will look like this:
#docker-compose version 1.26.0, build 8a1c60f6
```

*6. Copy the docker-compose files.yaml and nginx/default.conf from your project to the server in home/<your_isegame>/docker-compose.yaml and home/<your_isegame>/nginx/default.conf, respectively.:*

```bash
#These files need to be copied from the infra directory of the local
scp docker-compose machine.yml nginx.conf admin@011.222.333.444:/home/admin/
```

## Launch

The git push command is the project workflow trigger. When executing the git push command, a set of jobs command blocks will be launched (see the file [Workflow](https://github.com/evgvol/websity-by-designer/actions/workflows/main.yml)). The following blocks will be executed sequentially:

**build_and_push_to_docker_hub** - upon successful completion of the tests, an image is collected for the docker container and sent to DockerHub

**deploy** - after sending the image to DockerHub, the deployment of the project on the server begins.

After completing the above procedures, you need to establish a connection to the server:

```bash
ssh admin@011.222.333.444
```

Execute the commands one by one:

```bash
sudo docker-compose exec web python manage.py migrate
sudo docker-compose exec web python manage.py createsuperuser
sudo docker-compose exec web python manage.py collectstatic --no-input
```

The project is now available at http://011.222.333.444/.

## The Chicken or the Egg?

Download the script to your working directory as init-letsencrypt.sh:

```bash
cd infra/
curl -L https://raw.githubusercontent.com/wmnnd/nginx-certbot/master/init-letsencrypt.sh > init-letsencrypt.sh
```
Edit the script to add in your domain(s) and your email address. If you’ve changed the directories of the shared Docker volumes, make sure you also adjust the data_path variable as well.

Then run:
```bash
chmod +x init-letsencrypt.sh
``` 
and

```bash
sudo ./init-letsencrypt.sh
```

Everything is in place now. The initial certificates have been obtained and our containers are ready to launch. Simply run docker-compose up and enjoy your HTTPS-secured website or app.

The project is now available at https://011.222.333.444/.

## Credits
This project was created by [Evgeniy Volochek](https://github.com/EvgVol). The Bootstrap framework was used to assist with the layout and styling of the website.

## License
This project is licensed under the MIT License. See the LICENSE.md file for details.