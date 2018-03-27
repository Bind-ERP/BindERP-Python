# swagger_client.ServicesApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**services_add_product**](ServicesApi.md#services_add_product) | **POST** /api/Services | Agregar Concepto de Venta
[**services_delete_by_id**](ServicesApi.md#services_delete_by_id) | **DELETE** /api/Services/{id} | Borrar Servicio
[**services_edit_product**](ServicesApi.md#services_edit_product) | **PUT** /api/Services | Editar Concepto de Venta
[**services_get_services**](ServicesApi.md#services_get_services) | **GET** /api/Services | Obtiene la lista de conceptos de venta.


# **services_add_product**
> str services_add_product(new_service)

Agregar Concepto de Venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
new_service = swagger_client.NewService() # NewService | 

try:
    # Agregar Concepto de Venta
    api_response = api_instance.services_add_product(new_service)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_service** | [**NewService**](NewService.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_delete_by_id**
> services_delete_by_id(id)

Borrar Servicio



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
id = 'id_example' # str | 

try:
    # Borrar Servicio
    api_instance.services_delete_by_id(id)
except ApiException as e:
    print("Exception when calling ServicesApi->services_delete_by_id: %s\n" % e)
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

# **services_edit_product**
> services_edit_product(service)

Editar Concepto de Venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
service = swagger_client.EditService() # EditService | 

try:
    # Editar Concepto de Venta
    api_instance.services_edit_product(service)
except ApiException as e:
    print("Exception when calling ServicesApi->services_edit_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **service** | [**EditService**](EditService.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **services_get_services**
> ServicesPage services_get_services(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de conceptos de venta.

El filtro es opcional

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ServicesApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de conceptos de venta.
    api_response = api_instance.services_get_services(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ServicesApi->services_get_services: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**ServicesPage**](ServicesPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

