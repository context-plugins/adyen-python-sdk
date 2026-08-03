
# Fund Recipient

*This model accepts additional fields of type Any.*

## Structure

`FundRecipient`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `iban` | `str` | Optional | The IBAN of the bank account where the funds are being transferred to. |
| `billing_address` | [`BillingAddress7`](../../doc/models/billing-address-7.md) | Optional | - |
| `payment_method` | [`CardDetails`](../../doc/models/card-details.md) | Optional | - |
| `shopper_email` | `str` | Optional | The email address of the shopper. |
| `shopper_name` | [`ShopperName`](../../doc/models/shopper-name.md) | Optional | - |
| `shopper_reference` | `str` | Optional | Required for recurring payments.<br>Your reference to uniquely identify this shopper, for example user ID or account ID. The value is case-sensitive and must be at least three characters.<br><br>> Your reference must not include personally identifiable information (PII) such as name or email address.<br><br>**Constraints**: *Minimum Length*: `3`, *Maximum Length*: `256` |
| `stored_payment_method_id` | `str` | Optional | This is the `recurringDetailReference` returned in the response when you created the token.<br><br>**Constraints**: *Maximum Length*: `64` |
| `sub_merchant` | [`SubMerchant1`](../../doc/models/sub-merchant-1.md) | Optional | - |
| `telephone_number` | `str` | Optional | The telephone number of the shopper. |
| `wallet_identifier` | `str` | Optional | The unique identifier for the wallet the funds are being transferred to. You can use the shopper reference or any other identifier. |
| `wallet_owner_tax_id` | `str` | Optional | The tax identifier of the person receiving the funds. |
| `wallet_purpose` | [`WalletPurpose`](../../doc/models/wallet-purpose.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.billing_address_7 import BillingAddress7
from adyen.models.card_details import CardDetails
from adyen.models.fund_recipient import FundRecipient
from adyen.models.shopper_name import ShopperName

fund_recipient = FundRecipient(
    iban='IBAN4',
    billing_address=BillingAddress7(
        city='city8',
        country='country6',
        house_number_or_name='houseNumberOrName0',
        postal_code='postalCode6',
        street='street2',
        state_or_province='stateOrProvince0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    payment_method=CardDetails(
        billing_sequence_number='billingSequenceNumber2',
        brand='brand6',
        checkout_attempt_id='checkoutAttemptId8',
        cupsecureplus_smscode='cupsecureplus.smscode0',
        cvc='cvc6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    shopper_email='shopperEmail6',
    shopper_name=ShopperName(
        first_name='firstName2',
        last_name='lastName6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

