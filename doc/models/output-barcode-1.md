
# Output Barcode 1

Barcode content to display or print.
Mandatory if `OutputFormat` is Barcode, not allowed otherwise.

## Structure

`OutputBarcode1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_value` | `str` | Required | Value with a Barcode coding. The barcode value to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.output_barcode_1 import OutputBarcode1

output_barcode_1 = OutputBarcode1(
    barcode_value='BarcodeValue0'
)
```

