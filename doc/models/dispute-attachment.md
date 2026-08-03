
# Dispute Attachment

*This model accepts additional fields of type Any.*

## Structure

`DisputeAttachment`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `attachment_type` | [`AttachmentType1`](../../doc/models/attachment-type-1.md) | Required | - |
| `content` | `str` | Required | The content of the image. An attachment must be base64-encoded data. Make sure that all base64-encoded data strings are generated without line breaks or "wrapping". For example, do not use `Base64.NO_WRAP` in Java, or its equivalent in other languages. Newline characters at the end of the base64-encoded data string will also result in a malformed input error.<br><br>**Constraints**: *Minimum Length*: `1` |
| `file_name` | `str` | Required | The name of the attachment, including its filename extension. Supported filename extensions: **jpeg**, **pdf**, **tiff**.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `17`, *Pattern*: `([^\s]+(\.(?i)(jpeg\|tiff\|pdf))$)` |
| `id` | `str` | Optional, Read-only | The unique identifier of the attachment. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.attachment_type_1 import AttachmentType1
from adyen.models.dispute_attachment import DisputeAttachment

dispute_attachment = DisputeAttachment(
    attachment_type=AttachmentType1.OTHER,
    content='content2',
    file_name='fileName2',
    id='id8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

