
# Test Card Range

## Structure

`TestCardRange`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`AvsAddress1`](../../doc/models/avs-address-1.md) | Optional | Contains the billing address of the card holder. The address details need to be AVS-compliant, which means that you need to provide at least street address. |
| `card_holder_name` | `str` | Required | The name of the card holder, as it appears on the card, for the test card range. |
| `cvc` | `str` | Optional | The test card range security code.<br><br>Example: 123 |
| `expiry_month` | [`ExpiryMonthEnum`](../../doc/models/expiry-month-enum.md) | Required | Expiry month for the test card range.<br><br>Allowed values:<br><br>* JANUARY<br>* FEBRUARY<br>* MARCH<br>* APRIL<br>* MAY<br>* JUNE<br>* JULY<br>* AUGUST<br>* SEPTEMBER<br>* OCTOBER<br>* NOVEMBER<br>* DECEMBER |
| `expiry_year` | `int` | Required | Expiry year for the test card range.<br><br>Example: 2020 |
| `range_end` | `str` | Required | The last test card number in the test card range (inclusive):<br><br>* Min 6, max 19 digits<br>* BIN compliant<br>  Example: 5432 1234 1234 4321 |
| `range_start` | `str` | Required | The first test card number in the test card range (inclusive):<br><br>* Min 6, max 19 digits<br>* BIN compliant<br>  Example: 5432 1234 1234 1234 |
| `three_d_directory_server_response` | [`ThreeDDirectoryServerResponseEnum`](../../doc/models/three-d-directory-server-response-enum.md) | Optional | 3D Secure server response. It notifies whether the specified card holder is enrolled in a 3D Secure service. Possible values:<br><br>* Y (Authentication available)<br>* N (Card holder not enrolled/not participating)<br>* U (Unable to authenticate) |
| `three_d_password` | `str` | Optional | The password used for 3D Secure authentication. |
| `three_d_username` | `str` | Optional | The username used for 3D Secure authentication. |

## Example

```python
from adyen.models.avs_address_1 import AvsAddress1
from adyen.models.expiry_month_enum import ExpiryMonthEnum
from adyen.models.test_card_range import TestCardRange
from adyen.models.three_d_directory_server_response_enum import ThreeDDirectoryServerResponseEnum

test_card_range = TestCardRange(
    card_holder_name='cardHolderName2',
    expiry_month=ExpiryMonthEnum.DECEMBER,
    expiry_year=166,
    range_end='rangeEnd6',
    range_start='rangeStart6',
    address=AvsAddress1(
        street_address='streetAddress6',
        zip='zip0'
    ),
    cvc='cvc2',
    three_d_directory_server_response=ThreeDDirectoryServerResponseEnum.N,
    three_d_password='threeDPassword0',
    three_d_username='threeDUsername0'
)
```

