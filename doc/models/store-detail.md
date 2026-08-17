
# Store Detail

## Structure

`StoreDetail`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `address` | [`ViasAddress7`](../../doc/models/vias-address-7.md) | Required | The address of the physical store where the account holder will process payments from. |
| `full_phone_number` | `str` | Optional | The phone number of the store provided as a single string.  It will be handled as a landline phone.<br><br>Examples: "0031 6 11 22 33 44", "+316/1122-3344", "(0031) 611223344" |
| `logo` | `str` | Optional | Store logo for payment method setup. |
| `merchant_account` | `str` | Required | The merchant account to which the store belongs. |
| `merchant_category_code` | `str` | Required | The merchant category code (MCC) that classifies the business of the account holder. |
| `merchant_house_number` | `str` | Optional | Merchant house number for payment method setup. |
| `phone_number` | [`ViasPhoneNumber4`](../../doc/models/vias-phone-number-4.md) | Optional | The phone number of the store. |
| `shopper_interaction` | [`PaymentFlowEnum`](../../doc/models/payment-flow-enum.md) | Optional | The sales channel. Possible values: **Ecommerce**, **POS**. |
| `split_configuration_uuid` | `str` | Optional | The unique reference for the split configuration, returned when you configure splits in your Customer Area. When this is provided, the `virtualAccount` is also required. Adyen uses the configuration and the `virtualAccount` to split funds between accounts in your platform. |
| `status` | [`Status8Enum`](../../doc/models/status-8-enum.md) | Optional | The status of the store. Possible values: **Pending**, **Active**, **Inactive**, **InactiveWithModifications**, **Closed**. |
| `store` | `str` | Optional | Adyen-generated unique alphanumeric identifier (UUID) for the store, returned in the response when you create a store. Required when updating an existing store in an `/updateAccountHolder` request. |
| `store_name` | `str` | Optional | The name of the account holder's store. This value is shown in shopper statements.<br><br>* Length: Between 3 to 22 characters<br><br>* The following characters are *not* supported: **:;}{$#@!\|<>%^*+=\\**<br><br>**Note:** storeName does not appear in American Express shopper statements by default. Contact Adyen Support to enable this for American Express. |
| `store_reference` | `str` | Optional | Your unique identifier for the store. The Customer Area also uses this value for the store description.<br><br>* Length: Between 3 to 128 characters<br><br>* The following characters are *not* supported: **:;}{$#@!\|<>%^*+=\\** |
| `virtual_account` | `str` | Optional | The account holder's `accountCode` where the split amount will be sent. Required when you provide the `splitConfigurationUUID`. |
| `web_address` | `str` | Optional | URL of the ecommerce store. |

## Example

```python
from adyen.models.payment_flow_enum import PaymentFlowEnum
from adyen.models.phone_type_enum import PhoneTypeEnum
from adyen.models.store_detail import StoreDetail
from adyen.models.vias_address_7 import ViasAddress7
from adyen.models.vias_phone_number_4 import ViasPhoneNumber4

store_detail = StoreDetail(
    address=ViasAddress7(
        country='country0',
        city='city6',
        house_number_or_name='houseNumberOrName4',
        postal_code='postalCode8',
        state_or_province='stateOrProvince4',
        street='street6'
    ),
    merchant_account='merchantAccount6',
    merchant_category_code='merchantCategoryCode0',
    full_phone_number='fullPhoneNumber6',
    logo='logo2',
    merchant_house_number='merchantHouseNumber0',
    phone_number=ViasPhoneNumber4(
        phone_country_code='phoneCountryCode8',
        phone_number='phoneNumber0',
        phone_type=PhoneTypeEnum.FAX
    ),
    shopper_interaction=PaymentFlowEnum.ECOMMERCE
)
```

