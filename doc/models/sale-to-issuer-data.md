
# Sale to Issuer Data

Sale information intended for the Issuer.
The POI System receives this information and sends it to the Acquirer for the Issuer without any change.

## Structure

`SaleToIssuerData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `statement_reference` | `str` | Optional | Label to print on the bank statement.<br><br>**Constraints**: *Pattern*: `^.+$` |

## Example

```python
from adyen.models.sale_to_issuer_data import SaleToIssuerData

sale_to_issuer_data = SaleToIssuerData(
    statement_reference='StatementReference6'
)
```

