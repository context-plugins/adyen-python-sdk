
# Network Token

## Structure

`NetworkToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_variant` | `str` | Optional | The card brand variant of the payment instrument associated with the network token. For example, **mc_prepaid_mrw**. |
| `creation_date` | `datetime` | Optional | Date and time when the network token was created, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) extended format. For example, **2025-03-19T10:15:30+01:00**.. |
| `device` | [`DeviceInfo1`](../../doc/models/device-info-1.md) | Optional | Contains information about the device used to provision the network token. |
| `id` | `str` | Optional | The unique identifier of the network token. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument to which this network token belongs to. |
| `status` | [`Status91Enum`](../../doc/models/status-91-enum.md) | Optional | The status of the network token. Possible values: **active**, **inactive**, **suspended**, **closed**. |
| `token_last_four` | `str` | Optional | The last four digits of the network token `id`. |
| `token_requestor` | [`Item`](../../doc/models/item.md) | Optional | The token requestor is an entity who requested tokenization of the card for secure payments. |
| `mtype` | `str` | Optional | The type of network token. For example, **wallet**, **cof**. |

## Example

```python
import dateutil.parser

from adyen.models.device_info_1 import DeviceInfo1
from adyen.models.network_token import NetworkToken
from adyen.models.phone_info_2 import PhoneInfo2

network_token = NetworkToken(
    brand_variant='brandVariant4',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    device=DeviceInfo1(
        form_factor='formFactor4',
        os_name='osName6',
        phone=PhoneInfo2(
            hashed_number='hashedNumber2',
            last_four_digits='lastFourDigits8',
            number='number8'
        )
    ),
    id='id2',
    payment_instrument_id='paymentInstrumentId4'
)
```

