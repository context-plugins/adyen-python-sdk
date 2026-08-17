
# Output Barcode

## Structure

`OutputBarcode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_value` | `str` | Required | Value with a Barcode coding. The barcode value to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.output_barcode import OutputBarcode

output_barcode = OutputBarcode(
    barcode_value='BarcodeValue4'
)
```

