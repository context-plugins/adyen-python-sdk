
# Vias Personal Data 2

Personal information of the individual.

## Structure

`ViasPersonalData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `date_of_birth` | `str` | Optional | The person's date of birth, in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**. |
| `document_data` | [`List[PersonalDocumentData]`](../../doc/models/personal-document-data.md) | Optional | Array that contains information about the person's identification document. You can submit only one entry per document type. |
| `nationality` | `str` | Optional | The nationality of the person represented by a two-character country code,  in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |

## Example

```python
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.type_15_enum import Type15Enum
from adyen.models.vias_personal_data_2 import ViasPersonalData2

vias_personal_data_2 = ViasPersonalData2(
    date_of_birth='dateOfBirth4',
    document_data=[
        PersonalDocumentData(
            mtype=Type15Enum.ID,
            expiration_date='expirationDate8',
            issuer_country='issuerCountry0',
            issuer_state='issuerState0',
            number='number8'
        )
    ],
    nationality='nationality0'
)
```

