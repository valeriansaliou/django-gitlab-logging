import logging


class GitlabIssuesHandler(logging.Handler):
    """
    Handles logs as issues with GitLab API
    """

    def __init__(self):
        logging.Handler.__init__(self)


    def __open_issue(self, title, content):
        """
        Open an issue on GitLab with given content
        """
        task_log_gitlab_report.delay(title, content)


    def emit(self, record):
        """
        Fired when an error is emitted
        """
        from django.conf import settings
        from _commons.tasks import task_log_gitlab_report

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
            environment=settings.ENVIRONMENT,
        )

        # Generate issue content
        contents = {
            'head': '#### :zap: Note: this issue has been automatically opened.',
            'trace': '```python\n%s\n```' % self.format(record),
            'repr': '```\n%s\n```' % request_repr if has_repr\
                                                      else ('*%s*' % request_repr),
        }
        content = '{head}\n\n---\n\n{trace}\n\n---\n\n{repr}'.format(
            head=contents['head'],
            trace=contents['trace'],
            repr=contents['repr'],
        )

        self.__open_issue(title, content)
