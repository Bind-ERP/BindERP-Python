# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.accounting_journals_api import AccountingJournalsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestAccountingJournalsApi(unittest.TestCase):
    """AccountingJournalsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.accounting_journals_api.AccountingJournalsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_accounting_journals_add_accounting_journal(self):
        """Test case for accounting_journals_add_accounting_journal

        Agregar póliza contable  # noqa: E501
        """
        pass

    def test_accounting_journals_delete_accounting_journal(self):
        """Test case for accounting_journals_delete_accounting_journal

        Eliminar póliza contable  # noqa: E501
        """
        pass

    def test_accounting_journals_edit_accounting_journal(self):
        """Test case for accounting_journals_edit_accounting_journal

        Editar póliza contable  # noqa: E501
        """
        pass

    def test_accounting_journals_get(self):
        """Test case for accounting_journals_get

        Obtiene la lista de pólizas contables.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
