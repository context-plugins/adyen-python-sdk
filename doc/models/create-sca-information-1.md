
# Create Sca Information 1

Information for the Strong Customer Authentication (SCA)

## Structure

`CreateScaInformation1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `exemption` | [`ScaExemptionEnum`](../../doc/models/sca-exemption-enum.md) | Optional | The type of exemption for Strong Customer Authentication (SCA). Possible values:<br><br>* **lowerLimit**: the newly created limit is lower than the existing limit.<br>* **notRegulated**: the limit is created in a country, region, or industry where it is not mandated by law to use SCA.<br>* **setByPlatform**: you set a limit for one of your user's balance accounts, or for your balance platform.<br>* **initialLimit**: there are no existing transfer limits set on the balance account or balance platform.<br>* **alreadyPerformed**: you are confident about your user's identity and do not need to verify this using SCA. |
| `sca_on_approval` | `bool` | Optional | Indicates whether to initiate Strong Customer Authentication (SCA) later, during approval, or immediately after you submit this request. Possible values:<br><br>* **true**: you can initiate SCA later, during approval, for all pending transfer limits.<br>* **false** (default): you initiate SCA immediately after submitting the transfer limit request. |

## Example

```python
from adyen.models.create_sca_information_1 import CreateScaInformation1
from adyen.models.sca_exemption_enum import ScaExemptionEnum

create_sca_information_1 = CreateScaInformation1(
    exemption=ScaExemptionEnum.INITIALLIMIT,
    sca_on_approval=False
)
```

