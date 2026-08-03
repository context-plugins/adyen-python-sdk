# Transferlimits-Balanceaccountlevel

```python
transferlimits_balanceaccountlevel_api = client.transferlimits_balanceaccountlevel
```

## Class Name

`TransferlimitsBalanceaccountlevelApi`

## Methods

* [Get-Balance Accounts-Id-Transfer Limits](../../doc/controllers/transferlimits-balanceaccountlevel.md#get-balance-accounts-id-transfer-limits)
* [Post-Balance Accounts-Id-Transfer Limits](../../doc/controllers/transferlimits-balanceaccountlevel.md#post-balance-accounts-id-transfer-limits)
* [Post-Balance Accounts-Id-Transfer Limits-Approve](../../doc/controllers/transferlimits-balanceaccountlevel.md#post-balance-accounts-id-transfer-limits-approve)
* [Get-Balance Accounts-Id-Transfer Limits-Current](../../doc/controllers/transferlimits-balanceaccountlevel.md#get-balance-accounts-id-transfer-limits-current)
* [Get-Balance Accounts-Id-Transfer Limits-Transfer Limit Id](../../doc/controllers/transferlimits-balanceaccountlevel.md#get-balance-accounts-id-transfer-limits-transfer-limit-id)
* [Delete-Balance Accounts-Id-Transfer Limits-Transfer Limit Id](../../doc/controllers/transferlimits-balanceaccountlevel.md#delete-balance-accounts-id-transfer-limits-transfer-limit-id)


# Get-Balance Accounts-Id-Transfer Limits

Filter and view the transfer limits configured for a balance account using the balance account's unique `id` and the available query parameters.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_id_transfer_limits(self,
                                           id,
                                           scope=None,
                                           transfer_type=None,
                                           status=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `scope` | [`Scope`](../../doc/models/scope.md) | Query, Optional | The scope to which the transfer limit applies. Possible values:<br><br>* **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.<br>* **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| `transfer_type` | [`TransferType`](../../doc/models/transfer-type.md) | Query, Optional | The type of transfer to which the limit applies. Possible values:<br><br>* **instant**: the limit applies to transfers with an **instant** priority.<br>* **all**: the limit applies to all transfers, regardless of priority. |
| `status` | [`LimitStatus`](../../doc/models/limit-status.md) | Query, Optional | The status of the transfer limit. Possible values:<br><br>* **active**: the limit is currently active.<br>* **inactive**: the limit is currently inactive.<br>* **pendingSCA**: the limit is pending until your user performs SCA.<br>* **scheduled**: the limit is scheduled to become active at a future date. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferLimitListResponse`](../../doc/models/transfer-limit-list-response.md).

## Example Usage

```python
id = 'id0'

result = transfer_limits_balance_account_level_api.get_balance_accounts_id_transfer_limits(id)

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
| 404 | Not found - One of the transfer limits could not be found. | [`BalanceAccountsTransferLimits404ErrorException`](../../doc/models/balance-accounts-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimits422ErrorException`](../../doc/models/balance-accounts-transfer-limits-422-error-exception.md) |


# Post-Balance Accounts-Id-Transfer Limits

Create a transfer limit for your balance account using the unique `id` of your balance account.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_accounts_id_transfer_limits(self,
                                            id,
                                            body,
                                            www_authenticate=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`CreateTransferLimitRequest`](../../doc/models/create-transfer-limit-request.md) | Body, Required | - |
| `www_authenticate` | `str` | Header, Optional | Header for authenticating through SCA |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountsTransferLimitsResponse1`](../../doc/models/balance-accounts-transfer-limits-response-1.md).

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

result = transfer_limits_balance_account_level_api.post_balance_accounts_id_transfer_limits(
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
| 400 | Bad Request - The input is invalid, or no registered device for SCA was found. | [`BalanceAccountsTransferLimits400ErrorException`](../../doc/models/balance-accounts-transfer-limits-400-error-exception.md) |
| 401 | Unauthorized - Authentication required via Strong Customer Authentication (SCA). The client must resolve the provided challenge. | [`BalanceAccountsTransferLimits401ErrorException`](../../doc/models/balance-accounts-transfer-limits-401-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimits422ErrorException`](../../doc/models/balance-accounts-transfer-limits-422-error-exception.md) |


# Post-Balance Accounts-Id-Transfer Limits-Approve

Approve transfer limits that are pending SCA authentication.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_accounts_id_transfer_limits_approve(self,
                                                    id,
                                                    body,
                                                    www_authenticate=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`ApproveTransferLimitRequest`](../../doc/models/approve-transfer-limit-request.md) | Body, Required | - |
| `www_authenticate` | `str` | Header, Optional | Header for authenticating using SCA. |

## Response Type

**204**: No Content - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
id = 'id0'

body = ApproveTransferLimitRequest(
    transfer_limit_ids=[
        'TRLI00000000000000000000000001',
        'TRLI00000000000000000000000002'
    ]
)

result = transfer_limits_balance_account_level_api.post_balance_accounts_id_transfer_limits_approve(
    id,
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
| 401 | Unauthorized - Authentication required via Strong Customer Authentication (SCA). The client must resolve the provided challenge. | [`BalanceAccountsTransferLimitsApprove401ErrorException`](../../doc/models/balance-accounts-transfer-limits-approve-401-error-exception.md) |
| 404 | Not found - One of the transfer limits could not be found. | [`BalanceAccountsTransferLimitsApprove404ErrorException`](../../doc/models/balance-accounts-transfer-limits-approve-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimitsApprove422ErrorException`](../../doc/models/balance-accounts-transfer-limits-approve-422-error-exception.md) |


# Get-Balance Accounts-Id-Transfer Limits-Current

Get all transfer limits that currently apply to a balance account using the unique `id` of the balance account.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_id_transfer_limits_current(self,
                                                   id,
                                                   scope=None,
                                                   transfer_type=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `scope` | [`Scope`](../../doc/models/scope.md) | Query, Optional | The scope to which the transfer limit applies. Possible values:<br><br>* **perTransaction**: you set a maximum amount for each transfer made from the balance account or balance platform.<br>* **perDay**: you set a maximum total amount for all transfers made from the balance account or balance platform in a day. |
| `transfer_type` | [`TransferType`](../../doc/models/transfer-type.md) | Query, Optional | The type of transfer to which the limit applies. Possible values:<br><br>* **instant**: the limit applies to transfers with an **instant** priority.<br>* **all**: the limit applies to all transfers, regardless of priority. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TransferLimitListResponse`](../../doc/models/transfer-limit-list-response.md).

## Example Usage

```python
id = 'id0'

result = transfer_limits_balance_account_level_api.get_balance_accounts_id_transfer_limits_current(id)

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
      "scope": "perDay",
      "startsAt": "2025-08-13T23:00:00+01:00",
      "transferType": "instant"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 404 | Not found - One of the transfer limits could not be found. | [`BalanceAccountsTransferLimitsCurrent404ErrorException`](../../doc/models/balance-accounts-transfer-limits-current-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimitsCurrent422ErrorException`](../../doc/models/balance-accounts-transfer-limits-current-422-error-exception.md) |


# Get-Balance Accounts-Id-Transfer Limits-Transfer Limit Id

Get the details of a transfer limit using its unique `transferLimitId`.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_id_transfer_limits_transfer_limit_id(self,
                                                             id,
                                                             transfer_limit_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `transfer_limit_id` | `str` | Template, Required | The unique identifier of the transfer limit. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountsTransferLimitsResponse1`](../../doc/models/balance-accounts-transfer-limits-response-1.md).

## Example Usage

```python
id = 'id0'

transfer_limit_id = 'transferLimitId6'

result = transfer_limits_balance_account_level_api.get_balance_accounts_id_transfer_limits_transfer_limit_id(
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
| 404 | Not found - One of the transfer limits could not be found. | [`BalanceAccountsTransferLimits404ErrorException`](../../doc/models/balance-accounts-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimits422ErrorException`](../../doc/models/balance-accounts-transfer-limits-422-error-exception.md) |


# Delete-Balance Accounts-Id-Transfer Limits-Transfer Limit Id

Delete a scheduled or pending transfer limit using its unique `transferLimitId`. You cannot delete an active limit.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_balance_accounts_id_transfer_limits_transfer_limit_id(self,
                                                                id,
                                                                transfer_limit_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the balance account. |
| `transfer_limit_id` | `str` | Template, Required | The unique identifier of the transfer limit. |

## Response Type

**204**: No Content - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
id = 'id0'

transfer_limit_id = 'transferLimitId6'

result = transfer_limits_balance_account_level_api.delete_balance_accounts_id_transfer_limits_transfer_limit_id(
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
| 404 | Not found - One of the transfer limits could not be found. | [`BalanceAccountsTransferLimits404ErrorException`](../../doc/models/balance-accounts-transfer-limits-404-error-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`BalanceAccountsTransferLimits422ErrorException`](../../doc/models/balance-accounts-transfer-limits-422-error-exception.md) |

