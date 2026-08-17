
# Offline Processing

## Structure

`OfflineProcessing`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `chip_floor_limit` | `int` | Optional | The maximum offline transaction amount for chip cards, in the processing currency and specified in [minor units](https://docs.adyen.com/development-resources/currency-codes). |

## Example

```python
from adyen.models.offline_processing import OfflineProcessing

offline_processing = OfflineProcessing(
    chip_floor_limit=10
)
```

