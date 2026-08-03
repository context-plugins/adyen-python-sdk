
# Additional Data Level 23

*This model accepts additional fields of type Any.*

## Structure

`AdditionalDataLevel23`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `enhanced_scheme_data_customer_reference` | `str` | Optional | The reference number to identify the customer and their order.<br><br>* Encoding: ASCII<br>* Max length: 25 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros. |
| `enhanced_scheme_data_destination_country_code` | `str` | Optional | The three-letter [ISO 3166-1 alpha-3 country code](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-3) for the destination address.<br><br>* Encoding: ASCII<br>* Fixed length: 3 characters |
| `enhanced_scheme_data_destination_postal_code` | `str` | Optional | The postal code of the destination address.<br><br>* Encoding: ASCII<br>* Max length: 10 characters<br>* Must not start with a space.<br>* For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.<br>* For Canada, it must be in 6 digits format. For example, M4B 1G5. |
| `enhanced_scheme_data_destination_state_province_code` | `str` | Optional | The state or province code of the destination address.<br><br>* Encoding: ASCII<br>* Max length: 3 characters<br>* Must not start with a space. |
| `enhanced_scheme_data_duty_amount` | `str` | Optional | The duty tax amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max length: 12 characters |
| `enhanced_scheme_data_freight_amount` | `str` | Optional | The shipping amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max length: 12 characters |
| `enhanced_scheme_data_item_detail_line_item_nr_commodity_code` | `str` | Optional | The code that identifies the item in a standardized commodity coding scheme. There are different commodity coding schemes:<br><br>* [UNSPSC commodity codes](https://www.ungm.org/public/unspsc)<br><br>* [HS commodity codes](https://www.wcoomd.org/en/topics/nomenclature/overview.aspx)<br><br>* [NAICS commodity codes](https://www.census.gov/naics/)<br><br>* [NAPCS commodity codes](https://www.census.gov/naics/napcs/)<br><br>* Encoding: ASCII<br><br>* Max length: 12 characters<br><br>* Must not start with a space or be all spaces.<br><br>* Must not be all zeros. |
| `enhanced_scheme_data_item_detail_line_item_nr_description` | `str` | Optional | A description of the item, that provides details about the purchase.<br><br>For Visa transactions with level 3 ESD, the description must not be the same or very similar to your merchant name, or, consist only of common words like "product", or "service".<br><br>* Encoding: ASCII<br>* Max length: 26 characters<br>* Must not be a single character.<br>* Must not be blank.<br>* Must not be all special characters.<br>* Must not be blank.<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros. |
| `enhanced_scheme_data_item_detail_line_item_nr_discount_amount` | `str` | Optional | The discount amount, in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max length: 12 characters |
| `enhanced_scheme_data_item_detail_line_item_nr_product_code` | `str` | Optional | The product code. Must be a unique product code associated with the item or service. This can be your unique code for the item, or the manufacturer's product code.<br><br>* Encoding: ASCII.<br>* Max length: 12 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros. |
| `enhanced_scheme_data_item_detail_line_item_nr_quantity` | `str` | Optional | The number of items. Must be an integer greater than zero.<br><br>* Encoding: Numeric<br>* Max length: 12 characters<br>* Must not start with a space or be all spaces. |
| `enhanced_scheme_data_item_detail_line_item_nr_total_amount` | `str` | Optional | The total amount for the line item, in [minor units](https://docs.adyen.com/development-resources/currency-codes). See [Amount requirements for level 2/3 ESD](https://docs.adyen.com//payment-methods/cards/enhanced-scheme-data/l2-l3#amount-requirements) to learn more about how to calculate the line item total.<br><br>* For example, 2000 means USD 20.00.<br>* Max length: 12 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros. |
| `enhanced_scheme_data_item_detail_line_item_nr_unit_of_measure` | `str` | Optional | The unit of measurement for an item.<br><br>* Encoding: ASCII<br>* Max length: 3 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros. |
| `enhanced_scheme_data_item_detail_line_item_nr_unit_price` | `str` | Optional | The unit price in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max length: 12 characters<br>* Must not be all zeros. |
| `enhanced_scheme_data_order_date` | `str` | Optional | The order date.<br><br>* Format: `ddMMyy`<br>* Encoding: ASCII<br>* Max length: 6 characters |
| `enhanced_scheme_data_ship_from_postal_code` | `str` | Optional | The postal code of the address where the item is shipped from.<br><br>* Encoding: ASCII<br>* Max length: 10 characters<br>* Must not start with a space or be all spaces.<br>* Must not be all zeros.For the US, it must be in five or nine digits format. For example, 10001 or 10001-0000.<br>* For Canada, it must be in 6 digits format. For example, M4B 1G5. |
| `enhanced_scheme_data_total_tax_amount` | `str` | Optional | The amount of state or provincial [tax included in the total transaction amount](https://docs.adyen.com/payment-methods/cards/enhanced-scheme-data/l2-l3#requirements-to-send-level-2-3-esd), in [minor units](https://docs.adyen.com/development-resources/currency-codes).<br><br>* For example, 2000 means USD 20.00.<br>* Encoding: Numeric<br>* Max length: 12 characters<br>* For L2 data: must not be all zeroes.<br>* For L3 data: can be zero. |
| `additional_properties` | `Dict[str, Any]` | Optional | - |

## Example

```python
import jsonpickle

from adyen.models.additional_data_level_23 import AdditionalDataLevel23

additional_data_level_23 = AdditionalDataLevel23(
    enhanced_scheme_data_customer_reference='enhancedSchemeData.customerReference2',
    enhanced_scheme_data_destination_country_code='enhancedSchemeData.destinationCountryCode2',
    enhanced_scheme_data_destination_postal_code='enhancedSchemeData.destinationPostalCode4',
    enhanced_scheme_data_destination_state_province_code='enhancedSchemeData.destinationStateProvinceCode8',
    enhanced_scheme_data_duty_amount='enhancedSchemeData.dutyAmount8',
    additional_properties={
        'exampleAdditionalProperty': jsonpickle.decode('{"key1":"val1","key2":"val2"}')
    }
)
```

