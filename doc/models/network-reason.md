
# Network Reason

## Structure

`NetworkReason`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code provided by the network. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | [`NamespaceEnum`](../../doc/models/namespace-enum.md) | Optional | The namespace that corresponds to the reason code.<br><br>Possible values:<br><br>* **ukFpsRejectionCode**<br>* **ukFpsReturnReasonCode**<br>* **usAchReturnReasonCode**<br>* **iso8583ResponseCode** |

## Example

```python
from adyen.models.namespace_enum import NamespaceEnum
from adyen.models.network_reason import NetworkReason

network_reason = NetworkReason(
    code='code8',
    description='description0',
    namespace=NamespaceEnum.UKFPSRETURNREASONCODE
)
```

