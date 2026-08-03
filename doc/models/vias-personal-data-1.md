
# Vias Personal Data 1

Contains information about the person.

*This model accepts additional fields of type Any.*

## Structure

`ViasPersonalData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**. |
| `document_data` | [`List[PersonalDocumentData]`](../../doc/models/personal-document-data.md) | Optional | Array that contains information about the person's identification document. You can submit only one entry per document type. |
| `nationality` | `str` | Optional | The nationality of the person represented by a two-character country code,  in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mtype import Type
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.vias_personal_data_1 import ViasPersonalData1

vias_personal_data_1 = ViasPersonalData1(
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
        )
    ],
    nationality='nationality4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

