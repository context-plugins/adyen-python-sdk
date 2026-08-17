# Initialization

```python
initialization_api = client.initialization
```

## Class Name

`InitializationApi`

## Methods

* [Post-Store Detail](../../doc/controllers/initialization.md#post-store-detail)
* [Post-Store Detail and Submit Third Party](../../doc/controllers/initialization.md#post-store-detail-and-submit-third-party)
* [Post-Submit Third Party](../../doc/controllers/initialization.md#post-submit-third-party)


# Post-Store Detail

> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
> 
> - If you are building a new integration, use the [Transfers API](https://docs.adyen.com/api-explorer/transfers/latest/overview) instead.
> - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
> 
> With the Transfers API, you can:
> 
> - Handle multiple payout use cases with a single API.
> - Use new payout functionalities, such as instant payouts to bank accounts.
> - Receive webhooks with more details and defined transfer states.
> 
> For more information about the payout features of the Transfers API, see our [Payouts](https://docs.adyen.com/payouts/payout-service) documentation.

Stores payment details under the `PAYOUT` recurring contract. These payment details can be used later to submit a payout via the `/submitThirdParty` call.

```python
def post_store_detail(self,
                     body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoreDetailRequest`](../../doc/models/store-detail-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoreDetailResponse`](../../doc/models/store-detail-response.md)

## Example Usage

```python
result = initialization_api.post_store_detail()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "991617894326362D",
  "recurringDetailReference": "9916178936754752",
  "resultCode": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Store Detail and Submit Third Party

> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
> 
> - If you are building a new integration, use the POST [/transfers](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) endpoint instead.
> - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
> 
> With the Transfers API, you can:
> 
> - Handle multiple payout use cases with a single API.
> - Use new payout functionalities, such as instant payouts to bank accounts.
> - Receive webhooks with more details and defined transfer states.
> 
> For more information about the payout features of the Transfers API, see our [Payouts](https://docs.adyen.com/payouts/payout-service) documentation.

Submits a payout and stores its details for subsequent payouts.

The submitted payout must be confirmed or declined either by a reviewer or via `/confirmThirdParty` or `/declineThirdParty` calls.

```python
def post_store_detail_and_submit_third_party(self,
                                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoreDetailAndSubmitRequest`](../../doc/models/store-detail-and-submit-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoreDetailAndSubmitResponse`](../../doc/models/store-detail-and-submit-response.md)

## Example Usage

```python
result = initialization_api.post_store_detail_and_submit_third_party()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Submit Third Party

> This endpoint is **deprecated** and no longer supports new integrations. Do one of the following:
> 
> - If you are building a new integration, use the POST [/transfers](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) endpoint instead.
> - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
> 
> With the Transfers API, you can:
> 
> - Handle multiple payout use cases with a single API.
> - Use new payout functionalities, such as instant payouts to bank accounts.
> - Receive webhooks with more details and defined transfer states.
> 
> For more information about the payout features of the Transfers API, see our [Payouts](https://docs.adyen.com/payouts/payout-service) documentation.

Submits a payout using the previously stored payment details. To store payment details, use the `/storeDetail` API call.

The submitted payout must be confirmed or declined either by a reviewer or via `/confirmThirdParty` or `/declineThirdParty` calls.

```python
def post_submit_third_party(self,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubmitRequest`](../../doc/models/submit-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`SubmitResponse`](../../doc/models/submit-response.md)

## Example Usage

```python
result = initialization_api.post_submit_third_party()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |

