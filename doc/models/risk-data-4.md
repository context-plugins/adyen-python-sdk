
# Risk Data 4

Contains risk data, such as client-side data, used to identify risk for a transaction.

## Structure

`RiskData4`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_data` | `str` | Optional | Contains client-side data, like the device fingerprint, cookies, and specific browser settings.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `custom_fields` | `Dict[str, str]` | Optional | Any custom fields used as part of the input to configured risk rules. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `profile_reference` | `str` | Optional | The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied. |

## Example

```python
from adyen.models.risk_data_4 import RiskData4

risk_data_4 = RiskData4(
    client_data='clientData2',
    custom_fields={
        'key0': 'customFields0',
        'key1': 'customFields1',
        'key2': 'customFields2'
    },
    fraud_offset=138,
    profile_reference='profileReference0'
)
```

