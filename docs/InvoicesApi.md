# swagger_client.InvoicesApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_add_invoice**](InvoicesApi.md#invoices_add_invoice) | **POST** /api/Invoices | Agregar Venta
[**invoices_add_payment**](InvoicesApi.md#invoices_add_payment) | **POST** /api/Invoices/Payment | Registrar pago a venta
[**invoices_delete_invoice**](InvoicesApi.md#invoices_delete_invoice) | **DELETE** /api/Invoices/{id} | Eliminar factura
[**invoices_get**](InvoicesApi.md#invoices_get) | **GET** /api/Invoices | Obtiene la lista de ventas.
[**invoices_get_by_number**](InvoicesApi.md#invoices_get_by_number) | **GET** /api/Invoices/{idOrNumber} | Obtiene los detalles de una venta por número
[**invoices_get_pdf**](InvoicesApi.md#invoices_get_pdf) | **GET** /api/Invoices/{id}/pdf | Obtener el PDF de una venta
[**invoices_get_xml**](InvoicesApi.md#invoices_get_xml) | **GET** /api/Invoices/{id}/xml | Obtener el XML de una venta


# **invoices_add_invoice**
> str invoices_add_invoice(new_invoice)

Agregar Venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
new_invoice = swagger_client.NewInvoice() # NewInvoice | 

try:
    # Agregar Venta
    api_response = api_instance.invoices_add_invoice(new_invoice)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_add_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_invoice** | [**NewInvoice**](NewInvoice.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_add_payment**
> invoices_add_payment(new_payment)

Registrar pago a venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
new_payment = swagger_client.NewPayment() # NewPayment | 

try:
    # Registrar pago a venta
    api_instance.invoices_add_payment(new_payment)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_add_payment: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_payment** | [**NewPayment**](NewPayment.md)|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_delete_invoice**
> invoices_delete_invoice(id)

Eliminar factura



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | ID

try:
    # Eliminar factura
    api_instance.invoices_delete_invoice(id)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_delete_invoice: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get**
> InvoiceListItemPage invoices_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de ventas.

El filtro es opcional

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de ventas.
    api_response = api_instance.invoices_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**InvoiceListItemPage**](InvoiceListItemPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_by_number**
> InvoiceDetails invoices_get_by_number(id_or_number)

Obtiene los detalles de una venta por número



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id_or_number = 'id_or_number_example' # str | 

try:
    # Obtiene los detalles de una venta por número
    api_response = api_instance.invoices_get_by_number(id_or_number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_by_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_or_number** | **str**|  | 

### Return type

[**InvoiceDetails**](InvoiceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_pdf**
> file invoices_get_pdf(id)

Obtener el PDF de una venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | ID

try:
    # Obtener el PDF de una venta
    api_response = api_instance.invoices_get_pdf(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_pdf: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

[**file**](file.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/octet-stream

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_xml**
> str invoices_get_xml(id)

Obtener el XML de una venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
id = 'id_example' # str | ID

try:
    # Obtener el XML de una venta
    api_response = api_instance.invoices_get_xml(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_xml: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

