from django.db import models


class History(models.Model):
    """
    Keeps track of the issues that have been already reported
    """
    checksum = models.CharField(max_length=20, db_index=True)  # Length of a SHA-1 hex hash
    date = models.DateTimeField(auto_now_add=True)