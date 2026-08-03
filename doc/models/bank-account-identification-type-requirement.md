
# Bank Account Identification Type Requirement

*This model accepts additional fields of type Any.*

## Structure

`BankAccountIdentificationTypeRequirement`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_account_identification_types` | [`List[BankAccountIdentificationType]`](../../doc/models/bank-account-identification-type.md) | Optional | List of bank account identification types: eg.; [iban , numberAndBic] |
| `description` | `str` | Optional | Specifies the bank account details for a particular route per required field in this object depending on the country of the bank account and the currency of the transfer. |
| `mtype` | [`Type293`](../../doc/models/type-293.md) | Required | **bankAccountIdentificationTypeRequirement** |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.bank_account_identification_type import BankAccountIdentificationType
from adyen.models.bank_account_identification_type_requirement import BankAccountIdentificationTypeRequirement
from adyen.models.type_293 import Type293

bank_account_identification_type_requirement = BankAccountIdentificationTypeRequirement(
    mtype=Type293.BANKACCOUNTIDENTIFICATIONTYPEREQUIREMENT,
    bank_account_identification_types=[
        BankAccountIdentificationType.SELOCAL,
        BankAccountIdentificationType.SGLOCAL,
        BankAccountIdentificationType.UKLOCAL
    ],
    description='description0',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

