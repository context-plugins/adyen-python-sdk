
# Amount

The amount that needs to be captured. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount., The amount to be donated.The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount., The base amount., The buy rate., The interbank amount., The sell rate., For prepaid or gift card purchase, the purchase amount total of prepaid or gift card(s)., If you want a [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) request to use a non-zero value, assign this value to `additionalAmount` (while the amount must be still set to 0 to trigger BIN or card verification).
Required to be in the same currency as the `amount`., The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero)., Includes the currency of the conversion and the value of the transaction.

> This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new)., The amount that needs to be refunded. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount., The amount that needs to be captured/refunded. Required for `/capture` and `/refund`, not allowed for `/cancel`. The `currency` must match the currency used in authorisation, the `value` must be smaller than or equal to the authorised amount., The currency and value of the new total amount in minor units. For example, to increase the amount, the value is the sum of the pre-authorized amount and the additional amount., The total sum amount of one or more payments made using this permit may not exceed this amount if set., The amount of any single payment using this permit may not exceed this amount if set., The amount of the upcoming payment., The amount information for the transaction (in [minor units](https://docs.adyen.com/development-resources/currency-codes)). For [BIN or card verification](https://docs.adyen.com/payment-methods/cards/bin-data-and-card-verification) requests, set amount to 0 (zero)., Includes the currency of the conversion and the value of the transaction.
> This value only applies if you have implemented Dynamic Currency Conversion. For more information, [contact Support](https://www.adyen.help/hc/en-us/requests/new)., A container object for the payable amount information of the transaction., The transaction amount used as a base for the cost estimation., The estimated cost (scheme fee + interchange) in the settlement currency. If the settlement currency cannot be determined, the fee in EUR is returned., The amount information for the transaction., The balance currently on the payment method., The amount of the payment that the notification is about. Set the value in [minor units](https://docs.adyen.com/development-resources/currency-codes)., The lower bound of the processing tier (i.e., an account holder must have processed at least this amount of money in order to be placed into this tier)., The upper bound of the processing tier (i.e., an account holder must have processed less than this amount of money in order to be placed into this tier)., The maximum amount that payouts are limited to. Only applies if payouts are allowed but limited., The amount of the transaction., The amount to be debited from the account holder's bank account., An object containing the currency and value of the payout.
> If the account has multiple currencies, specify the currency to be used.
> If the `bankAccountUUID` is provided in the request, the currency supported by the bank is used.
> If the `payoutMethodCode` is provided in the request, the specified payout method is selected., The amount to be transferred.

## Structure

`Amount`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `currency` | `str` | Required | The three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes) of the amount.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `3` |
| `value` | `int` | Required | The numeric value of the amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes#minor-units). |

## Example

```python
from adyen.models.amount import Amount

amount = Amount(
    currency='currency2',
    value=110
)
```

