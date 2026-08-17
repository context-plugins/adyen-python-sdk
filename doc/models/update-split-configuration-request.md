
# Update Split Configuration Request

## Structure

`UpdateSplitConfigurationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `description` | `str` | Required | Your description for the split configuration.<br><br>**Constraints**: *Maximum Length*: `300` |

## Example

```python
from adyen.models.update_split_configuration_request import UpdateSplitConfigurationRequest

update_split_configuration_request = UpdateSplitConfigurationRequest(
    description='description8'
)
```

