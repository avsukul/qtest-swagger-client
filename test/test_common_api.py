# coding: utf-8

"""
    qTest Manager API Version 8.6 - 9.0

    qTest Manager API Version 8.6 - 9.0

    OpenAPI spec version: 8.6 - 9.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import swagger_client
from swagger_client.rest import ApiException
from swagger_client.apis.common_api import CommonApi


class TestCommonApi(unittest.TestCase):
    """ CommonApi unit test stubs """

    def setUp(self):
        self.api = swagger_client.apis.common_api.CommonApi()

    def tearDown(self):
        pass

    def test_edit_system_field(self):
        """
        Test case for edit_system_field

        Edit System Field of an Object Type by the field
        """
        pass

    def test_update_custom_field(self):
        """
        Test case for update_custom_field

        field.updateCustomField
        """
        pass


if __name__ == '__main__':
    unittest.main()
