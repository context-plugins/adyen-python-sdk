
# Store Creation Request

## Structure

`StoreCreationRequest`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`StoreLocation1`](../../doc/models/store-location-1.md) | Required | The address of the store. |
| `business_line_ids` | `List[str]` | Optional | The unique identifiers of the [business lines](https://docs.adyen.com/api-explorer/legalentity/latest/post/businessLines#responses-200-id) that the store is associated with.<br>If not specified, the business line of the merchant account is used. Required when there are multiple business lines under the merchant account. |
| `description` | `str` | Required | Your description of the store. |
| `external_reference_id` | `str` | Optional | The unique identifier of the store, used by certain payment methods and tax authorities.<br><br>Required for CNPJ in Brazil, in the format 00.000.000/0000-00 separated by dots, slashes, hyphens, or without separators.<br><br>Optional for SIRET in France, up to 14 digits.<br><br>Optional for Zip in Australia, up to 50 digits. |
| `localized_information` | [`LocalizedInformation2`](../../doc/models/localized-information-2.md) | Optional | Localized information about the store. |
| `phone_number` | `str` | Required | The phone number of the store, including '+' and country code in the [E.164](https://en.wikipedia.org/wiki/E.164) format. If passed in a different format, we convert and validate the phone number against E.164. |
| `reference` | `str` | Optional | Your reference to recognize the store by. Also known as the store code.<br>Allowed characters: lowercase and uppercase letters without diacritics, numbers 0 through 9, hyphen (-), and underscore (_).<br><br>If you do not provide a reference in your POST request, it is populated with the Adyen-generated [id](https://docs.adyen.com/api-explorer/Management/latest/post/stores#responses-200-id). |
| `shopper_statement` | `str` | Required | The store name to be shown on the shopper's bank or credit card statement and on the shopper receipt.<br>Maximum length: 22 characters; can't be all numbers. |
| `split_configuration` | [`StoreSplitConfiguration1`](../../doc/models/store-split-configuration-1.md) | Optional | Rules for Adyen for Platforms merchants to split the transaction amount and fees. |
| `sub_merchant_data` | [`SubMerchantData1`](../../doc/models/sub-merchant-data-1.md) | Optional | The sub-merchant data relevant for registered payment facilitators transacting on standalone terminals. |

## Example

```python
from adyen.models.local_shopper_statement import LocalShopperStatement
from adyen.models.localized_information_2 import LocalizedInformation2
from adyen.models.store_creation_request import StoreCreationRequest
from adyen.models.store_location_1 import StoreLocation1
from adyen.models.store_split_configuration_1 import StoreSplitConfiguration1

store_creation_request = StoreCreationRequest(
    address=StoreLocation1(
        country='country0',
        city='city6',
        line_1='line18',
        line_2='line20',
        line_3='line38',
        postal_code='postalCode8'
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
    localized_information=LocalizedInformation2(
        local_shopper_statement=[
            LocalShopperStatement(
                script='script4',
                value='value6'
            ),
            LocalShopperStatement(
                script='script4',
                value='value6'
            ),
            LocalShopperStatement(
                script='script4',
                value='value6'
            )
        ]
    ),
    reference='reference2',
    split_configuration=StoreSplitConfiguration1(
        balance_account_id='balanceAccountId8',
        split_configuration_id='splitConfigurationId4'
    )
)
```

