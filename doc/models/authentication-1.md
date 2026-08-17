
# Authentication 1

Contains the card user's password and mobile phone number. This is required when you issue cards that can be used to make online payments within the EEA and the UK, or can be added to digital wallets. Refer to [3D Secure and digital wallets](https://docs.adyen.com/issuing/3d-secure-and-wallets) for more information.

## Structure

`Authentication1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `email` | `str` | Optional | The email address where the one-time password (OTP) is sent. |
| `password` | `str` | Optional | The password used for 3D Secure password-based authentication. The value must be between 1 to 30 characters and must only contain the following supported characters.<br><br>* Characters between **a-z**, **A-Z**, and **0-9**<br><br>* Special characters: **äöüßÄÖÜ+-*/ç%()=?!~#'",;:$&àùòâôûáúó**<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `30` |
| `phone` | [`Phone11`](../../doc/models/phone-11.md) | Optional | The phone number where the one-time password (OTP) is sent.<br><br>This object must have:<br><br>* A `type` set to **mobile**.<br><br>* A `number` with a valid country code.<br><br>* A `number` with more than 4 digits, excluding the country code.<br><br>> Make sure to verify that the card user owns the phone number. |

## Example

```python
from adyen.models.authentication_1 import Authentication1
from adyen.models.phone_11 import Phone11
from adyen.models.type_410_enum import Type410Enum

authentication_1 = Authentication1(
    email='email6',
    password='password4',
    phone=Phone11(
        number='number8',
        mtype=Type410Enum.LANDLINE
    )
)
```

