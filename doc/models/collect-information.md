
# Collect Information

*This model accepts additional fields of type Any.*

## Structure

`CollectInformation`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `bank_details` | `bool` | Optional | Indicates whether [bank account details](https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#bank-accounts) must be collected. Default is **true**. |
| `business_details` | `bool` | Optional | Indicates whether [business details](https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#organizations) must be collected. Default is **true**. |
| `individual_details` | `bool` | Optional | Indicates whether [individual details](https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#individuals) must be collected. Default is **true**. |
| `legal_arrangement_details` | `bool` | Optional | Indicates whether [legal arrangement details](https://docs.adyen.com/classic-platforms/verification-checks/legal-arrangements) must be collected. Default is **true**. |
| `pci_questionnaire` | `bool` | Optional | Indicates whether answers to a [PCI questionnaire](https://docs.adyen.com/classic-platforms/platforms-for-partners#onboard-partner-platform) must be collected. Applies only to partner platforms. Default is **true**. |
| `shareholder_details` | `bool` | Optional | Indicates whether [shareholder details](https://docs.adyen.com/classic-platforms/verification-process/accepted-data-format/#individuals) must be collected. Defaults to **true**. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.collect_information import CollectInformation

collect_information = CollectInformation(
    bank_details=False,
    business_details=False,
    individual_details=False,
    legal_arrangement_details=False,
    pci_questionnaire=False,
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

