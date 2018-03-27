# swagger_client.ActivitiesApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**activities_add_activity**](ActivitiesApi.md#activities_add_activity) | **POST** /api/Activities | Agregar actividad


# **activities_add_activity**
> activities_add_activity(new_activity)

Agregar actividad



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ActivitiesApi()
new_activity = swagger_client.NewActivity() # NewActivity | 

try:
    # Agregar actividad
    api_instance.activities_add_activity(new_activity)
except ApiException as e:
    print("Exception when calling ActivitiesApi->activities_add_activity: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_activity** | [**NewActivity**](NewActivity.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

