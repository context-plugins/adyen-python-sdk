
# Shareholder Contact

## Structure

`ShareholderContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress2`](../../doc/models/vias-address-2.md) | Optional | The address of the person. |
| `email` | `str` | Optional | The e-mail address of the person. |
| `full_phone_number` | `str` | Optional | The phone number of the person provided as a single string.  It will be handled as a landline phone.<br>Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `job_title` | `str` | Optional | Job title of the person. Required when the `shareholderType` is **Controller**.<br><br>Example values: **Chief Executive Officer**, **Chief Financial Officer**, **Chief Operating Officer**, **President**, **Vice President**, **Executive President**, **Managing Member**, **Partner**, **Treasurer**, **Director**, or **Other**. |
| `name` | [`ViasName1`](../../doc/models/vias-name-1.md) | Optional | The name of the person. |
| `personal_data` | [`ViasPersonalData1`](../../doc/models/vias-personal-data-1.md) | Optional | Contains information about the person. |
| `phone_number` | [`ViasPhoneNumber1`](../../doc/models/vias-phone-number-1.md) | Optional | The phone number of the person. |
| `shareholder_code` | `str` | Optional | The unique identifier (UUID) of the shareholder entry.<br><br>> **If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Shareholder will be created with a procedurally-generated UUID.**<br><br>> **If, during an Account Holder create request, a UUID is provided, the creation of Account Holder will fail with a validation Error..**<br><br>> **If, during an Account Holder update request, a UUID that is not correlated with an existing Shareholder is provided, the update of the Shareholder will fail.**<br><br>> **If, during an Account Holder update request, a UUID that is correlated with an existing Shareholder is provided, the existing Shareholder will be updated.** |
| `shareholder_reference` | `str` | Optional | Your reference for the shareholder entry. |
| `shareholder_type` | [`ShareholderTypeEnum`](../../doc/models/shareholder-type-enum.md) | Optional | Specifies how the person is associated with the account holder.<br><br>Possible values:<br><br>* **Owner**: Individuals who directly or indirectly own 25% or more of a company.<br><br>* **Controller**: Individuals who are members of senior management staff responsible for managing a company or organization. |
| `web_address` | `str` | Optional | The URL of the person's website. |

## Example

```python
from adyen.models.gender_enum import GenderEnum
from adyen.models.shareholder_contact import ShareholderContact
from adyen.models.vias_address_2 import ViasAddress2
from adyen.models.vias_name_1 import ViasName1

shareholder_contact = ShareholderContact(
    address=ViasAddress2(
        country='country0',
        city='city6',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street='street6'
    ),
    email='email2',
    full_phone_number='fullPhoneNumber8',
    job_title='jobTitle8',
    name=ViasName1(
        first_name='firstName4',
        gender=GenderEnum.MALE,
        infix='infix4',
        last_name='lastName4'
    )
)
```

