# CreateOrderRequest
> squareconnect.models.create_order_request

### Description

Defines the parameters that can be included in the body of a request to the [CreateCheckout](#endpoint-createcheckout) endpoint.

## Properties
Name | Type | Notes
------------ | ------------- | -------------
**reference_id** | **str** | [optional] 
**line_items** | [**list[CreateOrderRequestLineItem]**](CreateOrderRequestLineItem.md) | 
**taxes** | [**list[CreateOrderRequestTax]**](CreateOrderRequestTax.md) | [optional] 
**discounts** | [**list[CreateOrderRequestDiscount]**](CreateOrderRequestDiscount.md) | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


