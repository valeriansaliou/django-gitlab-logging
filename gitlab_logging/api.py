# -*- coding: utf-8 -*-
"""
pyapi-gitlab, a gitlab python wrapper for the gitlab API
by Itxaka Serrano Garcia <itxakaserrano@gmail.com>

Modified by Valérian Saliou <valerian@valeriansaliou.name> for django-gitlab-logging requirements
"""

import requests
import json


class Gitlab(object):
    """
    Gitlab class
    """
    def __init__(self, host, user, token=""):
        """
        on init we setup the token used for all the api calls and all the urls
        :param host: host of gitlab
        :param user: user
        :param token: token
        """
        if token != "":
            self.token = token
            self.headers = {"PRIVATE-TOKEN": self.token}
        if host[-1] == '/':
            self.host = host[:-1]
        else:
            self.host = host
        self.projects_url = self.host + "/api/v3/projects"
        self.users_url = self.host + "/api/v3/users"
        self.keys_url = self.host + "/api/v3/user/keys"
        self.groups_url = self.host + "/api/v3/groups"
        self.user = user

    def createissue(self, id_, title, description="", assignee_id="",
                    milestone_id="", labels="", sudo=""):
        """
        create a new issue
        :param id_: project id
        :param title: title of the issue
        :param description: description
        :param assignee_id: assignee for the issue
        :param milestone_id: milestone
        :param labels: label
        :param sudo: do the request as another user
        :return: true if success
        """
        data = {"id": id_, "title": title, "description": description,
                "assignee_id": assignee_id,
                "milestone_id": milestone_id, "labels": labels}
        if sudo != "":
            data['sudo'] = sudo
        request = requests.post(self.projects_url + "/" + str(id_) + "/issues",
                                headers=self.headers, data=data)
        response = json.loads(request.text)
        if request.status_code == 201:
            return True, response
        else:
            
            return False, response

    def editissue(self, id_, issue_id, title="", description="",
                  assignee_id="", milestone_id="", labels="",
                  state_event="", sudo=""):
        """
        edit an existing issue data
        :param id_: project id
        :param issue_id: issue id
        :param title: title
        :param description: description
        :param assignee_id: asignee
        :param milestone_id: milestone
        :param labels: label
        :param state_event: state
        :param sudo: do the request as another user
        :return: true if success
        """
        data = {"id": id_, "issue_id": issue_id, "title": title,
                "description": description, "assignee_id": assignee_id,
                "milestone_id": milestone_id, "labels": labels,
                "state_event": state_event}
        if sudo != "":
            data['sudo'] = sudo
        request = requests.put(self.projects_url + "/" + str(id_) + "/issues/" +
                               str(issue_id), headers=self.headers,
                               data=data)
        response = json.loads(request.text)
        if request.status_code == 201:
            return True, response
        else:
            
            return False, response
