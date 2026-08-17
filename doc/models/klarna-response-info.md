
# Klarna Response Info

## Structure

`KlarnaResponseInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). |
| `dispute_email` | `str` | Optional | The email address for disputes. |
| `region` | [`Region1Enum`](../../doc/models/region-1-enum.md) | Optional | The region of operation. |
| `support_email` | `str` | Optional | The email address of merchant support. |

## Example

```python
from adyen.models.klarna_response_info import KlarnaResponseInfo
from adyen.models.region_1_enum import Region1Enum

klarna_response_info = KlarnaResponseInfo(
    auto_capture=False,
    dispute_email='disputeEmail0',
    region=Region1Enum.AU,
    support_email='supportEmail4'
)
```

