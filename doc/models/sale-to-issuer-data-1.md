
# Sale to Issuer Data 1

Sale information intended for the Issuer.
Send to the Acquirer if present.

*This model accepts additional fields of type Any.*

## Structure

`SaleToIssuerData1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_reference` | `str` | Optional | Label to print on the bank statement.<br><br>**Constraints**: *Pattern*: `^.+$` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.sale_to_issuer_data_1 import SaleToIssuerData1

sale_to_issuer_data_1 = SaleToIssuerData1(
    statement_reference='StatementReference6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

