
# Cardholder Receipt

## Structure

`CardholderReceipt`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `header_for_authorized_receipt` | `str` | Optional | The structure of the header to show on the shopper receipt. You can define the order of one or two header lines and blank lines. For example, **header1,header2,filler**. The text of the header lines is defined in the Customer Area under **In-person payments** > **Terminal settings** > **Receipts** in the **Receipt lines** block. |

## Example

```python
from adyen.models.cardholder_receipt import CardholderReceipt

cardholder_receipt = CardholderReceipt(
    header_for_authorized_receipt='headerForAuthorizedReceipt4'
)
```

