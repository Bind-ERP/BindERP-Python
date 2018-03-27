# swagger_client.ClientsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**clients_add_client**](ClientsApi.md#clients_add_client) | **POST** /api/Clients | Agregar Cliente
[**clients_delete_by_id**](ClientsApi.md#clients_delete_by_id) | **DELETE** /api/Clients/{id} | Borrar Cliente
[**clients_edit_client**](ClientsApi.md#clients_edit_client) | **PUT** /api/Clients | Editar Cliente
[**clients_get**](ClientsApi.md#clients_get) | **GET** /api/Clients | Obtiene la lista de clientes.
[**clients_get_details**](ClientsApi.md#clients_get_details) | **GET** /api/Clients/{id} | Obtiene los detalles de un cliente.


# **clients_add_client**
> str clients_add_client(new_client)

Agregar Cliente



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
new_client = swagger_client.NewClient() # NewClient | 

try:
    # Agregar Cliente
    api_response = api_instance.clients_add_client(new_client)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_add_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_client** | [**NewClient**](NewClient.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_delete_by_id**
> clients_delete_by_id(id)

Borrar Cliente



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
id = 'id_example' # str | 

try:
    # Borrar Cliente
    api_instance.clients_delete_by_id(id)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_delete_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_edit_client**
> clients_edit_client(client)

Editar Cliente



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
client = swagger_client.EditClient() # EditClient | 

try:
    # Editar Cliente
    api_instance.clients_edit_client(client)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_edit_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **client** | [**EditClient**](EditClient.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get**
> ClientListItemPage clients_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de clientes.

El filtro es opcional

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de clientes.
    api_response = api_instance.clients_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**ClientListItemPage**](ClientListItemPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **clients_get_details**
> ClientDetails clients_get_details(id)

Obtiene los detalles de un cliente.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ClientsApi()
id = 'id_example' # str | 

try:
    # Obtiene los detalles de un cliente.
    api_response = api_instance.clients_get_details(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ClientsApi->clients_get_details: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ClientDetails**](ClientDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

