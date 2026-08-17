
# Risk Data

## Structure

`RiskData`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `client_data` | `str` | Optional | Contains client-side data, like the device fingerprint, cookies, and specific browser settings.<br><br>**Constraints**: *Maximum Length*: `5000` |
| `custom_fields` | `Dict[str, str]` | Optional | Any custom fields used as part of the input to configured risk rules. |
| `fraud_offset` | `int` | Optional | An integer value that is added to the normal fraud score. The value can be either positive or negative. |
| `profile_reference` | `str` | Optional | The risk profile to assign to this payment. When left empty, the merchant-level account's default risk profile will be applied. |

## Example

```python
from adyen.models.risk_data import RiskData

risk_data = RiskData(
    client_data='clientData4',
    custom_fields={
        'key0': 'customFields2'
    },
    fraud_offset=234,
    profile_reference='profileReference2'
)
```

