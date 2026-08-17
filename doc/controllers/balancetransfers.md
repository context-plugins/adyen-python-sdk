# Balancetransfers

```python
balancetransfers_api = client.balancetransfers
```

## Class Name

`BalancetransfersApi`


# Post-Balance Transfers

Performs a balance transfer between merchant accounts. The following conditions must be met before you can successfully transfer balances:

* The source and destination merchant accounts must be under the same company account and legal entity.
* The source merchant account must have sufficient funds.
* The source and destination merchant accounts must have at least one common processing currency.\n\n
  When sending multiple API requests with the same source and destination merchant accounts, send the requests sequentially and *not* in parallel. Some requests may not be processed if the requests are sent in parallel.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_transfers(self,
                          body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BalanceTransferRequest`](../../doc/models/balance-transfer-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

[`BalanceTransferResponse`](../../doc/models/balance-transfer-response.md)

## Example Usage

```python
body = BalanceTransferRequest(
    amount=Amount17(
        currency='EUR',
        value=3000
    ),
    from_merchant='SOURCE_MERCHANT_ACCOUNT',
    to_merchant='DESTINATION_MERCHANT_ACCOUNT',
    mtype=BalanceTransferType2Enum.ADJUSTMENT,
    reference='Your reference for the balance transfer.'
)

result = balance_transfers_api.post_balance_transfers(body)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "createdAt": "2025-10-27T07:06:15+00:00",
  "pspReference": "993617895204576J"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

