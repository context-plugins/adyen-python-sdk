# Businesslines

```python
businesslines_api = client.businesslines
```

## Class Name

`BusinesslinesApi`

## Methods

* [Post-Business Lines](../../doc/controllers/businesslines.md#post-business-lines)
* [Get-Business Lines-Id](../../doc/controllers/businesslines.md#get-business-lines-id)
* [Delete-Business Lines-Id](../../doc/controllers/businesslines.md#delete-business-lines-id)
* [Patch-Business Lines-Id](../../doc/controllers/businesslines.md#patch-business-lines-id)


# Post-Business Lines

Creates a business line.

This resource contains information about your user's line of business, including their industry and their source of funds. Adyen uses this information to verify your users as required by payment industry regulations.Adyen informs you of the verification results through webhooks or API responses.

You can create a maximum of 200 business lines per legal entity for payment processing.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_business_lines(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BusinessLineInfo`](../../doc/models/business-line-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`BusinessLine`](../../doc/models/business-line.md)

## Example Usage

```python
body = BusinessLineInfo(
    industry_code='4531',
    legal_entity_id='LE00000000000000000000001',
    service=ServiceEnum.BANKING,
    source_of_funds=SourceOfFunds11(
        adyen_processed_funds=False,
        amount=PatchableAmountDTO(
            currency='EUR',
            value=600000
        ),
        description='Funds from my flower shop business',
        mtype=Type74Enum.BUSINESS
    ),
    web_data=[
        WebData(
            web_address='https://www.adyen.com'
        )
    ]
)

result = business_lines_api.post_business_lines(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "industryCode": "4531",
  "legalEntityId": "LE00000000000000000000001",
  "service": "banking",
  "sourceOfFunds": {
    "adyenProcessedFunds": false,
    "amount": {
      "currency": "EUR",
      "value": 600000
    },
    "description": "Funds from my flower shop business",
    "type": "business"
  },
  "webData": [
    {
      "webAddress": "https://www.adyen.com",
      "webAddressId": "SE322JV223222F5H4CQGS77V4"
    }
  ],
  "id": "SE322KT223222D5FJ7TJN2986"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Get-Business Lines-Id

Returns the detail of a business line.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_business_lines_id(self,
                         id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the business line. |

## Response Type

**200**: OK - the request has succeeded.

[`BusinessLine`](../../doc/models/business-line.md)

## Example Usage

```python
id = 'id0'

result = business_lines_api.get_business_lines_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "service": "banking",
  "industryCode": "4531",
  "legalEntityId": "LE00000000000000000000001",
  "sourceOfFunds": {
    "adyenProcessedFunds": false,
    "description": "Funds from my flower shop business",
    "type": "business"
  },
  "webData": [
    {
      "webAddress": "https://www.adyen.com",
      "webAddressId": "SE322JV223222J5H8V87B3DHN"
    }
  ],
  "id": "SE322KH223222F5GV2SQ924F6"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Delete-Business Lines-Id

Deletes a business line.

> If you delete a business line linked to a [payment method](https://docs.adyen.com/development-resources/paymentmethodvariant#management-api), it can affect your merchant account's ability to use the [payment method](https://docs.adyen.com/api-explorer/Management/latest/post/merchants/_merchantId_/paymentMethodSettings). The business line is removed from all linked merchant accounts.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def delete_business_lines_id(self,
                            id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the business line to be deleted. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
id = 'id0'

business_lines_api.delete_business_lines_id(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Patch-Business Lines-Id

Updates a business line.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def patch_business_lines_id(self,
                           id,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the business line. |
| `body` | [`BusinessLineInfoUpdate`](../../doc/models/business-line-info-update.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`BusinessLine`](../../doc/models/business-line.md)

## Example Usage

```python
id = 'id0'

body = BusinessLineInfoUpdate(
    industry_code='55',
    web_data=[
        WebData(
            web_address='https://www.example.com'
        )
    ]
)

result = business_lines_api.patch_business_lines_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "service": "banking",
  "industryCode": "55",
  "legalEntityId": "LE00000000000000000000001",
  "sourceOfFunds": {
    "adyenProcessedFunds": false,
    "description": "Funds from my flower shop business",
    "type": "business"
  },
  "webData": [
    {
      "webAddress": "https://www.example.com",
      "webAddressId": "SE966LI345672J5H8V87B3FGH"
    }
  ],
  "id": "SE322JV223222F5GVGMLNB83F"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |

