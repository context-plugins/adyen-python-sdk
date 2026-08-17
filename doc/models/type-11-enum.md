
# Type 11 Enum

The part of the payment you want to book to the specified `account`.

Possible values for the [Balance Platform](https://docs.adyen.com/adyen-for-platforms-model):

* **BalanceAccount**: Books part of the payment (specified in `amount`) to the specified `account`.
* Transaction fees types that you can book to the specified `account`:
  * **AcquiringFees**: The aggregated amount of the interchange and scheme fees.
  * **PaymentFee**: The aggregated amount of all transaction fees.
  * **AdyenFees**: The aggregated amount of Adyen's commission and markup fees.
  * **AdyenCommission**: The transaction fees due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/interchange-fees-explained).
  * **AdyenMarkup**: The transaction fees due to Adyen under [Interchange ++ pricing](https://www.adyen.com/knowledge-hub/interchange-fees-explained).
  * **Interchange**: The fees paid to the issuer for each payment made with the card network.
  * **SchemeFee**: The fees paid to the card scheme for using their network.
* **Commission**: Your platform's commission on the payment (specified in `amount`), booked to your liable balance account.
* **Remainder**: The amount left over after a currency conversion, booked to the specified `account`.
* **Surcharge**: The payment acceptance fee imposed by the card scheme or debit network provider, paid by your user's customer.
* **TopUp**: Allows you and your users to top up balance accounts using direct debit, card payments, or other payment methods.
* **VAT**: The value-added tax charged on the payment, booked to your platforms liable balance account.
* **Default**: In very specific use cases, allows you to book the specified `amount` to the specified `account`. For more information, contact Adyen support.

Possible values for the [Classic Platforms integration](https://docs.adyen.com/classic-platforms): **Commission**, **Default**, **MarketPlace**, **PaymentFee**, **VAT**.

## Enumeration

`Type11Enum`

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
| `TOPUP` |
| `VAT` |

## Example

```python
from adyen.models.type_11_enum import Type11Enum

type_11 = Type11Enum.ADYENFEES
```

