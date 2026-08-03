
# In Person Donation Settings Response

*This model accepts additional fields of type Any.*

## Structure

`InPersonDonationSettingsResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `amounts` | [`List[DonationAmount]`](../../doc/models/donation-amount.md) | Optional | The currency and fixed amounts for donations. We automatically add calculated amounts in other currencies for participating stores that use a different currency than the default. |
| `default_currency` | `str` | Optional | The currency that was used in the request to set fixed donation amounts. Format: three-character [ISO currency code](https://docs.adyen.com/development-resources/currency-codes#currency-codes). |
| `display_text_field` | [`DisplayTextField1`](../../doc/models/display-text-field-1.md) | Optional | - |
| `donation_flow` | [`DonationFlow4`](../../doc/models/donation-flow-4.md) | Optional | - |
| `donation_type` | [`DonationType1`](../../doc/models/donation-type-1.md) | Optional | - |
| `merchant_accounts` | `List[str]` | Optional | The merchant accounts for this sales channel that are associated with the donation campaign. |
| `present_card_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to present their card. |
| `prompt_timeout_ms` | `int` | Optional | The time, in milliseconds, that the terminal waits for the shopper to respond to the text asking for a donation. |
| `store_ids` | `List[str]` | Optional | The Adyen-generated unique identifiers of stores for this sales channel that are associated with the donation campaign. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.display_text_field_1 import DisplayTextField1
from adyen.models.donation_amount import DonationAmount
from adyen.models.donation_flow_4 import DonationFlow4
from adyen.models.donation_type_1 import DonationType1
from adyen.models.in_person_donation_settings_response import InPersonDonationSettingsResponse

in_person_donation_settings_response = InPersonDonationSettingsResponse(
    amounts=[
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        DonationAmount(
            amounts=[
                48,
                49,
                50
            ],
            currency_code='currencyCode6',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        )
    ],
    default_currency='defaultCurrency8',
    display_text_field=DisplayTextField1.CAUSENAME,
    donation_flow=DonationFlow4.ONESTEP,
    donation_type=DonationType1.FIXEDAMOUNTS,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

