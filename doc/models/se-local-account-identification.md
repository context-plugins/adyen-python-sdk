
# SE Local Account Identification

## Structure

`SELocalAccountIdentification`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `account_number` | `str` | Required | The 7- to 10-digit bank account number ([Bankkontonummer](https://sv.wikipedia.org/wiki/Bankkonto)), without the clearing number, separators, or whitespace.<br><br>**Constraints**: *Minimum Length*: `7`, *Maximum Length*: `10` |
| `clearing_number` | `str` | Required | The 4- to 5-digit clearing number ([Clearingnummer](https://sv.wikipedia.org/wiki/Clearingnummer)), without separators or whitespace.<br><br>**Constraints**: *Minimum Length*: `4`, *Maximum Length*: `5` |
| `mtype` | `str` | Required, Constant | **seLocal**<br><br>**Value**: `"seLocal"` |

## Example

```python
from adyen.models.se_local_account_identification import SELocalAccountIdentification

se_local_account_identification = SELocalAccountIdentification(
    account_number='accountNumber2',
    clearing_number='clearingNumber0'
)
```

