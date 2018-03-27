# swagger_client.AccountingJournalsApi

All URIs are relative to *http://api.bind.com.mx*

Method | HTTP request | Description
------------- | ------------- | -------------
[**accounting_journals_add_accounting_journal**](AccountingJournalsApi.md#accounting_journals_add_accounting_journal) | **POST** /api/AccountingJournals | Agregar póliza contable
[**accounting_journals_delete_accounting_journal**](AccountingJournalsApi.md#accounting_journals_delete_accounting_journal) | **DELETE** /api/AccountingJournals | Eliminar póliza contable
[**accounting_journals_edit_accounting_journal**](AccountingJournalsApi.md#accounting_journals_edit_accounting_journal) | **PUT** /api/AccountingJournals | Editar póliza contable
[**accounting_journals_get**](AccountingJournalsApi.md#accounting_journals_get) | **GET** /api/AccountingJournals | Obtiene la lista de pólizas contables.


# **accounting_journals_add_accounting_journal**
> str accounting_journals_add_accounting_journal(new_accounting_journal)

Agregar póliza contable



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingJournalsApi()
new_accounting_journal = swagger_client.NewAccountingJournal() # NewAccountingJournal | 

try:
    # Agregar póliza contable
    api_response = api_instance.accounting_journals_add_accounting_journal(new_accounting_journal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingJournalsApi->accounting_journals_add_accounting_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **new_accounting_journal** | [**NewAccountingJournal**](NewAccountingJournal.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_journals_delete_accounting_journal**
> accounting_journals_delete_accounting_journal(id_list)

Eliminar póliza contable



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingJournalsApi()
id_list = [swagger_client.list[str]()] # list[str] | 

try:
    # Eliminar póliza contable
    api_instance.accounting_journals_delete_accounting_journal(id_list)
except ApiException as e:
    print("Exception when calling AccountingJournalsApi->accounting_journals_delete_accounting_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **id_list** | **list[str]**|  | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: Not defined

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_journals_edit_accounting_journal**
> str accounting_journals_edit_accounting_journal(accounting_journal)

Editar póliza contable



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingJournalsApi()
accounting_journal = swagger_client.EditAccountingJournal() # EditAccountingJournal | 

try:
    # Editar póliza contable
    api_response = api_instance.accounting_journals_edit_accounting_journal(accounting_journal)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingJournalsApi->accounting_journals_edit_accounting_journal: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **accounting_journal** | [**EditAccountingJournal**](EditAccountingJournal.md)|  | 

### Return type

**str**

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/xml, text/xml, application/x-www-form-urlencoded
 - **Accept**: application/json, text/json, application/xml, text/xml

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **accounting_journals_get**
> AccountingJournalPage accounting_journals_get(filter=filter, orderby=orderby, top=top, skip=skip)

Obtiene la lista de pólizas contables.



### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.AccountingJournalsApi()
filter = 'filter_example' # str | Filters the results, based on a Boolean condition. (optional)
orderby = 'orderby_example' # str | Sorts the results. (optional)
top = 56 # int | Returns only the first n results. (optional)
skip = 56 # int | Skips the first n results. (optional)

try:
    # Obtiene la lista de pólizas contables.
    api_response = api_instance.accounting_journals_get(filter=filter, orderby=orderby, top=top, skip=skip)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling AccountingJournalsApi->accounting_journals_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **filter** | **str**| Filters the results, based on a Boolean condition. | [optional] 
 **orderby** | **str**| Sorts the results. | [optional] 
 **top** | **int**| Returns only the first n results. | [optional] 
 **skip** | **int**| Skips the first n results. | [optional] 

### Return type

[**AccountingJournalPage**](AccountingJournalPage.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

