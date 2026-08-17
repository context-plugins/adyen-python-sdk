
# Setup Beneficiary Request

## Structure

`SetupBeneficiaryRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `destination_account_code` | `str` | Required | The destination account code. |
| `merchant_reference` | `str` | Optional | A value that can be supplied at the discretion of the executing user. |
| `source_account_code` | `str` | Required | The benefactor account. |

## Example

```python
from adyen.models.setup_beneficiary_request import SetupBeneficiaryRequest

setup_beneficiary_request = SetupBeneficiaryRequest(
    destination_account_code='destinationAccountCode4',
    source_account_code='sourceAccountCode4',
    merchant_reference='merchantReference4'
)
```

