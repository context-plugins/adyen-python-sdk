
# Pix Pay by Bank Risk Signals

*This model accepts additional fields of type Any.*

## Structure

`PixPayByBankRiskSignals`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `confidence_score` | [`ConfidenceScore`](../../doc/models/confidence-score.md) | Optional | - |
| `elapsed_time_since_boot` | `int` | Optional | - |
| `is_rooted_device` | `bool` | Optional | - |
| `language` | `str` | Optional | - |
| `os_version` | `str` | Optional | **Constraints**: *Maximum Length*: `32` |
| `screen_brightness` | `int` | Optional | - |
| `screen_dimensions` | [`ScreenDimensions`](../../doc/models/screen-dimensions.md) | Optional | - |
| `user_time_zone_offset` | `int` | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.confidence_score import ConfidenceScore
from adyen.models.pix_pay_by_bank_risk_signals import PixPayByBankRiskSignals

pix_pay_by_bank_risk_signals = PixPayByBankRiskSignals(
    confidence_score=ConfidenceScore(
        errors=[
            'errors9',
            'errors0',
            'errors1'
        ],
        score=155.44,
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    elapsed_time_since_boot=28,
    is_rooted_device=False,
    language='language6',
    os_version='osVersion4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

