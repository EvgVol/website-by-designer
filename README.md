# The website by design presentations [![Python Version](https://img.shields.io/badge/python-v3.11-blue)](https://www.python.org/downloads/release/python-3110/) [![Django Version](https://img.shields.io/badge/django-v4.2-green)](https://docs.djangoproject.com/en/4.2/) [![Bootstrap Version](https://img.shields.io/badge/bootstrap-v4.3-orange)](https://getbootstrap.com/docs/4.3/getting-started/introduction/) [![HTML](https://img.shields.io/badge/HTML-v5-red)](https://developer.mozilla.org/en-US/docs/Web/Guide/HTML/HTML5) [![CSS](https://img.shields.io/badge/CSS-v3-blue)](https://developer.mozilla.org/en-US/docs/Web/CSS)
Website of the designer for creating presentations


## Description

This is a website for a designer that specializes in creating presentations. The website showcases the designer's portfolio, skills, and services. Visitors can view the designer's previous work and can contact them for potential collaborations.

## Features

Portfolio showcasing previous work
About the designer section
Advantages
Contact form for potential collaborations

## Technologies Used
* Django
* Bootstrap framework
* HTML
* CSS

## Installation
To install and run the project locally, follow these steps:

1. Clone the repository using:
```
git clone https://github.com/evgvol/website-by-designer.git
```
2. Create a .env file in the root directory of the project.

3. Add the following environment variables to the .env file:
```
SECRET_KEY='django-insecure-+%_0#njq$hkob)bx)les6ta6vh!@9=d5%mz3j#rvfcj%2)k4-u'
DEBUG=False
ALLOWED_HOSTS=127.0.0.1, localhost
EMAIL_HOST_USER='your-email@yandex.ru'
EMAIL_HOST_PASSWORD='your-password'
EMAIL_ADMIN='your-email@yandex.ru'
```

4. Navigate to the project directory using:
```
cd website-by-designer/website
```

5. Install the dependencies using the following command: 
```
pip install -r requirements.txt
```

6. Start the Django development server using the following command:
```
python manage.py runserver
```

7. Open your web browser and navigate to http://localhost:8000 to view the application.
[![example](https://raw.githubusercontent.com/EvgVol/website-by-designer/main/example.gif)]()

## Credits
This project was created by [Evgeniy Volochek](https://github.com/EvgVol). The Bootstrap framework was used to assist with the layout and styling of the website.

## License
This project is licensed under the MIT License. See the LICENSE.md file for details.