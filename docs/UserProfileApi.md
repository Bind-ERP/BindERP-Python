# swagger_client.UserProfileApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**user_profile_get**](UserProfileApi.md#user_profile_get) | **GET** /api/UserProfile | Obtiene la lista de cuentas contables.


# **user_profile_get**
> UserProfile user_profile_get()

Obtiene la lista de cuentas contables.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.UserProfileApi()

try:
    # Obtiene la lista de cuentas contables.
    api_response = api_instance.user_profile_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling UserProfileApi->user_profile_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**UserProfile**](UserProfile.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

