import hashlib, api
from django.conf import settings


class GitlabIssuesHelper(object):
    """
    Handlers on GitLab issues operations
    """

    @staticmethod
    def store_issue(trace, iid):
        """
        Store new issue in database (avoids from opening it multiple times on GitLab-side)
        """
        from models import History

        checksum = hashlib.sha1(trace).hexdigest()

        history = History(
            checksum=checksum,
            iid=iid,
        ).save()


    @staticmethod
    def check_issue(trace):
        """
        Check whether the issue is new (not in GitLab database) or not
        """
        from models import History

        exists, iid = False, None
        checksum = hashlib.sha1(trace).hexdigest()

        try:
            history = History.objects.get(checksum=checksum)
            exists, iid = True, history.iid
        except History.DoesNotExist:
            pass

        return exists, iid


    @staticmethod
    def gitlab():
        """
        Return a connector object to the configured GitLab instance
        """
        return api.Gitlab(settings.GITLAB_HOST, settings.GITLAB_USER, token=settings.GITLAB_TOKEN)
