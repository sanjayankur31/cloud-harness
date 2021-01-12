# coding: utf-8

from __future__ import absolute_import
from datetime import date, datetime  # noqa: F401

from typing import List, Dict  # noqa: F401

from cloudharness_cli.samples.models.base_model_ import Model
from cloudharness_cli.samples.models.inline_response202_task import InlineResponse202Task
from cloudharness_cli.samples import util

from cloudharness_cli.samples.models.inline_response202_task import InlineResponse202Task  # noqa: E501

class InlineResponse202(Model):
    """NOTE: This class is auto generated by OpenAPI Generator (https://openapi-generator.tech).

    Do not edit the class manually.
    """

    def __init__(self, task=None):  # noqa: E501
        """InlineResponse202 - a model defined in OpenAPI

        :param task: The task of this InlineResponse202.  # noqa: E501
        :type task: InlineResponse202Task
        """
        self.openapi_types = {
            'task': InlineResponse202Task
        }

        self.attribute_map = {
            'task': 'task'
        }

        self._task = task

    @classmethod
    def from_dict(cls, dikt) -> 'InlineResponse202':
        """Returns the dict as a model

        :param dikt: A dict.
        :type: dict
        :return: The inline_response_202 of this InlineResponse202.  # noqa: E501
        :rtype: InlineResponse202
        """
        return util.deserialize_model(dikt, cls)

    @property
    def task(self):
        """Gets the task of this InlineResponse202.


        :return: The task of this InlineResponse202.
        :rtype: InlineResponse202Task
        """
        return self._task

    @task.setter
    def task(self, task):
        """Sets the task of this InlineResponse202.


        :param task: The task of this InlineResponse202.
        :type task: InlineResponse202Task
        """

        self._task = task
