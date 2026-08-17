
# Stored Payment Method Request

## Structure

`StoredPaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `payment_method` | [`PaymentMethodToStore1`](../../doc/models/payment-method-to-store-1.md) | Required | Contains the information required to store a payment method. |
| `recurring_processing_model` | [`RecurringProcessingModel1Enum`](../../doc/models/recurring-processing-model-1-enum.md) | Required | Defines a recurring payment type. Required when creating a token to store payment details.<br>Allowed values:<br><br>* `Subscription` – A transaction for a fixed or variable amount, which follows a fixed schedule.<br>* `CardOnFile` – With a card-on-file (CoF) transaction, card details are stored to enable one-click or omnichannel journeys, or simply to streamline the checkout process. Any subscription not following a fixed schedule is also considered a card-on-file transaction.<br>* `UnscheduledCardOnFile` – An unscheduled card-on-file (UCoF) transaction is a transaction that occurs on a non-fixed schedule and/or have variable amounts. For example, automatic top-ups when a cardholder's balance drops below a certain amount. |
| `shopper_email` | `str` | Optional | The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. |
| `shopper_ip` | `str` | Optional | The IP address of a shopper. |
| `shopper_reference` | `str` | Required | A unique identifier for the shopper (for example, user ID or account ID). |

## Example

```python
from adyen.models.payment_method_to_store_1 import PaymentMethodToStore1
from adyen.models.recurring_processing_model_1_enum import RecurringProcessingModel1Enum
from adyen.models.stored_payment_method_request import StoredPaymentMethodRequest

stored_payment_method_request = StoredPaymentMethodRequest(
    merchant_account='merchantAccount2',
    payment_method=PaymentMethodToStore1(
        brand='brand6',
        cvc='cvc6',
        encrypted_card='encryptedCard4',
        encrypted_card_number='encryptedCardNumber0',
        encrypted_expiry_month='encryptedExpiryMonth2'
    ),
    recurring_processing_model=RecurringProcessingModel1Enum.CARDONFILE,
    shopper_reference='shopperReference8',
    shopper_email='shopperEmail4',
    shopper_ip='shopperIP8'
)
```

