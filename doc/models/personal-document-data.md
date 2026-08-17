
# Personal Document Data

## Structure

`PersonalDocumentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expiration_date` | `str` | Optional | The expiry date of the document,<br>in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**. |
| `issuer_country` | `str` | Optional | The country where the document was issued, in the two-character<br>[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `issuer_state` | `str` | Optional | The state where the document was issued (if applicable). |
| `number` | `str` | Optional | The number in the document. |
| `mtype` | [`Type15Enum`](../../doc/models/type-15-enum.md) | Required | The type of the document. Possible values: **ID**, **DRIVINGLICENSE**, **PASSPORT**, **SOCIALSECURITY**, **VISA**.<br><br>To delete an existing entry for a document `type`, send only the `type` field in your request. |

## Example

```python
from adyen.models.personal_document_data import PersonalDocumentData
from adyen.models.type_15_enum import Type15Enum

personal_document_data = PersonalDocumentData(
    mtype=Type15Enum.PASSPORT,
    expiration_date='expirationDate2',
    issuer_country='issuerCountry4',
    issuer_state='issuerState4',
    number='number4'
)
```

