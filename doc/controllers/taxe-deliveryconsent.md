# Taxe Deliveryconsent

```python
taxe_deliveryconsent_api = client.taxe_deliveryconsent
```

## Class Name

`TaxeDeliveryconsentApi`

## Methods

* [Post-Legal Entities-Id-Check Tax Electronic Delivery Consent](../../doc/controllers/taxe-deliveryconsent.md#post-legal-entities-id-check-tax-electronic-delivery-consent)
* [Post-Legal Entities-Id-Set Tax Electronic Delivery Consent](../../doc/controllers/taxe-deliveryconsent.md#post-legal-entities-id-set-tax-electronic-delivery-consent)


# Post-Legal Entities-Id-Check Tax Electronic Delivery Consent

Returns the consent status for electronic delivery of tax forms.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_check_tax_electronic_delivery_consent(self,
                                                                id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. For organizations, this is the ID of the organization. |

## Response Type

**200**: OK - the request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`CheckTaxElectronicDeliveryConsentResponse`](../../doc/models/check-tax-electronic-delivery-consent-response.md).

## Example Usage

```python
id = 'id0'

result = tax_e_delivery_consent_api.post_legal_entities_id_check_tax_electronic_delivery_consent(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |


# Post-Legal Entities-Id-Set Tax Electronic Delivery Consent

Set the consent status for electronic delivery of tax forms.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_set_tax_electronic_delivery_consent(self,
                                                              id,
                                                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. For sole proprietorships, this is the individual legal entity ID of the owner. For organizations, this is the ID of the organization. |
| `body` | [`SetTaxElectronicDeliveryConsentRequest`](../../doc/models/set-tax-electronic-delivery-consent-request.md) | Body, Optional | - |

## Response Type

**200**: No Content - look at the actual response code for the status of the request.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
id = 'id0'

result = tax_e_delivery_consent_api.post_legal_entities_id_set_tax_electronic_delivery_consent(id)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorException`](../../doc/models/service-error-exception.md) |

