
# Update Store Request

*This model accepts additional fields of type Any.*

## Structure

`UpdateStoreRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`UpdatableAddress`](../../doc/models/updatable-address.md) | Optional | - |
| `business_line_ids` | `List[str]` | Optional | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/#/legalentity/latest/post/businessLines__resParam_id) that the store is associated with. |
| `description` | `str` | Optional | The description of the store. |
| `external_reference_id` | `str` | Optional | The unique identifier of the store, used by certain payment methods and tax authorities.<br><br>Required for CNPJ in Brazil, in the format 00.000.000/0000-00 separated by dots, slashes, hyphens, or without separators.<br><br>Optional for SIRET in France, up to 14 digits.<br><br>Optional for Zip in Australia, up to 50 digits. |
| `phone_number` | `str` | Optional | The phone number of the store, including '+' and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number against E.164. |
| `split_configuration` | [`StoreSplitConfiguration`](../../doc/models/store-split-configuration.md) | Optional | - |
| `status` | [`Status43`](../../doc/models/status-43.md) | Optional | - |
| `sub_merchant_data` | [`SubMerchantData`](../../doc/models/sub-merchant-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.updatable_address import UpdatableAddress
from adyen.models.update_store_request import UpdateStoreRequest

update_store_request = UpdateStoreRequest(
    address=UpdatableAddress(
        city='city6',
        line_1='line18',
        line_2='line20',
        line_3='line38',
        postal_code='postalCode8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    business_line_ids=[
        'businessLineIds6',
        'businessLineIds7',
        'businessLineIds8'
    ],
    description='description8',
    external_reference_id='externalReferenceId0',
    phone_number='phoneNumber8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

