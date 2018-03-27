# swagger_client.InventoryApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**inventory_add_inventory_adjustment**](InventoryApi.md#inventory_add_inventory_adjustment) | **POST** /api/Inventory | Agregar ajuste de inventario.
[**inventory_get_inventory_by_warehouse_id**](InventoryApi.md#inventory_get_inventory_by_warehouse_id) | **GET** /api/Inventory | Obtener inventario por almacén.


# **inventory_add_inventory_adjustment**
> inventory_add_inventory_adjustment(new_adjustment)

Agregar ajuste de inventario.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
new_adjustment = swagger_client.NewInventoryAdjustment() # NewInventoryAdjustment | 

try:
    # Agregar ajuste de inventario.
    api_instance.inventory_add_inventory_adjustment(new_adjustment)
except ApiException as e:
    print("Exception when calling InventoryApi->inventory_add_inventory_adjustment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_adjustment** | [**NewInventoryAdjustment**](NewInventoryAdjustment.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **inventory_get_inventory_by_warehouse_id**
> InventorytPage inventory_get_inventory_by_warehouse_id(warehouse_id, filter=filter, orderby=orderby, top=top, skip=skip)

Obtener inventario por almacén.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InventoryApi()
warehouse_id = 'warehouse_id_example' # str | 
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtener inventario por almacén.
    api_response = api_instance.inventory_get_inventory_by_warehouse_id(warehouse_id, filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InventoryApi->inventory_get_inventory_by_warehouse_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **warehouse_id** | [**str**](.md)|  | 
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**InventorytPage**](InventorytPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

