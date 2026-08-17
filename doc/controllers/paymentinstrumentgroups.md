# Paymentinstrumentgroups

```python
paymentinstrumentgroups_api = client.paymentinstrumentgroups
```

## Class Name

`PaymentinstrumentgroupsApi`

## Methods

* [Post-Payment Instrument Groups](../../doc/controllers/paymentinstrumentgroups.md#post-payment-instrument-groups)
* [Get-Payment Instrument Groups-Id](../../doc/controllers/paymentinstrumentgroups.md#get-payment-instrument-groups-id)
* [Get-Payment Instrument Groups-Id-Transaction Rules](../../doc/controllers/paymentinstrumentgroups.md#get-payment-instrument-groups-id-transaction-rules)


# Post-Payment Instrument Groups

Creates a payment instrument group to associate and group payment instrument resources together. You can apply a transaction rule to a payment instrument group.

```python
def post_payment_instrument_groups(self,
                                  body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentInstrumentGroupInfo`](../../doc/models/payment-instrument-group-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentInstrumentGroup`](../../doc/models/payment-instrument-group.md)

## Example Usage

```python
body = PaymentInstrumentGroupInfo(
    balance_platform='YOUR_BALANCE_PLATFORM',
    tx_variant='mc'
)

result = payment_instrument_groups_api.post_payment_instrument_groups(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "txVariant": "mc",
  "id": "PG32272223222H5J4DCRVC9DH"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Payment Instrument Groups-Id

Returns the details of a payment instrument group.

```python
def get_payment_instrument_groups_id(self,
                                    id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the payment instrument group. |

## Response Type

**200**: OK - the request has succeeded.

[`PaymentInstrumentGroup`](../../doc/models/payment-instrument-group.md)

## Example Usage

```python
id = 'id0'

result = payment_instrument_groups_api.get_payment_instrument_groups_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "txVariant": "mc",
  "id": "PG3227C223222B5CMD3FJFKGZ"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Payment Instrument Groups-Id-Transaction Rules

Returns a list of all the transaction rules associated with a payment instrument group.

```python
def get_payment_instrument_groups_id_transaction_rules(self,
                                                      id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the payment instrument group. |

## Response Type

**200**: OK - the request has succeeded.

[`TransactionRulesResponse`](../../doc/models/transaction-rules-response.md)

## Example Usage

```python
id = 'id0'

result = payment_instrument_groups_api.get_payment_instrument_groups_id_transaction_rules(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "transactionRules": [
    {
      "aggregationLevel": "paymentInstrument",
      "description": "Up to 1000 EUR per card for the last 12 hours",
      "entityKey": {
        "entityReference": "PG3227C223222C5GXR3M5592Q",
        "entityType": "paymentInstrumentGroup"
      },
      "interval": {
        "duration": {
          "unit": "hours",
          "value": 12
        },
        "timeZone": "UTC",
        "type": "sliding"
      },
      "outcomeType": "hardBlock",
      "reference": "YOUR_REFERENCE_2918A",
      "requestType": "authorization",
      "ruleRestrictions": {
        "totalAmount": {
          "operation": "greaterThan",
          "value": {
            "currency": "EUR",
            "value": 100000
          }
        }
      },
      "status": "inactive",
      "type": "velocity",
      "id": "TR3227C223222C5GXR3XP596N"
    },
    {
      "aggregationLevel": "paymentInstrument",
      "description": "NL only",
      "entityKey": {
        "entityReference": "PG3227C223222C5GXR3M5592Q",
        "entityType": "paymentInstrumentGroup"
      },
      "interval": {
        "duration": {
          "unit": "hours",
          "value": 12
        },
        "timeZone": "UTC",
        "type": "sliding"
      },
      "outcomeType": "hardBlock",
      "reference": "myRule12345",
      "requestType": "authorization",
      "ruleRestrictions": {
        "totalAmount": {
          "operation": "greaterThan",
          "value": {
            "currency": "EUR",
            "value": 100000
          }
        }
      },
      "status": "inactive",
      "type": "velocity",
      "id": "TR3227C223222C5GXR3WC595H"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

