
# Individual Details 3

Details about the individual account holder.
Required when creating an account holder with `legalEntity` **Individual**.

## Structure

`IndividualDetails3`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `name` | [`ViasName2`](../../doc/models/vias-name-2.md) | Optional | The name of the individual.<br><br>> Make sure your account holder registers using the name shown on their Photo ID.<br>> Maximum length: 80 characters<br>> Cannot contain numbers. /n Cannot be empty. |
| `personal_data` | [`ViasPersonalData2`](../../doc/models/vias-personal-data-2.md) | Optional | Personal information of the individual. |

## Example

```python
from adyen.models.gender_enum import GenderEnum
from adyen.models.individual_details_3 import IndividualDetails3
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.type_15_enum import Type15Enum
from adyen.models.vias_name_2 import ViasName2
from adyen.models.vias_personal_data_2 import ViasPersonalData2

individual_details_3 = IndividualDetails3(
    name=ViasName2(
        first_name='firstName4',
        gender=GenderEnum.MALE,
        infix='infix4',
        last_name='lastName4'
    ),
    personal_data=ViasPersonalData2(
        date_of_birth='dateOfBirth2',
        document_data=[
            PersonalDocumentData(
                mtype=Type15Enum.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8'
            ),
            PersonalDocumentData(
                mtype=Type15Enum.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8'
            ),
            PersonalDocumentData(
                mtype=Type15Enum.ID,
                expiration_date='expirationDate8',
                issuer_country='issuerCountry0',
                issuer_state='issuerState0',
                number='number8'
            )
        ],
        nationality='nationality4'
    )
)
```

