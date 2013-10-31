from django.db import models


class History(models.Model):
    """
    Keeps track of the issues that have been already reported
    """
    checksum = models.CharField(max_length=40, db_index=True, unique=True)  # Length of a SHA-1 hex hash
    project_id = models.PositiveIntegerField(db_index=True)                 # GitLab project ID
    issue_id = models.PositiveIntegerField(db_index=True)                   # GitLab project issue ID
    date = models.DateTimeField(auto_now_add=True)
