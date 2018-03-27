# NewInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **str** |  | 
**exchange_rate** | **float** |  | [optional] 
**isr_ret_rate** | **float** |  | [optional] 
**vat_ret_rate** | **float** |  | [optional] 
**client_id** | **str** |  | [optional] 
**location_id** | **str** |  | [optional] 
**comments** | **str** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**discount_type** | **int** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**products** | [**list[NewInvoiceProduct]**](NewInvoiceProduct.md) |  | [optional] 
**services** | [**list[NewInvoiceService]**](NewInvoiceService.md) |  | [optional] 
**emails** | **list[str]** |  | [optional] 
**warehouse_id** | **str** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**credit_days** | **int** |  | [optional] 
**is_fiscal_invoice** | **bool** |  | [optional] 
**show_ieps** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**cfdi_use** | **int** |  | [optional] 
**account** | **str** |  | [optional] 
**payments** | [**list[NewInvoicePayment]**](NewInvoicePayment.md) |  | [optional] 
**invoice_date** | **datetime** |  | 
**price_list_id** | **str** |  | 
**serie** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


