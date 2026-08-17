
# Merchant

## Structure

`Merchant`

## Fields

| Name | Type | Tags | Description |
|  --- | --- | --- | --- |
| `links` | [`MerchantLinks2`](../../doc/models/merchant-links-2.md) | Optional | References to resources connected with this merchant. |
| `capture_delay` | `str` | Optional | The [capture delay](https://docs.adyen.com/online-payments/capture#capture-delay) set for the merchant account.<br><br>Possible values:<br><br>* **Immediate**<br>* **Manual**<br>* Number of days from **1** to **29** |
| `company_id` | `str` | Optional | The unique identifier of the company account this merchant belongs to |
| `data_centers` | [`List[DataCenter]`](../../doc/models/data-center.md) | Optional | List of available data centers.<br><br>Adyen has several data centers around the world.In the URL that you use for making API requests, we recommend you use the live URL prefix from the data center closest to your shoppers. |
| `default_shopper_interaction` | `str` | Optional | The default [`shopperInteraction`](https://docs.adyen.com/api-explorer/#/CheckoutService/v68/post/payments__reqParam_shopperInteraction) value used when processing payments through this merchant account. |
| `description` | `str` | Optional | Your description for the merchant account, maximum 300 characters |
| `id` | `str` | Optional | The unique identifier of the merchant account. |
| `merchant_city` | `str` | Optional | The city where the legal entity of this merchant account is registered. |
| `name` | `str` | Optional | The name of the legal entity associated with the merchant account. |
| `pricing_plan` | `str` | Optional | Only applies to merchant accounts managed by Adyen's partners. The name of the pricing plan assigned to the merchant account. |
| `primary_settlement_currency` | `str` | Optional | The currency of the country where the legal entity of this merchant account is registered. Format: [ISO currency code](https://docs.adyen.com/development-resources/currency-codes). For example, a legal entity based in the United States has USD as the primary settlement currency. |
| `reference` | `str` | Optional | Reference of the merchant account. |
| `shop_web_address` | `str` | Optional | The URL for the ecommerce website used with this merchant account. |
| `status` | `str` | Optional | The status of the merchant account.<br><br>Possible values:<br><br>* **PreActive**: The merchant account has been created. Users cannot access the merchant account in the Customer Area. The account cannot process payments.<br>* **Active**: Users can access the merchant account in the Customer Area. If the company account is also **Active**, then payment processing and payouts are enabled.<br>* **InactiveWithModifications**: Users can access the merchant account in the Customer Area. You cannot process new payments but you can still modify payments, for example issue refunds. You can still receive payouts.<br>* **Inactive**: Users can access the merchant account in the Customer Area. Payment processing and payouts are disabled.<br>* **Closed**: The account is closed and this cannot be reversed. Users cannot log in. Payment processing and payouts are disabled. |

## Example

```python
from adyen.models.data_center import DataCenter
from adyen.models.links_element import LinksElement
from adyen.models.links_element_6 import LinksElement6
from adyen.models.merchant import Merchant
from adyen.models.merchant_links_2 import MerchantLinks2

merchant = Merchant(
    links=MerchantLinks2(
        mself=LinksElement6(
            href='href0'
        ),
        api_credentials=LinksElement(
            href='href8'
        ),
        users=LinksElement(
            href='href8'
        ),
        webhooks=LinksElement(
            href='href8'
        )
    ),
    capture_delay='captureDelay0',
    company_id='companyId4',
    data_centers=[
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        ),
        DataCenter(
            live_prefix='livePrefix4',
            name='name6'
        )
    ],
    default_shopper_interaction='defaultShopperInteraction2'
)
```

