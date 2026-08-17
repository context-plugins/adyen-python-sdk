
# Address

The address where to send the invoice., The address where to send the invoice.

> The `billingAddress` object is required in the following scenarios. Include all of the fields within this object.
> 
> * For 3D Secure 2 transactions in all browser-based and mobile implementations.
> * For cross-border payouts to and from Canada., The address where the purchased goods should be delivered., The billing address., The address where to send the invoice., The address where to send the invoice.
>   The `billingAddress` object is required in the following scenarios. Include all of the fields within this object.
> * For 3D Secure 2 transactions in all browser-based and mobile implementations.
> * For cross-border payouts to and from Canada., The billing address.

> The `billingAddress` object is required for cross-border payouts to and from Canada. Include all of the fields within this object., The address of the account holder.

## Structure

`Address`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `city` | `str` | Required | The name of the city. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `country` | `str` | Required | The two-character ISO-3166-1 alpha-2 country code. For example, **US**.<br><br>> If you don't know the country or are not collecting the country from the shopper, provide `country` as `ZZ`. |
| `house_number_or_name` | `str` | Required | The number or name of the house. Maximum length: 3000 characters.<br><br>**Constraints**: *Maximum Length*: `3000` |
| `postal_code` | `str` | Required | A maximum of five digits for an address in the US, or a maximum of ten characters for an address in all other countries. |
| `state_or_province` | `str` | Optional | The two-character ISO 3166-2 state or province code. For example, **CA** in the US or **ON** in Canada.<br><br>> Required for the US and Canada. |
| `street` | `str` | Required | The name of the street. Maximum length: 3000 characters.<br><br>> The house number should not be included in this field; it should be separately provided via `houseNumberOrName`.<br><br>**Constraints**: *Maximum Length*: `3000` |

## Example

```python
from adyen.models.address import Address

address = Address(
    city='city6',
    country='country0',
    house_number_or_name='houseNumberOrName4',
    postal_code='postalCode8',
    street='street6',
    state_or_province='stateOrProvince4'
)
```

