# Legalentities

```python
legalentities_api = client.legalentities
```

## Class Name

`LegalentitiesApi`

## Methods

* [Post-Legal Entities](../../doc/controllers/legalentities.md#post-legal-entities)
* [Get-Legal Entities-Id](../../doc/controllers/legalentities.md#get-legal-entities-id)
* [Patch-Legal Entities-Id](../../doc/controllers/legalentities.md#patch-legal-entities-id)
* [Get-Legal Entities-Id-Business Lines](../../doc/controllers/legalentities.md#get-legal-entities-id-business-lines)
* [Post-Legal Entities-Id-Check Verification Errors](../../doc/controllers/legalentities.md#post-legal-entities-id-check-verification-errors)
* [Post-Legal Entities-Id-Confirm Data Review](../../doc/controllers/legalentities.md#post-legal-entities-id-confirm-data-review)
* [Post-Legal Entities-Id-Request Periodic Review](../../doc/controllers/legalentities.md#post-legal-entities-id-request-periodic-review)


# Post-Legal Entities

Creates a legal entity.

This resource contains information about the user that will be onboarded in your platform. Adyen uses this information to perform verification checks as required by payment industry regulations. Adyen informs you of the verification results through webhooks or API responses.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities(self,
                       x_requested_verification_code=None,
                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `x_requested_verification_code` | `str` | Header, Optional | Use a suberror code as your requested verification code. You can include one code at a time in your request header. Requested verification codes can only be used in your test environment. |
| `body` | [`LegalEntityInfoRequiredType`](../../doc/models/legal-entity-info-required-type.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`LegalEntity3`](../../doc/models/legal-entity-3.md)

## Example Usage

```python
body = LegalEntityInfoRequiredType(
    mtype=Type213Enum.INDIVIDUAL,
    individual=Individual1(
        name=Name23(
            first_name='Shelly',
            last_name='Eller'
        ),
        residential_address=Address13(
            country='AU',
            city='Sydney',
            postal_code='1122',
            state_or_province='NSW',
            street='Winfield Avenue',
            street_2='12'
        ),
        birth_data=BirthData1(
            date_of_birth='1991-01-01'
        ),
        email='s.hopper@example.com',
        identification_data=IdentificationData1(
            mtype=Type132Enum.DRIVERSLICENSE,
            card_number='112327',
            issuer_state='NSW',
            number='1234567891'
        )
    )
)

result = legal_entities_api.post_legal_entities(
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "individual": {
    "email": "s.hopper@example.com",
    "birthData": {
      "dateOfBirth": "1991-01-01"
    },
    "identificationData": {
      "cardNumber": "112327",
      "issuerState": "NSW",
      "number": "1234567891",
      "type": "driversLicense"
    },
    "name": {
      "firstName": "Shelly",
      "lastName": "Eller"
    },
    "residentialAddress": {
      "city": "Sydney",
      "country": "AU",
      "postalCode": "1122",
      "stateOrProvince": "NSW",
      "street": "Winfield Avenue",
      "street2": "12"
    }
  },
  "type": "individual",
  "id": "LE00000000000000000000001"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Get-Legal Entities-Id

Returns a legal entity.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_legal_entities_id(self,
                         id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |

## Response Type

**200**: OK - the request has succeeded.

[`LegalEntity3`](../../doc/models/legal-entity-3.md)

## Example Usage

```python
id = 'id0'

result = legal_entities_api.get_legal_entities_id(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "capabilities": {
    "sendToTransferInstrument": {
      "allowed": false,
      "requested": true,
      "transferInstruments": [
        {
          "allowed": false,
          "id": "SE322KH223222F5GXZFNM3BGP",
          "requested": true,
          "verificationStatus": "pending"
        }
      ],
      "verificationStatus": "pending"
    },
    "receivePayments": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "sendToBalanceAccount": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "receiveFromPlatformPayments": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    },
    "receiveFromBalanceAccount": {
      "allowed": false,
      "requested": true,
      "verificationStatus": "pending"
    }
  },
  "individual": {
    "email": "s.hopper@example.com",
    "birthData": {
      "dateOfBirth": "1990-06-21"
    },
    "name": {
      "firstName": "Simone",
      "lastName": "Hopper"
    },
    "phone": {
      "number": "+31858888138",
      "phoneCountryCode": "NL",
      "type": "mobile"
    },
    "residentialAddress": {
      "city": "Amsterdam",
      "country": "NL",
      "postalCode": "1011DJ",
      "street": "Simon Carmiggeltstraat 6 - 50",
      "street2": "274"
    }
  },
  "type": "individual",
  "id": "YOUR_LEGAL_ENTITY",
  "transferInstruments": [
    {
      "id": "SE322KH223222F5GXZFNM3BGP",
      "accountIdentifier": "NL**ABNA******0123",
      "trustedSource": false
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Patch-Legal Entities-Id

Updates a legal entity.

> To change the legal entity type, include only the new `type` in your request.

If you need to update information for the legal entity, make a separate request. To update the `entityAssociations` array, you need to replace the entire array.For example, if the array has 3 entries and you want to remove 1 entry, you need to PATCH the resource with the remaining 2 entries.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def patch_legal_entities_id(self,
                           id,
                           x_requested_verification_code=None,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |
| `x_requested_verification_code` | `str` | Header, Optional | Use the requested verification code 0_0001 to resolve any suberrors associated with the legal entity. Requested verification codes can only be used in your test environment. |
| `body` | [`LegalEntityInfo`](../../doc/models/legal-entity-info.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`LegalEntity3`](../../doc/models/legal-entity-3.md)

## Example Usage

```python
id = 'id0'

body = LegalEntityInfo(
    mtype=Type182Enum.INDIVIDUAL
)

result = legal_entities_api.patch_legal_entities_id(
    id,
    body=body
)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "individual": {
    "name": {
      "firstName": "Explorer",
      "lastName": "Company based in US"
    },
    "residentialAddress": {
      "country": "US"
    }
  },
  "type": "individual",
  "id": "LE00000000000000000000001"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Get-Legal Entities-Id-Business Lines

Returns the business lines owned by a legal entity.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def get_legal_entities_id_business_lines(self,
                                        id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |

## Response Type

**200**: OK - the request has succeeded.

[`BusinessLines`](../../doc/models/business-lines.md)

## Example Usage

```python
id = 'id0'

result = legal_entities_api.get_legal_entities_id_business_lines(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "businessLines": [
    {
      "service": "banking",
      "industryCode": "55",
      "legalEntityId": "LE00000000000000000000001",
      "sourceOfFunds": {
        "adyenProcessedFunds": false,
        "description": "Funds from my flower shop business",
        "type": "business"
      },
      "webData": [
        {
          "webAddress": "https://www.adyen.com",
          "webAddressId": "SE577HA334222K5H8V87B3BPU"
        }
      ],
      "id": "SE322JV223222F5GVGMLNB83F"
    },
    {
      "service": "paymentProcessing",
      "industryCode": "339E",
      "legalEntityId": "LE00000000000000000000001",
      "salesChannels": [
        "eCommerce",
        "ecomMoto"
      ],
      "webData": [
        {
          "webAddress": "https://yoururl.com",
          "webAddressId": "SE908HJ723222F5GVGPNR55YH"
        }
      ],
      "id": "SE322JV223222F5GVGPNRB9GJ"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Legal Entities-Id-Check Verification Errors

Returns the verification errors for a legal entity and its supporting entities.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_check_verification_errors(self,
                                                    id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |

## Response Type

**200**: OK - the request has succeeded.

[`VerificationErrors`](../../doc/models/verification-errors.md)

## Example Usage

```python
id = 'id0'

result = legal_entities_api.post_legal_entities_id_check_verification_errors(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "problems": [
    {
      "entity": {
        "id": "LE00000000000000000000001",
        "type": "LegalEntity"
      },
      "verificationErrors": [
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8179",
          "message": "'vatNumber' was missing.",
          "remediatingActions": [
            {
              "code": "2_158",
              "message": "Add 'organization.vatNumber' to legal entity."
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8067",
          "message": "'Signatory' was missing.",
          "remediatingActions": [
            {
              "code": "2_124",
              "message": "Add 'organization.entityAssociations' of type 'signatory' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8189",
          "message": "'UBO through control' was missing.",
          "remediatingActions": [
            {
              "code": "2_151",
              "message": "Add 'organization.entityAssociations' of type 'uboThroughControl' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments"
          ],
          "code": "2_8190",
          "message": "'businessLine' was missing.",
          "remediatingActions": [
            {
              "code": "2_136",
              "message": "Add business line"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8021",
          "message": "'individual.residentialAddress.postalCode' was missing.",
          "remediatingActions": [
            {
              "code": "2_108",
              "message": "Add 'individual.residentialAddress.postalCode' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8064",
          "message": "'UBO through ownership' was missing.",
          "remediatingActions": [
            {
              "code": "2_123",
              "message": "Add 'organization.entityAssociations' of type 'uboThroughOwnership' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8141",
          "message": "'Registration document' was missing.",
          "remediatingActions": [
            {
              "code": "1_501",
              "message": "Upload a registration document"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8019",
          "message": "'individual.residentialAddress.street' was missing.",
          "remediatingActions": [
            {
              "code": "2_106",
              "message": "Add 'individual.residentialAddress.street' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8020",
          "message": "'individual.residentialAddress.city' was missing.",
          "remediatingActions": [
            {
              "code": "2_107",
              "message": "Add 'individual.residentialAddress.city' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8045",
          "message": "'organization.taxId' was missing.",
          "remediatingActions": [
            {
              "code": "2_118",
              "message": "Add 'organization.taxId' to legal entity"
            }
          ],
          "type": "dataMissing"
        },
        {
          "capabilities": [
            "receivePayments",
            "sendToTransferInstrument"
          ],
          "code": "2_8043",
          "message": "'organization.registrationNumber' was missing.",
          "remediatingActions": [
            {
              "code": "2_117",
              "message": "Add 'organization.registrationNumber' to legal entity"
            }
          ],
          "type": "dataMissing"
        }
      ]
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Legal Entities-Id-Confirm Data Review

Confirms that your user has reviewed the data for the legal entity specified in the path. Call this endpoint to inform Adyen that your user reviewed and verified that the data is up-to-date. The endpoint returns the timestamp of when Adyen received the request.

Requests to this endpoint are subject to rate limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

```python
def post_legal_entities_id_confirm_data_review(self,
                                              id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |

## Response Type

**200**: OK - the request has succeeded.

[`DataReviewConfirmationResponse`](../../doc/models/data-review-confirmation-response.md)

## Example Usage

```python
id = 'id0'

result = legal_entities_api.post_legal_entities_id_confirm_data_review(id)
print(result)
```

## Example Response *(as JSON)*

```json
{
  "dataReviewedAt": "2023-11-13T15:19:02Z"
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 401 | Unauthorized - authentication required. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`ServiceErrorError1Exception`](../../doc/models/service-error-error-1-exception.md) |


# Post-Legal Entities-Id-Request Periodic Review

Requests a periodic data review for the legal entity of the user specified in the path.

:information_source: **Note** This endpoint does not require authentication.

```python
def post_legal_entities_id_request_periodic_review(self,
                                                  id)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `id` | `str` | Template, Required | The unique identifier of the legal entity. |

## Response Type

**204**: No Content - the request has been successfully processed, but there is no additional content.

`Any`

## Example Usage

```python
id = 'id0'

result = legal_entities_api.post_legal_entities_id_request_periodic_review(id)
print(result)
```

