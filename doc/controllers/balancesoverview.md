# Balancesoverview

```python
balancesoverview_api = client.balancesoverview
```

## Class Name

`BalancesoverviewApi`

## Methods

* [Get-Balance Overview-Companies-Company Account Code-Balances](../../doc/controllers/balancesoverview.md#get-balance-overview-companies-company-account-code-balances)
* [Get-Balance Overview-Merchants-Merchant Account Code-Balances](../../doc/controllers/balancesoverview.md#get-balance-overview-merchants-merchant-account-code-balances)


# Get-Balance Overview-Companies-Company Account Code-Balances

Returns an array with details about the balances available for all merchant accounts under your company account. For each merchant account, the response returns the following:

* **Available funds**: The funds in the merchant account that have been settled and are available for use.

* **Pending balance**: The funds in the merchant account that have not been settled yet.

* **Next payout amount**: The amount that will be settled to your bank account with the next payout.

* **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that cannot be covered by your in-process funds.

* **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_overview_companies_company_account_code_balances(self,
                                                                company_account_code,
                                                                currency)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_account_code` | `str` | Template, Required | The unique identifier of your company account. |
| `currency` | `str` | Query, Required | The currency for which you want a balances overview.<br><br>**Constraints**: *Minimum Length*: `1` |

## Response Type

**200**: OK - The request has succeeded.

[`CompanyBalances`](../../doc/models/company-balances.md)

## Example Usage

```python
company_account_code = 'companyAccountCode6'

currency = 'currency0'

result = balances_overview_api.get_balance_overview_companies_company_account_code_balances(
    company_account_code,
    currency
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Balance Overview-Merchants-Merchant Account Code-Balances

Returns an overview of the different balances available for the merchant account. This includes details about the following:

* **Available funds**: The funds in the merchant account that have been settled and are available for use.

* **Pending balance**: The funds in the merchant account that have not been settled yet.

* **Next payout amount**: The amount that will be settled to your bank account with the next payout.

* **Reserve**: The available amount to cover refunds, payouts, chargebacks, and other operational expenses that cannot be covered by your in-process funds.

* **Deposit**: The amount withheld by Adyen to cover potential losses and liabilities due to payment processing.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_balance_overview_merchants_merchant_account_code_balances(self,
                                                                 merchant_account_code,
                                                                 currency)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account_code` | `str` | Template, Required | The unique identifier of your merchant account. |
| `currency` | `str` | Query, Required | The currency for which you want a balances overview.<br><br>**Constraints**: *Minimum Length*: `1` |

## Response Type

**200**: OK - The request has succeeded.

[`MerchantBalance`](../../doc/models/merchant-balance.md)

## Example Usage

```python
merchant_account_code = 'merchantAccountCode8'

currency = 'currency0'

result = balances_overview_api.get_balance_overview_merchants_merchant_account_code_balances(
    merchant_account_code,
    currency
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - Authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Content - A request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

