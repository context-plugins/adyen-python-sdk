
# Cardholder Receipt

*This model accepts additional fields of type Any.*

## Structure

`CardholderReceipt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `header_for_authorized_receipt` | `str` | Optional | The structure of the header to show on the shopper receipt. You can define the order of one or two header lines and blank lines. For example, **header1,header2,filler**. The text of the header lines is defined in the Customer Area under **In-person payments** > **Terminal settings** > **Receipts** in the **Receipt lines** block. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.cardholder_receipt import CardholderReceipt

cardholder_receipt = CardholderReceipt(
    header_for_authorized_receipt='headerForAuthorizedReceipt4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

