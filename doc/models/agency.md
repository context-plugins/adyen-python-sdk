
# Agency

*This model accepts additional fields of type Any.*

## Structure

`Agency`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `invoice_number` | `str` | Optional | The reference number for the invoice, issued by the agency.<br><br>* Encoding: ASCII<br>* minLength: 1 character<br>* maxLength: 6 characters<br>* **additionalData key:** `airline.agency_invoice_number` |
| `plan_name` | `str` | Optional | The two-letter agency plan identifier.<br><br>* Encoding: ASCII<br>* minLength: 2 characters<br>* maxLength: 2 characters<br>* **additionalData key:** `airline.agency_plan_name` |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.agency import Agency

agency = Agency(
    invoice_number='invoiceNumber6',
    plan_name='planName6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

