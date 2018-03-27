# swagger_client.WebHooksApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**web_hooks_add_web_hook_subscriptions**](WebHooksApi.md#web_hooks_add_web_hook_subscriptions) | **POST** /api/WebHookSubscriptions | Suscribirse a un WebHook
[**web_hooks_delete_web_hook_subscriptio_by_id**](WebHooksApi.md#web_hooks_delete_web_hook_subscriptio_by_id) | **DELETE** /api/WebHookSubscriptions | Borrar suscripción a WebHook
[**web_hooks_edit_web_hook_subscription**](WebHooksApi.md#web_hooks_edit_web_hook_subscription) | **PUT** /api/WebHookSubscriptions | Editar suscripción a WebHook
[**web_hooks_get_web_hook_sample_data**](WebHooksApi.md#web_hooks_get_web_hook_sample_data) | **GET** /api/WebHooks/{eventID} | Obtiene un ejemplo del modelo de datos que envía el WebHook.
[**web_hooks_get_web_hook_subscriptions**](WebHooksApi.md#web_hooks_get_web_hook_subscriptions) | **GET** /api/WebHookSubscriptions | Obtiene la lista de su suscripciones a WebHooks
[**web_hooks_get_web_hooks**](WebHooksApi.md#web_hooks_get_web_hooks) | **GET** /api/WebHooks | Obtiene la lista de WebHooks disponibles.


# **web_hooks_add_web_hook_subscriptions**
> object web_hooks_add_web_hook_subscriptions(web_hook_subscription)

Suscribirse a un WebHook



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
web_hook_subscription = swagger_client.NewWebHookSubscription() # NewWebHookSubscription | 

try:
    # Suscribirse a un WebHook
    api_response = api_instance.web_hooks_add_web_hook_subscriptions(web_hook_subscription)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_add_web_hook_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_subscription** | [**NewWebHookSubscription**](NewWebHookSubscription.md)|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_delete_web_hook_subscriptio_by_id**
> web_hooks_delete_web_hook_subscriptio_by_id(id)

Borrar suscripción a WebHook



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
id = 'id_example' # str | 

try:
    # Borrar suscripción a WebHook
    api_instance.web_hooks_delete_web_hook_subscriptio_by_id(id)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_delete_web_hook_subscriptio_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | **str**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_edit_web_hook_subscription**
> web_hooks_edit_web_hook_subscription(web_hook_subscription)

Editar suscripción a WebHook



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
web_hook_subscription = swagger_client.NewWebHookSubscription() # NewWebHookSubscription | 

try:
    # Editar suscripción a WebHook
    api_instance.web_hooks_edit_web_hook_subscription(web_hook_subscription)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_edit_web_hook_subscription: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **web_hook_subscription** | [**NewWebHookSubscription**](NewWebHookSubscription.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_get_web_hook_sample_data**
> object web_hooks_get_web_hook_sample_data(event_id)

Obtiene un ejemplo del modelo de datos que envía el WebHook.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
event_id = 'event_id_example' # str | 

try:
    # Obtiene un ejemplo del modelo de datos que envía el WebHook.
    api_response = api_instance.web_hooks_get_web_hook_sample_data(event_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_get_web_hook_sample_data: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **event_id** | **str**|  | 

### Return type

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_get_web_hook_subscriptions**
> WebHookSubscriptionPage web_hooks_get_web_hook_subscriptions(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de su suscripciones a WebHooks



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de su suscripciones a WebHooks
    api_response = api_instance.web_hooks_get_web_hook_subscriptions(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_get_web_hook_subscriptions: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**WebHookSubscriptionPage**](WebHookSubscriptionPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **web_hooks_get_web_hooks**
> WebHookPage web_hooks_get_web_hooks(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de WebHooks disponibles.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.WebHooksApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de WebHooks disponibles.
    api_response = api_instance.web_hooks_get_web_hooks(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling WebHooksApi->web_hooks_get_web_hooks: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**WebHookPage**](WebHookPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

