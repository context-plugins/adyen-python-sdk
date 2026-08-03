# Directdebitmandates

```python
directdebitmandates_api = client.directdebitmandates
```

## Class Name

`DirectdebitmandatesApi`

## Methods

* [Get-Mandates](../../doc/controllers/directdebitmandates.md#get-mandates)
* [Get-Mandates-Mandate Id](../../doc/controllers/directdebitmandates.md#get-mandates-mandate-id)
* [Patch-Mandates-Mandate Id](../../doc/controllers/directdebitmandates.md#patch-mandates-mandate-id)
* [Post-Mandates-Mandate Id-Cancel](../../doc/controllers/directdebitmandates.md#post-mandates-mandate-id-cancel)


# Get-Mandates

Returns a list of all [direct debit mandates](https://docs.adyen.com/business-accounts/accept-direct-debits-uk) created for a business account.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_mandates(self,
                balance_account_id=None,
                payment_instrument_id=None,
                cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Query, Optional | The unique identifier of the balance account linked to the payment instrument. |
| `payment_instrument_id` | `str` | Query, Optional | The unique identifier of the payment instrument linked to the mandate. |
| `cursor` | `str` | Query, Optional | The pagination cursor returned in a previous GET `/mandates` request. |

## Response Type

**200**: OK - The request has succeeded

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListMandatesResponse`](../../doc/models/list-mandates-response.md).

## Example Usage

```python
result = direct_debit_mandates_api.get_mandates()

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`Mandates401ErrorException`](../../doc/models/mandates-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`Mandates403ErrorException`](../../doc/models/mandates-403-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`Mandates422ErrorException`](../../doc/models/mandates-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`Mandates500ErrorException`](../../doc/models/mandates-500-error-exception.md) |


# Get-Mandates-Mandate Id

Returns the details of the specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_mandates_mandate_id(self,
                           mandate_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |

## Response Type

**200**: OK - The request has succeeded

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`Mandate`](../../doc/models/mandate.md).

## Example Usage

```python
mandate_id = 'mandateId8'

result = direct_debit_mandates_api.get_mandates_mandate_id(mandate_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`Mandates401ErrorException`](../../doc/models/mandates-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`Mandates403ErrorException`](../../doc/models/mandates-403-error-exception.md) |
| 404 | The mandate was not found. | [`Mandates404ErrorException`](../../doc/models/mandates-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`Mandates422ErrorException`](../../doc/models/mandates-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`Mandates500ErrorException`](../../doc/models/mandates-500-error-exception.md) |


# Patch-Mandates-Mandate Id

Amend the specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_mandates_mandate_id(self,
                             mandate_id,
                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |
| `body` | [`MandateUpdate`](../../doc/models/mandate-update.md) | Body, Required | - |

## Response Type

**202**: Accepted - The request has been accepted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
mandate_id = 'mandateId8'

body = MandateUpdate()

result = direct_debit_mandates_api.patch_mandates_mandate_id(
    mandate_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`Mandates401ErrorException`](../../doc/models/mandates-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`Mandates403ErrorException`](../../doc/models/mandates-403-error-exception.md) |
| 404 | The mandate was not found | [`Mandates404ErrorException`](../../doc/models/mandates-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`Mandates422ErrorException`](../../doc/models/mandates-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`Mandates500ErrorException`](../../doc/models/mandates-500-error-exception.md) |


# Post-Mandates-Mandate Id-Cancel

Cancel a specified [direct debit mandate](https://docs.adyen.com/business-accounts/accept-direct-debits-uk).

:information_source: **Note** This endpoint does not require authentication.

```python
def post_mandates_mandate_id_cancel(self,
                                   mandate_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mandate_id` | `str` | Template, Required | The unique identifier of the mandate. |

## Response Type

**202**: Accepted - The request has been accepted

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
mandate_id = 'mandateId8'

result = direct_debit_mandates_api.post_mandates_mandate_id_cancel(mandate_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`MandatesCancel401ErrorException`](../../doc/models/mandates-cancel-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`MandatesCancel403ErrorException`](../../doc/models/mandates-cancel-403-error-exception.md) |
| 404 | The mandate was not found. | [`MandatesCancel404ErrorException`](../../doc/models/mandates-cancel-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`MandatesCancel422ErrorException`](../../doc/models/mandates-cancel-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`MandatesCancel500ErrorException`](../../doc/models/mandates-cancel-500-error-exception.md) |

