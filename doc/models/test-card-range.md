
# Test Card Range

*This model accepts additional fields of type Any.*

## Structure

`TestCardRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`AvsAddress`](../../doc/models/avs-address.md) | Optional | - |
| `card_holder_name` | `str` | Required | The name of the card holder, as it appears on the card, for the test card range. |
| `cvc` | `str` | Optional | The test card range security code.<br><br>Example: 123 |
| `expiry_month` | [`ExpiryMonth`](../../doc/models/expiry-month.md) | Required | - |
| `expiry_year` | `int` | Required | Expiry year for the test card range.<br><br>Example: 2020 |
| `range_end` | `str` | Required | The last test card number in the test card range (inclusive):<br><br>* Min 6, max 19 digits<br>* BIN compliant<br>  Example: 5432 1234 1234 4321 |
| `range_start` | `str` | Required | The first test card number in the test card range (inclusive):<br><br>* Min 6, max 19 digits<br>* BIN compliant<br>  Example: 5432 1234 1234 1234 |
| `three_d_directory_server_response` | [`ThreeDDirectoryServerResponse`](../../doc/models/three-d-directory-server-response.md) | Optional | - |
| `three_d_password` | `str` | Optional | The password used for 3D Secure authentication. |
| `three_d_username` | `str` | Optional | The username used for 3D Secure authentication. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.avs_address import AvsAddress
from adyen.models.expiry_month import ExpiryMonth
from adyen.models.test_card_range import TestCardRange
from adyen.models.three_d_directory_server_response import ThreeDDirectoryServerResponse

test_card_range = TestCardRange(
    card_holder_name='cardHolderName2',
    expiry_month=ExpiryMonth.DECEMBER,
    expiry_year=166,
    range_end='rangeEnd6',
    range_start='rangeStart6',
    address=AvsAddress(
        street_address='streetAddress6',
        zip='zip0',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    cvc='cvc2',
    three_d_directory_server_response=ThreeDDirectoryServerResponse.N,
    three_d_password='threeDPassword0',
    three_d_username='threeDUsername0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

