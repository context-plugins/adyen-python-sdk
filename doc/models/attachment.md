
# Attachment

## Structure

`Attachment`

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
from adyen.models.attachment import Attachment

attachment = Attachment(
    content='content2',
    content_type='contentType4',
    filename='filename0',
    page_name='pageName0',
    page_type='pageType6'
)
```

