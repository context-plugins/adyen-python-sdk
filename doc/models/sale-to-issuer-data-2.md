
# Sale to Issuer Data 2

*This model accepts additional fields of type Any.*

## Structure

`SaleToIssuerData2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_reference` | `str` | Optional | Label to print on the bank statement.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sale_to_issuer_data_2 import SaleToIssuerData2

sale_to_issuer_data_2 = SaleToIssuerData2(
    statement_reference='StatementReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

