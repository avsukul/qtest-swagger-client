# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class SchedulePermission(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, create=False, edit=False, delete=False, view=False):
        """
        SchedulePermission - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'create': 'bool',
            'edit': 'bool',
            'delete': 'bool',
            'view': 'bool'
        }

        self.attribute_map = {
            'create': 'create',
            'edit': 'edit',
            'delete': 'delete',
            'view': 'view'
        }

        self._create = create
        self._edit = edit
        self._delete = delete
        self._view = view

    @property
    def create(self):
        """
        Gets the create of this SchedulePermission.
        Can create schedule

        :return: The create of this SchedulePermission.
        :rtype: bool
        """
        return self._create

    @create.setter
    def create(self, create):
        """
        Sets the create of this SchedulePermission.
        Can create schedule

        :param create: The create of this SchedulePermission.
        :type: bool
        """

        self._create = create

    @property
    def edit(self):
        """
        Gets the edit of this SchedulePermission.
        Can edit schedule

        :return: The edit of this SchedulePermission.
        :rtype: bool
        """
        return self._edit

    @edit.setter
    def edit(self, edit):
        """
        Sets the edit of this SchedulePermission.
        Can edit schedule

        :param edit: The edit of this SchedulePermission.
        :type: bool
        """

        self._edit = edit

    @property
    def delete(self):
        """
        Gets the delete of this SchedulePermission.
        Can delete schedule

        :return: The delete of this SchedulePermission.
        :rtype: bool
        """
        return self._delete

    @delete.setter
    def delete(self, delete):
        """
        Sets the delete of this SchedulePermission.
        Can delete schedule

        :param delete: The delete of this SchedulePermission.
        :type: bool
        """

        self._delete = delete

    @property
    def view(self):
        """
        Gets the view of this SchedulePermission.
        Can views= schedule

        :return: The view of this SchedulePermission.
        :rtype: bool
        """
        return self._view

    @view.setter
    def view(self, view):
        """
        Sets the view of this SchedulePermission.
        Can views= schedule

        :param view: The view of this SchedulePermission.
        :type: bool
        """

        self._view = view

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, SchedulePermission):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
