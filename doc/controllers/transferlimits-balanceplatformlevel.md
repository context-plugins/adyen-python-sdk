# Transferlimits-Balanceplatformlevel

```python
transferlimits_balanceplatformlevel_api = client.transferlimits_balanceplatformlevel
```

## Class Name

`TransferlimitsBalanceplatformlevelApi`

## Methods

* [Get-Balance Platforms-Id-Transfer Limits](../../doc/controllers/transferlimits-balanceplatformlevel.md#get-balance-platforms-id-transfer-limits)
* [Post-Balance Platforms-Id-Transfer Limits](../../doc/controllers/transferlimits-balanceplatformlevel.md#post-balance-platforms-id-transfer-limits)
* [Get-Balance Platforms-Id-Transfer Limits-Transfer Limit Id](../../doc/controllers/transferlimits-balanceplatformlevel.md#get-balance-platforms-id-transfer-limits-transfer-limit-id)
* [Delete-Balance Platforms-Id-Transfer Limits-Transfer Limit Id](../../doc/controllers/transferlimits-balanceplatformlevel.md#delete-balance-platforms-id-transfer-limits-transfer-limit-id)


# Get-Balance Platforms-Id-Transfer Limits

Filter and view the transfer limits configured for your balance platform using the balance platform's unique `id` and the available query parameters.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_id_transfer_limits(self,
                                            id,
                                            scope=None,
                                            transfer_type=None,
                                            status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `scope` | [`Scope`](../../doc/models/scope.md) | Query, Optional | The scope to which the transfer limit applies. Possible values:<br><br>* **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.<br>* **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| `transfer_type` | [`TransferType`](../../doc/models/transfer-type.md) | Query, Optional | The type of transfer to which the limit applies. Possible values:<br><br>* **instant**: the limit applies to transfers with an **instant** priority.<br>* **all**: the limit applies to all transfers, regardless of priority. |
| `status` | [`LimitStatus`](../../doc/models/limit-status.md) | Query, Optional | The status of the transfer limit. Possible values:<br><br>* **active**: the limit is currently active.<br>* **inactive**: the limit is currently inactive.<br>* **pendingSCA**: the limit is pending until your user performs SCA.<br>* **scheduled**: the limit is scheduled to become active at a future date. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferLimitListResponse`](../../doc/models/transfer-limit-list-response.md).

## Example Usage

```python
id = 'id0'

result = transfer_limits_balance_platform_level_api.get_balance_platforms_id_transfer_limits(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "transferLimits": [
    {
      "amount": {
        "currency": "EUR",
        "value": 10000
      },
      "endsAt": "2026-08-13T23:00:00+01:00",
      "id": "TRLI00000000000000000000000001",
      "limitStatus": "active",
      "reference": "Your reference for the transfer limit",
      "scaInformation": {
        "exemption": "initialLimit",
        "status": "notPerformed"
      },
      "scope": "perTransaction",
      "startsAt": "2025-08-13T23:00:00+01:00",
      "transferType": "instant"
    },
    {
      "amount": {
        "currency": "EUR",
        "value": 20000
      },
      "endsAt": "2026-08-13T23:00:00+01:00",
      "id": "TRLI00000000000000000000000002",
      "limitStatus": "active",
      "reference": "Your reference for the transfer limit",
      "scaInformation": {
        "exemption": "initialLimit",
        "status": "notPerformed"
      },
      "scope": "perTransaction",
      "startsAt": "2025-08-13T23:00:00+01:00",
      "transferType": "all"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found - One of the transfer limits could not be found. | [`BalancePlatformsTransferLimits404ErrorException`](../../doc/models/balance-platforms-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalancePlatformsTransferLimits422ErrorException`](../../doc/models/balance-platforms-transfer-limits-422-error-exception.md) |


# Post-Balance Platforms-Id-Transfer Limits

Create a transfer limit for your balance platform using the unique `id` of your balance platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_platforms_id_transfer_limits(self,
                                             id,
                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `body` | [`CreateTransferLimitRequest`](../../doc/models/create-transfer-limit-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalancePlatformsTransferLimitsResponse1`](../../doc/models/balance-platforms-transfer-limits-response-1.md).

## Example Usage

```python
id = 'id0'

body = CreateTransferLimitRequest(
    amount=Amount5(
        currency='EUR',
        value=10000
    ),
    scope=Scope.PERTRANSACTION,
    transfer_type=TransferType.ALL,
    ends_at=dateutil.parser.parse('2026-08-14T00:00:00+01:00'),
    reference='Your reference for the transfer limit',
    sca_information=CreateScaInformation(
        sca_on_approval=True
    ),
    starts_at=dateutil.parser.parse('2025-08-15T06:36:20+01:00')
)

result = transfer_limits_balance_platform_level_api.post_balance_platforms_id_transfer_limits(
    id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "amount": {
    "currency": "EUR",
    "value": 10000
  },
  "endsAt": "2026-08-13T23:00:00+01:00",
  "id": "TRLI00000000000000000000000001",
  "limitStatus": "pendingSCA",
  "reference": "Your reference for the transfer limit",
  "scaInformation": {
    "status": "pending"
  },
  "scope": "perTransaction",
  "startsAt": "2025-08-15T06:36:20+01:00",
  "transferType": "all"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found - One of the transfer limits could not be found. | [`BalancePlatformsTransferLimits404ErrorException`](../../doc/models/balance-platforms-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalancePlatformsTransferLimits422ErrorException`](../../doc/models/balance-platforms-transfer-limits-422-error-exception.md) |


# Get-Balance Platforms-Id-Transfer Limits-Transfer Limit Id

Get the details of a transfer limit using its unique `transferLimitId`.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_id_transfer_limits_transfer_limit_id(self,
                                                              id,
                                                              transfer_limit_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `transfer_limit_id` | `str` | Template, Required | The unique identifier of the transfer limit. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalancePlatformsTransferLimitsResponse1`](../../doc/models/balance-platforms-transfer-limits-response-1.md).

## Example Usage

```python
id = 'id0'

transfer_limit_id = 'transferLimitId6'

result = transfer_limits_balance_platform_level_api.get_balance_platforms_id_transfer_limits_transfer_limit_id(
    id,
    transfer_limit_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "amount": {
    "currency": "EUR",
    "value": 10000
  },
  "endsAt": "2026-08-13T23:00:00+01:00",
  "id": "TRLI00000000000000000000000001",
  "limitStatus": "active",
  "reference": "Your reference for the transfer limit",
  "scaInformation": {
    "exemption": "initialLimit",
    "status": "notPerformed"
  },
  "scope": "perTransaction",
  "startsAt": "2025-08-13T23:00:00+01:00",
  "transferType": "all"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found - One of the transfer limits could not be found. | [`BalancePlatformsTransferLimits404ErrorException`](../../doc/models/balance-platforms-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalancePlatformsTransferLimits422ErrorException`](../../doc/models/balance-platforms-transfer-limits-422-error-exception.md) |


# Delete-Balance Platforms-Id-Transfer Limits-Transfer Limit Id

Delete a scheduled or pending transfer limit using its unique `transferLimitId`. You cannot delete an active limit.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_balance_platforms_id_transfer_limits_transfer_limit_id(self,
                                                                 id,
                                                                 transfer_limit_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `transfer_limit_id` | `str` | Template, Required | The unique identifier of the transfer limit. |

## Response Type

**204**: No Content - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
id = 'id0'

transfer_limit_id = 'transferLimitId6'

result = transfer_limits_balance_platform_level_api.delete_balance_platforms_id_transfer_limits_transfer_limit_id(
    id,
    transfer_limit_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found - One of the transfer limits could not be found. | [`BalancePlatformsTransferLimits404ErrorException`](../../doc/models/balance-platforms-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalancePlatformsTransferLimits422ErrorException`](../../doc/models/balance-platforms-transfer-limits-422-error-exception.md) |

