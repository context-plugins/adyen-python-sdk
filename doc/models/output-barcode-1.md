
# Output Barcode 1

Barcode content to display or print.
Mandatory if `OutputFormat` is Barcode, not allowed otherwise.

*This model accepts additional fields of type Any.*

## Structure

`OutputBarcode1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_value` | `str` | Required | Value with a Barcode coding. The barcode value to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.output_barcode_1 import OutputBarcode1

output_barcode_1 = OutputBarcode1(
    barcode_value='BarcodeValue0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

