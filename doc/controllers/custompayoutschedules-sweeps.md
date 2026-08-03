# Custompayoutschedules Sweeps

```python
custompayoutschedules_sweeps_api = client.custompayoutschedules_sweeps
```

## Class Name

`CustompayoutschedulesSweepsApi`

## Methods

* [Get-Balance Accounts-Balance Account Id-Sweeps](../../doc/controllers/custompayoutschedules-sweeps.md#get-balance-accounts-balance-account-id-sweeps)
* [Post-Balance Accounts-Balance Account Id-Sweeps](../../doc/controllers/custompayoutschedules-sweeps.md#post-balance-accounts-balance-account-id-sweeps)
* [Get-Balance Accounts-Balance Account Id-Sweeps-Sweep Id](../../doc/controllers/custompayoutschedules-sweeps.md#get-balance-accounts-balance-account-id-sweeps-sweep-id)
* [Delete-Balance Accounts-Balance Account Id-Sweeps-Sweep Id](../../doc/controllers/custompayoutschedules-sweeps.md#delete-balance-accounts-balance-account-id-sweeps-sweep-id)
* [Patch-Balance Accounts-Balance Account Id-Sweeps-Sweep Id](../../doc/controllers/custompayoutschedules-sweeps.md#patch-balance-accounts-balance-account-id-sweeps-sweep-id)


# Get-Balance Accounts-Balance Account Id-Sweeps

Returns a list of the sweeps configured for a balance account.

To fetch multiple pages, use the query parameters. For example, to limit the page to 5 sweeps and to skip the first 10, use `/balanceAccounts/{balanceAccountId}/sweeps?limit=5&offset=10`.

```python
def get_balance_accounts_balance_account_id_sweeps(self,
                                                  balance_account_id,
                                                  offset=None,
                                                  limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `offset` | `int` | Query, Optional | The number of items that you want to skip. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceSweepConfigurationsResponse`](../../doc/models/balance-sweep-configurations-response.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

result = custom_payout_schedules_sweeps_api.get_balance_accounts_balance_account_id_sweeps(balance_account_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "hasNext": false,
  "hasPrevious": false,
  "sweeps": [
    {
      "id": "SWPC4227C224555B5FTD2NT2JV4WN5",
      "schedule": {
        "type": "daily"
      },
      "status": "active",
      "targetAmount": {
        "currency": "EUR",
        "value": 0
      },
      "triggerAmount": {
        "currency": "EUR",
        "value": 0
      },
      "type": "push",
      "counterparty": {
        "balanceAccountId": "BA32272223222B5FTD2KR6TJD"
      },
      "currency": "EUR"
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


# Post-Balance Accounts-Balance Account Id-Sweeps

Creates a sweep that results in moving funds from or to a balance account.

A sweep pulls in or pushes out funds based on a defined schedule, amount, currency, and a source or a destination.

```python
def post_balance_accounts_balance_account_id_sweeps(self,
                                                   balance_account_id,
                                                   body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`CreateSweepConfigurationV2`](../../doc/models/create-sweep-configuration-v2.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SweepConfigurationV2`](../../doc/models/sweep-configuration-v2.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

body = CreateSweepConfigurationV2(
    counterparty=SweepCounterparty(
        merchant_account='YOUR_MERCHANT_ACCOUNT'
    ),
    currency='EUR',
    schedule=SweepSchedule(
        mtype=Type6.BALANCE
    ),
    status=Status51.ACTIVE,
    trigger_amount=TriggerAmount(
        currency='EUR',
        value=50000
    ),
    mtype=Type7.PULL
)

result = custom_payout_schedules_sweeps_api.post_balance_accounts_balance_account_id_sweeps(
    balance_account_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "SWPC4227C224555B5FTD2NT2JV4WN5",
  "counterparty": {
    "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
  },
  "triggerAmount": {
    "currency": "EUR",
    "value": 50000
  },
  "currency": "EUR",
  "schedule": {
    "type": "balance"
  },
  "type": "pull",
  "status": "active"
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


# Get-Balance Accounts-Balance Account Id-Sweeps-Sweep Id

Returns a sweep.

```python
def get_balance_accounts_balance_account_id_sweeps_sweep_id(self,
                                                           balance_account_id,
                                                           sweep_id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `sweep_id` | `str` | Template, Required | The unique identifier of the sweep. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SweepConfigurationV2`](../../doc/models/sweep-configuration-v2.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

sweep_id = 'sweepId4'

result = custom_payout_schedules_sweeps_api.get_balance_accounts_balance_account_id_sweeps_sweep_id(
    balance_account_id,
    sweep_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "SWPC4227C224555B5FTD2NT2JV4WN5",
  "schedule": {
    "type": "daily"
  },
  "status": "active",
  "targetAmount": {
    "currency": "EUR",
    "value": 0
  },
  "triggerAmount": {
    "currency": "EUR",
    "value": 0
  },
  "type": "push",
  "counterparty": {
    "balanceAccountId": "BA32272223222B5FTD2KR6TJD"
  },
  "currency": "EUR"
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


# Delete-Balance Accounts-Balance Account Id-Sweeps-Sweep Id

Deletes a sweep for a balance account.

```python
def delete_balance_accounts_balance_account_id_sweeps_sweep_id(self,
                                                              balance_account_id,
                                                              sweep_id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `sweep_id` | `str` | Template, Required | The unique identifier of the sweep. |

## Response Type

**204**: No Content - look at the actual response code for the status of the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

sweep_id = 'sweepId4'

result = custom_payout_schedules_sweeps_api.delete_balance_accounts_balance_account_id_sweeps_sweep_id(
    balance_account_id,
    sweep_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Balance Accounts-Balance Account Id-Sweeps-Sweep Id

Updates a sweep. When updating a sweep resource, note that if a request parameter is not provided, the parameter is left unchanged.

```python
def patch_balance_accounts_balance_account_id_sweeps_sweep_id(self,
                                                             balance_account_id,
                                                             sweep_id,
                                                             body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `sweep_id` | `str` | Template, Required | The unique identifier of the sweep. |
| `body` | [`UpdateSweepConfigurationV2`](../../doc/models/update-sweep-configuration-v2.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`SweepConfigurationV2`](../../doc/models/sweep-configuration-v2.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

sweep_id = 'sweepId4'

body = UpdateSweepConfigurationV2(
    status=Status51.INACTIVE
)

result = custom_payout_schedules_sweeps_api.patch_balance_accounts_balance_account_id_sweeps_sweep_id(
    balance_account_id,
    sweep_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "SWPC4227C224555B5FTD2NT2JV4WN5",
  "counterparty": {
    "merchantAccount": "YOUR_MERCHANT_ACCOUNT"
  },
  "triggerAmount": {
    "currency": "EUR",
    "value": 50000
  },
  "currency": "EUR",
  "schedule": {
    "type": "balance"
  },
  "type": "pull",
  "status": "inactive"
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

