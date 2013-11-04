import hashlib, api
from django.conf import settings


class GitlabIssuesHelper(object):
    """
    Handlers on GitLab issues operations
    """

    @staticmethod
    def __trace_checksum(trace):
        """
        Process the trace checksum
        """
        return hashlib.sha1(trace).hexdigest()


    @classmethod
    def store_issue(_class, trace, project_id, issue_id):
        """
        Store new issue in database (avoids from opening it multiple times on GitLab-side)
        """
        from models import History

        history, created = History.objects.get_or_create(
            checksum=_class.__trace_checksum(trace),
            defaults={
                'project_id': project_id,
                'issue_id': issue_id,
            },
        )

        # Ensure data consistency (in case project ID changes)
        if not created:
            history.project_id = project_id
            history.issue_id = issue_id
            history.save()


    @classmethod
    def check_issue(_class, project_id, trace):
        """
        Check whether the issue is new (not in GitLab database) or not
        """
        from models import History

        exists, issue_id = False, None
        checksum = _class.__trace_checksum(trace)

        try:
            history = History.objects.get(project_id=project_id, checksum=checksum)
            exists, issue_id = True, history.issue_id
        except History.DoesNotExist:
            pass

        return exists, issue_id


    @staticmethod
    def gitlab():
        """
        Return a connector object to the configured GitLab instance
        """
        return api.Gitlab(settings.GITLAB_HOST, settings.GITLAB_USER, token=settings.GITLAB_TOKEN)
