
# Disable Request

*This model accepts additional fields of type Any.*

## Structure

`DisableRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `contract` | `str` | Optional | Specify the contract if you only want to disable a specific use.<br><br>This field can be set to one of the following values, or to their combination (comma-separated):<br><br>* ONECLICK<br>* RECURRING<br>* PAYOUT |
| `merchant_account` | `str` | Required | The merchant account identifier with which you want to process the transaction. |
| `recurring_detail_reference` | `str` | Optional | The ID that uniquely identifies the recurring detail reference.<br><br>If it is not provided, the whole recurring contract of the `shopperReference` will be disabled, which includes all recurring details. |
| `shopper_reference` | `str` | Required | The ID that uniquely identifies the shopper.<br><br>This `shopperReference` must be the same as the `shopperReference` used in the initial payment. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.disable_request import DisableRequest

disable_request = DisableRequest(
    merchant_account='merchantAccount4',
    shopper_reference='shopperReference2',
    contract='contract4',
    recurring_detail_reference='recurringDetailReference4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

