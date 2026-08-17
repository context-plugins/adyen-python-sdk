
# Temporary Services

## Structure

`TemporaryServices`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `employee_name` | `str` | Optional | The name or ID of the person working in a temporary capacity.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `enhancedSchemeData.employeeName` |
| `end_date` | `date` | Optional | The billing period end date.<br><br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `enhancedSchemeData.tempWeekEnding` |
| `hour_rate` | `int` | Optional | The hourly rate for the temporary services, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max value: 10000000000<br>* **additionalData key:** `enhancedSchemeData.regularHoursRate` |
| `hours_worked` | `int` | Optional | The number of hours worked during the billing period.<br><br>* Format: Numeric<br>* **additionalData key:** `enhancedSchemeData.regularHoursWorked` |
| `job_description` | `str` | Optional | The job description of the person working in a temporary capacity.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `enhancedSchemeData.jobDescription` |
| `service_requestor` | `str` | Optional | The name of the person requesting the temporary services.<br><br>* Format: ASCII<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.<br>* **additionalData key:** `enhancedSchemeData.requestName` |
| `start_date` | `date` | Optional | The billing period start date.<br><br>* Format [ISO 8601](https://www.w3.org/TR/NOTE-datetime): yyyy-MM-dd<br>* **additionalData key:** `enhancedSchemeData.tempStartDate` |

## Example

```python
import dateutil.parser

from adyen.models.temporary_services import TemporaryServices

temporary_services = TemporaryServices(
    employee_name='employeeName6',
    end_date=dateutil.parser.parse('2016-03-13').date(),
    hour_rate=184,
    hours_worked=124,
    job_description='jobDescription2'
)
```

