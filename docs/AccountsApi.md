# swagger_client.AccountsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounts_add_account**](AccountsApi.md#accounts_add_account) | **POST** /api/Accounts | Agregar Cuenta Contable
[**accounts_delete_account**](AccountsApi.md#accounts_delete_account) | **DELETE** /api/Accounts/{id} | Borrar Cuenta Contable
[**accounts_get**](AccountsApi.md#accounts_get) | **GET** /api/Accounts | Obtiene la lista de cuentas contables.
[**accounts_get_account_categories**](AccountsApi.md#accounts_get_account_categories) | **GET** /api/AccountCategories | Obtiene las categorías de cuentas contables.


# **accounts_add_account**
> str accounts_add_account(new_account)

Agregar Cuenta Contable



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
new_account = swagger_client.NewAccount() # NewAccount | 

try:
    # Agregar Cuenta Contable
    api_response = api_instance.accounts_add_account(new_account)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_add_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_account** | [**NewAccount**](NewAccount.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_delete_account**
> accounts_delete_account(id, replacement_id=replacement_id)

Borrar Cuenta Contable



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
id = 'id_example' # str | 
replacement_id = 'replacement_id_example' # str |  (optional)

try:
    # Borrar Cuenta Contable
    api_instance.accounts_delete_account(id, replacement_id=replacement_id)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_delete_account: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 
 **replacement_id** | [**str**](.md)|  | [optional] 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get**
> AccountPage accounts_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de cuentas contables.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de cuentas contables.
    api_response = api_instance.accounts_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**AccountPage**](AccountPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounts_get_account_categories**
> AccountCategories accounts_get_account_categories()

Obtiene las categorías de cuentas contables.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountsApi()

try:
    # Obtiene las categorías de cuentas contables.
    api_response = api_instance.accounts_get_account_categories()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountsApi->accounts_get_account_categories: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**AccountCategories**](AccountCategories.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

