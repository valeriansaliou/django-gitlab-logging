import json

from celery import task
from django.conf import settings

from helpers import GitlabIssuesHelper


@task
def task_log_gitlab_issue_open(issue_title, issue_content, trace_raw):
    """
    Proceed the issue opening task
    """
    gitlab = GitlabIssuesHelper.gitlab()

    print "Opening issue: %s..." % issue_title

    # Create issue
    success, response = gitlab.createissue(
        settings.GITLAB_PROJECT_ID,
        issue_title,

        description=issue_content,
        assignee_id=getattr(settings, 'GITLAB_PROJECT_ASSIGNEE_ID', ''),
        labels='backend, error, bug',
    )

    if success and response:
        response = json.loads(response)
        iid = response.get('iid', None)

        if iid is not None:
            print "Issue opened: %s [IID: %s]" % (issue_title, iid)

            GitlabIssuesHelper.store_issue(trace_raw, response['iid'])
    else:
        print "Issue could not be opened: %s" % issue_title


@task
def task_log_gitlab_issue_reopen(issue_id):
    """
    Proceed the issue re-opening task
    """
    print "Re-opening issue [IID: %s]" % issue_id

    success, _ = GitlabIssuesHelper.gitlab().editissue(
        settings.GITLAB_PROJECT_ID,
        issue_id,

        state_event='reopen',
    )

    if success:
        print "Issue re-opened [IID: %s]" % issue_id
    else:
        print "Issue could not be re-opened [IID: %s]" % issue_id
