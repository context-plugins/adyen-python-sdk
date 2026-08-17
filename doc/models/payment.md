
# Payment

## Structure

`Payment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amount` | [`Amount26`](../../doc/models/amount-26.md) | Optional | Authorised amount in the transaction. |
| `payment_method` | [`PaymentResponse3`](../../doc/models/payment-response-3.md) | Optional | Only returned for `resultCode`: **Authorised**.<br>Details about the payment method used in the transaction. |
| `psp_reference` | `str` | Optional | Adyen's 16-character reference associated with the transaction/request. This value is globally unique. Use this reference when you communicate with us about this request. |
| `result_code` | [`ResultCode2Enum`](../../doc/models/result-code-2-enum.md) | Optional | The result of the payment. For more information, see [Result codes](https://docs.adyen.com/online-payments/payment-result-codes).<br><br>Possible values:<br><br>* **Authorised** – The payment was successfully authorised. This state serves as an indicator to proceed with the delivery of goods and services. This is a final state.<br>* **Received** – Indicates the payment request was successfully received by Adyen, and will be processed. This is the initial state for all payments.<br>* **Pending** – The payment order was successfully received but the final status of the payment is not available yet. This is common for payment methods with an asynchronous flow. |

## Example

```python
from adyen.models.amount_26 import Amount26
from adyen.models.payment import Payment
from adyen.models.payment_response_3 import PaymentResponse3
from adyen.models.result_code_2_enum import ResultCode2Enum

payment = Payment(
    amount=Amount26(
        currency='currency2',
        value=110
    ),
    payment_method=PaymentResponse3(
        brand='brand6',
        mtype='type8'
    ),
    psp_reference='pspReference2',
    result_code=ResultCode2Enum.AUTHORISED
)
```

