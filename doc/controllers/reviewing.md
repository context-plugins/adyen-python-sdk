# Reviewing

```python
reviewing_api = client.reviewing
```

## Class Name

`ReviewingApi`

## Methods

* [Post-Confirm Third Party](../../doc/controllers/reviewing.md#post-confirm-third-party)
* [Post-Decline Third Party](../../doc/controllers/reviewing.md#post-decline-third-party)


# Post-Confirm Third Party

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

Confirms a previously submitted payout.

To cancel a payout, use the `/declineThirdParty` endpoint.

```python
def post_confirm_third_party(self,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModifyRequest`](../../doc/models/modify-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ModifyResponse`](../../doc/models/modify-response.md)

## Example Usage

```python
body = ModifyRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_reference='9913140798220028'
)

result = reviewing_api.post_confirm_third_party(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "991617894325358C",
  "response": "[payout-confirm-received]"
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


# Post-Decline Third Party

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

Cancels a previously submitted payout.

To confirm and send a payout, use the `/confirmThirdParty` endpoint.

```python
def post_decline_third_party(self,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ModifyRequest`](../../doc/models/modify-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ModifyResponse`](../../doc/models/modify-response.md)

## Example Usage

```python
body = ModifyRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    original_reference='9913140798220028'
)

result = reviewing_api.post_decline_third_party(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "991617894325360J",
  "response": "[payout-decline-received]"
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

