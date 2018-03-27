# swagger_client.BankAccountsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**bank_accounts_get**](BankAccountsApi.md#bank_accounts_get) | **GET** /api/BankAccounts | Obtiene la lista de cuentas bancarias.


# **bank_accounts_get**
> BankAccountPage bank_accounts_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de cuentas bancarias.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.BankAccountsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de cuentas bancarias.
    api_response = api_instance.bank_accounts_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling BankAccountsApi->bank_accounts_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**BankAccountPage**](BankAccountPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

