# Cardorders

```python
cardorders_api = client.cardorders
```

## Class Name

`CardordersApi`

## Methods

* [Get-Cardorders](../../doc/controllers/cardorders.md#get-cardorders)
* [Get-Cardorders-Id-Items](../../doc/controllers/cardorders.md#get-cardorders-id-items)


# Get-Cardorders

Returns a paginated list of card orders.

```python
def get_cardorders(self,
                  id=None,
                  card_manufacturing_profile_id=None,
                  status=None,
                  tx_variant_code=None,
                  created_since=None,
                  created_until=None,
                  locked_since=None,
                  locked_until=None,
                  service_center=None,
                  offset=None,
                  limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Query, Optional | The unique identifier of the card order. |
| `card_manufacturing_profile_id` | `str` | Query, Optional | The unique identifier of the card manufacturer profile. |
| `status` | `str` | Query, Optional | The status of the card order. |
| `tx_variant_code` | `str` | Query, Optional | The unique code of the card manufacturer profile.<br><br>Possible values: **mcmaestro**, **mc**, **visa**, **mcdebit**. |
| `created_since` | `datetime` | Query, Optional | Only include card orders that have been created on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `created_until` | `datetime` | Query, Optional | Only include card orders that have been created on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `locked_since` | `datetime` | Query, Optional | Only include card orders that have been locked on or after this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `locked_until` | `datetime` | Query, Optional | Only include card orders that have been locked on or before this point in time. The value must be in ISO 8601 format. For example, **2021-05-30T15:07:40Z**. |
| `service_center` | `str` | Query, Optional | The service center at which the card is issued. The value is case-sensitive. |
| `offset` | `int` | Query, Optional | Specifies the position of an element in a list of card orders. The response includes a list of card orders that starts at the specified offset.<br><br>**Default:** 0, which means that the response contains all the elements in the list of card orders. |
| `limit` | `int` | Query, Optional | The number of card orders returned per page. **Default:** 10. |

## Response Type

**200**: OK - the request has succeeded.

[`PaginatedGetCardOrderResponse`](../../doc/models/paginated-get-card-order-response.md)

## Example Usage

```python
result = card_orders_api.get_cardorders()
print(result)
```

## Example Response *(as JSON)*

```json
{
  "cardOrders": [
    {
      "beginDate": "2022-12-05T00:00:00+01:00",
      "cardManufacturingProfileId": "UNIQUE_CARD_MANUFACTURER_PROFILE_ID",
      "endDate": "2022-12-06T00:00:00+01:00",
      "id": "UNIQUE_CARD_ORDER_ID",
      "lockDate": "2023-04-14T16:43:02+02:00",
      "serviceCenter": "IDEMIA Sittard",
      "status": "closed"
    }
  ],
  "hasNext": true,
  "hasPrevious": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Cardorders-Id-Items

Returns the item list of a specific card order.

```python
def get_cardorders_id_items(self,
                           id,
                           offset=None,
                           limit=None)
```

## Authentication

This endpoint requires [clientKey](../../doc/auth/custom-query-parameter.md) **OR** [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the card order. |
| `offset` | `int` | Query, Optional | Specifies the position of an element in a list of card orders. The response includes a list of card order items that starts at the specified offset.<br><br>**Default:** 0, which means that the response contains all the elements in the list of card order items. |
| `limit` | `int` | Query, Optional | The number of card order items returned per page. **Default:** 10. |

## Response Type

**200**: OK - the request has succeeded.

[`PaginatedGetCardOrderItemResponse`](../../doc/models/paginated-get-card-order-item-response.md)

## Example Usage

```python
id = 'id0'

result = card_orders_api.get_cardorders_id_items(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "card": {
        "status": "shipped"
      },
      "cardOrderItemId": "UNIQUE_CARD_ORDER_ITEM_ID",
      "paymentInstrumentId": "UNIQUE_PAYMENT_INSTRUMENT_ID",
      "pin": {
        "status": "produced"
      },
      "shippingMethod": "Cardholder Post Basic National"
    }
  ],
  "hasNext": false,
  "hasPrevious": false
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

