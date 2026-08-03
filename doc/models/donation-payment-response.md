
# Donation Payment Response

*This model accepts additional fields of type Any.*

## Structure

`DonationPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount16`](../../doc/models/amount-16.md) | Optional | - |
| `donation_account` | `str` | Optional | The Adyen account name of your charity. We will provide you with this account name once your chosen charity has been [onboarded](https://docs.adyen.com/online-payments/donations#onboarding). |
| `id` | `str` | Optional | Your unique resource identifier. |
| `merchant_account` | `str` | Optional | The merchant account identifier, with which you want to process the transaction. |
| `payment` | [`PaymentResponse`](../../doc/models/payment-response.md) | Optional | - |
| `reference` | `str` | Optional | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters. |
| `status` | [`Status12`](../../doc/models/status-12.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.amount_16 import Amount16
from adyen.models.checkout_await_action import CheckoutAwaitAction
from adyen.models.donation_payment_response import DonationPaymentResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result import FraudResult
from adyen.models.payment_response import PaymentResponse
from adyen.models.type_493 import Type493

donation_payment_response = DonationPaymentResponse(
    amount=Amount16(
        currency='currency2',
        value=110,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    donation_account='donationAccount2',
    id='id8',
    merchant_account='merchantAccount0',
    payment=PaymentResponse(
        action=CheckoutAwaitAction(
            mtype=Type493.AWAIT,
            payment_data='paymentData8',
            payment_method_type='paymentMethodType8',
            url='url0',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_data={
            'key0': 'additionalData6'
        },
        amount=Amount16(
            currency='currency2',
            value=110,
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        donation_token='donationToken8',
        fraud_result=FraudResult(
            account_score=232,
            results=[
                FraudCheckResult(
                    account_score=102,
                    check_id=246,
                    name='name6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                ),
                FraudCheckResult(
                    account_score=102,
                    check_id=246,
                    name='name6',
                    additional_properties={
                        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                    }
                )
            ],
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

