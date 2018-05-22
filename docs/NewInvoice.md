# NewInvoice

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**currency_id** | **str** |  | 
**client_id** | **str** |  | 
**location_id** | **str** |  | 
**warehouse_id** | **str** |  | 
**cfdi_use** | **int** |  | 
**invoice_date** | **datetime** |  | 
**price_list_id** | **str** |  | 
**exchange_rate** | **float** |  | [optional] 
**isr_ret_rate** | **float** |  | [optional] 
**vat_ret_rate** | **float** |  | [optional] 
**comments** | **str** |  | [optional] 
**vat_rate** | **float** |  | [optional] 
**discount_type** | **int** |  | [optional] 
**discount_amount** | **float** |  | [optional] 
**products** | [**list[NewInvoiceProduct]**](NewInvoiceProduct.md) |  | [optional] 
**services** | [**list[NewInvoiceService]**](NewInvoiceService.md) |  | [optional] 
**emails** | **list[str]** |  | [optional] 
**purchase_order** | **str** |  | [optional] 
**credit_days** | **int** |  | [optional] 
**is_fiscal_invoice** | **bool** |  | [optional] 
**show_ieps** | **bool** |  | [optional] 
**number** | **int** |  | [optional] 
**account** | **str** |  | [optional] 
**payments** | [**list[NewInvoicePayment]**](NewInvoicePayment.md) |  | [optional] 
**serie** | **str** |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


