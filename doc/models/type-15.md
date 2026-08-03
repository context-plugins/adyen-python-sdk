
# Type 15

The part of the payment you want to book to the specified `account`.

Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):

* **BalanceAccount**: books part of the payment (specified in `amount`) to the specified `account`.
* Transaction fees types that you can book to the specified `account`:
  * **AcquiringFees**: the aggregated amount of the interchange and scheme fees.
  * **PaymentFee**: the aggregated amount of all transaction fees.
  * **AdyenFees**: the aggregated amount of Adyen's commission and markup fees.
  * **AdyenCommission**: the transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).
  * **AdyenMarkup**: the transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).
  * **Interchange**: the fees paid to the issuer for each payment made with the card network.
  * **SchemeFee**: the fees paid to the card scheme for using their network.
* **Commission**: your platform's commission on the payment (specified in `amount`), booked to your liable balance account.
* **Remainder**: the amount left over after a currency conversion, booked to the specified `account`.
* **TopUp**: allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.
* **VAT**: the value-added tax charged on the payment, booked to your platforms liable balance account.
* **Commission**: your platform's commission (specified in `amount`) on the payment, booked to your liable balance account.
* **Default**: in very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.

Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **Marketplace**, **PaymentFee**, **VAT**.

## Enumeration

`Type15`

## Fields

| Name |
|  --- |
| `ACQUIRINGFEES` |
| `ADYENCOMMISSION` |
| `ADYENFEES` |
| `ADYENMARKUP` |
| `BALANCEACCOUNT` |
| `COMMISSION` |
| `DEFAULT` |
| `INTERCHANGE` |
| `MARKETPLACE` |
| `PAYMENTFEE` |
| `REMAINDER` |
| `SCHEMEFEE` |
| `SURCHARGE` |
| `TIP` |
| `VAT` |

## Example

```python
from adyen.models.type_15 import Type15

type_15 = Type15.SURCHARGE
```

