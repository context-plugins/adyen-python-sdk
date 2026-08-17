
# Platform Payment

## Structure

`PlatformPayment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `modification_merchant_reference` | `str` | Optional | The capture's merchant reference included in the transfer. |
| `modification_psp_reference` | `str` | Optional | The capture reference included in the transfer. |
| `payment_merchant_reference` | `str` | Optional | The payment's merchant reference included in the transfer. |
| `platform_payment_type` | [`PlatformPaymentTypeEnum`](../../doc/models/platform-payment-type-enum.md) | Optional | Specifies the nature of the transfer. This parameter helps categorize transfers so you can reconcile transactions at a later time, using the Balance Platform Accounting Report for [marketplaces](https://docs.adyen.com/marketplaces/reports-and-fees/balance-platform-accounting-report/) or [platforms](https://docs.adyen.com/platforms/reports-and-fees/balance-platform-accounting-report/).<br><br>Possible values:<br><br>* **AcquiringFees**: The acquiring fee (the aggregated amount of interchange and scheme fee) incurred on a transaction.<br><br>* **AdyenCommission**: The transaction fee due to Adyen under [blended rates](https://www.adyen.com/knowledge-hub/guides/payments-training-guide/get-the-best-from-your-card-processing).<br><br>* **AdyenFees**: All transaction fees due to Adyen. This is the aggregated amount of Adyen's commission and markup.<br><br>* **AdyenMarkup**: The transaction fee due to Adyen under [Interchange++ pricing](https://www.adyen.com/pricing).<br><br>* **BalanceAccount**: The amount booked to your user after the deduction of the relevant fees.<br><br>* **Commission**: Your platform's or marketplace's commission on a transaction.<br><br>* **DCCPlatformCommission**: **deprecated** The Dynamic Currency Conversion (DCC) fee on a transaction.<br><br>* **DCCMarkup**: The Dynamic Currency Conversion (DCC) fee on a transaction.<br><br>* **Interchange**: The interchange fee (fee paid to the issuer) incurred on a transaction.<br><br>* **PaymentFee**: The aggregated amount of all transaction fees.<br><br>* **Remainder**: The leftover amount after currency conversion.<br><br>* **SchemeFee**: The scheme fee incurred on a transaction.<br><br>* **Surcharge**: The surcharge paid by the customer on a transaction.<br><br>* **Tip**: The tip paid by the customer.<br><br>* **TopUp**: An incoming transfer to top up your user's balance account.<br><br>* **VAT**: The value-added tax charged on the payment. |
| `psp_payment_reference` | `str` | Optional | The payment reference included in the transfer. |
| `mtype` | [`Type63Enum`](../../doc/models/type-63-enum.md) | Optional | **platformPayment**<br><br>**Default**: `"platformPayment"` |

## Example

```python
from adyen.models.platform_payment import PlatformPayment
from adyen.models.platform_payment_type_enum import PlatformPaymentTypeEnum
from adyen.models.type_63_enum import Type63Enum

platform_payment = PlatformPayment(
    modification_merchant_reference='modificationMerchantReference8',
    modification_psp_reference='modificationPspReference0',
    payment_merchant_reference='paymentMerchantReference2',
    platform_payment_type=PlatformPaymentTypeEnum.INTERCHANGE,
    psp_payment_reference='pspPaymentReference8',
    mtype=Type63Enum.PLATFORMPAYMENT
)
```

