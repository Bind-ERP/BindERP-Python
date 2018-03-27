# swagger_client.InvoicesApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**invoices_add_invoice**](InvoicesApi.md#invoices_add_invoice) | **POST** /api/Invoices | Agregar factura
[**invoices_add_payment**](InvoicesApi.md#invoices_add_payment) | **POST** /api/Invoices/Payment | Registrar pago a factura
[**invoices_delete_invoice**](InvoicesApi.md#invoices_delete_invoice) | **DELETE** /api/Invoices/{id} | Eliminar factura
[**invoices_get_by_id**](InvoicesApi.md#invoices_get_by_id) | **GET** /api/Invoices/{id} | Obtiene los detalles de una venta
[**invoices_get_by_number**](InvoicesApi.md#invoices_get_by_number) | **GET** /api/Invoices | Obtiene los detalles de una venta
[**invoices_get_pdf**](InvoicesApi.md#invoices_get_pdf) | **GET** /api/Invoices/{id}/pdf | Obtener el PDF de una venta
[**invoices_get_xml**](InvoicesApi.md#invoices_get_xml) | **GET** /api/Invoices/{id}/xml | Obtener el XML de una venta


# **invoices_add_invoice**
> str invoices_add_invoice(new_invoice)

Agregar factura



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
    # Agregar factura
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

Registrar pago a factura



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
    # Registrar pago a factura
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

# **invoices_get_by_id**
> InvoiceDetails invoices_get_by_id(id)

Obtiene los detalles de una venta



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
    # Obtiene los detalles de una venta
    api_response = api_instance.invoices_get_by_id(id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_by_id: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id** | [**str**](.md)| ID | 

### Return type

[**InvoiceDetails**](InvoiceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_by_number**
> InvoiceDetails invoices_get_by_number(number)

Obtiene los detalles de una venta



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.InvoicesApi()
number = 'number_example' # str | Serie y Número

try:
    # Obtiene los detalles de una venta
    api_response = api_instance.invoices_get_by_number(number)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling InvoicesApi->invoices_get_by_number: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **number** | **str**| Serie y Número | 

### Return type

[**InvoiceDetails**](InvoiceDetails.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **invoices_get_pdf**
> object invoices_get_pdf(id)

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

**object**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json, application/xml, text/xml

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

