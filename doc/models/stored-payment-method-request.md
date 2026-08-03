
# Stored Payment Method Request

*This model accepts additional fields of type Any.*

## Structure

`StoredPaymentMethodRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The merchant account identifier, with which you want to process the transaction. |
| `payment_method` | [`PaymentMethodToStore`](../../doc/models/payment-method-to-store.md) | Required | - |
| `recurring_processing_model` | [`RecurringProcessingModel1`](../../doc/models/recurring-processing-model-1.md) | Required | - |
| `shopper_email` | `str` | Optional | The shopper's email address. We recommend that you provide this data, as it is used in velocity fraud checks. |
| `shopper_ip` | `str` | Optional | The IP address of a shopper. |
| `shopper_reference` | `str` | Required | A unique identifier for the shopper (for example, user ID or account ID). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.payment_method_to_store import PaymentMethodToStore
from adyen.models.recurring_processing_model_1 import RecurringProcessingModel1
from adyen.models.stored_payment_method_request import StoredPaymentMethodRequest

stored_payment_method_request = StoredPaymentMethodRequest(
    merchant_account='merchantAccount2',
    payment_method=PaymentMethodToStore(
        brand='brand6',
        cvc='cvc6',
        encrypted_card='encryptedCard4',
        encrypted_card_number='encryptedCardNumber0',
        encrypted_expiry_month='encryptedExpiryMonth2',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    recurring_processing_model=RecurringProcessingModel1.CARDONFILE,
    shopper_reference='shopperReference8',
    shopper_email='shopperEmail4',
    shopper_ip='shopperIP8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

