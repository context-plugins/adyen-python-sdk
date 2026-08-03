
# Output Barcode

*This model accepts additional fields of type Any.*

## Structure

`OutputBarcode`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `barcode_value` | `str` | Required | Value with a Barcode coding. The barcode value to display or print.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.output_barcode import OutputBarcode

output_barcode = OutputBarcode(
    barcode_value='BarcodeValue4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

