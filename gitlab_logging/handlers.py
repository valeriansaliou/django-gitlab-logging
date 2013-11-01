import logging


class GitlabIssuesHandler(logging.Handler):
    """
    Handles logs as issues with GitLab API
    """

    def __init__(self):
        logging.Handler.__init__(self)


    def __open_issue(self, title, content, trace_raw):
        """
        Open an issue on GitLab with given content
        """
        from tasks import task_log_gitlab_issue_open

        task_log_gitlab_issue_open.delay(title, content, trace_raw)


    def __reopen_issue(self, issue_id):
        """
        Re-open a given issue on GitLab
        """
        from tasks import task_log_gitlab_issue_reopen

        task_log_gitlab_issue_reopen.delay(issue_id)


    def emit(self, record):
        """
        Fired when an error is emitted
        """
        from django.conf import settings
        from django.views.debug import get_exception_reporter_filter
        from helpers import GitlabIssuesHelper

        try:
            has_repr, request_repr = True, '\n{0}'.format(
                get_exception_reporter_filter(record.request).get_request_repr(record.request)
            )
        except Exception:
            has_repr, request_repr = False, ':warning: Request data unavailable.'

        # Generate issue title
        title = '[{level}@{environment}] {message}'.format(
            level=record.levelname,
            message=record.getMessage(),
            environment=getattr(settings, 'ENVIRONMENT', 'default'),
        )

        # Generate issue content
        trace_raw = self.format(record)
        contents = {
            'head': '#### :zap: Note: this issue has been automatically opened.',
            'trace': '```python\n%s\n```' % trace_raw,
            'repr': '```\n%s\n```' % request_repr if has_repr\
                                                      else ('*%s*' % request_repr),
        }

        issue_exists, issue_id = GitlabIssuesHelper.check_issue(settings.GITLAB_PROJECT_ID, trace_raw)

        if not issue_exists:
            content = '{head}\n\n---\n\n{trace}\n\n---\n\n{repr}'.format(
                head=contents['head'],
                trace=contents['trace'],
                repr=contents['repr'],
            )

            self.__open_issue(title, content, trace_raw)
        elif issue_id:
            self.__reopen_issue(issue_id)
