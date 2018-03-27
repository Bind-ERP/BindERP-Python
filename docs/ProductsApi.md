# swagger_client.ProductsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**products_add_product**](ProductsApi.md#products_add_product) | **POST** /api/Products | Agregar Producto
[**products_delete_by_id**](ProductsApi.md#products_delete_by_id) | **DELETE** /api/Products/{id} | Borrar Producto
[**products_edit_product**](ProductsApi.md#products_edit_product) | **PUT** /api/Products | Editar Producto
[**products_get**](ProductsApi.md#products_get) | **GET** /api/Products | Obtiene la lista de productos.
[**products_get_detail**](ProductsApi.md#products_get_detail) | **GET** /api/Products/{id} | Obtiene los detalles de un producto.
[**products_get_image**](ProductsApi.md#products_get_image) | **GET** /api/Products/{id}/image | Obtiene la imagen del producto.


# **products_add_product**
> str products_add_product(new_product)

Agregar Producto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
new_product = swagger_client.NewProduct() # NewProduct | 

try:
    # Agregar Producto
    api_response = api_instance.products_add_product(new_product)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_add_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_product** | [**NewProduct**](NewProduct.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_delete_by_id**
> products_delete_by_id(id)

Borrar Producto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 'id_example' # str | 

try:
    # Borrar Producto
    api_instance.products_delete_by_id(id)
except ApiException as e:
    print("Exception when calling ProductsApi->products_delete_by_id: %s\n" % e)
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

# **products_edit_product**
> products_edit_product(product)

Editar Producto



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
product = swagger_client.EditProduct() # EditProduct | 

try:
    # Editar Producto
    api_instance.products_edit_product(product)
except ApiException as e:
    print("Exception when calling ProductsApi->products_edit_product: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **product** | [**EditProduct**](EditProduct.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get**
> ProductPage products_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de productos.

El filtro es opcional

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de productos.
    api_response = api_instance.products_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**ProductPage**](ProductPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get_detail**
> ProductDetails products_get_detail(id)

Obtiene los detalles de un producto.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 'id_example' # str | 

try:
    # Obtiene los detalles de un producto.
    api_response = api_instance.products_get_detail(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get_detail: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

[**ProductDetails**](ProductDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **products_get_image**
> str products_get_image(id)

Obtiene la imagen del producto.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.ProductsApi()
id = 'id_example' # str | 

try:
    # Obtiene la imagen del producto.
    api_response = api_instance.products_get_image(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ProductsApi->products_get_image: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

