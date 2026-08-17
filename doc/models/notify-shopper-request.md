
# Notify Shopper Request

## Structure

`NotifyShopperRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount`](../../doc/models/amount.md) | Required | The amount of the upcoming payment. |
| `billing_date` | `str` | Optional | Date on which the subscription amount will be debited from the shopper. In YYYY-MM-DD format |
| `billing_sequence_number` | `str` | Optional | Sequence of the debit. Depends on Frequency and Billing Attempts Rule. |
| `displayed_reference` | `str` | Optional | Reference of Pre-debit notification that is displayed to the shopper. Optional field. Maps to reference if missing |
| `merchant_account` | `str` | Required | The merchant account identifier with which you want to process the transaction. |
| `recurring_detail_reference` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |
| `reference` | `str` | Required | Pre-debit notification reference sent by the merchant. This is a mandatory field |
| `shopper_reference` | `str` | Required | The ID that uniquely identifies the shopper.<br><br>This `shopperReference` must be the same as the `shopperReference` used in the initial payment. |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token. |

## Example

```python
from adyen.models.amount import Amount
from adyen.models.notify_shopper_request import NotifyShopperRequest

notify_shopper_request = NotifyShopperRequest(
    amount=Amount(
        currency='currency2',
        value=110
    ),
    merchant_account='merchantAccount2',
    reference='reference8',
    shopper_reference='shopperReference4',
    billing_date='billingDate8',
    billing_sequence_number='billingSequenceNumber6',
    displayed_reference='displayedReference4',
    recurring_detail_reference='recurringDetailReference6',
    stored_payment_method_id='storedPaymentMethodId0'
)
```

