# swagger_client.ProvidersApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**providers_add_provider**](ProvidersApi.md#providers_add_provider) | **POST** /api/Providers | Agregar Proveedor
[**providers_delete_by_id**](ProvidersApi.md#providers_delete_by_id) | **DELETE** /api/Providers/{id} | Borrar Proveedor
[**providers_edit_provider**](ProvidersApi.md#providers_edit_provider) | **PUT** /api/Providers | Editar Proveedor
[**providers_get_providers**](ProvidersApi.md#providers_get_providers) | **GET** /api/Providers | Obtiene la lista de proveedores.


# **providers_add_provider**
> str providers_add_provider(new_provider)

Agregar Proveedor



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvidersApi()
new_provider = swagger_client.NewProvider() # NewProvider | 

try:
    # Agregar Proveedor
    api_response = api_instance.providers_add_provider(new_provider)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_add_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_provider** | [**NewProvider**](NewProvider.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_delete_by_id**
> providers_delete_by_id(id)

Borrar Proveedor



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvidersApi()
id = 'id_example' # str | 

try:
    # Borrar Proveedor
    api_instance.providers_delete_by_id(id)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_delete_by_id: %s\n" % e)
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

# **providers_edit_provider**
> providers_edit_provider(provider)

Editar Proveedor



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvidersApi()
provider = swagger_client.EditProvider() # EditProvider | 

try:
    # Editar Proveedor
    api_instance.providers_edit_provider(provider)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_edit_provider: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **provider** | [**EditProvider**](EditProvider.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **providers_get_providers**
> ProviderListItemPage providers_get_providers(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de proveedores.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProvidersApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de proveedores.
    api_response = api_instance.providers_get_providers(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProvidersApi->providers_get_providers: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**ProviderListItemPage**](ProviderListItemPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

