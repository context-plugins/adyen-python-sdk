
# Individual Details 1

Required when creating an entity with `legalEntityType` **Individual**.

*This model accepts additional fields of type Any.*

## Structure

`IndividualDetails1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`ViasName`](../../doc/models/vias-name.md) | Optional | - |
| `personal_data` | [`ViasPersonalData`](../../doc/models/vias-personal-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.gender import Gender
from adyen.models.individual_details_1 import IndividualDetails1
from adyen.models.mtype import Type
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.vias_name import ViasName
from adyen.models.vias_personal_data import ViasPersonalData

individual_details_1 = IndividualDetails1(
    name=ViasName(
        first_name='firstName4',
        gender=Gender.MALE,
        infix='infix4',
        last_name='lastName4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    personal_data=ViasPersonalData(
        date_of_birth='dateOfBirth2',
        document_data=[
            PersonalDocumentData(
                mtype=Type.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PersonalDocumentData(
                mtype=Type.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            PersonalDocumentData(
                mtype=Type.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        nationality='nationality4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

