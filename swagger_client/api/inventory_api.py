# coding: utf-8

"""
    Bind ERP API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: v1
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six

from swagger_client.api_client import ApiClient


class InventoryApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def inventory_add_inventory_adjustment(self, new_adjustment, **kwargs):  # noqa: E501
        """Agregar ajuste de inventario.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_add_inventory_adjustment(new_adjustment, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewInventoryAdjustment new_adjustment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_add_inventory_adjustment_with_http_info(new_adjustment, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_add_inventory_adjustment_with_http_info(new_adjustment, **kwargs)  # noqa: E501
            return data

    def inventory_add_inventory_adjustment_with_http_info(self, new_adjustment, **kwargs):  # noqa: E501
        """Agregar ajuste de inventario.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_add_inventory_adjustment_with_http_info(new_adjustment, async=True)
        >>> result = thread.get()

        :param async bool
        :param NewInventoryAdjustment new_adjustment:  (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['new_adjustment']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_add_inventory_adjustment" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'new_adjustment' is set
        if ('new_adjustment' not in params or
                params['new_adjustment'] is None):
            raise ValueError("Missing the required parameter `new_adjustment` when calling `inventory_add_inventory_adjustment`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'new_adjustment' in params:
            body_params = params['new_adjustment']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(  # noqa: E501
            ['application/json', 'text/json', 'application/xml', 'text/xml', 'application/x-www-form-urlencoded'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Inventory', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def inventory_get_inventory_by_warehouse_id(self, warehouse_id, **kwargs):  # noqa: E501
        """Obtener inventario por almacén.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_get_inventory_by_warehouse_id(warehouse_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str warehouse_id:  (required)
        :param str filter: Filters the results, based on a Boolean condition.
        :param str orderby: Sorts the results.
        :param int top: Returns only the first n results.
        :param int skip: Skips the first n results.
        :return: InventorytPage
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        if kwargs.get('async'):
            return self.inventory_get_inventory_by_warehouse_id_with_http_info(warehouse_id, **kwargs)  # noqa: E501
        else:
            (data) = self.inventory_get_inventory_by_warehouse_id_with_http_info(warehouse_id, **kwargs)  # noqa: E501
            return data

    def inventory_get_inventory_by_warehouse_id_with_http_info(self, warehouse_id, **kwargs):  # noqa: E501
        """Obtener inventario por almacén.  # noqa: E501

          # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async=True
        >>> thread = api.inventory_get_inventory_by_warehouse_id_with_http_info(warehouse_id, async=True)
        >>> result = thread.get()

        :param async bool
        :param str warehouse_id:  (required)
        :param str filter: Filters the results, based on a Boolean condition.
        :param str orderby: Sorts the results.
        :param int top: Returns only the first n results.
        :param int skip: Skips the first n results.
        :return: InventorytPage
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['warehouse_id', 'filter', 'orderby', 'top', 'skip']  # noqa: E501
        all_params.append('async')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method inventory_get_inventory_by_warehouse_id" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'warehouse_id' is set
        if ('warehouse_id' not in params or
                params['warehouse_id'] is None):
            raise ValueError("Missing the required parameter `warehouse_id` when calling `inventory_get_inventory_by_warehouse_id`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'warehouse_id' in params:
            query_params.append(('warehouseID', params['warehouse_id']))  # noqa: E501
        if 'filter' in params:
            query_params.append(('$filter', params['filter']))  # noqa: E501
        if 'orderby' in params:
            query_params.append(('$orderby', params['orderby']))  # noqa: E501
        if 'top' in params:
            query_params.append(('$top', params['top']))  # noqa: E501
        if 'skip' in params:
            query_params.append(('$skip', params['skip']))  # noqa: E501

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/json'])  # noqa: E501

        # Authentication setting
        auth_settings = []  # noqa: E501

        return self.api_client.call_api(
            '/api/Inventory', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='InventorytPage',  # noqa: E501
            auth_settings=auth_settings,
            async=params.get('async'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)