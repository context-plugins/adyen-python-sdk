
# Network Token

*This model accepts additional fields of type Any.*

## Structure

`NetworkToken`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `brand_variant` | `str` | Optional | The card brand variant of the payment instrument associated with the network token. For example, **mc_prepaid_mrw**. |
| `creation_date` | `datetime` | Optional | Date and time when the network token was created, in [ISO 8601](https://www.iso.org/iso-8601-date-and-time-format.html) extended format. For example, **2025-03-19T10:15:30+01:00**.. |
| `device` | [`DeviceInfo`](../../doc/models/device-info.md) | Optional | - |
| `id` | `str` | Optional | The unique identifier of the network token. |
| `payment_instrument_id` | `str` | Optional | The unique identifier of the payment instrument to which this network token belongs to. |
| `status` | [`Status9`](../../doc/models/status-9.md) | Optional | - |
| `token_last_four` | `str` | Optional | The last four digits of the network token `id`. |
| `token_requestor` | [`NetworkTokenRequestor`](../../doc/models/network-token-requestor.md) | Optional | - |
| `mtype` | `str` | Optional | The type of network token. For example, **wallet**, **cof**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.device_info import DeviceInfo
from adyen.models.network_token import NetworkToken
from adyen.models.phone_info import PhoneInfo

network_token = NetworkToken(
    brand_variant='brandVariant4',
    creation_date=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    device=DeviceInfo(
        form_factor='formFactor4',
        os_name='osName6',
        phone=PhoneInfo(
            hashed_number='hashedNumber2',
            last_four_digits='lastFourDigits8',
            number='number8',
            additional_properties={
                'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
            }
        ),
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    id='id2',
    payment_instrument_id='paymentInstrumentId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

