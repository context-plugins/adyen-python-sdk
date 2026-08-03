
# Personal Document Data

*This model accepts additional fields of type Any.*

## Structure

`PersonalDocumentData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `expiration_date` | `str` | Optional | The expiry date of the document,<br>in ISO-8601 YYYY-MM-DD format. For example, **2000-01-31**. |
| `issuer_country` | `str` | Optional | The country where the document was issued, in the two-character<br>[ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **NL**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `issuer_state` | `str` | Optional | The state where the document was issued (if applicable). |
| `number` | `str` | Optional | The number in the document. |
| `mtype` | [`Type`](../../doc/models/type.md) | Required | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mtype import Type
from adyen.models.personal_document_data import PersonalDocumentData

personal_document_data = PersonalDocumentData(
    mtype=Type.PASSPORT,
    expiration_date='expirationDate2',
    issuer_country='issuerCountry4',
    issuer_state='issuerState4',
    number='number4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

