
# Masterpass

## Structure

`Masterpass`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `checkout_attempt_id` | `str` | Optional | The checkout attempt identifier. |
| `funding_source` | [`FundingSourceEnum`](../../doc/models/funding-source-enum.md) | Optional | The funding source that should be used when multiple sources are available. For Brazilian combo cards, by default the funding source is credit. To use debit, set this value to **debit**. |
| `masterpass_transaction_id` | `str` | Required | The Masterpass transaction ID. |
| `sdk_data` | `str` | Optional | Base64-encoded JSON object containing SDK related parameters required by the SDK<br><br>**Constraints**: *Maximum Length*: `50000` |
| `mtype` | [`Type35Enum`](../../doc/models/type-35-enum.md) | Optional | **masterpass**<br><br>**Default**: `"masterpass"` |

## Example

```python
from adyen.models.funding_source_enum import FundingSourceEnum
from adyen.models.masterpass import Masterpass
from adyen.models.type_35_enum import Type35Enum

masterpass = Masterpass(
    masterpass_transaction_id='masterpassTransactionId6',
    checkout_attempt_id='checkoutAttemptId8',
    funding_source=FundingSourceEnum.DEBIT,
    sdk_data='sdkData8',
    mtype=Type35Enum.MASTERPASS
)
```

