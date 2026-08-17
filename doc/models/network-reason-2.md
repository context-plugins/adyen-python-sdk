
# Network Reason 2

Contains information that explains why the transfer was rejected or returned by the network.

## Structure

`NetworkReason2`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `code` | `str` | Optional | The reason code provided by the network. |
| `description` | `str` | Optional | The description of the reason code. |
| `namespace` | [`NamespaceEnum`](../../doc/models/namespace-enum.md) | Optional | The namespace that corresponds to the reason code.<br><br>Possible values:<br><br>* **ukFpsRejectionCode**<br>* **ukFpsReturnReasonCode**<br>* **usAchReturnReasonCode**<br>* **iso8583ResponseCode** |

## Example

```python
from adyen.models.namespace_enum import NamespaceEnum
from adyen.models.network_reason_2 import NetworkReason2

network_reason_2 = NetworkReason2(
    code='code2',
    description='description6',
    namespace=NamespaceEnum.ISO8583RESPONSECODE
)
```

