
# Rental Surcharges

## Structure

`RentalSurcharges`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `fuel` | `int` | Optional | The fuel charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.fuelCharges` |
| `insurance` | `int` | Optional | Any insurance charges associated with the rental, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.insuranceCharges` |
| `one_way_drop_off` | `int` | Optional | The charge for not returning a car to the original rental location, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `carRental.oneWayDropOffCharges` |

## Example

```python
from adyen.models.rental_surcharges import RentalSurcharges

rental_surcharges = RentalSurcharges(
    fuel=134,
    insurance=246,
    one_way_drop_off=66
)
```

