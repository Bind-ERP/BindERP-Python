# swagger_client.OrdersApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**orders_add_order**](OrdersApi.md#orders_add_order) | **POST** /api/Orders | Agregar pedido
[**orders_delete_order**](OrdersApi.md#orders_delete_order) | **DELETE** /api/Orders/{id} | Eliminar pedido
[**orders_edit_order**](OrdersApi.md#orders_edit_order) | **PUT** /api/Orders | Editar pedido
[**orders_get_by_id**](OrdersApi.md#orders_get_by_id) | **GET** /api/Orders/{id} | Obtiene los detalles de un pedido


# **orders_add_order**
> str orders_add_order(new_order)

Agregar pedido



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
new_order = swagger_client.NewOrder() # NewOrder | 

try:
    # Agregar pedido
    api_response = api_instance.orders_add_order(new_order)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_add_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_order** | [**NewOrder**](NewOrder.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_delete_order**
> orders_delete_order(id)

Eliminar pedido



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
id = 'id_example' # str | ID

try:
    # Eliminar pedido
    api_instance.orders_delete_order(id)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_delete_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_edit_order**
> orders_edit_order(order)

Editar pedido



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
order = swagger_client.EditOrder() # EditOrder | 

try:
    # Editar pedido
    api_instance.orders_edit_order(order)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_edit_order: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **order** | [**EditOrder**](EditOrder.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **orders_get_by_id**
> OrderDetails orders_get_by_id(id)

Obtiene los detalles de un pedido



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.OrdersApi()
id = 'id_example' # str | ID

try:
    # Obtiene los detalles de un pedido
    api_response = api_instance.orders_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling OrdersApi->orders_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

[**OrderDetails**](OrderDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

