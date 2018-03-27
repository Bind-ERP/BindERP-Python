# swagger_client.CommentsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**comments_add_comment**](CommentsApi.md#comments_add_comment) | **POST** /api/Comments | Agregar comentario
[**comments_get**](CommentsApi.md#comments_get) | **GET** /api/Comments | Listar comentarios por external ID


# **comments_add_comment**
> comments_add_comment(new_comment)

Agregar comentario



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
new_comment = swagger_client.NewComment() # NewComment | 

try:
    # Agregar comentario
    api_instance.comments_add_comment(new_comment)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_add_comment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_comment** | [**NewComment**](NewComment.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **comments_get**
> CommentPage comments_get(filter=filter, orderby=orderby, top=top, skip=skip)

Listar comentarios por external ID



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.CommentsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Listar comentarios por external ID
    api_response = api_instance.comments_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling CommentsApi->comments_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**CommentPage**](CommentPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

