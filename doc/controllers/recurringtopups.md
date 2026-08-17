# Recurringtopups

```python
recurringtopups_api = client.recurringtopups
```

## Class Name

`RecurringtopupsApi`

## Methods

* [Get-Balance Accounts-Balance Account Id-Recurring Top Ups](../../doc/controllers/recurringtopups.md#get-balance-accounts-balance-account-id-recurring-top-ups)
* [Post-Balance Accounts-Balance Account Id-Recurring Top Ups](../../doc/controllers/recurringtopups.md#post-balance-accounts-balance-account-id-recurring-top-ups)
* [Delete-Balance Accounts-Balance Account Id-Recurring Top Ups-Top Up Id](../../doc/controllers/recurringtopups.md#delete-balance-accounts-balance-account-id-recurring-top-ups-top-up-id)
* [Patch-Balance Accounts-Balance Account Id-Recurring Top Ups-Top Up Id](../../doc/controllers/recurringtopups.md#patch-balance-accounts-balance-account-id-recurring-top-ups-top-up-id)


# Get-Balance Accounts-Balance Account Id-Recurring Top Ups

View all recurring top ups configured for a specific `balanceAccountId`.

For more information, refer to [Manage recurring top-ups](https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_accounts_balance_account_id_recurring_top_ups(self,
                                                             balance_account_id,
                                                             limit=10,
                                                             cursor=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `limit` | `int` | Query, Optional | The number of items to return per page. Value must be between 1 and 100.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |
| `cursor` | `str` | Query, Optional | The cursor used for pagination. Required if you want to see the next or previous page of results. |

## Response Type

**200**: OK - the request has succeeded.

[`RecurringTopUpsResult`](../../doc/models/recurring-top-ups-result.md)

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

limit = 10

result = recurring_top_ups_api.get_balance_accounts_balance_account_id_recurring_top_ups(
    balance_account_id,
    limit=limit
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "recurringTopUps": [
    {
      "id": "TUPC0000000000000000000001",
      "counterparty": {
        "transferInstrumentId": "SE000000000000000000000001"
      },
      "description": "My description",
      "topUpAmount": {
        "fixed": {
          "value": 1000,
          "currency": "EUR"
        }
      },
      "trigger": {
        "schedule": {
          "type": "weekdays"
        },
        "threshold": {
          "value": 100,
          "currency": "EUR"
        }
      },
      "status": "active"
    }
  ],
  "link": {
    "next": {
      "href": "/balanceAccounts/balanceAccount1/recurringTopUps?limit=10&cursor=nextCursorToken"
    },
    "previous": {
      "href": "/balanceAccounts/balanceAccount1/recurringTopUps?limit=10&cursor=previousCursorToken"
    }
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | Not Found - the recurring top up was not found | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Balance Accounts-Balance Account Id-Recurring Top Ups

Create a recurring top up configuration.

For more information, refer to [Create recurring top-ups](https://docs.adyen.com/issuing/add-manage-funds/top-ups/create-recurring-top-ups).

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_accounts_balance_account_id_recurring_top_ups(self,
                                                              balance_account_id,
                                                              body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `body` | [`CreateRecurringTopUp`](../../doc/models/create-recurring-top-up.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`RecurringTopUp`](../../doc/models/recurring-top-up.md)

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

body = CreateRecurringTopUp(
    counterparty=TopUpCounterparty1(
        transfer_instrument_id='SE000000000000000000000001'
    ),
    description='My description',
    top_up_amount=TopUpAmount1(
        fixed=Amount17(
            currency='EUR',
            value=1000
        )
    ),
    trigger=Trigger1(
        threshold=Amount17(
            currency='EUR',
            value=100
        ),
        schedule=Schedule21(
            mtype=ScheduleType1Enum.WEEKDAYS
        )
    )
)

result = recurring_top_ups_api.post_balance_accounts_balance_account_id_recurring_top_ups(
    balance_account_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "TUPC0000000000000000000001",
  "counterparty": {
    "transferInstrumentId": "SE000000000000000000000001"
  },
  "description": "My description",
  "topUpAmount": {
    "fixed": {
      "value": 1000,
      "currency": "EUR"
    }
  },
  "trigger": {
    "schedule": {
      "type": "weekdays"
    },
    "threshold": {
      "value": 100,
      "currency": "EUR"
    }
  },
  "status": "active"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Delete-Balance Accounts-Balance Account Id-Recurring Top Ups-Top Up Id

Delete a recurring top up configuration by `topUpId`.

For more information, refer to [Manage recurring top-ups](https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups).

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(self,
                                                                          balance_account_id,
                                                                          top_up_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `top_up_id` | `str` | Template, Required | The unique identifier of the recurring top-up you want to delete. |

## Response Type

**204**: No Content - the request has been successfully processed, but there is no additional content.

`Any`

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

top_up_id = 'topUpId8'

result = recurring_top_ups_api.delete_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
    balance_account_id,
    top_up_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 404 | Not Found - the recurring top up was not found | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Patch-Balance Accounts-Balance Account Id-Recurring Top Ups-Top Up Id

Update the configuration of an existing recurring top up.

For more information, refer to [Manage recurring top-ups](https://docs.adyen.com/issuing/add-manage-funds/top-ups/manage-recurring-top-ups).

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(self,
                                                                         balance_account_id,
                                                                         top_up_id,
                                                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_account_id` | `str` | Template, Required | The unique identifier of the balance account. |
| `top_up_id` | `str` | Template, Required | The unique identifier of the recurring top-up you want to update. |
| `body` | [`PatchableCreateRecurringTopUp`](../../doc/models/patchable-create-recurring-top-up.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

[`RecurringTopUp`](../../doc/models/recurring-top-up.md)

## Example Usage

```python
balance_account_id = 'balanceAccountId8'

top_up_id = 'topUpId8'

body = PatchableCreateRecurringTopUp(
    description='new description'
)

result = recurring_top_ups_api.patch_balance_accounts_balance_account_id_recurring_top_ups_top_up_id(
    balance_account_id,
    top_up_id,
    body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "TUPC0000000000000000000001",
  "counterparty": {
    "transferInstrumentId": "SE000000000000000000000001"
  },
  "description": "new description",
  "topUpAmount": {
    "fixed": {
      "value": 1000,
      "currency": "EUR"
    }
  },
  "trigger": {
    "schedule": {
      "type": "weekdays"
    },
    "threshold": {
      "value": 100,
      "currency": "EUR"
    }
  },
  "status": "inactive"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

