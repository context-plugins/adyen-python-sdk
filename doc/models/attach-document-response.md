
# Attach Document Response

*This model accepts additional fields of type Any.*

## Structure

`AttachDocumentResponse`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment_id` | `str` | Optional, Read-only | The unique identifier of the attachment. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.attach_document_response import AttachDocumentResponse

attach_document_response = AttachDocumentResponse(
    attachment_id='attachmentId4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

