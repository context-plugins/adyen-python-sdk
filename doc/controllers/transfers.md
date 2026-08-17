# Transfers

```python
transfers_api = client.transfers
```

## Class Name

`TransfersApi`

## Methods

* [Get-Transfers](../../doc/controllers/transfers.md#get-transfers)
* [Post-Transfers](../../doc/controllers/transfers.md#post-transfers)
* [Post-Transfers-Approve](../../doc/controllers/transfers.md#post-transfers-approve)
* [Post-Transfers-Cancel](../../doc/controllers/transfers.md#post-transfers-cancel)
* [Get-Transfers-Id](../../doc/controllers/transfers.md#get-transfers-id)
* [Post-Transfers-Transfer Id-Returns](../../doc/controllers/transfers.md#post-transfers-transfer-id-returns)


# Get-Transfers

Returns all the transfers related to a balance account, account holder, or balance platform.

When making this request, you must include at least one of the following:

- `balanceAccountId`
- `accountHolderId`
- `balancePlatform`.

This endpoint supports cursor-based pagination. The response returns the first page of results, and returns links to the next and previous pages when applicable. You can use the links to page through the results.

```python
def get_transfers(self,
                 created_since,
                 created_until,
                 balance_platform=None,
                 account_holder_id=None,
                 balance_account_id=None,
                 payment_instrument_id=None,
                 reference=None,
                 category=None,
                 sort_order=None,
                 cursor=None,
                 limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_since` | `datetime` | Query, Required | Only include transfers that have been created on or after this point in time. The value must be in ISO 8601 format and not earlier than 6 months before the `createdUntil` date. For example, **2021-05-30T15:07:40Z**. |
| `created_until` | `datetime` | Query, Required | Only include transfers that have been created on or before this point in time. The value must be in ISO 8601 format and not later than 6 months after the `createdSince` date. For example, **2021-05-30T15:07:40Z**. |
| `balance_platform` | `str` | Query, Optional | The unique identifier of the [balance platform](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balancePlatforms/{id}__queryParam_id).<br><br>Required if you don't provide a `balanceAccountId` or `accountHolderId`. |
| `account_holder_id` | `str` | Query, Optional | The unique identifier of the [account holder](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/accountHolders/{id}__queryParam_id).<br><br>Required if you don't provide a `balanceAccountId` or `balancePlatform`.<br><br>If you provide a `balanceAccountId`, the `accountHolderId` must be related to the `balanceAccountId`. |
| `balance_account_id` | `str` | Query, Optional | The unique identifier of the [balance account](https://docs.adyen.com/api-explorer/#/balanceplatform/latest/get/balanceAccounts/{id}__queryParam_id).<br><br>Required if you don't provide an `accountHolderId` or `balancePlatform`.<br><br>If you provide an `accountHolderId`, the `balanceAccountId` must be related to the `accountHolderId`. |
| `payment_instrument_id` | `str` | Query, Optional | The unique identifier of the [payment instrument](https://docs.adyen.com/api-explorer/balanceplatform/latest/get/paymentInstruments/_id_).<br><br>To use this parameter, you must also provide a `balanceAccountId`, `accountHolderId`, or `balancePlatform`.<br><br>The `paymentInstrumentId` must be related to the `balanceAccountId` or `accountHolderId` that you provide. |
| `reference` | `str` | Query, Optional | The reference you provided in the POST [/transfers](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers) request |
| `category` | [`Category2Enum`](../../doc/models/category-2-enum.md) | Query, Optional | The category of the transfer.<br><br>Possible values:<br><br>- **bank**: A transfer involving a [transfer instrument](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments#responses-200-id) or a bank account.<br><br>- **card**: A transfer involving a third-party card.<br><br>- **internal**: A transfer between [balance accounts](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts#responses-200-id) within your platform.<br><br>- **issuedCard**: A transfer initiated by an Adyen-issued card.<br><br>- **platformPayment**: Funds movements related to payments that are acquired for your users.<br><br>- **topUp**: An incoming transfer initiated by your user to top up their balance account. |
| `sort_order` | [`SortOrderEnum`](../../doc/models/sort-order-enum.md) | Query, Optional | Determines the sort order of the returned transfers. The sort order is based on the creation date of the transfers.<br><br>Possible values:<br><br>- **asc**: Ascending order, from oldest to most recent.<br><br>- **desc**: Descending order, from most recent to oldest.<br><br>Default value: **asc**. |
| `cursor` | `str` | Query, Optional | The `cursor` returned in the links of the previous response. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page. |

## Response Type

**200**: OK - the request has succeeded.

[`FindTransfersResponse`](../../doc/models/find-transfers-response.md)

## Example Usage

```python
created_since = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

created_until = dateutil.parser.parse('2016-03-13T12:52:32.123Z')

result = transfers_api.get_transfers(
    created_since,
    created_until
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2021-05-03T15:20:06+02:00",
      "id": "1W1UG35QQEBJLHZ8",
      "accountHolder": {
        "description": "S. Eller - Staff 123",
        "id": "AH32272223222B5CZW6QZ2V34"
      },
      "amount": {
        "currency": "EUR",
        "value": 5400
      },
      "balanceAccount": {
        "description": "My Balance Account",
        "id": "BA3227C223222B5B9SCR82TMV"
      },
      "category": "internal",
      "categoryData": {
        "type": "internal"
      },
      "counterparty": {
        "balanceAccountId": "BA00000000000000000000001"
      },
      "description": "Your description",
      "direction": "outgoing",
      "reason": "approved",
      "reference": "312M2060T6S4UOIF",
      "status": "booked",
      "balances": [
        {
          "balance": -5400,
          "currency": "EUR",
          "received": 0,
          "reserved": 0
        }
      ],
      "events": [
        {
          "bookingDate": "2021-05-03T14:53:39+01:00",
          "id": "EVJN4233Q22322375JQ72V55G92ZXF",
          "mutations": [
            {
              "currency": "EUR",
              "received": -5400
            }
          ],
          "status": "received",
          "type": "accounting",
          "valueDate": "2021-05-03T14:53:39+01:00"
        },
        {
          "bookingDate": "2021-05-03T14:53:39+01:00",
          "id": "EVJN4233Q22322375JQ72V55GB4TPV",
          "mutations": [
            {
              "currency": "EUR",
              "received": 5400,
              "reserved": -5400
            }
          ],
          "status": "authorised",
          "type": "accounting",
          "valueDate": "2021-05-03T14:53:39+01:00"
        },
        {
          "bookingDate": "2021-05-03T14:53:39+01:00",
          "id": "EVJN4233Q22322375JQ72V55GD53HZ",
          "mutations": [
            {
              "balance": -5400,
              "currency": "EUR",
              "received": 0,
              "reserved": 5400
            }
          ],
          "status": "booked",
          "transactionId": "EVJN4233Q22322375JQ72V55GD53HZEUR",
          "type": "accounting",
          "valueDate": "2021-05-03T14:53:39+01:00"
        }
      ],
      "sequenceNumber": 3,
      "type": "internalTransfer"
    },
    {
      "balancePlatform": "YOUR_BALANCE_PLATFORM",
      "creationDate": "2021-08-02T15:20:06+02:00",
      "id": "312M2060T5Z3YWYQ",
      "accountHolder": {
        "description": "S. Doe - Staff 124",
        "id": "AH443397232222B5CZW6QZ2V34"
      },
      "amount": {
        "currency": "EUR",
        "value": 15000
      },
      "balanceAccount": {
        "description": "My Balance Account",
        "id": "BA3227C2582222B5B9SCR82VHM"
      },
      "category": "internal",
      "categoryData": {
        "type": "internal"
      },
      "counterparty": {
        "balanceAccountId": "BA00000000000000000000001"
      },
      "description": "Your description",
      "direction": "outgoing",
      "reason": "approved",
      "reference": "312M2060T6S4UOIF",
      "status": "booked",
      "balances": [
        {
          "balance": -15000,
          "currency": "EUR",
          "received": 0,
          "reserved": 0
        }
      ],
      "events": [
        {
          "bookingDate": "2021-08-02T14:53:39+01:00",
          "id": "EVJN4233Q22322375JQ72V55G92ZXF",
          "mutations": [
            {
              "currency": "EUR",
              "received": -15000
            }
          ],
          "status": "received",
          "type": "accounting",
          "valueDate": "2021-08-02T14:53:39+01:00"
        },
        {
          "bookingDate": "2021-08-02T14:53:39+01:00",
          "id": "EVJN4233Q22322375JQ72V55GB4TPV",
          "mutations": [
            {
              "currency": "EUR",
              "received": 15000,
              "reserved": -15000
            }
          ],
          "status": "authorised",
          "type": "accounting",
          "valueDate": "2021-08-02T14:53:39+01:00"
        },
        {
          "bookingDate": "2021-08-02T14:53:39+01:00",
          "id": "EVASDFOUPASFDHSADFA6SN65FG6TD53HZ",
          "mutations": [
            {
              "balance": -15000,
              "currency": "EUR",
              "received": 0,
              "reserved": 15000
            }
          ],
          "status": "booked",
          "transactionId": "EVJN4233Q22322375JQ6SN65FG6TFTEUR",
          "type": "accounting",
          "valueDate": "2021-08-02T14:53:39+01:00"
        }
      ],
      "sequenceNumber": 3,
      "type": "internalTransfer"
    }
  ],
  "_links": {
    "next": {
      "href": "https://balanceplatform-api-test.adyen.com/btl/v4/transfers?balancePlatform=YOUR_BALANCE_PLATFORM&createdUntil=2021-12-21T00%3A00%3A00Z&createdSince=2021-03-21T00%3A00%3A00Z&limit=2&cursor=S2B-TSAjOkIrYlIlbjdqe0RreHRyM32lKRSxubXBHRkhHL2E32XitQQz5SfzpucD5HbHwpM1p6NDR1eXVQLFF6MmY33J32sobDxQYT90MHIud1hwLnd6JitcX32xJ"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |


# Post-Transfers

> Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.

Starts a request to transfer funds to:

- [Balance accounts](https://docs.adyen.com/api-explorer/balanceplatform/latest/post/balanceAccounts)
- [Transfer instruments](https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments)
- [Third-party bank accounts](https://docs.adyen.com/payouts/payout-service/pay-out-to-bank-accounts)
- [Third-party cards](https://docs.adyen.com/payouts/payout-service/pay-out-to-cards)

Adyen sends the outcome of the transfer request through webhooks.

To use this endpoint:

- Your API credential must have the **TransferService Webservice Initiate** [role](https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3).
- The account holder must have the required [capabilities](https://docs.adyen.com/platforms/verification-overview/capabilities).

Reach out to your Adyen contact to set up these permissions.

```python
def post_transfers(self,
                  idempotency_key=None,
                  www_authenticate=None,
                  body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `www_authenticate` | `str` | Header, Optional | Header for authenticating through SCA |
| `body` | [`TransferInfo`](../../doc/models/transfer-info.md) | Body, Optional | - |

## Response Type

**200**: OK - The request has been accepted for processing, but has not been completed.

[`Transfer`](../../doc/models/transfer.md)

## Example Usage

```python
body = TransferInfo(
    amount=Amount17(
        currency='EUR',
        value=110000
    ),
    category=Category3Enum.BANK,
    counterparty=CounterpartyInfoV31(
        bank_account=BankAccountV31(
            account_holder=PartyIdentification3(
                address=Address12(
                    country='US',
                    city='San Francisco',
                    line_1='274',
                    line_2='Brannan Street',
                    postal_code='94678',
                    state_or_province='CA'
                ),
                full_name='A. Klaassen'
            ),
            account_identification=NumberAndBicAccountIdentification(
                account_number='123456789',
                bic='BOFAUS3NXXX'
            )
        )
    ),
    balance_account_id='BAB8B2C3D4E5F6G7H8D9J6GD4',
    description='Your description for the transfer',
    priority=Priority1Enum.CROSSBORDER,
    reference='Your internal reference for the transfer',
    reference_for_beneficiary='Your-reference-sent-to-the-beneficiary'
)

result = transfers_api.post_transfers(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |


# Post-Transfers-Approve

Initiates the approval of a list of transfers that triggered an additional [review](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review). Adyen sends the outcome of the approval request through webhooks.

To use this endpoint:

- Your API credential must have the **TransferService Approve** [role](https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3).
- The account holder must have the required [capabilities](https://docs.adyen.com/platforms/verification-overview/capabilities).

Reach out to your Adyen contact to set up these permissions.

```python
def post_transfers_approve(self,
                          idempotency_key=None,
                          www_authenticate=None,
                          body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `www_authenticate` | `str` | Header, Optional | Header for authenticating through SCA |
| `body` | [`ApproveTransfersRequest`](../../doc/models/approve-transfers-request.md) | Body, Optional | - |

## Response Type

**200**: No Content - look at the actual response code for the status of the request.

`Any`

## Example Usage

```python
body = ApproveTransfersRequest(
    transfer_ids=[
        'APUFHASUDF4AS',
        '407ASFPUAHSFA'
    ]
)

result = transfers_api.post_transfers_approve(
    body=body
)
print(result)
```

## Example Response

```
{}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |


# Post-Transfers-Cancel

Initiates the cancellation of a list of transfers that triggered an additional [review](https://docs.adyen.com/api-explorer/transfers/latest/post/transfers#request-review). Adyen sends the outcome of the cancel request through webhooks.

To use this endpoint:

- Your API credential must have the **TransferService Approve** [role](https://docs.adyen.com/platforms/manage-access/webservice-roles/?tab=transfers_3).
- The account holder must have the required [capabilities](https://docs.adyen.com/platforms/verification-overview/capabilities).

Reach out to your Adyen contact to set up these permissions.

```python
def post_transfers_cancel(self,
                         idempotency_key=None,
                         body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`CancelTransfersRequest`](../../doc/models/cancel-transfers-request.md) | Body, Optional | - |

## Response Type

**200**: No Content - look at the actual response code for the status of the request.

`Any`

## Example Usage

```python
body = CancelTransfersRequest(
    transfer_ids=[
        'APUFHASUDF4AS',
        '407ASFPUAHSFA'
    ]
)

result = transfers_api.post_transfers_cancel(
    body=body
)
print(result)
```

## Example Response

```
{}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |


# Get-Transfers-Id

Returns the details of a specified transfer.

```python
def get_transfers_id(self,
                    id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | Unique identifier of the transfer. |

## Response Type

**200**: OK - the request has succeeded.

[`TransferData`](../../doc/models/transfer-data.md)

## Example Usage

```python
id = 'id0'

result = transfers_api.get_transfers_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "creationDate": "2021-05-03T15:20:06+02:00",
  "id": "1W1UG35QQEBJLHZ8",
  "accountHolder": {
    "description": "S. Eller - Staff 123",
    "id": "AH32272223222B5CZW6QZ2V34"
  },
  "amount": {
    "currency": "EUR",
    "value": 5400
  },
  "balanceAccount": {
    "description": "My Balance Account",
    "id": "BA3227C223222B5B9SCR82TMV"
  },
  "category": "internal",
  "categoryData": {
    "type": "internal"
  },
  "counterparty": {
    "balanceAccountId": "BA00000000000000000000001"
  },
  "description": "Your description",
  "direction": "outgoing",
  "reason": "approved",
  "reference": "312M2060T6S4UOIF",
  "status": "booked",
  "balances": [
    {
      "balance": -5400,
      "currency": "EUR",
      "received": 0,
      "reserved": 0
    }
  ],
  "events": [
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55G92ZXF",
      "mutations": [
        {
          "currency": "EUR",
          "received": -5400
        }
      ],
      "status": "received",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    },
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55GB4TPV",
      "mutations": [
        {
          "currency": "EUR",
          "received": 5400,
          "reserved": -5400
        }
      ],
      "status": "authorised",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    },
    {
      "bookingDate": "2021-05-03T14:53:39+01:00",
      "id": "EVJN4233Q22322375JQ72V55GD53HZ",
      "mutations": [
        {
          "balance": -5400,
          "currency": "EUR",
          "received": 0,
          "reserved": 5400
        }
      ],
      "status": "booked",
      "transactionId": "EVJN4233Q22322375JQ72V55GD53HZEUR",
      "type": "accounting",
      "valueDate": "2021-05-03T14:53:39+01:00"
    }
  ],
  "sequenceNumber": 3,
  "type": "internalTransfer"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |


# Post-Transfers-Transfer Id-Returns

Initiates the return of previously transferred funds without creating a new `transferId`.

```python
def post_transfers_transfer_id_returns(self,
                                      transfer_id,
                                      idempotency_key=None,
                                      body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `transfer_id` | `str` | Template, Required | The unique identifier of the transfer to be returned. |
| `idempotency_key` | `str` | Header, Optional | A unique identifier for the message with a maximum of 64 characters (we recommend a UUID). |
| `body` | [`ReturnTransferRequest`](../../doc/models/return-transfer-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ReturnTransferResponse`](../../doc/models/return-transfer-response.md)

## Example Usage

```python
transfer_id = 'transferId8'

body = ReturnTransferRequest(
    amount=Amount17(
        currency='EUR',
        value=189
    ),
    reference='Your internal reference for the return'
)

result = transfers_api.post_transfers_transfer_id_returns(
    transfer_id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "1W1UG35QQEBJLHZ8",
  "reference": "Your internal reference for the return",
  "status": "Authorised",
  "transferId": "1W1UG35U8A9J5ZLG"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`TransferServiceRestServiceErrorException`](../../doc/models/transfer-service-rest-service-error-exception.md) |

