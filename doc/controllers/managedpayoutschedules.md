# Managedpayoutschedules

```python
managedpayoutschedules_api = client.managedpayoutschedules
```

## Class Name

`ManagedpayoutschedulesApi`

## Methods

* [Get-Balance Accounts-Balance Account Id-Payout Schedules](../../doc/controllers/managedpayoutschedules.md#get-balance-accounts-balance-account-id-payout-schedules)
* [Post-Balance Accounts-Balance Account Id-Payout Schedules](../../doc/controllers/managedpayoutschedules.md#post-balance-accounts-balance-account-id-payout-schedules)
* [Get-Balance Accounts-Balance Account Id-Payout Schedules-Id](../../doc/controllers/managedpayoutschedules.md#get-balance-accounts-balance-account-id-payout-schedules-id)
* [Delete-Balance Accounts-Balance Account Id-Payout Schedules-Id](../../doc/controllers/managedpayoutschedules.md#delete-balance-accounts-balance-account-id-payout-schedules-id)
* [Patch-Balance Accounts-Balance Account Id-Payout Schedules-Id](../../doc/controllers/managedpayoutschedules.md#patch-balance-accounts-balance-account-id-payout-schedules-id)
* [Get-Balance Accounts-Balance Account Id-Payout Schedules-Id-Executions](../../doc/controllers/managedpayoutschedules.md#get-balance-accounts-balance-account-id-payout-schedules-id-executions)
* [Get-Balance Platforms-Balance Platform Id-Payout Schedules](../../doc/controllers/managedpayoutschedules.md#get-balance-platforms-balance-platform-id-payout-schedules)
* [Get-Balance Platforms-Balance Platform Id-Payout Schedules-Id](../../doc/controllers/managedpayoutschedules.md#get-balance-platforms-balance-platform-id-payout-schedules-id)


# Get-Balance Accounts-Balance Account Id-Payout Schedules

Returns a list of all managed payout schedules that are configured on a balance account. You can use query parameters to filter the elements that are returned in the list.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_balance_account_id_payout_schedules(self,
                                                            balance_account_id,
                                                            currency=None,
                                                            cursor=None,
                                                            limit=10)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `currency` | `str` | Query, Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the currency used in the payout schedule. |
| `cursor` | `str` | Query, Optional | The `cursor` returned in the links of the previous response. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum of 100 items. By default, the response returns 10 items per page.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountConfigurations`](../../doc/models/balance-account-configurations.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

limit = 10

result = managed_payout_schedules_api.get_balance_accounts_balance_account_id_payout_schedules(
    balance_account_id,
    limit=limit
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "balanceAccountPayoutSchedules": [
    {
      "id": "PSAC00000000000000000000000001",
      "balancePlatformPayoutScheduleId": "PSPC00000000000000000000000001",
      "balanceAccountId": "BA000000000000000000001",
      "transferInstrumentId": "SE00000000000000000000001",
      "currency": "EUR",
      "reference": "Monthly payout",
      "description": "Scheduled payout to merchant bank account",
      "referenceForBeneficiary": "PAYOUT-REF-001",
      "retainedAmount": 10000,
      "minPayoutAmount": 1000,
      "maxPayoutAmount": 100000000,
      "createdAt": "2024-01-15T10:30:00Z",
      "enabled": true,
      "frequency": "monthly",
      "frequencyValue": 1
    }
  ],
  "link": {
    "next": {
      "href": "/balanceAccounts/BA000000000000000000001/payoutSchedules?limit=10"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedules401ErrorException`](../../doc/models/balance-accounts-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedules403ErrorException`](../../doc/models/balance-accounts-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedules404ErrorException`](../../doc/models/balance-accounts-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedules422ErrorException`](../../doc/models/balance-accounts-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedules500ErrorException`](../../doc/models/balance-accounts-payout-schedules-500-error-exception.md) |


# Post-Balance Accounts-Balance Account Id-Payout Schedules

Apply a managed payout schedule to a balance account. This payout schedule is based on an existing payout schedule in your balance platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_accounts_balance_account_id_payout_schedules(self,
                                                             balance_account_id,
                                                             body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`BalanceAccountConfigurationRequest`](../../doc/models/balance-account-configuration-request.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountConfiguration`](../../doc/models/balance-account-configuration.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

body = BalanceAccountConfigurationRequest(
    balance_platform_payout_schedule_id='PSPC00000000000000000000000001',
    frequency=Frequency.MONTHLY,
    transfer_instrument_id='SE00000000000000000000001',
    currency='EUR',
    description='Scheduled payout to merchant bank account',
    enabled=True,
    frequency_value=1,
    max_payout_amount=100000000,
    min_payout_amount=1000,
    reference='Monthly payout',
    reference_for_beneficiary='PAYOUT-REF-001',
    retained_amount=10000
)

result = managed_payout_schedules_api.post_balance_accounts_balance_account_id_payout_schedules(
    balance_account_id,
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
  "id": "PSAC00000000000000000000000001",
  "balancePlatformPayoutScheduleId": "PSPC00000000000000000000000001",
  "balanceAccountId": "BA000000000000000000001",
  "transferInstrumentId": "SE00000000000000000000001",
  "currency": "EUR",
  "reference": "Monthly payout",
  "description": "Scheduled payout to merchant bank account",
  "referenceForBeneficiary": "PAYOUT-REF-001",
  "retainedAmount": 10000,
  "minPayoutAmount": 1000,
  "maxPayoutAmount": 100000000,
  "createdAt": "2024-01-15T10:30:00Z",
  "enabled": true,
  "frequency": "monthly",
  "frequencyValue": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedules401ErrorException`](../../doc/models/balance-accounts-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedules403ErrorException`](../../doc/models/balance-accounts-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedules404ErrorException`](../../doc/models/balance-accounts-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedules422ErrorException`](../../doc/models/balance-accounts-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedules500ErrorException`](../../doc/models/balance-accounts-payout-schedules-500-error-exception.md) |


# Get-Balance Accounts-Balance Account Id-Payout Schedules-Id

Returns the specified payout schedule.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_balance_account_id_payout_schedules_id(self,
                                                               balance_account_id,
                                                               id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `id` | `str` | Template, Required | The unique identifier of the payout schedule for the balance account. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountConfiguration`](../../doc/models/balance-account-configuration.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

id = 'id0'

result = managed_payout_schedules_api.get_balance_accounts_balance_account_id_payout_schedules_id(
    balance_account_id,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "PSAC00000000000000000000000001",
  "balancePlatformPayoutScheduleId": "PSPC00000000000000000000000001",
  "balanceAccountId": "BA000000000000000000001",
  "transferInstrumentId": "SE00000000000000000000001",
  "currency": "EUR",
  "reference": "Monthly payout",
  "description": "Scheduled payout to merchant bank account",
  "referenceForBeneficiary": "PAYOUT-REF-001",
  "retainedAmount": 10000,
  "minPayoutAmount": 1000,
  "maxPayoutAmount": 100000000,
  "createdAt": "2024-01-15T10:30:00Z",
  "enabled": true,
  "frequency": "monthly",
  "frequencyValue": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedules401ErrorException`](../../doc/models/balance-accounts-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedules403ErrorException`](../../doc/models/balance-accounts-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedules404ErrorException`](../../doc/models/balance-accounts-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedules422ErrorException`](../../doc/models/balance-accounts-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedules500ErrorException`](../../doc/models/balance-accounts-payout-schedules-500-error-exception.md) |


# Delete-Balance Accounts-Balance Account Id-Payout Schedules-Id

Delete a payout schedule applied to a balance account.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_balance_accounts_balance_account_id_payout_schedules_id(self,
                                                                  balance_account_id,
                                                                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `id` | `str` | Template, Required | The unique identifier of the payout schedule applied to the balance account. |

## Response Type

**204**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

id = 'id0'

result = managed_payout_schedules_api.delete_balance_accounts_balance_account_id_payout_schedules_id(
    balance_account_id,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedules401ErrorException`](../../doc/models/balance-accounts-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedules403ErrorException`](../../doc/models/balance-accounts-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedules404ErrorException`](../../doc/models/balance-accounts-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedules422ErrorException`](../../doc/models/balance-accounts-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedules500ErrorException`](../../doc/models/balance-accounts-payout-schedules-500-error-exception.md) |


# Patch-Balance Accounts-Balance Account Id-Payout Schedules-Id

Update a managed payout schedule applied to a balance account. If an optional parameter is not included in the request, it remains unchanged.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_balance_accounts_balance_account_id_payout_schedules_id(self,
                                                                 balance_account_id,
                                                                 id,
                                                                 body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `id` | `str` | Template, Required | The unique identifier of the payout schedule applied to the balance account. |
| `body` | [`BalanceAccountConfigurationUpdate`](../../doc/models/balance-account-configuration-update.md) | Body, Required | - |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalanceAccountConfiguration`](../../doc/models/balance-account-configuration.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

id = 'id0'

body = BalanceAccountConfigurationUpdate(
    description='Updated payout description',
    enabled=False,
    retained_amount=20000
)

result = managed_payout_schedules_api.patch_balance_accounts_balance_account_id_payout_schedules_id(
    balance_account_id,
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
  "id": "PSAC00000000000000000000000001",
  "balancePlatformPayoutScheduleId": "PSPC00000000000000000000000001",
  "balanceAccountId": "BA000000000000000000001",
  "transferInstrumentId": "SE00000000000000000000001",
  "currency": "EUR",
  "reference": "Monthly payout",
  "description": "Updated payout description",
  "referenceForBeneficiary": "PAYOUT-REF-001",
  "retainedAmount": 20000,
  "minPayoutAmount": 1000,
  "maxPayoutAmount": 100000000,
  "createdAt": "2024-01-15T10:30:00Z",
  "updatedAt": "2024-01-16T14:00:00Z",
  "enabled": false,
  "frequency": "monthly",
  "frequencyValue": 1
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedules401ErrorException`](../../doc/models/balance-accounts-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedules403ErrorException`](../../doc/models/balance-accounts-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedules404ErrorException`](../../doc/models/balance-accounts-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedules422ErrorException`](../../doc/models/balance-accounts-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedules500ErrorException`](../../doc/models/balance-accounts-payout-schedules-500-error-exception.md) |


# Get-Balance Accounts-Balance Account Id-Payout Schedules-Id-Executions

View information about the executions of a managed payout schedule on the specified balance account. An execution is an attempt to make a payout according to the payout schedule.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_balance_account_id_payout_schedules_id_executions(self,
                                                                          balance_account_id,
                                                                          id,
                                                                          offset,
                                                                          results=None,
                                                                          limit=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `id` | `str` | Template, Required | The unique identifier of the payout schedule on the balance account. |
| `offset` | `int` | Query, Required | The page number to be returned.<br><br>Default: **1**<br><br>**Constraints**: `>= 1`, `<= 100` |
| `results` | [`List[ExecutionResult]`](../../doc/models/execution-result.md) | Query, Optional | Contains a list of payout statuses. If included, the response returns only executed payouts that currently have one of the specified statuses.<br><br>Possible statuses:<br><br>- **succeeded**: The payout was sent successfully.<br>- **failed**: The payout was not sent due to an error.<br>- **skipped**: The payout was not triggered as expected. |
| `limit` | `int` | Query, Optional | The number of items returned per page.<br><br>Default: **10**<br><br>**Constraints**: `>= 10` |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`PayoutScheduleExecutions`](../../doc/models/payout-schedule-executions.md).

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

id = 'id0'

offset = 12

result = managed_payout_schedules_api.get_balance_accounts_balance_account_id_payout_schedules_id_executions(
    balance_account_id,
    id,
    offset
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "payoutScheduleExecutions": [
    {
      "id": "PS0000000000001",
      "result": "skipped",
      "triggeredAt": "2026-03-11T08:00:00Z",
      "resultDetails": {
        "reasonCode": "noBalanceToPayOut",
        "reason": "No balance to pay out"
      }
    },
    {
      "id": "PS0000000000002",
      "result": "succeeded",
      "triggeredAt": "2026-03-12T08:00:00Z",
      "resultDetails": {
        "transferId": "A0A0A0A0A0A0A0A0"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalanceAccountsPayoutSchedulesExecutions401ErrorException`](../../doc/models/balance-accounts-payout-schedules-executions-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalanceAccountsPayoutSchedulesExecutions403ErrorException`](../../doc/models/balance-accounts-payout-schedules-executions-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalanceAccountsPayoutSchedulesExecutions404ErrorException`](../../doc/models/balance-accounts-payout-schedules-executions-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalanceAccountsPayoutSchedulesExecutions422ErrorException`](../../doc/models/balance-accounts-payout-schedules-executions-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalanceAccountsPayoutSchedulesExecutions500ErrorException`](../../doc/models/balance-accounts-payout-schedules-executions-500-error-exception.md) |


# Get-Balance Platforms-Balance Platform Id-Payout Schedules

Returns a list of all the payout schedules that are configured for your balance platform. You can use query parameters to filter the elements that are returned in the list.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_balance_platform_id_payout_schedules(self,
                                                              balance_platform_id,
                                                              country_code=None,
                                                              currency=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `country_code` | `str` | Query, Optional | The two-letter [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code of the country to which the payout configuration applies. |
| `currency` | `str` | Query, Optional | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes) of the currency used in the payout configuration. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalancePlatformConfigurations`](../../doc/models/balance-platform-configurations.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

result = managed_payout_schedules_api.get_balance_platforms_balance_platform_id_payout_schedules(balance_platform_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsPayoutSchedules401ErrorException`](../../doc/models/balance-platforms-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsPayoutSchedules403ErrorException`](../../doc/models/balance-platforms-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalancePlatformsPayoutSchedules404ErrorException`](../../doc/models/balance-platforms-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsPayoutSchedules422ErrorException`](../../doc/models/balance-platforms-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsPayoutSchedules500ErrorException`](../../doc/models/balance-platforms-payout-schedules-500-error-exception.md) |


# Get-Balance Platforms-Balance Platform Id-Payout Schedules-Id

Returns the specified managed payout schedule configured on your balance platform.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_balance_platform_id_payout_schedules_id(self,
                                                                 balance_platform_id,
                                                                 id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `id` | `str` | Template, Required | The unique identifier of the payout configuration for your balance platform. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BalancePlatformConfiguration`](../../doc/models/balance-platform-configuration.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

id = 'id0'

result = managed_payout_schedules_api.get_balance_platforms_balance_platform_id_payout_schedules_id(
    balance_platform_id,
    id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsPayoutSchedules401ErrorException`](../../doc/models/balance-platforms-payout-schedules-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsPayoutSchedules403ErrorException`](../../doc/models/balance-platforms-payout-schedules-403-error-exception.md) |
| 404 | Not Found - the resource was not found | [`BalancePlatformsPayoutSchedules404ErrorException`](../../doc/models/balance-platforms-payout-schedules-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsPayoutSchedules422ErrorException`](../../doc/models/balance-platforms-payout-schedules-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsPayoutSchedules500ErrorException`](../../doc/models/balance-platforms-payout-schedules-500-error-exception.md) |

