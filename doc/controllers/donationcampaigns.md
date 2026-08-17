# Donationcampaigns

```python
donationcampaigns_api = client.donationcampaigns
```

## Class Name

`DonationcampaignsApi`

## Methods

* [Post-Companies-Company Id-Campaign Management](../../doc/controllers/donationcampaigns.md#post-companies-company-id-campaign-management)
* [Get-Companies-Company Id-Campaign Management-Account Holders-Account Holder Id](../../doc/controllers/donationcampaigns.md#get-companies-company-id-campaign-management-account-holders-account-holder-id)
* [Delete-Companies-Company Id-Campaign Management-Donation Campaign Id](../../doc/controllers/donationcampaigns.md#delete-companies-company-id-campaign-management-donation-campaign-id)
* [Patch-Companies-Company Id-Campaign Management-Donation Campaign Id](../../doc/controllers/donationcampaigns.md#patch-companies-company-id-campaign-management-donation-campaign-id)
* [Post-Companies-Company Id-Campaign Management-Donation Campaign Id-Status-Status](../../doc/controllers/donationcampaigns.md#post-companies-company-id-campaign-management-donation-campaign-id-status-status)
* [Post-Companies-Company Id-Nonprofits](../../doc/controllers/donationcampaigns.md#post-companies-company-id-nonprofits)


# Post-Companies-Company Id-Campaign Management

Creates a new donation campaign, to give shoppers the option to donate to a nonprofit organization when making a payment. A campaign can be for online payments, in-person payments, or both online and in-person payments.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Campaign Management read and write

```python
def post_companies_company_id_campaign_management(self,
                                                 company_id,
                                                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `body` | [`DonationCampaignRequest`](../../doc/models/donation-campaign-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DonationCampaign1`](../../doc/models/donation-campaign-1.md)

## Example Usage

```python
company_id = 'companyId0'

result = donation_campaigns_api.post_companies_company_id_campaign_management(company_id)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Get-Companies-Company Id-Campaign Management-Account Holders-Account Holder Id

Returns a paginated list of donation campaigns associated with the account holder specified in the path. You can filter the list by campaign status.

To make this request, your API credential must have one of the following [roles](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Campaign Management read
* Management API—Campaign Management read and write

```python
def get_companies_company_id_campaign_management_account_holders_account_holder_id(self,
                                                                                  company_id,
                                                                                  account_holder_id,
                                                                                  status=None,
                                                                                  page_number=1,
                                                                                  page_size=10)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `account_holder_id` | `str` | Template, Required | The unique identifier of the account holder. |
| `status` | `str` | Query, Optional | The campaign status to return campaigns that match. Allowed values: **inactive**, **active**, or **ended**. |
| `page_number` | `int` | Query, Optional | The number of the page to fetch.<br><br>**Default**: `1`<br><br>**Constraints**: `>= 1` |
| `page_size` | `int` | Query, Optional | The number of items to have on a page, maximum 100. The default is 10 items on a page.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |

## Response Type

**200**: OK - the request has succeeded.

[`ListDonationCampaignsResponse`](../../doc/models/list-donation-campaigns-response.md)

## Example Usage

```python
company_id = 'companyId0'

account_holder_id = 'accountHolderId8'

page_number = 1

page_size = 10

result = donation_campaigns_api.get_companies_company_id_campaign_management_account_holders_account_holder_id(
    company_id,
    account_holder_id,
    page_number=page_number,
    page_size=page_size
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Delete-Companies-Company Id-Campaign Management-Donation Campaign Id

Removes the donation campaign specified in the path. This request is only allowed if the campaign has the status **inactive**.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Campaign Management read and write

```python
def delete_companies_company_id_campaign_management_donation_campaign_id(self,
                                                                        company_id,
                                                                        donation_campaign_id)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `donation_campaign_id` | `str` | Template, Required | The unique identifier of the donation campaign to be deleted. |

## Response Type

**204**: No Content - the request has been successfully processed, but there is no additional content.

`void`

## Example Usage

```python
company_id = 'companyId0'

donation_campaign_id = 'donationCampaignId0'

donation_campaigns_api.delete_companies_company_id_campaign_management_donation_campaign_id(
    company_id,
    donation_campaign_id
)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Patch-Companies-Company Id-Campaign Management-Donation Campaign Id

Updates the properties of the donation campaign specified in the path. Note the following restrictions:

* You cannot use a PATCH request to update the campaign status. To activate or end a campaign, make a POST request to the `/campaignManagement/{campaignId}/status/{status}` endpoint.
* You get a validation error if you add account holders that are not compatible with the nonprofit.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Campaign Management read and write

```python
def patch_companies_company_id_campaign_management_donation_campaign_id(self,
                                                                       company_id,
                                                                       donation_campaign_id,
                                                                       body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `donation_campaign_id` | `str` | Template, Required | The unique identifier of the donation campaign to be updated. |
| `body` | [`DonationCampaignUpdate`](../../doc/models/donation-campaign-update.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`DonationCampaign1`](../../doc/models/donation-campaign-1.md)

## Example Usage

```python
company_id = 'companyId0'

donation_campaign_id = 'donationCampaignId0'

result = donation_campaigns_api.patch_companies_company_id_campaign_management_donation_campaign_id(
    company_id,
    donation_campaign_id
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Companies-Company Id-Campaign Management-Donation Campaign Id-Status-Status

Starts or stops the donation campaign specified in the path, by providing a path parameter.
Use the path parameter **activate** to start an inactive campaign, or **end** to stop an active campaign. Other status transitions are not allowed.

To make this request, your API credential must have the following [role](https://docs.adyen.com/development-resources/api-credentials#api-permissions):

* Management API—Campaign Management read and write

```python
def post_companies_company_id_campaign_management_donation_campaign_id_status_status(self,
                                                                                    company_id,
                                                                                    donation_campaign_id,
                                                                                    status)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `donation_campaign_id` | `str` | Template, Required | The unique identifier of the donation campaign to activate or end. |
| `status` | [`CampaignStatusTransitionEnum`](../../doc/models/campaign-status-transition-enum.md) | Template, Required | The desired status change. Possible values: **activate** or **end**. |

## Response Type

**200**: OK - the request has succeeded.

[`DonationCampaign1`](../../doc/models/donation-campaign-1.md)

## Example Usage

```python
company_id = 'companyId0'

donation_campaign_id = 'donationCampaignId0'

status = CampaignStatusTransitionEnum.ACTIVATE

result = donation_campaigns_api.post_companies_company_id_campaign_management_donation_campaign_id_status_status(
    company_id,
    donation_campaign_id,
    status
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |


# Post-Companies-Company Id-Nonprofits

Returns a list of supported nonprofit organizations to choose from when creating a donation campaign. The list only contains nonprofits that are compatible with all the account holders specified in the request.

```python
def post_companies_company_id_nonprofits(self,
                                        company_id,
                                        search_term=None,
                                        page_number=None,
                                        page_size=10,
                                        goal=None,
                                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `company_id` | `str` | Template, Required | The unique identifier of the company account. |
| `search_term` | `str` | Query, Optional | A query to return nonprofit organizations for, maximum 100 characters. For example, `&searchTerm=clean%20water`.<br><br>**Constraints**: *Minimum Length*: `1`, *Maximum Length*: `100` |
| `page_number` | `int` | Query, Optional | The number of the page to fetch.<br><br>**Constraints**: `>= 1` |
| `page_size` | `int` | Query, Optional | The number of items to have on a page, maximum 100. The default is 10 items on a page.<br><br>**Default**: `10`<br><br>**Constraints**: `>= 1`, `<= 100` |
| `goal` | `List[str]` | Query, Optional | One or more United Nations Sustainable Development Goals to return nonprofit organizations for. Format: `unsdg_<number>`, for example, `&goal=unsdg_6&goal=unsdg_2`. |
| `body` | [`ListNonprofitsRequest`](../../doc/models/list-nonprofits-request.md) | Body, Optional | - |

## Response Type

**200**: OK - the request has succeeded.

[`ListNonprofitsResponse`](../../doc/models/list-nonprofits-response.md)

## Example Usage

```python
company_id = 'companyId0'

page_size = 10

result = donation_campaigns_api.post_companies_company_id_nonprofits(
    company_id,
    page_size=page_size
)
print(result)
```

## Errors

| HTTP Status Code | Error Description | Exception Class |
|  --- | --- | --- |
| 400 | Bad Request - a problem reading or understanding the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 401 | Unauthorized - authentication required. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 403 | Forbidden - insufficient permissions to process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 422 | Unprocessable Entity - a request validation error. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |
| 500 | Internal Server Error - the server could not process the request. | [`DefaultErrorResponseEntityException`](../../doc/models/default-error-response-entity-exception.md) |

