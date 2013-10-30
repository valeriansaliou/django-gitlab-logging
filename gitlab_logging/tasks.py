import gitlab

from celery import task
from django.conf import settings


@task
def task_log_gitlab_report(issue_title, issue_content):
    """
    Proceed the issue opening task
    """
    git = gitlab.Gitlab(settings.GITLAB_HOST, settings.GITLAB_USER, token=settings.GITLAB_TOKEN)

    git.createissue(
        settings.GITLAB_PROJECT_ID,
        issue_title,

        description=issue_content,
        assignee_id=getattr(settings, 'GITLAB_PROJECT_ASSIGNEE_ID', ''),
        labels='backend, error, bug',
    )