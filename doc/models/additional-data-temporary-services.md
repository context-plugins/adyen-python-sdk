
# Additional Data Temporary Services

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataTemporaryServices`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enhanced_scheme_data_customer_reference` | `str` | Optional | The customer code, if supplied by a customer.<br><br>* Encoding: ASCII<br>* maxLength: 25 |
| `enhanced_scheme_data_employee_name` | `str` | Optional | The name or ID of the person working in a temporary capacity.<br><br>* maxLength: 40.<br>* Must not be all spaces.<br>  *Must not be all zeros. |
| `enhanced_scheme_data_job_description` | `str` | Optional | The job description of the person working in a temporary capacity.<br><br>* maxLength: 40<br>* Must not be all spaces.<br>  *Must not be all zeros. |
| `enhanced_scheme_data_regular_hours_rate` | `str` | Optional | The amount paid for regular hours worked, [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* maxLength: 7<br>* Must not be empty<br>* Can be all zeros |
| `enhanced_scheme_data_regular_hours_worked` | `str` | Optional | The hours worked.<br><br>* maxLength: 7<br>* Must not be empty<br>* Can be all zeros |
| `enhanced_scheme_data_request_name` | `str` | Optional | The name of the person requesting temporary services.<br><br>* maxLength: 40<br>* Must not be all zeros<br>* Must not be all spaces |
| `enhanced_scheme_data_temp_start_date` | `str` | Optional | The billing period start date.<br><br>* Format: ddMMyy<br>* maxLength: 6 |
| `enhanced_scheme_data_temp_week_ending` | `str` | Optional | The billing period end date.<br><br>* Format: ddMMyy<br>* maxLength: 6 |
| `enhanced_scheme_data_total_tax_amount` | `str` | Optional | The total tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes). For example, 2000 means USD 20.00<br><br>* maxLength: 12 |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_temporary_services import AdditionalDataTemporaryServices

additional_data_temporary_services = AdditionalDataTemporaryServices(
    enhanced_scheme_data_customer_reference='enhancedSchemeData.customerReference0',
    enhanced_scheme_data_employee_name='enhancedSchemeData.employeeName0',
    enhanced_scheme_data_job_description='enhancedSchemeData.jobDescription0',
    enhanced_scheme_data_regular_hours_rate='enhancedSchemeData.regularHoursRate4',
    enhanced_scheme_data_regular_hours_worked='enhancedSchemeData.regularHoursWorked6',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

