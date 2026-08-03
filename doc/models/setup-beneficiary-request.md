
# Setup Beneficiary Request

*This model accepts additional fields of type Any.*

## Structure

`SetupBeneficiaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `destination_account_code` | `str` | Required | The destination account code. |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user. |
| `source_account_code` | `str` | Required | The benefactor account. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.setup_beneficiary_request import SetupBeneficiaryRequest

setup_beneficiary_request = SetupBeneficiaryRequest(
    destination_account_code='destinationAccountCode4',
    source_account_code='sourceAccountCode4',
    merchant_reference='merchantReference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

