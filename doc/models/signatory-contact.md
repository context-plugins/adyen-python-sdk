
# Signatory Contact

*This model accepts additional fields of type Any.*

## Structure

`SignatoryContact`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress`](../../doc/models/vias-address.md) | Optional | - |
| `email` | `str` | Optional | The e-mail address of the person. |
| `full_phone_number` | `str` | Optional | The phone number of the person provided as a single string.  It will be handled as a landline phone.<br>Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `job_title` | `str` | Optional | Job title of the signatory.<br><br>Example values: **Chief Executive Officer**, **Chief Financial Officer**, **Chief Operating Officer**, **President**, **Vice President**, **Executive President**, **Managing Member**, **Partner**, **Treasurer**, **Director**, or **Other**. |
| `name` | [`ViasName`](../../doc/models/vias-name.md) | Optional | - |
| `personal_data` | [`ViasPersonalData`](../../doc/models/vias-personal-data.md) | Optional | - |
| `phone_number` | [`PhoneNumber3`](../../doc/models/phone-number-3.md) | Optional | - |
| `signatory_code` | `str` | Optional | The unique identifier (UUID) of the signatory.<br><br>> **If, during an Account Holder create or update request, this field is left blank (but other fields provided), a new Signatory will be created with a procedurally-generated UUID.**<br><br>> **If, during an Account Holder create request, a UUID is provided, the creation of the Signatory will fail while the creation of the Account Holder will continue.**<br><br>> **If, during an Account Holder update request, a UUID that is not correlated with an existing Signatory is provided, the update of the Signatory will fail.**<br><br>> **If, during an Account Holder update request, a UUID that is correlated with an existing Signatory is provided, the existing Signatory will be updated.** |
| `signatory_reference` | `str` | Optional | Your reference for the signatory. |
| `web_address` | `str` | Optional | The URL of the person's website. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.gender import Gender
from adyen.models.signatory_contact import SignatoryContact
from adyen.models.vias_address import ViasAddress
from adyen.models.vias_name import ViasName

signatory_contact = SignatoryContact(
    address=ViasAddress(
        country='country0',
        city='city6',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street='street6',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    email='email8',
    full_phone_number='fullPhoneNumber2',
    job_title='jobTitle2',
    name=ViasName(
        first_name='firstName4',
        gender=Gender.MALE,
        infix='infix4',
        last_name='lastName4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

