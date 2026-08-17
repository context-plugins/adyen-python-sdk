
# Bank Account Model 1

Contains the business account details.

## Structure

`BankAccountModel1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `form_factor` | [`FormFactorEnum`](../../doc/models/form-factor-enum.md) | Optional | Business accounts with a `formFactor` value of **physical** are business accounts issued under the central bank of that country. The default value is **physical** for NL, US, and UK business accounts.<br><br>Adyen creates a local IBAN for business accounts when the `formFactor` value is set to **virtual**. The local IBANs that are supported are for DE and FR, which reference a physical NL account, with funds being routed through the central bank of NL.<br><br>**Default**: `"physical"` |

## Example

```python
from adyen.models.bank_account_model_1 import BankAccountModel1
from adyen.models.form_factor_enum import FormFactorEnum

bank_account_model_1 = BankAccountModel1(
    form_factor=FormFactorEnum.PHYSICAL
)
```

