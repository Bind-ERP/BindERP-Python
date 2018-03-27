# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import swagger_client
from swagger_client.api.products_api import ProductsApi  # noqa: E501
from swagger_client.rest import ApiException


class TestProductsApi(unittest.TestCase):
    """ProductsApi unit test stubs"""

    def setUp(self):
        self.api = swagger_client.api.products_api.ProductsApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_products_add_product(self):
        """Test case for products_add_product

        Agregar Producto  # noqa: E501
        """
        pass

    def test_products_delete_by_id(self):
        """Test case for products_delete_by_id

        Borrar Producto  # noqa: E501
        """
        pass

    def test_products_edit_product(self):
        """Test case for products_edit_product

        Editar Producto  # noqa: E501
        """
        pass

    def test_products_get(self):
        """Test case for products_get

        Obtiene la lista de productos.  # noqa: E501
        """
        pass

    def test_products_get_detail(self):
        """Test case for products_get_detail

        Obtiene los detalles de un producto.  # noqa: E501
        """
        pass

    def test_products_get_image(self):
        """Test case for products_get_image

        Obtiene la imagen del producto.  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
