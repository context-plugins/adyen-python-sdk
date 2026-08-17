# Accountholders

```python
accountholders_api = client.accountholders
```

## Class Name

`AccountholdersApi`

## Methods

* [Post-Close Account Holder](../../doc/controllers/accountholders.md#post-close-account-holder)
* [Post-Close Stores](../../doc/controllers/accountholders.md#post-close-stores)
* [Post-Create Account Holder](../../doc/controllers/accountholders.md#post-create-account-holder)
* [Post-Get Account Holder](../../doc/controllers/accountholders.md#post-get-account-holder)
* [Post-Get Tax Form](../../doc/controllers/accountholders.md#post-get-tax-form)
* [Post-Suspend Account Holder](../../doc/controllers/accountholders.md#post-suspend-account-holder)
* [Post-Un Suspend Account Holder](../../doc/controllers/accountholders.md#post-un-suspend-account-holder)
* [Post-Update Account Holder](../../doc/controllers/accountholders.md#post-update-account-holder)
* [Post-Update Account Holder State](../../doc/controllers/accountholders.md#post-update-account-holder-state)
* [Post-Account Holders](../../doc/controllers/accountholders.md#post-account-holders)
* [Get-Account Holders-Id](../../doc/controllers/accountholders.md#get-account-holders-id)
* [Patch-Account Holders-Id](../../doc/controllers/accountholders.md#patch-account-holders-id)
* [Get-Account Holders-Id-Balance Accounts](../../doc/controllers/accountholders.md#get-account-holders-id-balance-accounts)
* [Get-Account Holders-Id-Tax Forms](../../doc/controllers/accountholders.md#get-account-holders-id-tax-forms)
* [Get-Account Holders-Id-Transaction Rules](../../doc/controllers/accountholders.md#get-account-holders-id-transaction-rules)
* [Get-Account Holders-Id-Tax Form Summary](../../doc/controllers/accountholders.md#get-account-holders-id-tax-form-summary)


# Post-Close Account Holder

Changes the [status of an account holder](https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses) to **Closed**. This state is final. If an account holder is closed, you can't process transactions, pay out funds, or reopen it. If payments are made to an account of an account holder with a **Closed** [`status`](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status), the payments are sent to your liable account.

```python
def post_close_account_holder(self,
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

[`CloseAccountHolderResponse`](../../doc/models/close-account-holder-response.md)

## Example Usage

```python
body = CloseAccountHolderRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER'
)

result = account_holders_api.post_close_account_holder(
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


# Post-Close Stores

Closes stores associated with an account holder.

```python
def post_close_stores(self,
                     body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CloseStoresRequest`](../../doc/models/close-stores-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GenericResponse`](../../doc/models/generic-response.md)

## Example Usage

```python
result = account_holders_api.post_close_stores()
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


# Post-Create Account Holder

Creates an account holder that [represents the sub-merchant's entity](https://docs.adyen.com/classic-platforms/account-structure#your-platform) in your platform. The details that you need to provide in the request depend on the sub-merchant's legal entity type. For more information, refer to [Account holder and accounts](https://docs.adyen.com/classic-platforms/account-holders-and-accounts#legal-entity-types).

```python
def post_create_account_holder(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CreateAccountHolderRequest`](../../doc/models/create-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`CreateAccountHolderResponse`](../../doc/models/create-account-holder-response.md)

## Example Usage

```python
body = CreateAccountHolderRequest(
    account_holder_code='YOUR_UNIQUE_ACCOUNT_HOLDER_CODE',
    account_holder_details=AccountHolderDetails1(
        address=ViasAddress9(
            country='US'
        ),
        business_details=BusinessDetails3(
            doing_business_as='Real Good Restaurant',
            legal_business_name='Real Good Restaurant Inc.',
            shareholders=[
                ShareholderContact(
                    address=ViasAddress2(
                        country='NL'
                    ),
                    email='testshareholder@email.com',
                    name=ViasName1(
                        first_name='John',
                        last_name='Carpenter'
                    ),
                    shareholder_type=ShareholderTypeEnum.CONTROLLER
                )
            ]
        ),
        email='test@email.com',
        web_address='https://www.your-website.com'
    ),
    legal_entity=LegalEntityEnum.BUSINESS
)

result = account_holders_api.post_create_account_holder(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "pspReference": "ALPHANUMERIC_UNIQUE_RESPONSE_REFERENCE",
  "accountHolderCode": "YOUR_UNIQUE_ACCOUNT_HOLDER_CODE",
  "accountHolderDetails": {
    "address": {
      "country": "US"
    },
    "bankAccountDetails": [],
    "businessDetails": {
      "doingBusinessAs": "Real Good Restaurant",
      "legalBusinessName": "Real Good Restaurant Inc.",
      "shareholders": [
        {
          "address": {
            "country": "NL"
          },
          "email": "testshareholder@email.com",
          "name": {
            "firstName": "John",
            "lastName": "Carpenter"
          },
          "shareholderCode": "SHAREHOLDER_CODE",
          "shareholderType": "Controller"
        }
      ]
    },
    "email": "test@email.com",
    "merchantCategoryCode": "MCC_DEFAULT_VALUE",
    "payoutMethods": [],
    "webAddress": "https://www.your-website.com"
  },
  "accountHolderStatus": {
    "status": "Active",
    "processingState": {
      "disabled": false,
      "processedFrom": {
        "currency": "USD",
        "value": 0
      },
      "processedTo": {
        "currency": "USD",
        "value": 0
      },
      "tierNumber": 0
    },
    "payoutState": {
      "allowPayout": true,
      "payoutLimit": {
        "currency": "USD",
        "value": 0
      },
      "disabled": false,
      "tierNumber": 0
    },
    "events": []
  },
  "legalEntity": "Business",
  "invalidFields": [],
  "verification": {}
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


# Post-Get Account Holder

Returns the details of an account holder.

```python
def post_get_account_holder(self,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetAccountHolderRequest`](../../doc/models/get-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetAccountHolderResponse`](../../doc/models/get-account-holder-response.md)

## Example Usage

```python
body = GetAccountHolderRequest(
    account_code='CODE_OF_ACCOUNT'
)

result = account_holders_api.post_get_account_holder(
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


# Post-Get Tax Form

Generates a tax form for account holders operating in the US. For more information, refer to [Providing tax forms](https://docs.adyen.com/classic-platforms/tax-forms).

```python
def post_get_tax_form(self,
                     body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTaxFormRequest`](../../doc/models/get-tax-form-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetTaxFormResponse`](../../doc/models/get-tax-form-response.md)

## Example Usage

```python
body = GetTaxFormRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    form_type='1099-K',
    year=2020
)

result = account_holders_api.post_get_tax_form(
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


# Post-Suspend Account Holder

Changes the [status of an account holder](https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses) to **Suspended**.

```python
def post_suspend_account_holder(self,
                               body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`SuspendAccountHolderRequest`](../../doc/models/suspend-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`SuspendAccountHolderResponse`](../../doc/models/suspend-account-holder-response.md)

## Example Usage

```python
body = SuspendAccountHolderRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER'
)

result = account_holders_api.post_suspend_account_holder(
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


# Post-Un Suspend Account Holder

Changes the [status of an account holder](https://docs.adyen.com/classic-platforms/account-holders-and-accounts#account-holder-statuses) from **Suspended** to **Inactive**.
Account holders can have a **Suspended** [`status`](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status) if you suspend them through the [`/suspendAccountHolder`](https://docs.adyen.com/api-explorer/#/Account/v5/post/suspendAccountHolder) endpoint or if a verification deadline expires.

You can only unsuspend account holders if they do not have verification checks with a **FAILED** [`status`](https://docs.adyen.com/api-explorer/#/Account/latest/post/getAccountHolder__resParam_verification-accountHolder-checks-status).

```python
def post_un_suspend_account_holder(self,
                                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UnSuspendAccountHolderRequest`](../../doc/models/un-suspend-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`UnSuspendAccountHolderResponse`](../../doc/models/un-suspend-account-holder-response.md)

## Example Usage

```python
body = UnSuspendAccountHolderRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER'
)

result = account_holders_api.post_un_suspend_account_holder(
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


# Post-Update Account Holder

Updates the `accountHolderDetails` and `processingTier` of an account holder, and adds bank accounts and shareholders.

When updating `accountHolderDetails`, parameters that are not included in the request are left unchanged except for the following object:

* `metadata`: Updating the metadata replaces the entire object. This means that to update an existing key-value pair, you must provide the changes, as well as other existing key-value pairs.

When updating any field in the following objects, you must submit all the fields required for validation:

* `address`

* `fullPhoneNumber`

* `bankAccountDetails.BankAccountDetail`

* `businessDetails.shareholders.ShareholderContact`

For example, to update the `address.postalCode`, you must also submit the `address.country`, `.city`, `.street`, `.postalCode`, and possibly `.stateOrProvince` so that the address can be validated.

To add a bank account or shareholder, provide the bank account or shareholder details without a `bankAccountUUID` or a `shareholderCode`.

```python
def post_update_account_holder(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateAccountHolderRequest`](../../doc/models/update-account-holder-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`UpdateAccountHolderResponse`](../../doc/models/update-account-holder-response.md)

## Example Usage

```python
body = UpdateAccountHolderRequest(
    account_holder_code='YOUR_UNIQUE_ACCOUNT_HOLDER_CODE',
    account_holder_details=AccountHolderDetails4(
        address=ViasAddress9(
            country='US',
            city='NY',
            house_number_or_name='100',
            postal_code='12345',
            state_or_province='NH',
            street='Main Street'
        ),
        email='test@adyen.com',
        full_phone_number='+31612345678',
        merchant_category_code='7999',
        web_address='http://www.accountholderwebsite.com'
    )
)

result = account_holders_api.post_update_account_holder(
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


# Post-Update Account Holder State

Disables or enables the processing or payout state of an account holder.

```python
def post_update_account_holder_state(self,
                                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`UpdateAccountHolderStateRequest`](../../doc/models/update-account-holder-state-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`GetAccountHolderStatusResponse`](../../doc/models/get-account-holder-status-response.md)

## Example Usage

```python
body = UpdateAccountHolderStateRequest(
    account_holder_code='CODE_OF_ACCOUNT_HOLDER',
    disable=True,
    state_type=StateTypeEnum.PAYOUT,
    reason='test reason payout'
)

result = account_holders_api.post_update_account_holder_state(
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


# Post-Account Holders

Creates an account holder linked to a [legal entity](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/legalEntities).

```python
def post_account_holders(self,
                        body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AccountHolderInfo`](../../doc/models/account-holder-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AccountHolder`](../../doc/models/account-holder.md)

## Example Usage

```python
body = AccountHolderInfo(
    legal_entity_id='LE322JV223222D5GG42KN6869',
    description='Account holder used for international payments and payouts',
    reference='S.Eller-001'
)

result = account_holders_api.post_account_holders(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "description": "Account holder used for international payments and payouts",
  "legalEntityId": "LE322JV223222D5GG42KN6869",
  "reference": "S.Eller-001",
  "capabilities": {
    "receiveFromPlatformPayments": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "receiveFromBalanceAccount": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "sendToBalanceAccount": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "sendToTransferInstrument": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "requestedSettings": {
        "interval": "daily",
        "maxAmount": {
          "currency": "EUR",
          "value": 0
        }
      },
      "verificationStatus": "pending"
    }
  },
  "id": "AH3227C223222H5J4DCLW9VBV",
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


# Get-Account Holders-Id

Returns an account holder.

```python
def get_account_holders_id(self,
                          id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |

## Response Type

**200**: OK - the request has succeeded.

[`AccountHolder`](../../doc/models/account-holder.md)

## Example Usage

```python
id = 'id0'

result = account_holders_api.get_account_holders_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "description": "Account holder used for international payments and payouts",
  "legalEntityId": "LE322JV223222D5GG42KN6869",
  "reference": "S.Eller-001",
  "capabilities": {
    "receiveFromPlatformPayments": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "receiveFromBalanceAccount": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "sendToBalanceAccount": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    },
    "sendToTransferInstrument": {
      "enabled": true,
      "requested": true,
      "allowed": false,
      "transferInstruments": [
        {
          "enabled": true,
          "requested": true,
          "allowed": false,
          "id": "SE322KH223222F5GXZFNM3BGP",
          "verificationStatus": "pending"
        }
      ],
      "verificationStatus": "pending"
    }
  },
  "id": "AH3227C223222C5GXQXF658WB",
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


# Patch-Account Holders-Id

Updates an account holder. When updating an account holder resource, if a parameter is not provided in the request, it is left unchanged.

```python
def patch_account_holders_id(self,
                            id,
                            body=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |
| `body` | [`AccountHolderUpdateRequest`](../../doc/models/account-holder-update-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`AccountHolder`](../../doc/models/account-holder.md)

## Example Usage

```python
id = 'id0'

body = AccountHolderUpdateRequest(
    capabilities={
        'receivePayments': AccountHolderCapability(
            requested=True
        )
    },
    description='Account holder used for international payments and payouts',
    reference='S.Eller-001'
)

result = account_holders_api.patch_account_holders_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balancePlatform": "YOUR_BALANCE_PLATFORM",
  "description": "Account holder used for international payments and payouts",
  "legalEntityId": "LE322JV223222F5GKQZZ9DS99",
  "reference": "S.Eller-001",
  "capabilities": {
    "receivePayments": {
      "enabled": false,
      "requested": true,
      "allowed": false,
      "verificationStatus": "pending"
    }
  },
  "id": "AH3227C223222C5GKR23686TF",
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


# Get-Account Holders-Id-Balance Accounts

Returns a paginated list of the balance accounts associated with an account holder. To fetch multiple pages, use the query parameters.

For example, to limit the page to 5 balance accounts and skip the first 10, use `/accountHolders/{id}/balanceAccounts?limit=5&offset=10`.

```python
def get_account_holders_id_balance_accounts(self,
                                           id,
                                           offset=None,
                                           limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |
| `offset` | `int` | Query, Optional | The number of items that you want to skip. |
| `limit` | `int` | Query, Optional | The number of items returned per page, maximum 100 items. By default, the response returns 10 items per page. |

## Response Type

**200**: OK - the request has succeeded.

[`PaginatedBalanceAccountsResponse`](../../doc/models/paginated-balance-accounts-response.md)

## Example Usage

```python
id = 'id0'

result = account_holders_api.get_account_holders_id_balance_accounts(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "balanceAccounts": [
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CTDNB66W2Z",
      "status": "active"
    },
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CTDQPM6W2H",
      "status": "active"
    },
    {
      "accountHolderId": "AH32272223222B5CTBMZT6W2V",
      "defaultCurrencyCode": "EUR",
      "description": "S. Hopper - Main Account",
      "reference": "YOUR_REFERENCE-X173L",
      "timeZone": "Europe/Amsterdam",
      "id": "BA32272223222B5CVF5J63LMW",
      "status": "active"
    }
  ],
  "hasNext": true,
  "hasPrevious": false
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


# Get-Account Holders-Id-Tax Forms

Generates a tax form for account holders operating in the US. For more information, refer to US tax forms for [marketplaces](https://docs.adyen.com/marketplaces/us-tax-forms/) or [platforms](https://docs.adyen.com/platforms/us-tax-forms/) .

```python
def get_account_holders_id_tax_forms(self,
                                    id,
                                    form_type,
                                    year,
                                    legal_entity_id=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |
| `form_type` | [`FormTypeEnum`](../../doc/models/form-type-enum.md) | Query, Required | The type of tax form you want to retrieve. Accepted values are **US1099k** and **US1099nec**. |
| `year` | `int` | Query, Required | The tax year in **YYYY** format for the tax form you want to retrieve. |
| `legal_entity_id` | `str` | Query, Optional | The legal entity reference whose tax form you want to retrieve. |

## Response Type

**200**: OK - the request has succeeded.

[`GetTaxFormResponse1`](../../doc/models/get-tax-form-response-1.md)

## Example Usage

```python
id = 'id0'

form_type = FormTypeEnum.US1099K

year = 248

result = account_holders_api.get_account_holders_id_tax_forms(
    id,
    form_type,
    year
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "content": "JVBERi0xLjcKJcfsj6IKJSVJbnZvY2F0aW9uOiBwYXRoL2dzd2luNjQuZXhlIC1kRGlzcGxh",
  "contentType": "application/pdf"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 404 | The requested tax form was not available. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Account Holders-Id-Transaction Rules

Returns a list of transaction rules associated with an account holder.

```python
def get_account_holders_id_transaction_rules(self,
                                            id)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |

## Response Type

**200**: OK - the request has succeeded.

[`TransactionRulesResponse`](../../doc/models/transaction-rules-response.md)

## Example Usage

```python
id = 'id0'

result = account_holders_api.get_account_holders_id_transaction_rules(id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Account Holders-Id-Tax Form Summary

Returns a summary of all tax forms for an account holder.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_account_holders_id_tax_form_summary(self,
                                           id,
                                           form_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the account holder. |
| `form_type` | `str` | Query, Required | The type of tax form you want a summary for. Accepted values are **US1099k** and **US1099nec**. |

## Response Type

**200**: OK - the request has succeeded.

[`TaxFormSummaryResponse`](../../doc/models/tax-form-summary-response.md)

## Example Usage

```python
id = 'id0'

form_type = 'formType6'

result = account_holders_api.get_account_holders_id_tax_form_summary(
    id,
    form_type
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "legalEntityId": "LE123",
      "taxYears": [
        2023
      ]
    },
    {
      "legalEntityId": "LE987",
      "taxYears": [
        2024,
        2025
      ]
    }
  ]
}
```

