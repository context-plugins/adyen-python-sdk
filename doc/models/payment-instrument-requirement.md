
# Payment Instrument Requirement

## Structure

`PaymentInstrumentRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Optional | Specifies the requirements for the payment instrument that need to be included in the request for a particular route. |
| `issuing_country_code` | `str` | Optional | The two-character [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) country code where the payment instrument is issued. For example, **NL** or **US**. |
| `issuing_country_codes` | `List[str]` | Optional | The two-character ISO-3166-1 alpha-2 country code list for payment instruments. |
| `only_for_cross_balance_platform` | `bool` | Optional | Specifies if the requirement only applies to transfers to another balance platform. |
| `payment_instrument_type` | [`PaymentInstrumentTypeEnum`](../../doc/models/payment-instrument-type-enum.md) | Optional | The type of the payment instrument. For example, "BankAccount" or "Card". |
| `mtype` | `str` | Required, Constant | **paymentInstrumentRequirement**<br><br>**Value**: `"paymentInstrumentRequirement"` |

## Example

```python
from adyen.models.payment_instrument_requirement import PaymentInstrumentRequirement
from adyen.models.payment_instrument_type_enum import PaymentInstrumentTypeEnum

payment_instrument_requirement = PaymentInstrumentRequirement(
    description='description4',
    issuing_country_code='issuingCountryCode6',
    issuing_country_codes=[
        'issuingCountryCodes7',
        'issuingCountryCodes8'
    ],
    only_for_cross_balance_platform=False,
    payment_instrument_type=PaymentInstrumentTypeEnum.BANKACCOUNT
)
```

