
# Receipt Options 1

Generic receipt settings.

## Structure

`ReceiptOptions1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `header_line_1` | `str` | Optional | The text of the first header line to be shown on the receipt.<br><br>**Constraints**: *Maximum Length*: `100` |
| `header_line_2` | `str` | Optional | The text of the second header line to be shown on the receipt.<br><br>**Constraints**: *Maximum Length*: `100` |
| `logo` | `str` | Optional | The receipt logo converted to a Base64-encoded string. The image must be a .bmp file of < 256 KB, dimensions 240 (H) x 384 (W) px.<br><br>**Constraints**: *Maximum Length*: `350000` |
| `prompt_before_printing` | `bool` | Optional | Indicates whether a screen appears asking if you want to print the shopper receipt. |
| `qr_code_data` | `str` | Optional | Data to print on the receipt as a QR code. This can include static text and the following variables:<br><br>- `${merchantreference}`: the merchant reference of the transaction.<br>- `${pspreference}`: the PSP reference of the transaction.<br><br>For example, **http://www.example.com/order/${pspreference}/${merchantreference}**. |

## Example

```python
from adyen.models.receipt_options_1 import ReceiptOptions1

receipt_options_1 = ReceiptOptions1(
    header_line_1='headerLine10',
    header_line_2='headerLine28',
    logo='logo4',
    prompt_before_printing=False,
    qr_code_data='qrCodeData0'
)
```

