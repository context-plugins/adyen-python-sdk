
# Payout Method

## Structure

`PayoutMethod`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_account` | `str` | Required | The [`merchantAccount`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_merchantAccount) you used in the `/payments` request when you [saved the account holder's card details](https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store). |
| `payout_method_code` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the payout method, returned in the response when you create a payout method. Required when updating an existing payout method in an `/updateAccountHolder` request. |
| `payout_method_reference` | `str` | Optional | Your reference for the payout method. |
| `recurring_detail_reference` | `str` | Required | The [`recurringDetailReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__resParam_additionalData-ResponseAdditionalDataCommon-recurring-recurringDetailReference)  returned in the `/payments` response when you [saved the account holder's card details](https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store). |
| `shopper_reference` | `str` | Required | The [`shopperReference`](https://docs.adyen.com/api-explorer/#/CheckoutService/latest/post/payments__reqParam_shopperReference) you sent in the `/payments` request when you [saved the account holder's card details](https://docs.adyen.com/classic-platforms/payouts/manual-payout/payout-to-cards#check-and-store). |

## Example

```python
from adyen.models.payout_method import PayoutMethod

payout_method = PayoutMethod(
    merchant_account='merchantAccount6',
    recurring_detail_reference='recurringDetailReference4',
    shopper_reference='shopperReference2',
    payout_method_code='payoutMethodCode4',
    payout_method_reference='payoutMethodReference4'
)
```

