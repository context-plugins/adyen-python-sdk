
# Store Creation Request

*This model accepts additional fields of type Any.*

## Structure

`StoreCreationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`Address15`](../../doc/models/address-15.md) | Required | - |
| `business_line_ids` | `List[str]` | Optional | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/legalentity/latest/post/businessLines#responses-200-id) that the store is associated with.<br>If not specified, the business line of the merchant account is used. Required when there are multiple business lines under the merchant account. |
| `description` | `str` | Required | Your description of the store. |
| `external_reference_id` | `str` | Optional | The unique identifier of the store, used by certain payment methods and tax authorities.<br><br>Required for CNPJ in Brazil, in the format 00.000.000/0000-00 separated by dots, slashes, hyphens, or without separators.<br><br>Optional for SIRET in France, up to 14 digits.<br><br>Optional for Zip in Australia, up to 50 digits. |
| `localized_information` | [`LocalizedInformation`](../../doc/models/localized-information.md) | Optional | - |
| `phone_number` | `str` | Required | The phone number of the store, including '+' and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number against E.164. |
| `reference` | `str` | Optional | Your reference to recognize the store by. Also known as the store code.<br>Allowed characters: lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and underscore (_).<br><br>If you do not provide a reference in your POST request, it is populated with the Adyen-generated [id](https://docs.adyen.com/api-explorer/Management/latest/post/stores#responses-200-id). |
| `shopper_statement` | `str` | Required | The store name to be shown on the shopper's bank or credit card statement and on the shopper receipt.<br>Maximum length: 22 characters; can't be all numbers. |
| `split_configuration` | [`StoreSplitConfiguration`](../../doc/models/store-split-configuration.md) | Optional | - |
| `sub_merchant_data` | [`SubMerchantData`](../../doc/models/sub-merchant-data.md) | Optional | - |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.address_15 import Address15
from adyen.models.local_shopper_statement import LocalShopperStatement
from adyen.models.localized_information import LocalizedInformation
from adyen.models.store_creation_request import StoreCreationRequest
from adyen.models.store_split_configuration import StoreSplitConfiguration

store_creation_request = StoreCreationRequest(
    address=Address15(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        line_3='line38',
        postal_code='postalCode8',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    description='description6',
    phone_number='phoneNumber4',
    shopper_statement='shopperStatement0',
    business_line_ids=[
        'businessLineIds0',
        'businessLineIds1',
        'businessLineIds2'
    ],
    external_reference_id='externalReferenceId4',
    localized_information=LocalizedInformation(
        local_shopper_statement=[
            LocalShopperStatement(
                script='script4',
                value='value6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            LocalShopperStatement(
                script='script4',
                value='value6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            ),
            LocalShopperStatement(
                script='script4',
                value='value6',
                additional_properties={
                    'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
                }
            )
        ],
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    reference='reference2',
    split_configuration=StoreSplitConfiguration(
        balance_account_id='balanceAccountId8',
        split_configuration_id='splitConfigurationId4',
        additional_properties={
            'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
        }
    ),
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

