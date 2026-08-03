
# Notify Shopper Result

*This model accepts additional fields of type Any.*

## Structure

`NotifyShopperResult`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `displayed_reference` | `str` | Optional | Reference of Pre-debit notification that is displayed to the shopper |
| `message` | `str` | Optional | A simple description of the `resultCode`. |
| `psp_reference` | `str` | Optional | The unique reference that is associated with the request. |
| `reference` | `str` | Optional | Reference of Pre-debit notification sent in my the merchant |
| `result_code` | `str` | Optional | The code indicating the status of notification. |
| `shopper_notification_reference` | `str` | Optional | The unique reference for the request sent downstream. |
| `stored_payment_method_id` | `str` | Optional | This is the recurringDetailReference returned in the response when token was created |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.notify_shopper_result import NotifyShopperResult

notify_shopper_result = NotifyShopperResult(
    displayed_reference='displayedReference6',
    message='message8',
    psp_reference='pspReference0',
    reference='reference4',
    result_code='resultCode4',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

