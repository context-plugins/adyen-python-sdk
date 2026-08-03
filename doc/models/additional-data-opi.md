
# Additional Data Opi

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataOpi`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `opi_include_trans_token` | `str` | Optional | Optional boolean indicator. Set to **true** if you want an ecommerce transaction to return an `opi.transToken` as additional data in the response.<br><br>You can store this Oracle Payment Interface token in your Oracle Opera database. For more information and required settings, see [Oracle Opera](https://docs.adyen.com/plugins/oracle-opera#opi-token-ecommerce). |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_opi import AdditionalDataOpi

additional_data_opi = AdditionalDataOpi(
    opi_include_trans_token='opi.includeTransToken6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

