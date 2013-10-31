django-gitlab-logging
=====================

## Configuration

# GitLab options
GITLAB_HOST = 'https://gitlab.server.tld'  # Beware: no trailing slash there!
GITLAB_USER = 'gitlab.user'
GITLAB_TOKEN = 'USER_GITLAB_TOKEN'
GITLAB_PROJECT_ID = 114                    # Grep the project ID from the DB
GITLAB_ASSIGNEE_ID = 2                     # Grep the assignee ID from the DB (optional, you can leave drop this parameter)