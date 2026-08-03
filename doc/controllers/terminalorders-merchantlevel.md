# Terminalorders-Merchantlevel

```python
terminalorders_merchantlevel_api = client.terminalorders_merchantlevel
```

## Class Name

`TerminalordersMerchantlevelApi`

## Methods

* [Get-Merchants-Merchant Id-Billing Entities](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-billing-entities)
* [Get-Merchants-Merchant Id-Shipping Locations](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-shipping-locations)
* [Post-Merchants-Merchant Id-Shipping Locations](../../doc/controllers/terminalorders-merchantlevel.md#post-merchants-merchant-id-shipping-locations)
* [Get-Merchants-Merchant Id-Terminal Models](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-terminal-models)
* [Get-Merchants-Merchant Id-Terminal Orders](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-terminal-orders)
* [Post-Merchants-Merchant Id-Terminal Orders](../../doc/controllers/terminalorders-merchantlevel.md#post-merchants-merchant-id-terminal-orders)
* [Get-Merchants-Merchant Id-Terminal Orders-Order Id](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-terminal-orders-order-id)
* [Patch-Merchants-Merchant Id-Terminal Orders-Order Id](../../doc/controllers/terminalorders-merchantlevel.md#patch-merchants-merchant-id-terminal-orders-order-id)
* [Post-Merchants-Merchant Id-Terminal Orders-Order Id-Cancel](../../doc/controllers/terminalorders-merchantlevel.md#post-merchants-merchant-id-terminal-orders-order-id-cancel)
* [Get-Merchants-Merchant Id-Terminal Products](../../doc/controllers/terminalorders-merchantlevel.md#get-merchants-merchant-id-terminal-products)


# Get-Merchants-Merchant Id-Billing Entities

Returns the billing entities of the merchant account identified in the path.
A billing entity is a legal entity where we charge orders to. An order for terminal products must contain the ID of a billing entity.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_billing_entities(self,
                                              merchant_id,
                                              name=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `name` | `str` | Query, Optional | The name of the billing entity. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`BillingEntitiesResponse`](../../doc/models/billing-entities-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_billing_entities(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
      "name": "YOUR_MERCHANT_ACCOUNT",
      "taxId": "ES1234567890",
      "email": "Pablo.Mengano@company.com",
      "address": {
        "streetAddress": "Paseo de la Castellana 43, 7",
        "postalCode": "28046",
        "city": "Madrid",
        "country": "ES"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Shipping Locations

Returns the shipping locations for the merchant account identified in the path.
A shipping location includes the address where orders can be delivered, and an ID which you need to specify when ordering terminal products.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_shipping_locations(self,
                                                merchant_id,
                                                name=None,
                                                offset=None,
                                                limit=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `name` | `str` | Query, Optional | The name of the shipping location. |
| `offset` | `int` | Query, Optional | The number of locations to skip. |
| `limit` | `int` | Query, Optional | The number of locations to return. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ShippingLocationsResponse`](../../doc/models/shipping-locations-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_shipping_locations(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
      "name": "YOUR_COMPANY Spain",
      "contact": {
        "firstName": "Pablo",
        "lastName": "Mengano",
        "phoneNumber": "+34911234567",
        "email": "Pablo.Mengano@company.com"
      },
      "address": {
        "streetAddress": "Paseo de la Castellana 43",
        "streetAddress2": "7 piso",
        "postalCode": "28046",
        "city": "Madrid",
        "country": "ES"
      }
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Shipping Locations

Creates a shipping location for the merchant account identified in the path. A shipping location defines an address where orders can be shipped to.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def post_merchants_merchant_id_shipping_locations(self,
                                                 merchant_id,
                                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `body` | [`ShippingLocation`](../../doc/models/shipping-location.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ShippingLocation`](../../doc/models/shipping-location.md).

## Example Usage

```python
merchant_id = 'merchantId6'

body = ShippingLocation(
    address=Address6(
        city='Barcelona',
        company_name='YOUR_COMPANY',
        country='ES',
        postal_code='08012',
        state_or_province='',
        street_address='El quinto pino 42'
    ),
    contact=Contact(
        email='Rita.Perengano@company.com',
        first_name='Rita',
        last_name='Perengano',
        phone_number='+34 93 1234567'
    ),
    name='YOUR_MERCHANT_ACCOUNT Barcelona depot'
)

result = terminal_orders_merchant_level_api.post_merchants_merchant_id_shipping_locations(
    merchant_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "S2-73536B20665526704F30792642212044452F714622375D477270",
  "name": "YOUR_MERCHANT_ACCOUNT Barcelona depot",
  "contact": {
    "firstName": "Rita",
    "lastName": "Perengano",
    "phoneNumber": "+34931234567",
    "email": "Rita.Perengano@company.com"
  },
  "address": {
    "companyName": "YOUR_COMPANY",
    "streetAddress": "El quinto pino 42",
    "postalCode": "08012",
    "city": "Barcelona",
    "stateOrProvince": ""
  }
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Terminal Models

Returns the payment terminal models that the merchant account identified in the path has access to. The response includes the terminal model ID, which can be used as a query parameter when getting a list of terminals or a list of products for ordering.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_terminal_models(self,
                                             merchant_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalModelsResponse`](../../doc/models/terminal-models-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_terminal_models(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "Verifone.e315",
      "name": "Verifone e315"
    },
    {
      "id": "Verifone.e315M",
      "name": "Verifone e315M"
    },
    {
      "id": "Verifone.E355",
      "name": "Verifone E355"
    },
    {
      "id": "Verifone.M400",
      "name": "Verifone M400"
    },
    {
      "id": "Verifone.MX915",
      "name": "Verifone MX915"
    },
    {
      "id": "Verifone.MX925",
      "name": "Verifone MX925"
    },
    {
      "id": "Verifone.P400",
      "name": "Verifone P400"
    },
    {
      "id": "Verifone.P400Plus",
      "name": "Verifone P400Plus"
    },
    {
      "id": "Verifone.P400Eth",
      "name": "Verifone P400Eth"
    },
    {
      "id": "Verifone.V240m",
      "name": "Verifone V240m"
    },
    {
      "id": "Verifone.V240mPlus",
      "name": "Verifone V240mPlus"
    },
    {
      "id": "Verifone.UX300",
      "name": "Verifone UX300"
    },
    {
      "id": "Verifone.V200cPlus",
      "name": "Verifone V200cPlus"
    },
    {
      "id": "Verifone.V400cPlus",
      "name": "Verifone V400cPlus"
    },
    {
      "id": "Verifone.V400m",
      "name": "Verifone V400m"
    },
    {
      "id": "Verifone.V210mPlus",
      "name": "Verifone V210mPlus"
    },
    {
      "id": "Verifone.VX520",
      "name": "Verifone VX520"
    },
    {
      "id": "Verifone.VX6753G",
      "name": "Verifone VX6753G"
    },
    {
      "id": "Verifone.VX675WIFIBT",
      "name": "Verifone VX675WIFIBT"
    },
    {
      "id": "Verifone.VX680",
      "name": "Verifone VX680"
    },
    {
      "id": "Verifone.VX6803G",
      "name": "Verifone VX6803G"
    },
    {
      "id": "Verifone.VX690",
      "name": "Verifone VX690"
    },
    {
      "id": "Verifone.VX700",
      "name": "Verifone VX700"
    },
    {
      "id": "Verifone.VX810",
      "name": "Verifone VX810"
    },
    {
      "id": "Verifone.VX820",
      "name": "Verifone VX820"
    },
    {
      "id": "Verifone.VX825",
      "name": "Verifone VX825"
    },
    {
      "id": "Verifone.e285",
      "name": "Verifone e285"
    },
    {
      "id": "Verifone.E285",
      "name": "Verifone E285"
    },
    {
      "id": "Verifone.e285p",
      "name": "Verifone e285p"
    },
    {
      "id": "Verifone.e280",
      "name": "Verifone e280"
    },
    {
      "id": "Verifone.UX410",
      "name": "Verifone UX410"
    },
    {
      "id": "Castles.S1E",
      "name": "Castles S1E"
    },
    {
      "id": "Castles.S1EL",
      "name": "Castles S1EL"
    },
    {
      "id": "Castles.S1F",
      "name": "Castles S1F"
    },
    {
      "id": "Castles.S1F2",
      "name": "Castles S1F2"
    },
    {
      "id": "Castles.S1F2L",
      "name": "Castles S1F2L"
    },
    {
      "id": "Castles.S1E2",
      "name": "Castles S1E2"
    },
    {
      "id": "Castles.S1E2L",
      "name": "Castles S1E2L"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Terminal Orders

Returns a list of terminal products orders for the merchant account identified in the path.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_terminal_orders(self,
                                             merchant_id,
                                             customer_order_reference=None,
                                             status=None,
                                             offset=None,
                                             limit=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | - |
| `customer_order_reference` | `str` | Query, Optional | Your purchase order number. |
| `status` | `str` | Query, Optional | The order status. Possible values (not case-sensitive): Placed, Confirmed, Cancelled, Shipped, Delivered. |
| `offset` | `int` | Query, Optional | The number of orders to skip. |
| `limit` | `int` | Query, Optional | The number of orders to return. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalOrdersResponse`](../../doc/models/terminal-orders-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_terminal_orders(merchant_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "4154567890100682",
      "customerOrderReference": "YOUR_REFERENCE_M2",
      "status": "Placed",
      "shippingLocation": {
        "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
        "name": "YOUR_COMPANY Spain",
        "contact": {
          "firstName": "Pablo",
          "lastName": "Mengano",
          "phoneNumber": "+34911234567",
          "email": "Pablo.Mengano@company.com"
        },
        "address": {
          "streetAddress": "Paseo de la Castellana 43",
          "streetAddress2": "7 piso",
          "postalCode": "28046",
          "city": "Madrid",
          "country": "ES"
        }
      },
      "billingEntity": {
        "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
        "name": "YOUR_MERCHANT_ACCOUNT",
        "taxId": "ES1234567890",
        "email": "Pablo.Mengano@company.com",
        "address": {
          "streetAddress": "Paseo de la Castellana 43, 7",
          "postalCode": "28046",
          "city": "Madrid",
          "country": "ES"
        }
      },
      "orderDate": "2022-01-21T16:12:33Z",
      "items": [
        {
          "id": "PART-287001-EU",
          "name": "Bluetooth Charging Base - V400m",
          "quantity": 2
        },
        {
          "id": "PART-620222-EU",
          "name": "Receipt Roll",
          "quantity": 20
        }
      ]
    },
    {
      "id": "8315943674501996",
      "customerOrderReference": "YOUR_REFERENCE_M1",
      "status": "Cancelled",
      "shippingLocation": {
        "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
        "name": "YOUR_COMPANY Spain",
        "contact": {
          "firstName": "Pablo",
          "lastName": "Mengano",
          "phoneNumber": "+34911234567",
          "email": "Pablo.Mengano@company.com"
        },
        "address": {
          "streetAddress": "Paseo de la Castellana 43",
          "streetAddress2": "7 piso",
          "postalCode": "28046",
          "city": "Madrid",
          "country": "ES"
        }
      },
      "billingEntity": {
        "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
        "name": "YOUR_MERCHANT_ACCOUNT",
        "taxId": "ES1234567890",
        "email": "Pablo.Mengano@company.com",
        "address": {
          "streetAddress": "Paseo de la Castellana 43, 7",
          "postalCode": "28046",
          "city": "Madrid",
          "country": "ES"
        }
      },
      "orderDate": "2022-01-04T09:41:07.000Z",
      "items": [
        {
          "id": "TBOX-V400m-774-EU",
          "name": "V400m Package",
          "quantity": 1
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Terminal Orders

Creates an order for payment terminal products for the merchant account identified in the path.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read and write

> Requests to the Management API test endpoint do not create actual orders for test terminals. To order test terminals, you need to [submit a sales order](https://docs.adyen.com/point-of-sale/managing-terminals/order-terminals/#sales-order-steps) in your Customer Area.

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def post_merchants_merchant_id_terminal_orders(self,
                                              merchant_id,
                                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `body` | [`TerminalOrderRequest`](../../doc/models/terminal-order-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalOrder`](../../doc/models/terminal-order.md).

## Example Usage

```python
merchant_id = 'merchantId6'

body = TerminalOrderRequest(
    billing_entity_id='MerchantAccount.YOUR_MERCHANT_ACCOUNT',
    customer_order_reference='YOUR_REFERENCE',
    items=[
        OrderItem(
            id='PART-287001-EU',
            name='Bluetooth Charging Base - V400m',
            quantity=2
        ),
        OrderItem(
            id='PART-620222-EU',
            name='Receipt Roll',
            quantity=20
        )
    ],
    shipping_location_id='S2-6A6C2E3432747D4F2F2C3455485E3836457D'
)

result = terminal_orders_merchant_level_api.post_merchants_merchant_id_terminal_orders(
    merchant_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "4154567890100682",
  "customerOrderReference": "YOUR_REFERENCE",
  "status": "Placed",
  "shippingLocation": {
    "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
    "name": "YOUR_COMPANY Spain",
    "contact": {
      "firstName": "Pablo",
      "lastName": "Mengano",
      "phoneNumber": "+34911234567",
      "email": "Pablo.Mengano@company.com"
    },
    "address": {
      "streetAddress": "Paseo de la Castellana 43",
      "streetAddress2": "7 piso",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "billingEntity": {
    "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
    "name": "YOUR_MERCHANT_ACCOUNT",
    "taxId": "ES1234567890",
    "email": "Pablo.Mengano@company.com",
    "address": {
      "streetAddress": "Paseo de la Castellana 43, 7",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "orderDate": "2022-01-21T16:12:33Z",
  "items": [
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "quantity": 2
    },
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "quantity": 20
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Terminal Orders-Order Id

Returns the details of the terminal products order identified in the path.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_terminal_orders_order_id(self,
                                                      merchant_id,
                                                      order_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `order_id` | `str` | Template, Required | The unique identifier of the order. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalOrder`](../../doc/models/terminal-order.md).

## Example Usage

```python
merchant_id = 'merchantId6'

order_id = 'orderId2'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_terminal_orders_order_id(
    merchant_id,
    order_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "4154567890100682",
  "customerOrderReference": "YOUR_REFERENCE",
  "status": "Placed",
  "shippingLocation": {
    "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
    "name": "YOUR_COMPANY Spain",
    "contact": {
      "firstName": "Pablo",
      "lastName": "Mengano",
      "phoneNumber": "+34911234567",
      "email": "Pablo.Mengano@company.com"
    },
    "address": {
      "streetAddress": "Paseo de la Castellana 43",
      "streetAddress2": "7 piso",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "billingEntity": {
    "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
    "name": "YOUR_MERCHANT_ACCOUNT",
    "taxId": "ES1234567890",
    "email": "Pablo.Mengano@company.com",
    "address": {
      "streetAddress": "Paseo de la Castellana 43, 7",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "orderDate": "2022-01-21T16:12:33Z",
  "items": [
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "quantity": 2
    },
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "quantity": 20
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Patch-Merchants-Merchant Id-Terminal Orders-Order Id

Updates the terminal products order identified in the path.
Updating is only possible while the order has the status **Placed**.

The request body only needs to contain what you want to change.
However, to update the products in the `items` array, you must provide the entire array. For example, if the array has three items:
To remove one item, the array must include the remaining two items. Or to add one item, the array must include all four items.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def patch_merchants_merchant_id_terminal_orders_order_id(self,
                                                        merchant_id,
                                                        order_id,
                                                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `order_id` | `str` | Template, Required | The unique identifier of the order. |
| `body` | [`TerminalOrderRequest`](../../doc/models/terminal-order-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalOrder`](../../doc/models/terminal-order.md).

## Example Usage

```python
merchant_id = 'merchantId6'

order_id = 'orderId2'

body = TerminalOrderRequest(
    items=[
        OrderItem(
            id='TBOX-V400m-684-EU',
            name='V400m Package',
            quantity=1
        ),
        OrderItem(
            id='PART-287001-EU',
            name='Bluetooth Charging Base - V400m',
            quantity=2
        ),
        OrderItem(
            id='PART-620222-EU',
            name='Receipt Roll',
            quantity=20
        )
    ]
)

result = terminal_orders_merchant_level_api.patch_merchants_merchant_id_terminal_orders_order_id(
    merchant_id,
    order_id,
    body=body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "4154567890100682",
  "customerOrderReference": "YOUR_REFERENCE",
  "status": "Placed",
  "shippingLocation": {
    "id": "S2-73536B20665526704F30792642212044452F714622375D477270",
    "name": "YOUR_MERCHANT_ACCOUNT Barcelona depot",
    "contact": {
      "firstName": "Rita",
      "lastName": "Perengano",
      "phoneNumber": "+34931234567",
      "email": "Rita.Perengano@company.com"
    },
    "address": {
      "companyName": "YOUR_COMPANY",
      "streetAddress": "El quinto pino 42",
      "postalCode": "08012",
      "city": "Barcelona",
      "stateOrProvince": "",
      "country": "ES"
    }
  },
  "billingEntity": {
    "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
    "name": "YOUR_MERCHANT_ACCOUNT",
    "taxId": "ES1234567890",
    "email": "Pablo.Mengano@company.com",
    "address": {
      "streetAddress": "Paseo de la Castellana 43, 7",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "orderDate": "2022-01-21T16:12:33Z",
  "items": [
    {
      "id": "TBOX-V400m-684-EU",
      "name": "V400m Package",
      "quantity": 1
    },
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "quantity": 2
    },
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "quantity": 20
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Post-Merchants-Merchant Id-Terminal Orders-Order Id-Cancel

Cancels the terminal products order identified in the path.
Cancelling is only possible while the order has the status **Placed**.
To cancel an order, make a POST call without a request body. The response returns the full order details, but with the status changed to **Cancelled**.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def post_merchants_merchant_id_terminal_orders_order_id_cancel(self,
                                                              merchant_id,
                                                              order_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `order_id` | `str` | Template, Required | The unique identifier of the order. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalOrder`](../../doc/models/terminal-order.md).

## Example Usage

```python
merchant_id = 'merchantId6'

order_id = 'orderId2'

result = terminal_orders_merchant_level_api.post_merchants_merchant_id_terminal_orders_order_id_cancel(
    merchant_id,
    order_id
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "id": "4154567890100682",
  "customerOrderReference": "YOUR_REFERENCE",
  "status": "Cancelled",
  "shippingLocation": {
    "id": "S2-6A6C2E3432747D4F2F2C3455485E3836457D",
    "name": "YOUR_COMPANY Spain",
    "contact": {
      "firstName": "Pablo",
      "lastName": "Mengano",
      "phoneNumber": "+34911234567",
      "email": "Pablo.Mengano@company.com"
    },
    "address": {
      "streetAddress": "Paseo de la Castellana 43",
      "streetAddress2": "7 piso",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "billingEntity": {
    "id": "MerchantAccount.YOUR_MERCHANT_ACCOUNT",
    "name": "YOUR_MERCHANT_ACCOUNT",
    "taxId": "ES1234567890",
    "email": "Pablo.Mengano@company.com",
    "address": {
      "streetAddress": "Paseo de la Castellana 43, 7",
      "postalCode": "28046",
      "city": "Madrid",
      "country": "ES"
    }
  },
  "orderDate": "2022-01-21T16:12:33Z",
  "items": [
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "quantity": 2
    },
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "quantity": 20
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |


# Get-Merchants-Merchant Id-Terminal Products

Returns a country-specific list of payment terminal packages and parts that the merchant account identified in the path has access to.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Terminal ordering read
* Management API—Terminal ordering read and write

In the live environment, requests to this endpoint are subject to [rate limits](https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment).

```python
def get_merchants_merchant_id_terminal_products(self,
                                               merchant_id,
                                               country,
                                               terminal_model_id=None,
                                               offset=None,
                                               limit=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `merchant_id` | `str` | Template, Required | The unique identifier of the merchant account. |
| `country` | `str` | Query, Required | The country to return products for, in [ISO 3166-1 alpha-2](https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2) format. For example, **US** |
| `terminal_model_id` | `str` | Query, Optional | The terminal model to return products for. Use the ID returned in the [GET `/terminalModels`](https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/merchants/{merchantId}/terminalModels) response. For example, **Verifone.M400** |
| `offset` | `int` | Query, Optional | The number of products to skip. |
| `limit` | `int` | Query, Optional | The number of products to return. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`TerminalProductsResponse`](../../doc/models/terminal-products-response.md).

## Example Usage

```python
merchant_id = 'merchantId6'

country = 'country4'

result = terminal_orders_merchant_level_api.get_merchants_merchant_id_terminal_products(
    merchant_id,
    country
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "data": [
    {
      "id": "PART-620222-EU",
      "name": "Receipt Roll",
      "price": {
        "currency": "EUR",
        "value": 0
      }
    },
    {
      "id": "PART-175746-EU",
      "name": "Adyen Test Card",
      "price": {
        "currency": "EUR",
        "value": 0
      }
    },
    {
      "id": "PART-327486-EU",
      "name": "Battery - V400m",
      "price": {
        "currency": "EUR",
        "value": 0
      }
    },
    {
      "id": "PART-287001-EU",
      "name": "Bluetooth Charging Base - V400m",
      "price": {
        "currency": "EUR",
        "value": 0
      }
    },
    {
      "id": "PART-745984-EU",
      "name": "Power Supply EU - V400m",
      "price": {
        "currency": "EUR",
        "value": 0
      }
    },
    {
      "id": "TBOX-V400m-684-EU",
      "name": "V400m Package",
      "description": "Includes an EU Power Supply, SIM Card and battery",
      "price": {
        "currency": "EUR",
        "value": 0
      },
      "itemsIncluded": [
        "Receipt Roll",
        "Terminal Device V400m EU/GB"
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`RestServiceErrorException`](../../doc/models/rest-service-error-exception.md) |

