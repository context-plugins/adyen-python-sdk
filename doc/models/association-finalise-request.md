
# Association Finalise Request

## Structure

`AssociationFinaliseRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `ids` | `List[str]` | Required | The list of unique identifiers of the resources that you are associating with the SCA device.<br><br>Maximum: 5 strings. |
| `strong_customer_authentication` | [`AssociationDelegatedAuthenticationData1`](../../doc/models/association-delegated-authentication-data-1.md) | Required | Contains authentication information required to associate the resource with the SCA device. |
| `mtype` | `str` | Required, Constant | The type of resource that you are associating with the SCA device.<br><br>Possible value: **PaymentInstrument**<br><br>**Value**: `"PaymentInstrument"` |

## Example

```python
from adyen.models.association_delegated_authentication_data_1 import AssociationDelegatedAuthenticationData1
from adyen.models.association_finalise_request import AssociationFinaliseRequest

association_finalise_request = AssociationFinaliseRequest(
    ids=[
        'ids3'
    ],
    strong_customer_authentication=AssociationDelegatedAuthenticationData1(
        sdk_output='sdkOutput4'
    )
)
```

