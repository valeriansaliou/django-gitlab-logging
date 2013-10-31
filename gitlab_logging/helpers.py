import hashlib, api
from django.conf import settings


class GitlabIssuesHelper(object):
    """
    Handlers on GitLab issues operations
    """

    @staticmethod
    def store_issue(trace, project_id, issue_id):
        """
        Store new issue in database (avoids from opening it multiple times on GitLab-side)
        """
        from models import History

        checksum = hashlib.sha1(trace).hexdigest()

        history = History(
            checksum=checksum,
            project_id=project_id,
            issue_id=issue_id,
        ).save()


    @staticmethod
    def check_issue(project_id, trace):
        """
        Check whether the issue is new (not in GitLab database) or not
        """
        from models import History

        exists, issue_id = False, None
        checksum = hashlib.sha1(trace).hexdigest()

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
