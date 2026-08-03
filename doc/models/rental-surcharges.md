
# Rental Surcharges

*This model accepts additional fields of type Any.*

## Structure

`RentalSurcharges`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fuel` | `int` | Optional | The fuel charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.fuelCharges` |
| `insurance` | `int` | Optional | Any insurance charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.insuranceCharges` |
| `one_way_drop_off` | `int` | Optional | The charge for not returning a car to the original rental location, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.oneWayDropOffCharges` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.rental_surcharges import RentalSurcharges

rental_surcharges = RentalSurcharges(
    fuel=134,
    insurance=246,
    one_way_drop_off=66,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

