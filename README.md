# A online examination system based on Django
## Environment Configuration
1.Go to the code directory, build and active virtual environment.
```
virtualenv venv --no-site-packages
venv\Scripts\activate
```
2.Install the requirement python package under the source code root directory.
```
pip install -r requirements.txt
```
3. Build your database <br>
4. Modify MySQL/Redis config file, create the local_setting.py under the config file under the project root.<br>

5. Modify local_settings.py as follow:<br>
```
# -*- coding: utf-8 -*-

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'examination',
        'USER': 'root',
        'PASSWORD': 'Your password of database'
    }
}


# Redis configuration
REDIS = {
    'default': {
        'HOST': '127.0.0.1',
        'PORT': 6379,
        'USER': '',
        'PASSWORD': '',
        'db': 0,
    }
}
```
6. Create log file directory called tmp under your project's drive.
7. Execute the database migrate under your project root directory.
```
python manage.py migrate
```
8. Run your project:
```
python manage.py runserver 0.0.0.0:8000
```
9. Input  http://127.0.0.1:8000 to show your web.

## More content
For the email verification function, you should modify the information in settings.py under config file.
```
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_USE_TLS = True
EMAIL_HOST = 'Your email's smtp number'             # Your can find this in your email's setting                     
EMAIL_PORT = 25                                     # This depends on the protocol(SSL or NON-SSL) you used
EMAIL_HOST_USER = 'Your email address'
EMAIL_HOST_PASSWORD = 'Your verify code'            #You can find this in your email setting
```
