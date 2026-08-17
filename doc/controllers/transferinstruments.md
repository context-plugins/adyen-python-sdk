# Transferinstruments

```python
transferinstruments_api = client.transferinstruments
```

## Class Name

`TransferinstrumentsApi`

## Methods

* [Post-Transfer Instruments](../../doc/controllers/transferinstruments.md#post-transfer-instruments)
* [Get-Transfer Instruments-Id](../../doc/controllers/transferinstruments.md#get-transfer-instruments-id)
* [Delete-Transfer Instruments-Id](../../doc/controllers/transferinstruments.md#delete-transfer-instruments-id)
* [Patch-Transfer Instruments-Id](../../doc/controllers/transferinstruments.md#patch-transfer-instruments-id)


# Post-Transfer Instruments

Creates a transfer instrument.

A transfer instrument is a bank account that a legal entity owns. Adyen performs verification checks on the transfer instrument as required by payment industry regulations. We inform you of the verification results through webhooks or API responses.

When the transfer instrument passes the verification checks, you can start sending funds from the balance platform to the transfer instrument (such as payouts).

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_transfer_instruments(self,
                             x_requested_verification_code=None,
                             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_requested_verification_code` | `str` | Header, Optional | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. |
| `body` | [`TransferInstrumentInfo`](../../doc/models/transfer-instrument-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`TransferInstrument`](../../doc/models/transfer-instrument.md)

## Example Usage

```python
body = TransferInstrumentInfo(
    bank_account=BankAccountInfo1(
        account_identification=IbanAccountIdentification(
            iban='NL62ABNA0000000123'
        )
    ),
    legal_entity_id='LE00000000000000000000001',
    mtype=Type221Enum.BANKACCOUNT
)

result = transfer_instruments_api.post_transfer_instruments(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "bankAccount": {
    "accountIdentification": {
      "type": "iban",
      "iban": "NL62ABNA0000000123"
    },
    "countryCode": "NL",
    "trustedSource": false
  },
  "legalEntityId": "LE00000000000000000000001",
  "type": "bankAccount",
  "capabilities": {
    "sendToTransferInstrument": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    }
  },
  "id": "SE322KH223222F5GXZFNM3BGP"
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


# Get-Transfer Instruments-Id

Returns the details of a transfer instrument.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_transfer_instruments_id(self,
                               id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the transfer instrument. |

## Response Type

**200**: OK - the request has succeeded.

[`TransferInstrument`](../../doc/models/transfer-instrument.md)

## Example Usage

```python
id = 'id0'

result = transfer_instruments_api.get_transfer_instruments_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "bankAccount": {
    "accountIdentification": {
      "type": "iban",
      "iban": "NL62ABNA0000000123"
    },
    "countryCode": "NL"
  },
  "legalEntityId": "LE00000000000000000000001",
  "type": "bankAccount",
  "id": "SE322KH223222F5GXZFNM3BGP"
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


# Delete-Transfer Instruments-Id

Deletes a transfer instrument.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def delete_transfer_instruments_id(self,
                                  id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the transfer instrument to be deleted. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

`void`

## Example Usage

```python
id = 'id0'

transfer_instruments_api.delete_transfer_instruments_id(id)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Patch-Transfer Instruments-Id

Updates a transfer instrument.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def patch_transfer_instruments_id(self,
                                 id,
                                 x_requested_verification_code=None,
                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the transfer instrument. |
| `x_requested_verification_code` | `str` | Header, Optional | Use the requested verification code 0_0001 to resolve any suberrors associated with the transfer instrument. Requested verification codes can only be used in your test environment. |
| `body` | [`TransferInstrumentInfo`](../../doc/models/transfer-instrument-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`TransferInstrument`](../../doc/models/transfer-instrument.md)

## Example Usage

```python
id = 'id0'

body = TransferInstrumentInfo(
    bank_account=BankAccountInfo1(
        account_identification=IbanAccountIdentification(
            iban='NL02ABNA0123456789'
        )
    ),
    legal_entity_id='LE00000000000000000000001',
    mtype=Type221Enum.BANKACCOUNT
)

result = transfer_instruments_api.patch_transfer_instruments_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "bankAccount": {
    "accountIdentification": {
      "type": "iban",
      "iban": "NL02ABNA0123456789"
    },
    "countryCode": "NL"
  },
  "legalEntityId": "LE00000000000000000000001",
  "type": "bankAccount",
  "id": "SE322KH223222F5GXZFNM3BGP"
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

