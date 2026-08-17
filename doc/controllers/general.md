# General

```python
general_api = client.general
```

## Class Name

`GeneralApi`

## Methods

* [Post-Create Permit](../../doc/controllers/general.md#post-create-permit)
* [Post-Disable](../../doc/controllers/general.md#post-disable)
* [Post-Disable Permit](../../doc/controllers/general.md#post-disable-permit)
* [Post-List Recurring Details](../../doc/controllers/general.md#post-list-recurring-details)
* [Post-Notify Shopper](../../doc/controllers/general.md#post-notify-shopper)
* [Post-Schedule Account Updater](../../doc/controllers/general.md#post-schedule-account-updater)
* [Post-Get 3 Ds Availability](../../doc/controllers/general.md#post-get-3-ds-availability)
* [Post-Get Cost Estimate](../../doc/controllers/general.md#post-get-cost-estimate)
* [Post-Change Status](../../doc/controllers/general.md#post-change-status)
* [Post-Check Balance](../../doc/controllers/general.md#post-check-balance)
* [Post-Issue](../../doc/controllers/general.md#post-issue)
* [Post-Load](../../doc/controllers/general.md#post-load)
* [Post-Merge Balance](../../doc/controllers/general.md#post-merge-balance)
* [Post-Void Transaction](../../doc/controllers/general.md#post-void-transaction)
* [Post-Request Subject Erasure](../../doc/controllers/general.md#post-request-subject-erasure)
* [Post-Create Test Card Ranges](../../doc/controllers/general.md#post-create-test-card-ranges)
* [Post-Create Notification Configuration](../../doc/controllers/general.md#post-create-notification-configuration)
* [Post-Delete Notification Configurations](../../doc/controllers/general.md#post-delete-notification-configurations)
* [Post-Get Notification Configuration](../../doc/controllers/general.md#post-get-notification-configuration)
* [Post-Get Notification Configuration List](../../doc/controllers/general.md#post-get-notification-configuration-list)
* [Post-Test Notification Configuration](../../doc/controllers/general.md#post-test-notification-configuration)
* [Post-Update Notification Configuration](../../doc/controllers/general.md#post-update-notification-configuration)
* [Post-Account Holder Balance](../../doc/controllers/general.md#post-account-holder-balance)
* [Post-Account Holder Transaction List](../../doc/controllers/general.md#post-account-holder-transaction-list)
* [Post-Debit Account Holder](../../doc/controllers/general.md#post-debit-account-holder)
* [Post-Payout Account Holder](../../doc/controllers/general.md#post-payout-account-holder)
* [Post-Refund Funds Transfer](../../doc/controllers/general.md#post-refund-funds-transfer)
* [Post-Refund Not Paid Out Transfers](../../doc/controllers/general.md#post-refund-not-paid-out-transfers)
* [Post-Setup Beneficiary](../../doc/controllers/general.md#post-setup-beneficiary)
* [Post-Transfer Funds](../../doc/controllers/general.md#post-transfer-funds)
* [Post-Accept Dispute](../../doc/controllers/general.md#post-accept-dispute)
* [Post-Defend Dispute](../../doc/controllers/general.md#post-defend-dispute)
* [Post-Delete Dispute Defense Document](../../doc/controllers/general.md#post-delete-dispute-defense-document)
* [Post-Retrieve Applicable Defense Reasons](../../doc/controllers/general.md#post-retrieve-applicable-defense-reasons)
* [Post-Supply Defense Document](../../doc/controllers/general.md#post-supply-defense-document)
* [Post-Sessions](../../doc/controllers/general.md#post-sessions)
* [Post-Assign Terminals](../../doc/controllers/general.md#post-assign-terminals)
* [Post-Find Terminal](../../doc/controllers/general.md#post-find-terminal)
* [Post-Get Stores Under Account](../../doc/controllers/general.md#post-get-stores-under-account)
* [Post-Get Terminal Details](../../doc/controllers/general.md#post-get-terminal-details)
* [Post-Get Terminals Under Account](../../doc/controllers/general.md#post-get-terminals-under-account)


# Post-Create Permit

**This endpoint is deprecated.**

Create permits for a recurring contract, including support for defining restrictions.

```python
def post_create_permit(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreatePermitRequest`](../../doc/models/create-permit-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CreatePermitResult`](../../doc/models/create-permit-result.md)

## Example Usage

```python
body = CreatePermitRequest(
    merchant_account='merchantAccount2',
    permits=[
        Permit()
    ],
    recurring_detail_reference='recurringDetailReference6',
    shopper_reference='shopperReference4'
)

result = general_api.post_create_permit(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Disable

Disables stored payment details to stop charging a shopper with this particular recurring detail ID.

For more information, refer to [Disable stored details](https://docs.adyen.com/online-payments/classic-integrations/classic-api-integration/tokenization/disable-stored-details).

```python
def post_disable(self,
                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DisableRequest`](../../doc/models/disable-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DisableResult`](../../doc/models/disable-result.md)

## Example Usage

```python
body = DisableRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    shopper_reference='YOUR_SHOPPER_REFERENCE',
    recurring_detail_reference='8314442372419167'
)

result = general_api.post_disable(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Disable Permit

**This endpoint is deprecated.**

Disable a permit that was previously linked to a recurringDetailReference.

```python
def post_disable_permit(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DisablePermitRequest`](../../doc/models/disable-permit-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DisablePermitResult`](../../doc/models/disable-permit-result.md)

## Example Usage

```python
result = general_api.post_disable_permit()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-List Recurring Details

Lists the stored payment details for a shopper, if there are any available. The recurring detail ID can be used with a regular authorisation request to charge the shopper. A summary of the payment detail is returned for presentation to the shopper.

For more information, refer to [Retrieve stored details](https://docs.adyen.com/classic-integration/recurring-payments/retrieve-stored-details/).

```python
def post_list_recurring_details(self,
                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RecurringDetailsRequest`](../../doc/models/recurring-details-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`RecurringDetailsResult`](../../doc/models/recurring-details-result.md)

## Example Usage

```python
body = RecurringDetailsRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    shopper_reference='YOUR_SHOPPER_REFERENCE',
    recurring=Recurring(
        contract=ContractEnum.RECURRING
    )
)

result = general_api.post_list_recurring_details(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Notify Shopper

Sends a request to the issuer so they can inform the shopper about the upcoming recurring payment. This endpoint is used only for local acquiring in India. For more information, refer to [Recurring card payments in India](https://docs.adyen.com/payment-methods/cards/cards-recurring-india).

```python
def post_notify_shopper(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`NotifyShopperRequest`](../../doc/models/notify-shopper-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`NotifyShopperResult`](../../doc/models/notify-shopper-result.md)

## Example Usage

```python
body = NotifyShopperRequest(
    amount=Amount(
        currency='INR',
        value=1000
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='Example reference',
    shopper_reference='YOUR_SHOPPER_REFERENCE',
    billing_date='2021-03-16',
    displayed_reference='exampleDisplayedReference',
    stored_payment_method_id='8415995487234100'
)

result = general_api.post_notify_shopper(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "message": "Request Processed Successfully",
  "resultCode": "Success",
  "shopperNotificationReference": "9915003646742627",
  "storedPaymentMethodId": "8415995487234100",
  "pspReference": "M5N7TQ4TG5PFWR50",
  "reference": "Example reference",
  "displayedReference": "exampleDisplayedReference"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Schedule Account Updater

When making the API call, you can submit either the credit card information, or the recurring detail reference and the shopper reference:

* If the card information is provided, all the sub-fields for `card` are mandatory.
* If the recurring detail reference is provided, the fields for `shopperReference` and `selectedRecurringDetailReference` are mandatory.

```python
def post_schedule_account_updater(self,
                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ScheduleAccountUpdaterRequest`](../../doc/models/schedule-account-updater-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ScheduleAccountUpdaterResult`](../../doc/models/schedule-account-updater-result.md)

## Example Usage

```python
body = ScheduleAccountUpdaterRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    reference='YOUR_REFERENCE',
    card=Card(
        expiry_month='03',
        expiry_year='2030',
        holder_name='Adyen Test',
        number='4111111111111111'
    )
)

result = general_api.post_schedule_account_updater(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "QFQTPCQ8HXSKGK82",
  "result": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Get 3 Ds Availability

Verifies whether 3D Secure is available for the specified BIN or card brand. For 3D Secure 2, this endpoint also returns device fingerprinting keys.

For more information, refer to [3D Secure 2](https://docs.adyen.com/online-payments/3d-secure/native-3ds2).

```python
def post_get_3_ds_availability(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ThreeDSAvailabilityRequest`](../../doc/models/three-ds-availability-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ThreeDSAvailabilityResponse`](../../doc/models/three-ds-availability-response.md)

## Example Usage

```python
body = ThreeDSAvailabilityRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    card_number='4111111111111111'
)

result = general_api.post_get_3_ds_availability(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "threeDS1Supported": true,
  "threeDS2CardRangeDetails": [],
  "threeDS2supported": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Get Cost Estimate

> This API is available only for merchants operating in Australia, the EU, and the UK.

Use the Adyen Cost Estimation API to pre-calculate interchange and scheme fee costs. Knowing these costs prior actual payment authorisation gives you an opportunity to charge those costs to the cardholder, if necessary.

To retrieve this information, make the call to the `/getCostEstimate` endpoint. The response to this call contains the amount of the interchange and scheme fees charged by the network for this transaction, and also which surcharging policy is possible (based on current regulations).

> Since not all information is known in advance (for example, if the cardholder will successfully authenticate via 3D Secure or if you also plan to provide additional Level 2/3 data), the returned amounts are based on a set of assumption criteria you define in the `assumptions` parameter.

```python
def post_get_cost_estimate(self,
                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CostEstimateRequest`](../../doc/models/cost-estimate-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CostEstimateResponse`](../../doc/models/cost-estimate-response.md)

## Example Usage

```python
body = CostEstimateRequest(
    amount=Amount(
        currency='EUR',
        value=1234
    ),
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    assumptions=CostEstimateAssumptions1(
        assume_3_d_secure_authenticated=True,
        assume_level_3_data=True
    ),
    card_number='5101180000000007',
    merchant_details=MerchantDetails2(
        country_code='NL',
        enrolled_in_3_d_secure=True,
        mcc='7411'
    ),
    shopper_interaction=ShopperInteractionEnum.ECOMMERCE
)

result = general_api.post_get_cost_estimate(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "costEstimateAmount": {
    "currency": "EUR",
    "value": 12
  },
  "resultCode": "Success"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Change Status

Changes the status of the provided payment method to the specified status.

```python
def post_change_status(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueStatusChangeRequest`](../../doc/models/stored-value-status-change-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueStatusChangeResponse`](../../doc/models/stored-value-status-change-response.md)

## Example Usage

```python
result = general_api.post_change_status()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Check Balance

Checks the balance of the provided payment method.

```python
def post_check_balance(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueBalanceCheckRequest`](../../doc/models/stored-value-balance-check-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueBalanceCheckResponse`](../../doc/models/stored-value-balance-check-response.md)

## Example Usage

```python
result = general_api.post_check_balance()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Issue

Issues a new card of the given payment method.

```python
def post_issue(self,
              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueIssueRequest`](../../doc/models/stored-value-issue-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueIssueResponse`](../../doc/models/stored-value-issue-response.md)

## Example Usage

```python
result = general_api.post_issue()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Load

Loads the payment method with the specified funds.

```python
def post_load(self,
             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueLoadRequest`](../../doc/models/stored-value-load-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueLoadResponse`](../../doc/models/stored-value-load-response.md)

## Example Usage

```python
result = general_api.post_load()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Merge Balance

Increases the balance of the paymentmethod by the full amount left on the source paymentmethod

```python
def post_merge_balance(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueBalanceMergeRequest`](../../doc/models/stored-value-balance-merge-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueBalanceMergeResponse`](../../doc/models/stored-value-balance-merge-response.md)

## Example Usage

```python
result = general_api.post_merge_balance()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Void Transaction

Voids the referenced stored value transaction.

```python
def post_void_transaction(self,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueVoidRequest`](../../doc/models/stored-value-void-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`StoredValueVoidResponse`](../../doc/models/stored-value-void-response.md)

## Example Usage

```python
result = general_api.post_void_transaction()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Request Subject Erasure

Sends the PSP reference containing the shopper data that should be deleted.

```python
def post_request_subject_erasure(self,
                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SubjectErasureByPspReferenceRequest`](../../doc/models/subject-erasure-by-psp-reference-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`SubjectErasureResponse`](../../doc/models/subject-erasure-response.md)

## Example Usage

```python
result = general_api.post_request_subject_erasure()
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Create Test Card Ranges

Creates one or more test card ranges.

```python
def post_create_test_card_ranges(self,
                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateTestCardRangesRequest`](../../doc/models/create-test-card-ranges-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CreateTestCardRangesResult`](../../doc/models/create-test-card-ranges-result.md)

## Example Usage

```python
body = CreateTestCardRangesRequest(
    account_code='accountCode4',
    account_type_code='accountTypeCode0',
    test_card_ranges=[
        TestCardRange(
            card_holder_name='cardHolderName0',
            expiry_month=ExpiryMonthEnum.DECEMBER,
            expiry_year=138,
            range_end='rangeEnd6',
            range_start='rangeStart4'
        )
    ]
)

result = general_api.post_create_test_card_ranges(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Create Notification Configuration

Creates a subscription to notifications informing you of events on your platform. After the subscription is created, the events specified in the configuration will be sent to the URL specified in the configuration. Subscriptions must be configured on a per-event basis (as opposed to, for example, a per-account holder basis), so all event notifications of a marketplace and of a given type will be sent to the same endpoint(s). A marketplace may have multiple endpoints if desired; an event notification may be sent to as many or as few different endpoints as configured.

```python
def post_create_notification_configuration(self,
                                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateNotificationConfigurationRequest`](../../doc/models/create-notification-configuration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetNotificationConfigurationResponse`](../../doc/models/get-notification-configuration-response.md)

## Example Usage

```python
body = CreateNotificationConfigurationRequest(
    configuration_details=NotificationConfigurationDetails4(
        active=True,
        description='Unique description 123',
        event_configs=[
            NotificationEventConfiguration(
                event_type=EventTypeEnum.ACCOUNT_HOLDER_VERIFICATION,
                include_mode=IncludeModeEnum.INCLUDE
            )
        ],
        notify_password='testPassword',
        notify_url='https://www.adyen.com/notification-handler',
        notify_username='testUserName',
        ssl_protocol=SslProtocolEnum.TLSV13
    )
)

result = general_api.post_create_notification_configuration(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8516178952380553",
  "configurationDetails": {
    "active": true,
    "description": "Unique description 123",
    "eventConfigs": [
      {
        "eventType": "ACCOUNT_HOLDER_VERIFICATION",
        "includeMode": "INCLUDE"
      }
    ],
    "notificationId": 28468,
    "notifyURL": "https://www.adyen.com/notification-handler",
    "sslProtocol": "TLSv13"
  }
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


# Post-Delete Notification Configurations

Deletes an existing notification subscription configuration. After the subscription is deleted, no further event notifications will be sent to the URL defined in the subscription.

```python
def post_delete_notification_configurations(self,
                                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteNotificationConfigurationRequest`](../../doc/models/delete-notification-configuration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GenericResponse`](../../doc/models/generic-response.md)

## Example Usage

```python
body = DeleteNotificationConfigurationRequest(
    notification_ids=[
        27891
    ]
)

result = general_api.post_delete_notification_configurations(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8516480472498802"
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


# Post-Get Notification Configuration

Returns the details of the configuration of a notification subscription.

```python
def post_get_notification_configuration(self,
                                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetNotificationConfigurationRequest`](../../doc/models/get-notification-configuration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetNotificationConfigurationResponse`](../../doc/models/get-notification-configuration-response.md)

## Example Usage

```python
body = GetNotificationConfigurationRequest(
    notification_id=21259
)

result = general_api.post_get_notification_configuration(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8616480378704419",
  "configurationDetails": {
    "active": true,
    "apiVersion": 5,
    "description": "test",
    "eventConfigs": [
      {
        "eventType": "ACCOUNT_HOLDER_VERIFICATION",
        "includeMode": "INCLUDE"
      }
    ],
    "notificationId": 50054,
    "notifyURL": "https://www.adyen.com/notification-handler",
    "sslProtocol": "TLSv13"
  }
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


# Post-Get Notification Configuration List

Returns the details of the configurations of all of the notification subscriptions in the platform of the executing user.

```python
def post_get_notification_configuration_list(self,
                                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | `Any` | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetNotificationConfigurationListResponse`](../../doc/models/get-notification-configuration-list-response.md)

## Example Usage

```python
body = jsonpickle.decode('{}')

result = general_api.post_get_notification_configuration_list(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8516480437185726",
  "configurations": [
    {
      "active": true,
      "description": "Unique description 12223",
      "eventConfigs": [
        {
          "eventType": "ACCOUNT_HOLDER_VERIFICATION",
          "includeMode": "INCLUDE"
        }
      ],
      "notificationId": 27893,
      "notifyURL": "https://www.adyen.com/notification-handler",
      "sslProtocol": "TLSv13"
    },
    {
      "active": true,
      "description": "just testing things",
      "eventConfigs": [
        {
          "eventType": "ACCOUNT_HOLDER_VERIFICATION",
          "includeMode": "INCLUDE"
        }
      ],
      "notificationId": 25032,
      "notifyURL": "https://www.adyen.com/notification-handler",
      "sslProtocol": "TLSv13"
    }
  ]
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


# Post-Test Notification Configuration

Tests an existing notification subscription configuration. For each event type specified, a test notification will be generated and sent to the URL configured in the subscription specified.

```python
def post_test_notification_configuration(self,
                                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TestNotificationConfigurationRequest`](../../doc/models/test-notification-configuration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`TestNotificationConfigurationResponse`](../../doc/models/test-notification-configuration-response.md)

## Example Usage

```python
body = TestNotificationConfigurationRequest(
    notification_id=25032,
    event_types=[
        EventType1Enum.ACCOUNT_HOLDER_VERIFICATION
    ]
)

result = general_api.post_test_notification_configuration(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8616480452462678",
  "errorMessages": [
    "The server did not respond with HTTP 2XX"
  ],
  "eventTypes": [
    "ACCOUNT_HOLDER_VERIFICATION"
  ],
  "exchangeMessages": [
    {
      "messageCode": "Number",
      "messageDescription": "1"
    },
    {
      "messageCode": "Title",
      "messageDescription": "Test 1: 8616480452462678"
    }
  ],
  "notificationId": 25032,
  "okMessages": [
    "...",
    "ResponseTime_ms: 262",
    "ResponseCode: 404"
  ]
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


# Post-Update Notification Configuration

Updates an existing notification subscription configuration. If you are updating the event types, you must provide all event types, otherwise the previous event type configuration will be overwritten.

```python
def post_update_notification_configuration(self,
                                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateNotificationConfigurationRequest`](../../doc/models/update-notification-configuration-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetNotificationConfigurationResponse`](../../doc/models/get-notification-configuration-response.md)

## Example Usage

```python
body = UpdateNotificationConfigurationRequest(
    configuration_details=NotificationConfigurationDetails3(
        active=False,
        description='Test notif config 756',
        event_configs=[
            NotificationEventConfiguration(
                event_type=EventTypeEnum.ACCOUNT_HOLDER_CREATED,
                include_mode=IncludeModeEnum.EXCLUDE
            ),
            NotificationEventConfiguration(
                event_type=EventTypeEnum.ACCOUNT_CREATED,
                include_mode=IncludeModeEnum.INCLUDE
            )
        ],
        notification_id=21259,
        notify_password='testPassword2',
        notify_url='https://www.adyen.com/notification-handler',
        notify_username='testUserName2',
        ssl_protocol=SslProtocolEnum.TLSV13
    )
)

result = general_api.post_update_notification_configuration(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "8516178952580574",
  "configurationDetails": {
    "active": false,
    "description": "Test notif config 756",
    "eventConfigs": [
      {
        "eventType": "ACCOUNT_CREATED",
        "includeMode": "INCLUDE"
      },
      {
        "eventType": "ACCOUNT_HOLDER_CREATED",
        "includeMode": "EXCLUDE"
      }
    ],
    "notificationId": 21259,
    "notifyURL": "https://www.adyen.com/notification-handler",
    "sslProtocol": "TLSv13"
  }
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


# Post-Account Holder Balance

Returns the account balances of an account holder. An account's balances are organized according by currencies. This mean that an account may have multiple balances: one for each currency.

```python
def post_account_holder_balance(self,
                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CloseAccountHolderRequest`](../../doc/models/close-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AccountHolderBalanceResponse`](../../doc/models/account-holder-balance-response.md)

## Example Usage

```python
body = CloseAccountHolderRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER'
)

result = general_api.post_account_holder_balance(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Account Holder Transaction List

Returns a list of transactions for an account holder's accounts. You can specify the accounts and transaction statuses to be included on the list. The call returns a maximum of 50 transactions for each account. To retrieve all transactions, you must make another call with the 'page' value incremented. Transactions are listed in chronological order, with the most recent transaction first.

```python
def post_account_holder_transaction_list(self,
                                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountHolderTransactionListRequest`](../../doc/models/account-holder-transaction-list-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AccountHolderTransactionListResponse`](../../doc/models/account-holder-transaction-list-response.md)

## Example Usage

```python
body = AccountHolderTransactionListRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    transaction_lists_per_account=[
        TransactionListForAccount(
            account_code='195752115',
            page=1
        )
    ]
)

result = general_api.post_account_holder_transaction_list(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Debit Account Holder

Sends a direct debit request to an account holder's bank account. If the direct debit is successful, the funds are settled in the accounts specified in the split instructions. Adyen sends the result of the direct debit in a [`DIRECT_DEBIT_INITIATED`](https://docs.adyen.com/api-explorer/#/NotificationService/latest/post/DIRECT_DEBIT_INITIATED) notification webhook.

To learn more about direct debits, see [Top up accounts](https://docs.adyen.com/classic-platforms/top-up-accounts).

```python
def post_debit_account_holder(self,
                             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DebitAccountHolderRequest`](../../doc/models/debit-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DebitAccountHolderResponse`](../../doc/models/debit-account-holder-response.md)

## Example Usage

```python
body = DebitAccountHolderRequest(
    account_holder_code='ACCOUNT_HOLDER_CODE',
    amount=Amount(
        currency='USD',
        value=6200
    ),
    bank_account_uuid='000b81aa-ae7e-4492-aa7e-72b2129dce0c',
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    splits=[
        Split1(
            mtype=Type60Enum.MARKETPLACE,
            account='8535516988037431',
            amount=SplitAmount(
                value=6000
            ),
            reference='YOUR_SPLIT_REFERENCE_1'
        ),
        Split1(
            mtype=Type60Enum.COMMISSION,
            amount=SplitAmount(
                value=200
            ),
            reference='YOUR_SPLIT_REFERENCE_2'
        )
    ],
    description='YOUR_DESCRIPTION'
)

result = general_api.post_debit_account_holder(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Payout Account Holder

Pays out a specified amount from an account to the bank account of account holder.

```python
def post_payout_account_holder(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PayoutAccountHolderRequest`](../../doc/models/payout-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`PayoutAccountHolderResponse`](../../doc/models/payout-account-holder-response.md)

## Example Usage

```python
body = PayoutAccountHolderRequest(
    account_code='118731451',
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    amount=Amount(
        currency='EUR',
        value=99792
    ),
    bank_account_uuid='000b81aa-ae7e-4492-aa7e-72b2129dce0c',
    description='12345 – Test'
)

result = general_api.post_payout_account_holder(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Refund Funds Transfer

Refunds funds transferred from one account to another. Both accounts must be in the same platform, but can have different account holders.

```python
def post_refund_funds_transfer(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RefundFundsTransferRequest`](../../doc/models/refund-funds-transfer-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`RefundFundsTransferResponse`](../../doc/models/refund-funds-transfer-response.md)

## Example Usage

```python
body = RefundFundsTransferRequest(
    amount=Amount(
        currency='EUR',
        value=1000
    ),
    original_reference='PSP_REFERENCE_OF_TRANSFER_TO_REFUND',
    merchant_reference='YOUR_REFERENCE_ID'
)

result = general_api.post_refund_funds_transfer(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Refund Not Paid Out Transfers

Refunds all the transactions of an account that have taken place since the most recent payout. This request is on a account basis (as opposed to a payment basis), so only the portion of the payment that was made to the specified account is refunded. The commissions, fees, and payments to other accounts remain in the accounts to which they were sent as designated by the original payment's split details.

```python
def post_refund_not_paid_out_transfers(self,
                                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`RefundNotPaidOutTransfersRequest`](../../doc/models/refund-not-paid-out-transfers-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GenericResponse`](../../doc/models/generic-response.md)

## Example Usage

```python
body = RefundNotPaidOutTransfersRequest(
    account_code='189184578',
    account_holder_code='CODE_OF_ACCOUNT_HOLDER'
)

result = general_api.post_refund_not_paid_out_transfers(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Setup Beneficiary

Defines a benefactor and a beneficiary relationship between two accounts. At the time of benefactor/beneficiary setup, the funds in the benefactor account are transferred to the beneficiary account, and any further payments to the benefactor account are automatically sent to the beneficiary account. A series of benefactor/beneficiaries may not exceed four beneficiaries and may not have a cycle in it.

```python
def post_setup_beneficiary(self,
                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SetupBeneficiaryRequest`](../../doc/models/setup-beneficiary-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GenericResponse`](../../doc/models/generic-response.md)

## Example Usage

```python
body = SetupBeneficiaryRequest(
    destination_account_code='128952522',
    source_account_code='134498192',
    merchant_reference='YOUR_REFERENCE_ID'
)

result = general_api.post_setup_beneficiary(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Transfer Funds

Transfers funds from one account to another account. Both accounts must be in the same platform, but can have different account holders. The transfer must include a transfer code, which should be determined by the platform, in compliance with local regulations.

```python
def post_transfer_funds(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransferFundsRequest`](../../doc/models/transfer-funds-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`TransferFundsResponse`](../../doc/models/transfer-funds-response.md)

## Example Usage

```python
body = TransferFundsRequest(
    amount=Amount(
        currency='EUR',
        value=2000
    ),
    destination_account_code='190324759',
    source_account_code='100000000',
    transfer_code='TransferCode_1'
)

result = general_api.post_transfer_funds(
    body=body
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Accept Dispute

Accepts a specific dispute.

```python
def post_accept_dispute(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AcceptDisputeRequest`](../../doc/models/accept-dispute-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AcceptDisputeResponse`](../../doc/models/accept-dispute-response.md)

## Example Usage

```python
body = AcceptDisputeRequest(
    dispute_psp_reference='DZ4DPSHB4WD2WN82',
    merchant_account_code='YOUR_MERCHANT_ACCOUNT'
)

result = general_api.post_accept_dispute(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "disputeServiceResult": {
    "success": true
  }
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


# Post-Defend Dispute

Defends a specific dispute.

```python
def post_defend_dispute(self,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DefendDisputeRequest`](../../doc/models/defend-dispute-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DefendDisputeResponse`](../../doc/models/defend-dispute-response.md)

## Example Usage

```python
body = DefendDisputeRequest(
    defense_reason_code='SupplyDefenseMaterial',
    dispute_psp_reference='DZ4DPSHB4WD2WN82',
    merchant_account_code='YOUR_MERCHANT_ACCOUNT'
)

result = general_api.post_defend_dispute(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "disputeServiceResult": {
    "success": true
  }
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


# Post-Delete Dispute Defense Document

Deletes a specific dispute defense document that was supplied earlier.

```python
def post_delete_dispute_defense_document(self,
                                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DeleteDefenseDocumentRequest`](../../doc/models/delete-defense-document-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DeleteDefenseDocumentResponse`](../../doc/models/delete-defense-document-response.md)

## Example Usage

```python
body = DeleteDefenseDocumentRequest(
    defense_document_type='DefenseMaterial',
    dispute_psp_reference='DZ4DPSHB4WD2WN82',
    merchant_account_code='YOUR_MERCHANT_ACCOUNT'
)

result = general_api.post_delete_dispute_defense_document(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "disputeServiceResult": {
    "success": true
  }
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


# Post-Retrieve Applicable Defense Reasons

Returns a list of all applicable defense reasons to defend a specific dispute.

```python
def post_retrieve_applicable_defense_reasons(self,
                                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DefenseReasonsRequest`](../../doc/models/defense-reasons-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DefenseReasonsResponse`](../../doc/models/defense-reasons-response.md)

## Example Usage

```python
body = DefenseReasonsRequest(
    dispute_psp_reference='DZ4DPSHB4WD2WN82',
    merchant_account_code='YOUR_MERCHANT_ACCOUNT'
)

result = general_api.post_retrieve_applicable_defense_reasons(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "defenseReasons": [
    {
      "defenseDocumentTypes": [
        {
          "available": false,
          "defenseDocumentTypeCode": "TIDorInvoice",
          "requirementLevel": "Optional"
        },
        {
          "available": false,
          "defenseDocumentTypeCode": "GoodsNotReturned",
          "requirementLevel": "Required"
        }
      ],
      "defenseReasonCode": "GoodsNotReturned",
      "satisfied": false
    },
    {
      "defenseDocumentTypes": [
        {
          "available": false,
          "defenseDocumentTypeCode": "TIDorInvoice",
          "requirementLevel": "Optional"
        },
        {
          "available": false,
          "defenseDocumentTypeCode": "GoodsRepairedOrReplaced",
          "requirementLevel": "Required"
        }
      ],
      "defenseReasonCode": "GoodsRepairedOrReplaced",
      "satisfied": false
    },
    {
      "defenseDocumentTypes": [
        {
          "available": false,
          "defenseDocumentTypeCode": "GoodsWereAsDescribed",
          "requirementLevel": "Required"
        },
        {
          "available": false,
          "defenseDocumentTypeCode": "TIDorInvoice",
          "requirementLevel": "Required"
        }
      ],
      "defenseReasonCode": "GoodsWereAsDescribed",
      "satisfied": false
    },
    {
      "defenseDocumentTypes": [
        {
          "available": false,
          "defenseDocumentTypeCode": "TIDorInvoice",
          "requirementLevel": "Optional"
        },
        {
          "available": false,
          "defenseDocumentTypeCode": "DefenseMaterial",
          "requirementLevel": "Required"
        }
      ],
      "defenseReasonCode": "SupplyDefenseMaterial",
      "satisfied": false
    }
  ],
  "disputeServiceResult": {
    "success": true
  }
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


# Post-Supply Defense Document

Supplies a specific dispute defense document.

```python
def post_supply_defense_document(self,
                                body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SupplyDefenseDocumentRequest`](../../doc/models/supply-defense-document-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`SupplyDefenseDocumentResponse`](../../doc/models/supply-defense-document-response.md)

## Example Usage

```python
body = SupplyDefenseDocumentRequest(
    defense_documents=[
        DefenseDocument(
            content='JVBERi0xLjQKJcOkw7zDtsOfCjIgMCBv+f/ub0j6JPRX+E3EmC==',
            content_type='application/pdf',
            defense_document_type_code='DefenseMaterial'
        )
    ],
    dispute_psp_reference='DZ4DPSHB4WD2WN82',
    merchant_account_code='YOUR_MERCHANT_ACCOUNT'
)

result = general_api.post_supply_defense_document(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "disputeServiceResult": {
    "success": true
  }
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


# Post-Sessions

**This endpoint is deprecated.**

Establishes a secure communications session between the POS Mobile SDK and the Adyen payments platform, through mutual authentication.
The request sends a setup token that identifies the SDK and the device. The response returns a session token that the SDK can use to authenticate responses received from the Adyen payments platform.

> This request applies to **mobile in-person** transactions. You cannot use this request to create online payments sessions.

```python
def post_sessions(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateSessionRequest`](../../doc/models/create-session-request.md) | Body, Optional | - |

## Response Type

**201**: Created - the request has been fulfilled and has resulted in one or more new resources being created.

[`CertificateLoadingResponse`](../../doc/models/certificate-loading-response.md)

## Example Usage

```python
body = CreateSessionRequest(
    merchant_account='YOUR_MERCHANT_ACCOUNT',
    setup_token='SETUP_TOKEN',
    store='YOUR_STORE_ID'
)

result = general_api.post_sessions(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "id": "APP_SESSION_ID",
  "installationId": "INSTALLATION_ID",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "store": "YOUR_STORE_ID",
  "sdkData": "SDK_DATA_BLOB"
}
```


# Post-Assign Terminals

**This endpoint is deprecated.**

Assigns one or more payment terminals to a merchant account or a store. You can also use this endpoint to reassign terminals between merchant accounts or stores, and to unassign a terminal and return it to company inventory.

> From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

```python
def post_assign_terminals(self,
                         body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AssignTerminalsRequest`](../../doc/models/assign-terminals-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AssignTerminalsResponse`](../../doc/models/assign-terminals-response.md)

## Example Usage

```python
body = AssignTerminalsRequest(
    company_account='YOUR_COMPANY_ACCOUNT',
    terminals=[
        'P400Plus-275479597'
    ]
)

result = general_api.post_assign_terminals(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "results": {
    "P400Plus-275479597": "RemoveConfigScheduled"
  }
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


# Post-Find Terminal

**This endpoint is deprecated.**

Returns the company account, merchant account, or store that a payment terminal is assigned to.

> From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

```python
def post_find_terminal(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`FindTerminalRequest`](../../doc/models/find-terminal-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`FindTerminalResponse`](../../doc/models/find-terminal-response.md)

## Example Usage

```python
body = FindTerminalRequest(
    terminal='M400-401972715'
)

result = general_api.post_find_terminal(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "companyAccount": "YOUR_COMPANY_ACCOUNT",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "merchantInventory": false,
  "store": "YOUR_STORE",
  "terminal": "M400-401972715"
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


# Post-Get Stores Under Account

**This endpoint is deprecated.**

Returns a list of stores associated with a company account or a merchant account, including the status of each store.

> From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

```python
def post_get_stores_under_account(self,
                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetStoresUnderAccountRequest`](../../doc/models/get-stores-under-account-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetStoresUnderAccountResponse`](../../doc/models/get-stores-under-account-response.md)

## Example Usage

```python
body = GetStoresUnderAccountRequest(
    company_account='YOUR_COMPANY_ACCOUNT'
)

result = general_api.post_get_stores_under_account(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "stores": [
    {
      "store": "YOUR_STORE",
      "description": "YOUR_STORE",
      "address": {
        "city": "The City",
        "countryCode": "NL",
        "postalCode": "1234",
        "streetAddress": "The Street"
      },
      "status": "Active",
      "merchantAccountCode": "YOUR_MERCHANT_ACCOUNT"
    }
  ]
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


# Post-Get Terminal Details

**This endpoint is deprecated.**

Returns the details of a payment terminal, including where the terminal is assigned to. The response returns the same details that are provided in the terminal list in your Customer Area and in the Terminal Fleet report.

> From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

```python
def post_get_terminal_details(self,
                             body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTerminalDetailsRequest`](../../doc/models/get-terminal-details-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetTerminalDetailsResponse`](../../doc/models/get-terminal-details-response.md)

## Example Usage

```python
body = GetTerminalDetailsRequest(
    terminal='M400-401972715'
)

result = general_api.post_get_terminal_details(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "companyAccount": "YOUR_COMPANY_ACCOUNT",
  "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
  "merchantInventory": false,
  "store": "YOUR_STORE",
  "terminal": "M400-401972715",
  "deviceModel": "M400",
  "serialNumber": "401-972-715",
  "permanentTerminalId": "88912016",
  "terminalStatus": "SwitchedOff",
  "firmwareVersion": "Verifone_VOS 1.57.6",
  "country": "NETHERLANDS",
  "storeDetails": {
    "store": "YOUR_STORE",
    "description": "TestStore",
    "address": {
      "city": "The City",
      "countryCode": "NL",
      "postalCode": "1234",
      "streetAddress": "The Street"
    }
  },
  "ethernetMac": "60:c7:98:5a:69:cd",
  "ethernetIp": "192.168.2.11",
  "wifiMac": "c4:ac:59:47:f3:71",
  "wifiIp": "192.168.2.12",
  "dhcpEnabled": false
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


# Post-Get Terminals Under Account

**This endpoint is deprecated.**

Returns a list of payment terminals associated with a company account, merchant account, or store. The response shows whether the terminals are in the inventory, or in-store (ready for boarding or already boarded).

> From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

```python
def post_get_terminals_under_account(self,
                                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTerminalsUnderAccountRequest`](../../doc/models/get-terminals-under-account-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetTerminalsUnderAccountResponse`](../../doc/models/get-terminals-under-account-response.md)

## Example Usage

```python
body = GetTerminalsUnderAccountRequest(
    company_account='YOUR_COMPANY_ACCOUNT'
)

result = general_api.post_get_terminals_under_account(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "companyAccount": "YOUR_COMPANY_ACCOUNT",
  "merchantAccounts": [
    {
      "merchantAccount": "YOUR_MERCHANT_ACCOUNT",
      "inStoreTerminals": [
        "P400Plus-275479597"
      ],
      "stores": [
        {
          "store": "YOUR_STORE",
          "inStoreTerminals": [
            "M400-401972715"
          ]
        }
      ]
    }
  ]
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

