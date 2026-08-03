# SC Aassociationmanagement

```python
sc_aassociationmanagement_api = client.sc_aassociationmanagement
```

## Class Name

`ScAassociationmanagementApi`

## Methods

* [Get-Sca Associations](../../doc/controllers/sc-aassociationmanagement.md#get-sca-associations)
* [Delete-Sca Associations](../../doc/controllers/sc-aassociationmanagement.md#delete-sca-associations)
* [Patch-Sca Associations](../../doc/controllers/sc-aassociationmanagement.md#patch-sca-associations)


# Get-Sca Associations

Returns a paginated list of the SCA devices associated with a specific entity.

:information_source: **Note** This endpoint does not require authentication.

```python
def get_sca_associations(self,
                        entity_type,
                        entity_id,
                        page_size,
                        page_number)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `entity_type` | [`ScaEntityType5`](../../doc/models/sca-entity-type-5.md) | Query, Required | The type of entity you want to retrieve a list of associations for.<br><br>Possible values: **accountHolder**, **legalEntity** or **paymentInstrument**. |
| `entity_id` | `str` | Query, Required | The unique identifier of the entity.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `page_size` | `int` | Query, Required | The number of items to have on a page.<br><br>Default: **5**.<br><br>**Constraints**: `>= 1`, `<= 10` |
| `page_number` | `int` | Query, Required | The index of the page to retrieve. The index of the first page is **0** (zero).<br><br>Default:  **0**. |

## Response Type

**200**: OK - The request has succeeded.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ListAssociationsResponse`](../../doc/models/list-associations-response.md).

## Example Usage

```python
entity_type = ScaEntityType5.ACCOUNTHOLDER

entity_id = 'entityId2'

page_size = 10

page_number = 110

result = sca_association_management_api.get_sca_associations(
    entity_type,
    entity_id,
    page_size,
    page_number
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Example Response *(as JSON)*

```json
{
  "_links": {
    "self": {
      "href": "https://exampledomain.com/bcl/api/v2/scaAssociations?pageNumber=0&entityType=accountHolder&pageSize=10&entityId=AH3227J223222D5HHM4779X6X"
    }
  },
  "itemsTotal": 2,
  "pagesTotal": 1,
  "data": [
    {
      "scaDeviceId": "BSDR11111111111A1AAA1AAAAA1AA1",
      "scaDeviceName": "Device 1",
      "scaDeviceType": "ios",
      "entityType": "accountHolder",
      "entityId": "AH00000000000000000000001",
      "status": "active",
      "createdAt": "2025-09-02T14:39:17.232Z"
    },
    {
      "scaDeviceId": "BSDR22222222222B2BBB2BBBBB2BB2",
      "scaDeviceName": "Device 2",
      "scaDeviceType": "ios",
      "entityType": "accountHolder",
      "entityId": "AH00000000000000000000001",
      "status": "pendingApproval",
      "createdAt": "2025-09-02T14:39:17.232Z"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad request - The request contains invalid input and fails validation. | [`ScaAssociations400ErrorException`](../../doc/models/sca-associations-400-error-exception.md) |
| 401 | Unauthorized - Authentication required. | [`ScaAssociations401ErrorException`](../../doc/models/sca-associations-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaAssociations403ErrorException`](../../doc/models/sca-associations-403-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaAssociations500ErrorException`](../../doc/models/sca-associations-500-error-exception.md) |


# Delete-Sca Associations

Deletes one or more SCA associations for a device.

:information_source: **Note** This endpoint does not require authentication.

```python
def delete_sca_associations(self,
                           www_authenticate,
                           content_type)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `www_authenticate` | `str` | Header, Required | The header for authenticating through SCA.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `20000` |
| `content_type` | [`ContentType3`](../../doc/models/content-type-3.md) | Header, Required | - |

## Response Type

**204**: No Content - Successful association deletion.

This method returns an [`ApiResponse`](../../doc/api-response.md) instance.

## Example Usage

```python
www_authenticate = 'WWW-Authenticate2'

content_type = ContentType3.ENUM_APPLICATIONJSON

result = sca_association_management_api.delete_sca_associations(
    www_authenticate,
    content_type
)

if result.is_success():
    print(result.body)
elif result.is_error():
    print(result.errors)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - Authentication required. | [`ScaAssociations401ErrorException`](../../doc/models/sca-associations-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaAssociations403ErrorException`](../../doc/models/sca-associations-403-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaAssociations500ErrorException`](../../doc/models/sca-associations-500-error-exception.md) |


# Patch-Sca Associations

Approves a previously created association that is in a pending state.

:information_source: **Note** This endpoint does not require authentication.

```python
def patch_sca_associations(self,
                          www_authenticate,
                          body=None)
```

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `www_authenticate` | `str` | Header, Required | The header for authenticating through SCA.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `20000` |
| `body` | [`ApproveAssociationRequest`](../../doc/models/approve-association-request.md) | Body, Optional | - |

## Response Type

**200**: OK - Successful approval

This method returns an [`ApiResponse`](../../doc/api-response.md) instance. The `body` property of this instance returns the response data which is of type [`ApproveAssociationResponse`](../../doc/models/approve-association-response.md).

## Example Usage

```python
www_authenticate = 'WWW-Authenticate2'

body = ApproveAssociationRequest(
    entity_id='AH00000000000000000000001',
    entity_type=ScaEntityType2.ACCOUNTHOLDER,
    sca_device_ids=[
        'BSDR42XV3223223S5N6CDQDGH53M8H'
    ],
    status=AssociationStatus1.ACTIVE
)

result = sca_association_management_api.patch_sca_associations(
    www_authenticate,
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
  "scaAssociations": [
    {
      "scaDeviceId": "BSDR42XV3223223S5N6CDQDGH53M8H",
      "entityType": "accountHolder",
      "entityId": "AH00000000000000000000001",
      "status": "active"
    }
  ]
}
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 401 | Unauthorized - Authentication required. | [`ScaAssociations401ErrorException`](../../doc/models/sca-associations-401-error-exception.md) |
| 403 | Forbidden - Insufficient permissions to process the request. | [`ScaAssociations403ErrorException`](../../doc/models/sca-associations-403-error-exception.md) |
| 500 | Internal Server Error - The server could not process the request. | [`ScaAssociations500ErrorException`](../../doc/models/sca-associations-500-error-exception.md) |

