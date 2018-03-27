# swagger_client.CatalogsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**catalogs_get_banks**](CatalogsApi.md#catalogs_get_banks) | **GET** /api/Banks | Obtiene la lista de bancos.
[**catalogs_get_categories**](CatalogsApi.md#catalogs_get_categories) | **GET** /api/Categories | Obtiene la lista de Categorias.
[**catalogs_get_currencies**](CatalogsApi.md#catalogs_get_currencies) | **GET** /api/Currencies | Obtiene la lista de monedas.
[**catalogs_get_locations**](CatalogsApi.md#catalogs_get_locations) | **GET** /api/Locations | Obtiene la lista de sucursales.
[**catalogs_get_price_lists**](CatalogsApi.md#catalogs_get_price_lists) | **GET** /api/PriceLists | Obtiene la lista de precios.
[**catalogs_get_series**](CatalogsApi.md#catalogs_get_series) | **GET** /api/Series | Obtiene la lista de Series.
[**catalogs_get_users**](CatalogsApi.md#catalogs_get_users) | **GET** /api/Users | Obtiene la lista de usuarios.


# **catalogs_get_banks**
> BankPage catalogs_get_banks(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de bancos.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de bancos.
    api_response = api_instance.catalogs_get_banks(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_banks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**BankPage**](BankPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_categories**
> list[Category1] catalogs_get_categories()

Obtiene la lista de Categorias.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()

try:
    # Obtiene la lista de Categorias.
    api_response = api_instance.catalogs_get_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[Category1]**](Category1.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_currencies**
> CurrencyPage catalogs_get_currencies(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de monedas.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de monedas.
    api_response = api_instance.catalogs_get_currencies(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_currencies: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**CurrencyPage**](CurrencyPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_locations**
> LocationPage catalogs_get_locations(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de sucursales.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de sucursales.
    api_response = api_instance.catalogs_get_locations(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_locations: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**LocationPage**](LocationPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_price_lists**
> PriceListPage catalogs_get_price_lists(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de precios.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de precios.
    api_response = api_instance.catalogs_get_price_lists(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_price_lists: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**PriceListPage**](PriceListPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_series**
> list[Series] catalogs_get_series(doc_type)

Obtiene la lista de Series.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
doc_type = 56 # int | 

try:
    # Obtiene la lista de Series.
    api_response = api_instance.catalogs_get_series(doc_type)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_series: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **doc_type** | **int**|  | 

### Return type

[**list[Series]**](Series.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **catalogs_get_users**
> UserPage catalogs_get_users(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de usuarios.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CatalogsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de usuarios.
    api_response = api_instance.catalogs_get_users(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CatalogsApi->catalogs_get_users: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**UserPage**](UserPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

