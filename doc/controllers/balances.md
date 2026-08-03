# Balances

```python
balances_api = client.balances
```

## Class Name

`BalancesApi`

## Methods

* [Get-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings](../../doc/controllers/balances.md#get-balance-platforms-balance-platform-id-webhooks-webhook-id-settings)
* [Post-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings](../../doc/controllers/balances.md#post-balance-platforms-balance-platform-id-webhooks-webhook-id-settings)
* [Get-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id](../../doc/controllers/balances.md#get-balance-platforms-balance-platform-id-webhooks-webhook-id-settings-setting-id)
* [Delete-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id](../../doc/controllers/balances.md#delete-balance-platforms-balance-platform-id-webhooks-webhook-id-settings-setting-id)
* [Patch-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id](../../doc/controllers/balances.md#patch-balance-platforms-balance-platform-id-webhooks-webhook-id-settings-setting-id)


# Get-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings

Returns all balance webhook settings configured for triggering [balance webhooks](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(self,
                                                                          balance_platform_id,
                                                                          webhook_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `webhook_id` | `str` | Template, Required | The unique identifier of the balance webhook. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WebhookSettings`](../../doc/models/webhook-settings.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

webhook_id = 'webhookId6'

result = balances_api.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
    balance_platform_id,
    webhook_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "webhookSettings": [
    {
      "id": "BWHS00000000000000000000000001",
      "type": "balance",
      "target": {
        "type": "balancePlatform",
        "id": "YOUR_BALANCE_PLATFORM"
      },
      "currency": "USD",
      "status": "active",
      "conditions": [
        {
          "balanceType": "available",
          "conditionType": "lessThan",
          "value": 500000
        }
      ]
    },
    {
      "id": "BWHS00000000000000000000000002",
      "type": "balance",
      "target": {
        "type": "balanceAccount",
        "id": "BA00000000000000000LIABLE"
      },
      "currency": "USD",
      "status": "active",
      "conditions": [
        {
          "balanceType": "available",
          "conditionType": "greaterThan",
          "value": 1000000
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`BalancePlatformsWebhooksSettings400ErrorException`](../../doc/models/balance-platforms-webhooks-settings-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsWebhooksSettings401ErrorException`](../../doc/models/balance-platforms-webhooks-settings-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsWebhooksSettings403ErrorException`](../../doc/models/balance-platforms-webhooks-settings-403-error-exception.md) |
| 404 | Not Found - the payment was not found | [`BalancePlatformsWebhooksSettings404ErrorException`](../../doc/models/balance-platforms-webhooks-settings-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsWebhooksSettings422ErrorException`](../../doc/models/balance-platforms-webhooks-settings-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsWebhooksSettings500ErrorException`](../../doc/models/balance-platforms-webhooks-settings-500-error-exception.md) |


# Post-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings

Configures the criteria for triggering [balance webhooks](https://docs.adyen.com/api-explorer/balance-webhooks/1/post/balancePlatform.balanceAccount.balance.updated).

Adyen sends balance webhooks to notify you of balance changes in your balance platform. They can be triggered when the balance reaches, exceeds, or drops below a specific value in a specific currency.

You can get notified about balance changes in your entire balance platform, in the balance accounts of a specific user, or a specific balance account. The hierarchy between the webhook settings are based on the following business logic:

* Settings on a higher level apply to all lower level resources (balance platform > account holder > balance acocunt).

* The most granular setting overrides higher level settings (balance account > account holder > balance platform).

:information_source: **Note** This endpoint does not require authentication.

```python
def post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(self,
                                                                           balance_platform_id,
                                                                           webhook_id,
                                                                           body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `webhook_id` | `str` | Template, Required | The unique identifier of the balance webhook. |
| `body` | [`BalanceWebhookSettingInfo`](../../doc/models/balance-webhook-setting-info.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WebhookSetting`](../../doc/models/webhook-setting.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

webhook_id = 'webhookId6'

body = BalanceWebhookSettingInfo(
    currency='USD',
    status=Status19.ACTIVE,
    target=Target(
        id='BA00000000000000000LIABLE',
        mtype=Type18.BALANCEACCOUNT
    ),
    mtype=Type20.BALANCE,
    conditions=[
        Condition(
            balance_type=BalanceType.AVAILABLE,
            condition_type=ConditionType.LESSTHAN,
            value=500000
        )
    ]
)

result = balances_api.post_balance_platforms_balance_platform_id_webhooks_webhook_id_settings(
    balance_platform_id,
    webhook_id,
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
  "id": "BWHS00000000000000000000000001",
  "type": "balance",
  "target": {
    "type": "balanceAccount",
    "id": "BA00000000000000000LIABLE"
  },
  "currency": "USD",
  "status": "active",
  "conditions": [
    {
      "balanceType": "available",
      "conditionType": "lessThan",
      "value": 500000
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`BalancePlatformsWebhooksSettings400ErrorException`](../../doc/models/balance-platforms-webhooks-settings-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsWebhooksSettings401ErrorException`](../../doc/models/balance-platforms-webhooks-settings-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsWebhooksSettings403ErrorException`](../../doc/models/balance-platforms-webhooks-settings-403-error-exception.md) |
| 404 | Not Found - the payment was not found | [`BalancePlatformsWebhooksSettings404ErrorException`](../../doc/models/balance-platforms-webhooks-settings-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsWebhooksSettings422ErrorException`](../../doc/models/balance-platforms-webhooks-settings-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsWebhooksSettings500ErrorException`](../../doc/models/balance-platforms-webhooks-settings-500-error-exception.md) |


# Get-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id

Returns the details of a specific balance webhook setting configured for triggering [balance webhooks](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated).

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(self,
                                                                                     balance_platform_id,
                                                                                     webhook_id,
                                                                                     setting_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `webhook_id` | `str` | Template, Required | The unique identifier of the balance webhook. |
| `setting_id` | `str` | Template, Required | The unique identifier of the balance webhook setting. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WebhookSetting`](../../doc/models/webhook-setting.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

webhook_id = 'webhookId6'

setting_id = 'settingId0'

result = balances_api.get_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
    balance_platform_id,
    webhook_id,
    setting_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "BWHS00000000000000000000000001",
  "type": "balance",
  "target": {
    "type": "balancePlatform",
    "id": "YOUR_BALANCE_PLATFORM"
  },
  "currency": "USD",
  "status": "active",
  "conditions": [
    {
      "balanceType": "available",
      "conditionType": "lessThan",
      "value": 500000
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`BalancePlatformsWebhooksSettingsSettingId400ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsWebhooksSettingsSettingId401ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsWebhooksSettingsSettingId403ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-403-error-exception.md) |
| 404 | Not Found - the payment was not found | [`BalancePlatformsWebhooksSettingsSettingId404ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsWebhooksSettingsSettingId422ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsWebhooksSettingsSettingId500ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-500-error-exception.md) |


# Delete-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id

Deletes a balance webhook setting that contains the conditions for triggering [balance webhooks](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated).

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(self,
                                                                                        balance_platform_id,
                                                                                        webhook_id,
                                                                                        setting_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `webhook_id` | `str` | Template, Required | The unique identifier of the balance webhook. |
| `setting_id` | `str` | Template, Required | The unique identifier of the balance webhook setting. |

## Response Type

**204**: No Content - the request has been successfully processed, but there is no additional content.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type `Any`.

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

webhook_id = 'webhookId6'

setting_id = 'settingId0'

result = balances_api.delete_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
    balance_platform_id,
    webhook_id,
    setting_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`BalancePlatformsWebhooksSettingsSettingId400ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsWebhooksSettingsSettingId401ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsWebhooksSettingsSettingId403ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-403-error-exception.md) |
| 404 | Not Found - the payment was not found | [`BalancePlatformsWebhooksSettingsSettingId404ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsWebhooksSettingsSettingId422ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsWebhooksSettingsSettingId500ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-500-error-exception.md) |


# Patch-Balance Platforms-Balance Platform Id-Webhooks-Webhook Id-Settings-Setting Id

Updates the conditions the balance change needs to meet for Adyen to send a [balance webhook](https://docs.adyen.com/api-explorer/balance-webhooks/latest/post/balanceAccount.balance.updated).

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(self,
                                                                                       balance_platform_id,
                                                                                       webhook_id,
                                                                                       setting_id,
                                                                                       body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `balance_platform_id` | `str` | Template, Required | The unique identifier of the balance platform. |
| `webhook_id` | `str` | Template, Required | The unique identifier of the balance webhook. |
| `setting_id` | `str` | Template, Required | The unique identifier of the balance webhook setting. |
| `body` | [`BalanceWebhookSettingInfoUpdate`](../../doc/models/balance-webhook-setting-info-update.md) | Body, Required | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`WebhookSetting`](../../doc/models/webhook-setting.md).

## Example Usage

```python
balance_platform_id = 'balancePlatformId8'

webhook_id = 'webhookId6'

setting_id = 'settingId0'

body = BalanceWebhookSettingInfoUpdate(
    status=Status19.INACTIVE,
    mtype=Type20.BALANCE
)

result = balances_api.patch_balance_platforms_balance_platform_id_webhooks_webhook_id_settings_setting_id(
    balance_platform_id,
    webhook_id,
    setting_id,
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
  "type": "balance",
  "id": "BWHS00000000000000000000000001",
  "target": {
    "type": "balanceAccount",
    "id": "BA00000000000000000LIABLE"
  },
  "currency": "USD",
  "status": "inactive",
  "conditions": [
    {
      "balanceType": "available",
      "conditionType": "lessThan",
      "value": 500000
    },
    {
      "balanceType": "balance",
      "conditionType": "greaterThan",
      "value": 1000000
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`BalancePlatformsWebhooksSettingsSettingId400ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-400-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`BalancePlatformsWebhooksSettingsSettingId401ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-401-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`BalancePlatformsWebhooksSettingsSettingId403ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-403-error-exception.md) |
| 404 | Not Found - the payment was not found | [`BalancePlatformsWebhooksSettingsSettingId404ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`BalancePlatformsWebhooksSettingsSettingId422ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-422-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`BalancePlatformsWebhooksSettingsSettingId500ErrorException`](../../doc/models/balance-platforms-webhooks-settings-setting-id-500-error-exception.md) |

