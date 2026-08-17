
# Klarna Info

## Structure

`KlarnaInfo`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `auto_capture` | `bool` | Optional | Indicates the status of [Automatic capture](https://docs.adyen.com/online-payments/capture#automatic-capture). Default value: **false**. |
| `dispute_email` | `str` | Required | The email address for disputes. |
| `region` | [`RegionEnum`](../../doc/models/region-enum.md) | Required | The region of operation. For example, **NA**, **EU**, **CH**, **AU**.<br><br>**Constraints**: *Minimum Length*: `2`, *Maximum Length*: `2` |
| `support_email` | `str` | Required | The email address of merchant support. |

## Example

```python
from adyen.models.klarna_info import KlarnaInfo
from adyen.models.region_enum import RegionEnum

klarna_info = KlarnaInfo(
    dispute_email='disputeEmail4',
    region=RegionEnum.NA,
    support_email='supportEmail8',
    auto_capture=False
)
```

