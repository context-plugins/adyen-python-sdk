
# Stored Value Load Request

## Structure

`StoredValueLoadRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount information for the transaction. |
| `load_type` | [`LoadTypeEnum`](../../doc/models/load-type-enum.md) | Optional | The type of load you are trying to do, when absent we default to 'load' |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `payment_method` | `Dict[str, str]` | Required | The collection that contains the type of the payment method and its specific information if available |
| `recurring_detail_reference` | `str` | Optional | - |
| `reference` | `str` | Required | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement.<br>If you need to provide multiple references for a transaction, separate them with hyphens ("-").<br>Maximum length: 80 characters. |
| `shopper_interaction` | [`ShopperInteractionEnum`](../../doc/models/shopper-interaction-enum.md) | Optional | Specifies the sales channel, through which the shopper gives their card details, and whether the shopper is a returning customer.<br>For the web service API, Adyen assumes Ecommerce shopper interaction by default.<br><br>This field has the following possible values:<br><br>* `Ecommerce` - Online transactions where the cardholder is present (online). For better authorisation rates, we recommend sending the card security code (CSC) along with the request.<br>* `ContAuth` - Card on file and/or subscription transactions, where the cardholder is known to the merchant (returning customer). If the shopper is present (online), you can supply also the CSC to improve authorisation (one-click payment).<br>* `Moto` - Mail-order and telephone-order transactions where the shopper is in contact with the merchant via email or telephone.<br>* `POS` - Point-of-sale transactions where the shopper is physically present to make a payment using a secure payment terminal. |
| `shopper_reference` | `str` | Optional | - |
| `store` | `str` | Optional | The physical store, for which this payment is processed.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `16` |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.load_type_enum import LoadTypeEnum
from adyen.models.shopper_interaction_enum import ShopperInteractionEnum
from adyen.models.stored_value_load_request import StoredValueLoadRequest

stored_value_load_request = StoredValueLoadRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount8',
    payment_method={
        'key0': 'paymentMethod8'
    },
    reference='reference2',
    load_type=LoadTypeEnum.MERCHANDISERETURN,
    recurring_detail_reference='recurringDetailReference6',
    shopper_interaction=ShopperInteractionEnum.ECOMMERCE,
    shopper_reference='shopperReference4',
    store='store6'
)
```

