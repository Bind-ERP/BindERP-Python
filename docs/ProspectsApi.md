# swagger_client.ProspectsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**prospects_add_prospect**](ProspectsApi.md#prospects_add_prospect) | **POST** /api/Prospects | Agregar Prospecto
[**prospects_delete_by_id**](ProspectsApi.md#prospects_delete_by_id) | **DELETE** /api/Prospects/{id} | Borrar Prospecto
[**prospects_edit_client**](ProspectsApi.md#prospects_edit_client) | **PUT** /api/Prospects | Editar Prospecto
[**prospects_get**](ProspectsApi.md#prospects_get) | **GET** /api/Prospects/{id} | Obtiene los detalles de un prospecto.
[**prospects_get_prospects**](ProspectsApi.md#prospects_get_prospects) | **GET** /api/Prospects | Obtiene la lista de prospectos.


# **prospects_add_prospect**
> str prospects_add_prospect(new_prospect)

Agregar Prospecto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProspectsApi()
new_prospect = swagger_client.NewProspect() # NewProspect | 

try:
    # Agregar Prospecto
    api_response = api_instance.prospects_add_prospect(new_prospect)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProspectsApi->prospects_add_prospect: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_prospect** | [**NewProspect**](NewProspect.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prospects_delete_by_id**
> prospects_delete_by_id(id)

Borrar Prospecto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProspectsApi()
id = 'id_example' # str | 

try:
    # Borrar Prospecto
    api_instance.prospects_delete_by_id(id)
except ApiException as e:
    print("Exception when calling ProspectsApi->prospects_delete_by_id: %s\n" % e)
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

# **prospects_edit_client**
> prospects_edit_client(prospect)

Editar Prospecto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProspectsApi()
prospect = swagger_client.EditProspect() # EditProspect | 

try:
    # Editar Prospecto
    api_instance.prospects_edit_client(prospect)
except ApiException as e:
    print("Exception when calling ProspectsApi->prospects_edit_client: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **prospect** | [**EditProspect**](EditProspect.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prospects_get**
> ProspectDetails prospects_get(id)

Obtiene los detalles de un prospecto.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProspectsApi()
id = 'id_example' # str | 

try:
    # Obtiene los detalles de un prospecto.
    api_response = api_instance.prospects_get(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProspectsApi->prospects_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ProspectDetails**](ProspectDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **prospects_get_prospects**
> ProspectListItemPage prospects_get_prospects(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de prospectos.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProspectsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de prospectos.
    api_response = api_instance.prospects_get_prospects(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProspectsApi->prospects_get_prospects: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**ProspectListItemPage**](ProspectListItemPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

