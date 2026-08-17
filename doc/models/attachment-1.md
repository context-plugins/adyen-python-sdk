
# Attachment 1

Object that contains the document.

## Structure

`Attachment1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `content` | `str` | Required | The document in Base64-encoded string format. |
| `content_type` | `str` | Optional | The file format.<br><br>Possible values: **application/pdf**, **image/jpg**, **image/jpeg**, **image/png**. |
| `filename` | `str` | Optional | The name of the file including the file extension. |
| `page_name` | `str` | Optional | The name of the file including the file extension. |
| `page_type` | `str` | Optional | Specifies which side of the ID card is uploaded.<br><br>* If the `type` is **driversLicense** or **identityCard**, you must set this to **front** or **back** and include both sides in the same API request.<br><br>* For any other types, when this is omitted, we infer the page number based on the order of attachments. |

## Example

```python
from adyen.models.attachment_1 import Attachment1

attachment_1 = Attachment1(
    content='content0',
    content_type='contentType2',
    filename='filename8',
    page_name='pageName8',
    page_type='pageType4'
)
```

