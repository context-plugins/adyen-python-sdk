
# Mandate Account Identification 2

Contains the bank account details of the counterparty. The fields required in this object depend on the country of the bank account and the currency of the transfer.

*This model accepts additional fields of type Any.*

## Structure

`MandateAccountIdentification2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `mtype` | `str` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.mandate_account_identification_2 import MandateAccountIdentification2

mandate_account_identification_2 = MandateAccountIdentification2(
    mtype='MandateAccountIdentification2',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

