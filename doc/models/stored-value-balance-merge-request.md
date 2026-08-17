
# Stored Value Balance Merge Request

## Structure

`StoredValueBalanceMergeRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Optional | The amount information for the transaction. |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `payment_method` | `Dict[str, str]` | Required | The collection that contains the type of the payment method and its specific information if available |
| `recurring_detail_reference` | `str` | Optional | - |
| `reference` | `str` | Required | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_reference` | `str` | Optional | - |
| `source_payment_method` | `Dict[str, str]` | Required | The collection that contains the source payment method and its specific information if available. Note that type should not be included since it is inferred from the (target) payment method |
| `store` | `str` | Optional | The physical store, for which this payment is processed.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.shopper_interaction_enum import ShopperInteractionEnum
from adyen.models.stored_value_balance_merge_request import StoredValueBalanceMergeRequest

stored_value_balance_merge_request = StoredValueBalanceMergeRequest(
    merchant_account='merchantAccount6',
    payment_method={
        'key0': 'paymentMethod6',
        'key1': 'paymentMethod7'
    },
    reference='reference0',
    source_payment_method={
        'key0': 'sourcePaymentMethod0',
        'key1': 'sourcePaymentMethod1',
        'key2': 'sourcePaymentMethod2'
    },
    amount=Amount(
        currency='currency2',
        value=110
    ),
    recurring_detail_reference='recurringDetailReference4',
    shopper_interaction=ShopperInteractionEnum.ECOMMERCE,
    shopper_reference='shopperReference2',
    store='store4'
)
```

