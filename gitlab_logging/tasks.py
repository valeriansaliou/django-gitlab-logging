from celery import task
from django.conf import settings

from helpers import GitlabIssuesHelper


@task
def task_log_gitlab_issue_open(issue_title, issue_content, trace_raw):
    """
    Proceed the issue opening task
    """
    gitlab = GitlabIssuesHelper.gitlab()

    print("Opening issue: %s..." % issue_title)

    # Create issue
    success, response = gitlab.createissue(
        settings.GITLAB_PROJECT_ID,
        issue_title,

        description=issue_content,
        assignee_id=getattr(settings, 'GITLAB_ASSIGNEE_ID', ''),
        labels='backend, error, bug',
    )

    if success:
        issue_id = response.get('id', None)

        if issue_id is not None:
            print("Issue opened: %s [ID: %s]" % (issue_title, issue_id))

            GitlabIssuesHelper.store_issue(trace_raw, settings.GITLAB_PROJECT_ID, response['id'])
    else:
        print("Issue could not be opened: %s" % issue_title)


@task
def task_log_gitlab_issue_reopen(issue_id):
    """
    Proceed the issue re-opening task
    """
    print("Re-opening issue [ID: %s]" % issue_id)

    success, _ = GitlabIssuesHelper.gitlab().editissue(
        settings.GITLAB_PROJECT_ID,
        issue_id,

        state_event='reopen',
    )

    if success:
        print("Issue re-opened [ID: %s]" % issue_id)
    else:
        print("Issue could not be re-opened [ID: %s]" % issue_id)
        
