
# Donation Payment Response

## Structure

`DonationPaymentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount26`](../../doc/models/amount-26.md) | Optional | Authorised amount in the transaction. |
| `donation_account` | `str` | Optional | The Adyen account name of your charity. We will provide you with this account name once your chosen charity has been [onboarded](https://docs.adyen.com/online-payments/donations#onboarding). |
| `id` | `str` | Optional | Your unique resource identifier. |
| `merchant_account` | `str` | Optional | The merchant account identifier, with which you want to process the transaction. |
| `payment` | [`PaymentResponse9`](../../doc/models/payment-response-9.md) | Optional | Action to be taken for completing the payment. |
| `reference` | `str` | Optional | The reference to uniquely identify a payment. This reference is used in all communication with you about the payment status. We recommend using a unique value per payment; however, it is not a requirement. If you need to provide multiple references for a transaction, separate them with hyphens ("-"). Maximum length: 80 characters. |
| `status` | [`Status1Enum`](../../doc/models/status-1-enum.md) | Optional | The status of the donation transaction.<br><br>Possible values:<br><br>* **completed**<br>* **pending**<br>* **refused** |

## Example

```python
from adyen.models.amount_26 import Amount26
from adyen.models.checkout_await_action import CheckoutAwaitAction
from adyen.models.donation_payment_response import DonationPaymentResponse
from adyen.models.fraud_check_result import FraudCheckResult
from adyen.models.fraud_result_1 import FraudResult1
from adyen.models.payment_response_9 import PaymentResponse9

donation_payment_response = DonationPaymentResponse(
    amount=Amount26(
        currency='currency2',
        value=110
    ),
    donation_account='donationAccount2',
    id='id8',
    merchant_account='merchantAccount0',
    payment=PaymentResponse9(
        action=CheckoutAwaitAction(
            payment_data='paymentData8',
            payment_method_type='paymentMethodType8',
            url='url0'
        ),
        additional_data={
            'key0': 'additionalData6'
        },
        amount=Amount26(
            currency='currency2',
            value=110
        ),
        donation_token='donationToken8',
        fraud_result=FraudResult1(
            account_score=232,
            results=[
                FraudCheckResult(
                    account_score=102,
                    check_id=246,
                    name='name6'
                ),
                FraudCheckResult(
                    account_score=102,
                    check_id=246,
                    name='name6'
                )
            ]
        )
    )
)
```

