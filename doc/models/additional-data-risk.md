
# Additional Data Risk

## Structure

`AdditionalDataRisk`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `riskdata_custom_field_name` | `str` | Optional | The data for your custom risk field. For more information, refer to [Create custom risk fields](https://docs.adyen.com/risk-management/configure-custom-risk-rules#step-1-create-custom-risk-fields). |
| `riskdata_basket_item_item_nr_amount_per_item` | `str` | Optional | The price of item in the basket, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `riskdata_basket_item_item_nr_brand` | `str` | Optional | Brand of the item. |
| `riskdata_basket_item_item_nr_category` | `str` | Optional | Category of the item. |
| `riskdata_basket_item_item_nr_color` | `str` | Optional | Color of the item. |
| `riskdata_basket_item_item_nr_currency` | `str` | Optional | The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
| `riskdata_basket_item_item_nr_item_id` | `str` | Optional | ID of the item. |
| `riskdata_basket_item_item_nr_manufacturer` | `str` | Optional | Manufacturer of the item. |
| `riskdata_basket_item_item_nr_product_title` | `str` | Optional | A text description of the product the invoice line refers to. |
| `riskdata_basket_item_item_nr_quantity` | `str` | Optional | Quantity of the item purchased. |
| `riskdata_basket_item_item_nr_receiver_email` | `str` | Optional | Email associated with the given product in the basket (usually in electronic gift cards). |
| `riskdata_basket_item_item_nr_size` | `str` | Optional | Size of the item. |
| `riskdata_basket_item_item_nr_sku` | `str` | Optional | [Stock keeping unit](https://en.wikipedia.org/wiki/Stock_keeping_unit). |
| `riskdata_basket_item_item_nr_upc` | `str` | Optional | [Universal Product Code](https://en.wikipedia.org/wiki/Universal_Product_Code). |
| `riskdata_promotions_promotion_item_nr_promotion_code` | `str` | Optional | Code of the promotion. |
| `riskdata_promotions_promotion_item_nr_promotion_discount_amount` | `str` | Optional | The discount amount of the promotion, represented in [minor units](https://docs.adyen.com/development-resources/currency-codes). |
| `riskdata_promotions_promotion_item_nr_promotion_discount_currency` | `str` | Optional | The three-character [ISO currency code](https://en.wikipedia.org/wiki/ISO_4217). |
| `riskdata_promotions_promotion_item_nr_promotion_discount_percentage` | `str` | Optional | Promotion's percentage discount. It is represented in percentage value and there is no need to include the '%' sign.<br><br>e.g. for a promotion discount of 30%, the value of the field should be 30. |
| `riskdata_promotions_promotion_item_nr_promotion_name` | `str` | Optional | Name of the promotion. |
| `riskdata_risk_profile_reference` | `str` | Optional | Reference number of the risk profile that you want to apply to the payment. If not provided or left blank, the merchant-level account's default risk profile will be applied to the payment. For more information, see [dynamically assign a risk profile to a payment](https://docs.adyen.com/risk-management/create-and-use-risk-profiles#dynamically-assign-a-risk-profile-to-a-payment). |
| `riskdata_skip_risk` | `str` | Optional | If this parameter is provided with the value **true**, risk checks for the payment request are skipped and the transaction will not get a risk score. |

## Example

```python
from adyen.models.additional_data_risk import AdditionalDataRisk

additional_data_risk = AdditionalDataRisk(
    riskdata_custom_field_name=Liquid error: Value cannot be null. (Parameter 'key'),
    riskdata_basket_item_item_nr_amount_per_item=Liquid error: Value cannot be null. (Parameter 'key'),
    riskdata_basket_item_item_nr_brand=Liquid error: Value cannot be null. (Parameter 'key'),
    riskdata_basket_item_item_nr_category=Liquid error: Value cannot be null. (Parameter 'key'),
    riskdata_basket_item_item_nr_color=Liquid error: Value cannot be null. (Parameter 'key')
)
```

