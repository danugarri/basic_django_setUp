# Run dev server
`Python manage.py runserver`

# Create a superUser to login
- Execute this command at the project root
`$ python manage.py createsuperuser`

# Deployment

<!-- ### Deployment notes ###

This Django app is deployed on Railway
To be deployed is absolutelly necessary to have a Virtual environment for each app
 -->

* In order to avoid deployment problems a nixpacks.toml file has been added to the root directory
    with the following content:
    `providers = ["python"]`
<!-- This way we are telling Railway which interpreter to use, instead of node.js -->

* A Procfile has been added to tell Railway which commands must me executed for deployment
    with the following content:
        `web: python manage.py collectstatic --no-input && gunicorn firstProject.wsgi`

* Other essentials config for production are:
    * * At settings.py:

   
    # App config
   INSTALLED_APPS = [
    "django.contrib.staticfiles",
    "whitenoise.runserver_nostatic",
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "firstProject",  # The app name is necessary to be added
    ]

    MIDDLEWARE = [
        "django.middleware.security.SecurityMiddleware",
        "django.contrib.sessions.middleware.SessionMiddleware",
        "django.middleware.common.CommonMiddleware",
        "django.middleware.csrf.CsrfViewMiddleware",
        "django.contrib.auth.middleware.AuthenticationMiddleware",
        "django.contrib.messages.middleware.MessageMiddleware",
        "django.middleware.clickjacking.XFrameOptionsMiddleware",
        # Add the following line to set the proper MIME type for CSS files.
        "django.middleware.common.BrokenLinkEmailsMiddleware",
        "whitenoise.middleware.WhiteNoiseMiddleware",
    ]
    # Required for production
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
    SECURE_SSL_REDIRECT = False
    # To Load static files in production
    STATIC_URL = "/static/"
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, "static"),
    ]
    # Set the STATIC_ROOT to a path accessible by the web server
    STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
    STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"
    
    ## FUNDAMENTAL ##
    - pip install the following dependencies on our Virtual environment:
    ` django gunicorn whitenoise`