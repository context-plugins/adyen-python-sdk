
# Fund Recipient 1

the person or entity receiving the money

## Structure

`FundRecipient1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Optional | The IBAN of the bank account where the funds are being transferred to. |
| `billing_address` | [`Address3`](../../doc/models/address-3.md) | Optional | The address where to send the invoice. |
| `payment_method` | [`CardDetails1`](../../doc/models/card-details-1.md) | Optional | The payment method used by the shopper. |
| `shopper_email` | `str` | Optional | The email address of the shopper. |
| `shopper_name` | [`Name2`](../../doc/models/name-2.md) | Optional | The name of the shopper. |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `sub_merchant` | [`SubMerchant2`](../../doc/models/sub-merchant-2.md) | Optional | Required for back-to-back/purchase-driven-load transactions, where the funds are taken from the shopper's stored card when the wallet balance is insufficient.<br>The final merchant who will receive the money, also known as a [sub-merchant](https://docs.adyen.com/get-started-with-adyen/payment-glossary/#submerchant). |
| `telephone_number` | `str` | Optional | The telephone number of the shopper. |
| `wallet_identifier` | `str` | Optional | The unique identifier for the wallet the funds are being transferred to. You can use the shopper reference or any other identifier. |
| `wallet_owner_tax_id` | `str` | Optional | The tax identifier of the person receiving the funds. |
| `wallet_purpose` | [`WalletPurposeEnum`](../../doc/models/wallet-purpose-enum.md) | Optional | The purpose of a digital wallet transaction. |

## Example

```python
from adyen.models.address_3 import Address3
from adyen.models.card_details_1 import CardDetails1
from adyen.models.fund_recipient_1 import FundRecipient1
from adyen.models.name_2 import Name2

fund_recipient_1 = FundRecipient1(
    iban='IBAN6',
    billing_address=Address3(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0'
    ),
    payment_method=CardDetails1(
        billing_sequence_number='billingSequenceNumber2',
        brand='brand6',
        checkout_attempt_id='checkoutAttemptId8',
        cupsecureplus_smscode='cupsecureplus.smscode0',
        cvc='cvc6'
    ),
    shopper_email='shopperEmail6',
    shopper_name=Name2(
        first_name='firstName2',
        last_name='lastName6'
    )
)
```

