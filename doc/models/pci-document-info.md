
# Pci Document Info

*This model accepts additional fields of type Any.*

## Structure

`PciDocumentInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `created_at` | `datetime` | Optional | The date the questionnaire was created, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00 |
| `id` | `str` | Optional | The unique identifier of the signed questionnaire. |
| `valid_until` | `datetime` | Optional | The expiration date of the questionnaire, in ISO 8601 extended format. For example, 2022-12-18T10:15:30+01:00 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import dateutil.parser
import jsonpickle

from adyen.models.pci_document_info import PciDocumentInfo

pci_document_info = PciDocumentInfo(
    created_at=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    id='id0',
    valid_until=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

