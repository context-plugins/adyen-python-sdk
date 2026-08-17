
# Klarna Response Info 1

**klarna** or its variant details

## Structure

`KlarnaResponseInfo1`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). |
| `dispute_email` | `str` | Optional | The email address for disputes. |
| `region` | [`Region1Enum`](../../doc/models/region-1-enum.md) | Optional | The region of operation. |
| `support_email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.klarna_response_info_1 import KlarnaResponseInfo1
from adyen.models.region_1_enum import Region1Enum

klarna_response_info_1 = KlarnaResponseInfo1(
    auto_capture=False,
    dispute_email='disputeEmail8',
    region=Region1Enum.EU,
    support_email='supportEmail2'
)
```

