
# Three DS Availability Request

## Structure

`ThreeDSAvailabilityRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `additional_data` | `Dict[str, str]` | Optional | This field contains additional data, which may be required for a particular request.<br><br>The `additionalData` object consists of entries, each of which includes the key and value. |
| `brands` | `List[str]` | Optional | List of brands. |
| `card_number` | `str` | Optional | Card number or BIN. |
| `merchant_account` | `str` | Required | The merchant account identifier. |
| `recurring_detail_reference` | `str` | Optional | A recurring detail reference corresponding to a card. |
| `shopper_reference` | `str` | Optional | The shopper's reference to uniquely identify this shopper (e.g. user ID or account ID). |

## Example

```python
from adyen.models.three_ds_availability_request import ThreeDSAvailabilityRequest

three_ds_availability_request = ThreeDSAvailabilityRequest(
    merchant_account='merchantAccount8',
    additional_data={
        'key0': 'additionalData6'
    },
    brands=[
        'brands7',
        'brands8'
    ],
    card_number='cardNumber2',
    recurring_detail_reference='recurringDetailReference6',
    shopper_reference='shopperReference4'
)
```

