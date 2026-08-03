# Authorizedcardusers

```python
authorizedcardusers_api = client.authorizedcardusers
```

## Class Name

`AuthorizedcardusersApi`

## Methods

* [Get-Payment Instruments-Payment Instrument Id-Authorised Card Users](../../doc/controllers/authorizedcardusers.md#get-payment-instruments-payment-instrument-id-authorised-card-users)
* [Post-Payment Instruments-Payment Instrument Id-Authorised Card Users](../../doc/controllers/authorizedcardusers.md#post-payment-instruments-payment-instrument-id-authorised-card-users)
* [Delete-Payment Instruments-Payment Instrument Id-Authorised Card Users](../../doc/controllers/authorizedcardusers.md#delete-payment-instruments-payment-instrument-id-authorised-card-users)
* [Patch-Payment Instruments-Payment Instrument Id-Authorised Card Users](../../doc/controllers/authorizedcardusers.md#patch-payment-instruments-payment-instrument-id-authorised-card-users)


# Get-Payment Instruments-Payment Instrument Id-Authorised Card Users

Returns the authorized users for a card.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_payment_instruments_payment_instrument_id_authorised_card_users(self,
                                                                       payment_instrument_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Template, Required | - |

## Response Type

**200**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`AuthorisedCardUsers`](../../doc/models/authorised-card-users.md).

## Example Usage

```python
payment_instrument_id = 'paymentInstrumentId2'

result = authorized_card_users_api.get_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "legalEntityIds": [
    "LE328V522322685LV3KTNF35M",
    "LE328SW223226B5LWVWNQ8THN"
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`PaymentInstrumentsAuthorisedCardUsers401ErrorException`](../../doc/models/payment-instruments-authorised-card-users-401-error-exception.md) |
| 403 | Forbidden | [`PaymentInstrumentsAuthorisedCardUsers403ErrorException`](../../doc/models/payment-instruments-authorised-card-users-403-error-exception.md) |
| 404 | Not Found | [`PaymentInstrumentsAuthorisedCardUsers404ErrorException`](../../doc/models/payment-instruments-authorised-card-users-404-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`PaymentInstrumentsAuthorisedCardUsers422ErrorException`](../../doc/models/payment-instruments-authorised-card-users-422-error-exception.md) |


# Post-Payment Instruments-Payment Instrument Id-Authorised Card Users

Assigns authorized users to a card. Users must have the **authorisedPaymentInstrumentUser** capability to be able to use the card.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_payment_instruments_payment_instrument_id_authorised_card_users(self,
                                                                        payment_instrument_id,
                                                                        body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Template, Required | - |
| `body` | [`AuthorisedCardUsers`](../../doc/models/authorised-card-users.md) | Body, Required | - |

## Response Type

**204**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
payment_instrument_id = 'paymentInstrumentId2'

body = AuthorisedCardUsers(
    legal_entity_ids=[
        'LE328V522322685LV3KTNF35M',
        'LE328SW223226B5LWVWNQ8THN'
    ]
)

result = authorized_card_users_api.post_payment_instruments_payment_instrument_id_authorised_card_users(
    payment_instrument_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`PaymentInstrumentsAuthorisedCardUsers400ErrorException`](../../doc/models/payment-instruments-authorised-card-users-400-error-exception.md) |
| 401 | Unauthorized | [`PaymentInstrumentsAuthorisedCardUsers401ErrorException`](../../doc/models/payment-instruments-authorised-card-users-401-error-exception.md) |
| 403 | Forbidden | [`PaymentInstrumentsAuthorisedCardUsers403ErrorException`](../../doc/models/payment-instruments-authorised-card-users-403-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`PaymentInstrumentsAuthorisedCardUsers422ErrorException`](../../doc/models/payment-instruments-authorised-card-users-422-error-exception.md) |


# Delete-Payment Instruments-Payment Instrument Id-Authorised Card Users

Deletes the list of authorized users assigned to a card.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_payment_instruments_payment_instrument_id_authorised_card_users(self,
                                                                          payment_instrument_id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Template, Required | - |

## Response Type

**204**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
payment_instrument_id = 'paymentInstrumentId2'

result = authorized_card_users_api.delete_payment_instruments_payment_instrument_id_authorised_card_users(payment_instrument_id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized | [`PaymentInstrumentsAuthorisedCardUsers401ErrorException`](../../doc/models/payment-instruments-authorised-card-users-401-error-exception.md) |
| 403 | Forbidden | [`PaymentInstrumentsAuthorisedCardUsers403ErrorException`](../../doc/models/payment-instruments-authorised-card-users-403-error-exception.md) |


# Patch-Payment Instruments-Payment Instrument Id-Authorised Card Users

Updates the list of authorized users for a card.

> This request replaces all existing authorized users for the card.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_payment_instruments_payment_instrument_id_authorised_card_users(self,
                                                                         payment_instrument_id,
                                                                         body)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `payment_instrument_id` | `str` | Template, Required | - |
| `body` | [`AuthorisedCardUsers`](../../doc/models/authorised-card-users.md) | Body, Required | - |

## Response Type

**204**: Successful operation

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
payment_instrument_id = 'paymentInstrumentId2'

body = AuthorisedCardUsers(
    legal_entity_ids=[
        'LE328V522322685LV3KTNF35M',
        'LE328SW223226B5LWVWNQ8THN'
    ]
)

result = authorized_card_users_api.patch_payment_instruments_payment_instrument_id_authorised_card_users(
    payment_instrument_id,
    body
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request | [`PaymentInstrumentsAuthorisedCardUsers400ErrorException`](../../doc/models/payment-instruments-authorised-card-users-400-error-exception.md) |
| 401 | Unauthorized | [`PaymentInstrumentsAuthorisedCardUsers401ErrorException`](../../doc/models/payment-instruments-authorised-card-users-401-error-exception.md) |
| 403 | Forbidden | [`PaymentInstrumentsAuthorisedCardUsers403ErrorException`](../../doc/models/payment-instruments-authorised-card-users-403-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`PaymentInstrumentsAuthorisedCardUsers422ErrorException`](../../doc/models/payment-instruments-authorised-card-users-422-error-exception.md) |

