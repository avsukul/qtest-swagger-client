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


class AutomationTestLogResource(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """
    def __init__(self, links=None, id=None, test_case_version_id=None, exe_start_date=None, exe_end_date=None, note=None, attachments=None, automation_content=None, name=None, test_case=None, defects=None, planned_exe_time=None, actual_exe_time=None, build_number=None, build_url=None, properties=None, system_name=None, status=None, order=None, test_step_logs=None, module_names=None):
        """
        AutomationTestLogResource - a model defined in Swagger

        :param dict swaggerTypes: The key is attribute name
                                  and the value is attribute type.
        :param dict attributeMap: The key is attribute name
                                  and the value is json key in definition.
        """
        self.swagger_types = {
            'links': 'list[Link]',
            'id': 'int',
            'test_case_version_id': 'int',
            'exe_start_date': 'datetime',
            'exe_end_date': 'datetime',
            'note': 'str',
            'attachments': 'list[AttachmentResource]',
            'automation_content': 'str',
            'name': 'str',
            'test_case': 'TestCaseWithCustomFieldResource',
            'defects': 'list[LinkedDefectResource]',
            'planned_exe_time': 'int',
            'actual_exe_time': 'int',
            'build_number': 'str',
            'build_url': 'str',
            'properties': 'list[PropertyResource]',
            'system_name': 'str',
            'status': 'str',
            'order': 'int',
            'test_step_logs': 'list[AutomationTestStepLog]',
            'module_names': 'list[str]'
        }

        self.attribute_map = {
            'links': 'links',
            'id': 'id',
            'test_case_version_id': 'test_case_version_id',
            'exe_start_date': 'exe_start_date',
            'exe_end_date': 'exe_end_date',
            'note': 'note',
            'attachments': 'attachments',
            'automation_content': 'automation_content',
            'name': 'name',
            'test_case': 'test_case',
            'defects': 'defects',
            'planned_exe_time': 'planned_exe_time',
            'actual_exe_time': 'actual_exe_time',
            'build_number': 'build_number',
            'build_url': 'build_url',
            'properties': 'properties',
            'system_name': 'system_name',
            'status': 'status',
            'order': 'order',
            'test_step_logs': 'test_step_logs',
            'module_names': 'module_names'
        }

        self._links = links
        self._id = id
        self._test_case_version_id = test_case_version_id
        self._exe_start_date = exe_start_date
        self._exe_end_date = exe_end_date
        self._note = note
        self._attachments = attachments
        self._automation_content = automation_content
        self._name = name
        self._test_case = test_case
        self._defects = defects
        self._planned_exe_time = planned_exe_time
        self._actual_exe_time = actual_exe_time
        self._build_number = build_number
        self._build_url = build_url
        self._properties = properties
        self._system_name = system_name
        self._status = status
        self._order = order
        self._test_step_logs = test_step_logs
        self._module_names = module_names

    @property
    def links(self):
        """
        Gets the links of this AutomationTestLogResource.

        :return: The links of this AutomationTestLogResource.
        :rtype: list[Link]
        """
        return self._links

    @links.setter
    def links(self, links):
        """
        Sets the links of this AutomationTestLogResource.

        :param links: The links of this AutomationTestLogResource.
        :type: list[Link]
        """

        self._links = links

    @property
    def id(self):
        """
        Gets the id of this AutomationTestLogResource.

        :return: The id of this AutomationTestLogResource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this AutomationTestLogResource.

        :param id: The id of this AutomationTestLogResource.
        :type: int
        """

        self._id = id

    @property
    def test_case_version_id(self):
        """
        Gets the test_case_version_id of this AutomationTestLogResource.
        ID of the Test Case Version

        :return: The test_case_version_id of this AutomationTestLogResource.
        :rtype: int
        """
        return self._test_case_version_id

    @test_case_version_id.setter
    def test_case_version_id(self, test_case_version_id):
        """
        Sets the test_case_version_id of this AutomationTestLogResource.
        ID of the Test Case Version

        :param test_case_version_id: The test_case_version_id of this AutomationTestLogResource.
        :type: int
        """

        self._test_case_version_id = test_case_version_id

    @property
    def exe_start_date(self):
        """
        Gets the exe_start_date of this AutomationTestLogResource.
        Execution start date

        :return: The exe_start_date of this AutomationTestLogResource.
        :rtype: datetime
        """
        return self._exe_start_date

    @exe_start_date.setter
    def exe_start_date(self, exe_start_date):
        """
        Sets the exe_start_date of this AutomationTestLogResource.
        Execution start date

        :param exe_start_date: The exe_start_date of this AutomationTestLogResource.
        :type: datetime
        """
        if exe_start_date is None:
            raise ValueError("Invalid value for `exe_start_date`, must not be `None`")

        self._exe_start_date = exe_start_date

    @property
    def exe_end_date(self):
        """
        Gets the exe_end_date of this AutomationTestLogResource.
        Execution end date

        :return: The exe_end_date of this AutomationTestLogResource.
        :rtype: datetime
        """
        return self._exe_end_date

    @exe_end_date.setter
    def exe_end_date(self, exe_end_date):
        """
        Sets the exe_end_date of this AutomationTestLogResource.
        Execution end date

        :param exe_end_date: The exe_end_date of this AutomationTestLogResource.
        :type: datetime
        """
        if exe_end_date is None:
            raise ValueError("Invalid value for `exe_end_date`, must not be `None`")

        self._exe_end_date = exe_end_date

    @property
    def note(self):
        """
        Gets the note of this AutomationTestLogResource.
        Note

        :return: The note of this AutomationTestLogResource.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """
        Sets the note of this AutomationTestLogResource.
        Note

        :param note: The note of this AutomationTestLogResource.
        :type: str
        """

        self._note = note

    @property
    def attachments(self):
        """
        Gets the attachments of this AutomationTestLogResource.
        Test Log attachments

        :return: The attachments of this AutomationTestLogResource.
        :rtype: list[AttachmentResource]
        """
        return self._attachments

    @attachments.setter
    def attachments(self, attachments):
        """
        Sets the attachments of this AutomationTestLogResource.
        Test Log attachments

        :param attachments: The attachments of this AutomationTestLogResource.
        :type: list[AttachmentResource]
        """

        self._attachments = attachments

    @property
    def automation_content(self):
        """
        Gets the automation_content of this AutomationTestLogResource.
        Test Case's automation content

        :return: The automation_content of this AutomationTestLogResource.
        :rtype: str
        """
        return self._automation_content

    @automation_content.setter
    def automation_content(self, automation_content):
        """
        Sets the automation_content of this AutomationTestLogResource.
        Test Case's automation content

        :param automation_content: The automation_content of this AutomationTestLogResource.
        :type: str
        """

        self._automation_content = automation_content

    @property
    def name(self):
        """
        Gets the name of this AutomationTestLogResource.
        Test Run's name

        :return: The name of this AutomationTestLogResource.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AutomationTestLogResource.
        Test Run's name

        :param name: The name of this AutomationTestLogResource.
        :type: str
        """

        self._name = name

    @property
    def test_case(self):
        """
        Gets the test_case of this AutomationTestLogResource.
        Test Case object

        :return: The test_case of this AutomationTestLogResource.
        :rtype: TestCaseWithCustomFieldResource
        """
        return self._test_case

    @test_case.setter
    def test_case(self, test_case):
        """
        Sets the test_case of this AutomationTestLogResource.
        Test Case object

        :param test_case: The test_case of this AutomationTestLogResource.
        :type: TestCaseWithCustomFieldResource
        """

        self._test_case = test_case

    @property
    def defects(self):
        """
        Gets the defects of this AutomationTestLogResource.
        Array of Defect

        :return: The defects of this AutomationTestLogResource.
        :rtype: list[LinkedDefectResource]
        """
        return self._defects

    @defects.setter
    def defects(self, defects):
        """
        Sets the defects of this AutomationTestLogResource.
        Array of Defect

        :param defects: The defects of this AutomationTestLogResource.
        :type: list[LinkedDefectResource]
        """

        self._defects = defects

    @property
    def planned_exe_time(self):
        """
        Gets the planned_exe_time of this AutomationTestLogResource.

        :return: The planned_exe_time of this AutomationTestLogResource.
        :rtype: int
        """
        return self._planned_exe_time

    @planned_exe_time.setter
    def planned_exe_time(self, planned_exe_time):
        """
        Sets the planned_exe_time of this AutomationTestLogResource.

        :param planned_exe_time: The planned_exe_time of this AutomationTestLogResource.
        :type: int
        """
        if planned_exe_time is not None and planned_exe_time > 9999999:
            raise ValueError("Invalid value for `planned_exe_time`, must be a value less than or equal to `9999999`")
        if planned_exe_time is not None and planned_exe_time < 0:
            raise ValueError("Invalid value for `planned_exe_time`, must be a value greater than or equal to `0`")

        self._planned_exe_time = planned_exe_time

    @property
    def actual_exe_time(self):
        """
        Gets the actual_exe_time of this AutomationTestLogResource.

        :return: The actual_exe_time of this AutomationTestLogResource.
        :rtype: int
        """
        return self._actual_exe_time

    @actual_exe_time.setter
    def actual_exe_time(self, actual_exe_time):
        """
        Sets the actual_exe_time of this AutomationTestLogResource.

        :param actual_exe_time: The actual_exe_time of this AutomationTestLogResource.
        :type: int
        """

        self._actual_exe_time = actual_exe_time

    @property
    def build_number(self):
        """
        Gets the build_number of this AutomationTestLogResource.
        Jenkins jobs build number

        :return: The build_number of this AutomationTestLogResource.
        :rtype: str
        """
        return self._build_number

    @build_number.setter
    def build_number(self, build_number):
        """
        Sets the build_number of this AutomationTestLogResource.
        Jenkins jobs build number

        :param build_number: The build_number of this AutomationTestLogResource.
        :type: str
        """

        self._build_number = build_number

    @property
    def build_url(self):
        """
        Gets the build_url of this AutomationTestLogResource.
        Jenkin jobs build URL

        :return: The build_url of this AutomationTestLogResource.
        :rtype: str
        """
        return self._build_url

    @build_url.setter
    def build_url(self, build_url):
        """
        Sets the build_url of this AutomationTestLogResource.
        Jenkin jobs build URL

        :param build_url: The build_url of this AutomationTestLogResource.
        :type: str
        """

        self._build_url = build_url

    @property
    def properties(self):
        """
        Gets the properties of this AutomationTestLogResource.

        :return: The properties of this AutomationTestLogResource.
        :rtype: list[PropertyResource]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """
        Sets the properties of this AutomationTestLogResource.

        :param properties: The properties of this AutomationTestLogResource.
        :type: list[PropertyResource]
        """

        self._properties = properties

    @property
    def system_name(self):
        """
        Gets the system_name of this AutomationTestLogResource.

        :return: The system_name of this AutomationTestLogResource.
        :rtype: str
        """
        return self._system_name

    @system_name.setter
    def system_name(self, system_name):
        """
        Sets the system_name of this AutomationTestLogResource.

        :param system_name: The system_name of this AutomationTestLogResource.
        :type: str
        """

        self._system_name = system_name

    @property
    def status(self):
        """
        Gets the status of this AutomationTestLogResource.
        Test Log status

        :return: The status of this AutomationTestLogResource.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this AutomationTestLogResource.
        Test Log status

        :param status: The status of this AutomationTestLogResource.
        :type: str
        """

        self._status = status

    @property
    def order(self):
        """
        Gets the order of this AutomationTestLogResource.

        :return: The order of this AutomationTestLogResource.
        :rtype: int
        """
        return self._order

    @order.setter
    def order(self, order):
        """
        Sets the order of this AutomationTestLogResource.

        :param order: The order of this AutomationTestLogResource.
        :type: int
        """

        self._order = order

    @property
    def test_step_logs(self):
        """
        Gets the test_step_logs of this AutomationTestLogResource.
        Arrays of Test Step Log

        :return: The test_step_logs of this AutomationTestLogResource.
        :rtype: list[AutomationTestStepLog]
        """
        return self._test_step_logs

    @test_step_logs.setter
    def test_step_logs(self, test_step_logs):
        """
        Sets the test_step_logs of this AutomationTestLogResource.
        Arrays of Test Step Log

        :param test_step_logs: The test_step_logs of this AutomationTestLogResource.
        :type: list[AutomationTestStepLog]
        """

        self._test_step_logs = test_step_logs

    @property
    def module_names(self):
        """
        Gets the module_names of this AutomationTestLogResource.
        Arrays of Modules

        :return: The module_names of this AutomationTestLogResource.
        :rtype: list[str]
        """
        return self._module_names

    @module_names.setter
    def module_names(self, module_names):
        """
        Sets the module_names of this AutomationTestLogResource.
        Arrays of Modules

        :param module_names: The module_names of this AutomationTestLogResource.
        :type: list[str]
        """

        self._module_names = module_names

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
        if not isinstance(other, AutomationTestLogResource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other