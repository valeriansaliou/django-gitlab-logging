Django GitLab Logging
=====================

Django GitLab Logging is a custom log handler that has been written with the purpose of auto-opening (and assigning) issues on GitLab everytime something goes south with backend code.

Useful for production deployments, where you want to move the flood of 500 errors you get in your mailbox to your GitLab issue tracker.

Django GitLab Logging is smart enough to recognize similar errors, thus not opening blindly a new issue everytime. It is also capable of re-opening closed issues that are encountered again.

## Configuration

* Add `gitlab_logging` to your INSTALLED_APPS.

* Drop **those lines of configuration in your settings.py**, taking care of filling everything:

```python
# GitLab options
GITLAB_HOST = 'https://gitlab.server.tld'  # Beware: no trailing slash there!
GITLAB_USER = 'gitlab.user'
GITLAB_TOKEN = 'USER_GITLAB_TOKEN'         # Get this from GitLab user account information
GITLAB_PROJECT_ID = 114                    # Get the project ID from the DB
GITLAB_ASSIGNEE_ID = 2                     # Get the assignee ID from the DB (optional, you can drop this parameter)
```

* Then, **ensure you have Celery installed with Django**. Django GitLab Logging cannot work without a tasker (here, Celery), since GitLab API calls needs to be done asynchronously to avoid blocking your Web workers in case of network delays or GitLab remote server downtimes.

* **Proceed either** a `syncdb` or a `migrate` (depending on if you're using South or not)

* **Map the custom GitLab Logging handler**:

```python
'handlers': {
    # (....)

    'gitlab_issues': {
        'level': 'ERROR',
        'class': 'gitlab_logging.handlers.GitlabIssuesHandler',
    },
},
```

* **Activate your GitLab logging handler** where you need it:

```python
LOGGING['loggers'] = {
    'django.request': {
        'handlers': ['all_console', 'django_file', 'gitlab_issues'],
        'level': 'DEBUG',
        'propagate': True,
    },

    # (....)
}
```

* You're done! :v:

## Notes

* This module is kept up-to-date with latest GitLab API changes. Thus, ensure you're running the latest GitLab version in time when using Django GitLab Logging!

* Django GitLab Logging has been built by the happy folks at [Waaave Network](https://waaave.com/), for their website needs.

* You may want to read the following tutorial about Django GitLab Logging: [Automatically open GitLab issues for Django errors](https://waaave.com/tutorial/django/automatically-open-gitlab-issues-for-django-errors/)