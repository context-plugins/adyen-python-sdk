from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_companies_company_id_campaign_management_donation_campaign_id_error import (
    DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody,
    delete_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
)
from ..errors.get_companies_company_id_campaign_management_account_holders_account_holder_id_error import (
    GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody,
    get_companies_company_id_campaign_management_account_holders_account_holder_id_error_mapper,
)
from ..errors.patch_companies_company_id_campaign_management_donation_campaign_id_error import (
    PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody,
    patch_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
)
from ..errors.post_companies_company_id_campaign_management_donation_campaign_id_status_status_error import (
    PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody,
    post_companies_company_id_campaign_management_donation_campaign_id_status_status_error_mapper,
)
from ..errors.post_companies_company_id_campaign_management_error import (
    PostCompaniesCompanyIdCampaignManagementErrorBody,
    post_companies_company_id_campaign_management_error_mapper,
)
from ..errors.post_companies_company_id_nonprofits_error import (
    PostCompaniesCompanyIdNonprofitsErrorBody,
    post_companies_company_id_nonprofits_error_mapper,
)
from ..models.donation_campaign1 import DonationCampaign1
from ..models.donation_campaign_request import DonationCampaignRequest, DonationCampaignRequestDict
from ..models.donation_campaign_update import DonationCampaignUpdate, DonationCampaignUpdateDict
from ..models.enums.campaign_status_transition import CampaignStatusTransitionOrStr
from ..models.list_donation_campaigns_response import ListDonationCampaignsResponse
from ..models.list_nonprofits_request import ListNonprofitsRequest, ListNonprofitsRequestDict
from ..models.list_nonprofits_response import ListNonprofitsResponse
from ..server.server import Server


class DonationCampaigns:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = DonationCampaignsWithRawResponse(client, server, auth)

    def delete_companies_company_id_campaign_management_donation_campaign_id(
        self, company_id: str, donation_campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the donation campaign specified in the path. This request is only allowed if the campaign has the
        status **inactive**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.delete_companies_company_id_campaign_management_donation_campaign_id(
                company_id, donation_campaign_id, request_options=request_options
            ),
        )

    def get_companies_company_id_campaign_management_account_holders_account_holder_id(
        self,
        company_id: str,
        account_holder_id: str,
        *,
        status: str | None = None,
        page_number: int | None = 1,
        page_size: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDonationCampaignsResponse:
        """Returns a paginated list of donation campaigns associated with the account holder specified in the path. You
        can filter the list by campaign status.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            account_holder_id: The unique identifier of the account holder.
            status: The campaign status to return campaigns that match. Allowed values: **inactive**, **active**, or
                **ended**.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.get_companies_company_id_campaign_management_account_holders_account_holder_id(
                company_id,
                account_holder_id,
                status=status,
                page_number=page_number,
                page_size=page_size,
                request_options=request_options,
            ),
        )

    def patch_companies_company_id_campaign_management_donation_campaign_id(
        self,
        company_id: str,
        donation_campaign_id: str,
        *,
        body: DonationCampaignUpdate | DonationCampaignUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Updates the properties of the donation campaign specified in the path. Note the following restrictions:

        * You cannot use a PATCH request to update the campaign status. To activate or end a campaign, make a POST
            request to the ``/campaignManagement/{campaignId}/status/{status}`` endpoint.
        * You get a validation error if you add account holders that are not compatible with the nonprofit.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be updated.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.patch_companies_company_id_campaign_management_donation_campaign_id(
                company_id, donation_campaign_id, body=body, request_options=request_options
            ),
        )

    def post_companies_company_id_campaign_management(
        self,
        company_id: str,
        *,
        body: DonationCampaignRequest | DonationCampaignRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Creates a new donation campaign, to give shoppers the option to donate to a nonprofit organization when
        making a payment. A campaign can be for online payments, in-person payments, or both online and in-person
        payments.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_campaign_management(
                company_id, body=body, request_options=request_options
            ),
        )

    def post_companies_company_id_campaign_management_donation_campaign_id_status_status(
        self,
        company_id: str,
        donation_campaign_id: str,
        status: CampaignStatusTransitionOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Starts or stops the donation campaign specified in the path, by providing a path parameter. Use the path
        parameter **activate** to start an inactive campaign, or **end** to stop an active campaign. Other status
        transitions are not allowed.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to activate or end.
            status: The desired status change. Possible values: **activate** or **end**.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_campaign_management_donation_campaign_id_status_status(
                company_id, donation_campaign_id, status, request_options=request_options
            ),
        )

    def post_companies_company_id_nonprofits(
        self,
        company_id: str,
        *,
        search_term: str | None = None,
        page_number: int | None = None,
        page_size: int | None = 10,
        goal: list[str] | None = None,
        body: ListNonprofitsRequest | ListNonprofitsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListNonprofitsResponse:
        """Returns a list of supported nonprofit organizations to choose from when creating a donation campaign. The
        list only contains nonprofits that are compatible with all the account holders specified in the request.

        Args:
            company_id: The unique identifier of the company account.
            search_term: A query to return nonprofit organizations for, maximum 100 characters. For example,
                ``&searchTerm=clean%20water``.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            goal: One or more United Nations Sustainable Development Goals to return nonprofit organizations for.
                Format: ``unsdg_<number>``, for example, ``&goal=unsdg_6&goal=unsdg_2``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_companies_company_id_nonprofits(
                company_id,
                search_term=search_term,
                page_number=page_number,
                page_size=page_size,
                goal=goal,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> DonationCampaignsWithRawResponse:
        return self._with_raw_response


class AsyncDonationCampaigns:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncDonationCampaignsWithRawResponse(client, server, auth)

    async def delete_companies_company_id_campaign_management_donation_campaign_id(
        self, company_id: str, donation_campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Removes the donation campaign specified in the path. This request is only allowed if the campaign has the
        status **inactive**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - the request has been successfully processed, but there is no additional content.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_companies_company_id_campaign_management_donation_campaign_id(
                company_id, donation_campaign_id, request_options=request_options
            ),
        )

    async def get_companies_company_id_campaign_management_account_holders_account_holder_id(
        self,
        company_id: str,
        account_holder_id: str,
        *,
        status: str | None = None,
        page_number: int | None = 1,
        page_size: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListDonationCampaignsResponse:
        """Returns a paginated list of donation campaigns associated with the account holder specified in the path. You
        can filter the list by campaign status.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            account_holder_id: The unique identifier of the account holder.
            status: The campaign status to return campaigns that match. Allowed values: **inactive**, **active**, or
                **ended**.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.get_companies_company_id_campaign_management_account_holders_account_holder_id(
                company_id,
                account_holder_id,
                status=status,
                page_number=page_number,
                page_size=page_size,
                request_options=request_options,
            ),
        )

    async def patch_companies_company_id_campaign_management_donation_campaign_id(
        self,
        company_id: str,
        donation_campaign_id: str,
        *,
        body: DonationCampaignUpdate | DonationCampaignUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Updates the properties of the donation campaign specified in the path. Note the following restrictions:

        * You cannot use a PATCH request to update the campaign status. To activate or end a campaign, make a POST
            request to the ``/campaignManagement/{campaignId}/status/{status}`` endpoint.
        * You get a validation error if you add account holders that are not compatible with the nonprofit.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be updated.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_companies_company_id_campaign_management_donation_campaign_id(
                company_id, donation_campaign_id, body=body, request_options=request_options
            ),
        )

    async def post_companies_company_id_campaign_management(
        self,
        company_id: str,
        *,
        body: DonationCampaignRequest | DonationCampaignRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Creates a new donation campaign, to give shoppers the option to donate to a nonprofit organization when
        making a payment. A campaign can be for online payments, in-person payments, or both online and in-person
        payments.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_campaign_management(
                company_id, body=body, request_options=request_options
            ),
        )

    async def post_companies_company_id_campaign_management_donation_campaign_id_status_status(
        self,
        company_id: str,
        donation_campaign_id: str,
        status: CampaignStatusTransitionOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> DonationCampaign1:
        """Starts or stops the donation campaign specified in the path, by providing a path parameter. Use the path
        parameter **activate** to start an inactive campaign, or **end** to stop an active campaign. Other status
        transitions are not allowed.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to activate or end.
            status: The desired status change. Possible values: **activate** or **end**.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_campaign_management_donation_campaign_id_status_status(
                company_id, donation_campaign_id, status, request_options=request_options
            ),
        )

    async def post_companies_company_id_nonprofits(
        self,
        company_id: str,
        *,
        search_term: str | None = None,
        page_number: int | None = None,
        page_size: int | None = 10,
        goal: list[str] | None = None,
        body: ListNonprofitsRequest | ListNonprofitsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListNonprofitsResponse:
        """Returns a list of supported nonprofit organizations to choose from when creating a donation campaign. The
        list only contains nonprofits that are compatible with all the account holders specified in the request.

        Args:
            company_id: The unique identifier of the company account.
            search_term: A query to return nonprofit organizations for, maximum 100 characters. For example,
                ``&searchTerm=clean%20water``.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            goal: One or more United Nations Sustainable Development Goals to return nonprofit organizations for.
                Format: ``unsdg_<number>``, for example, ``&goal=unsdg_6&goal=unsdg_2``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_companies_company_id_nonprofits(
                company_id,
                search_term=search_term,
                page_number=page_number,
                page_size=page_size,
                goal=goal,
                body=body,
                request_options=request_options,
            ),
        )

    @property
    def with_raw_response(self) -> AsyncDonationCampaignsWithRawResponse:
        return self._with_raw_response


class DonationCampaignsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_companies_company_id_campaign_management_donation_campaign_id(
        self, company_id: str, donation_campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]:
        """Removes the donation campaign specified in the path. This request is only allowed if the campaign has the
        status **inactive**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement/{donationCampaignId}"),
            path_params=[param[str]("companyId", company_id), param[str]("donationCampaignId", donation_campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_campaign_management_account_holders_account_holder_id(
        self,
        company_id: str,
        account_holder_id: str,
        *,
        status: str | None = None,
        page_number: int | None = 1,
        page_size: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        ListDonationCampaignsResponse, GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody
    ]:
        """Returns a paginated list of donation campaigns associated with the account holder specified in the path. You
        can filter the list by campaign status.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            account_holder_id: The unique identifier of the account holder.
            status: The campaign status to return campaigns that match. Allowed values: **inactive**, **active**, or
                **ended**.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/companies/{companyId}/campaignManagement/accountHolders/{accountHolderId}"
            ),
            path_params=[param[str]("companyId", company_id), param[str]("accountHolderId", account_holder_id)],
            query_params=[
                param[str | None]("status", status),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListDonationCampaignsResponse],
            error_mapper=get_companies_company_id_campaign_management_account_holders_account_holder_id_error_mapper,
            request_options=request_options,
        )

    def patch_companies_company_id_campaign_management_donation_campaign_id(
        self,
        company_id: str,
        donation_campaign_id: str,
        *,
        body: DonationCampaignUpdate | DonationCampaignUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]:
        """Updates the properties of the donation campaign specified in the path. Note the following restrictions:

        * You cannot use a PATCH request to update the campaign status. To activate or end a campaign, make a POST
            request to the ``/campaignManagement/{campaignId}/status/{status}`` endpoint.
        * You get a validation error if you add account holders that are not compatible with the nonprofit.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be updated.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement/{donationCampaignId}"),
            path_params=[param[str]("companyId", company_id), param[str]("donationCampaignId", donation_campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationCampaignUpdate | DonationCampaignUpdateDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DonationCampaign1],
            error_mapper=patch_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_campaign_management(
        self,
        company_id: str,
        *,
        body: DonationCampaignRequest | DonationCampaignRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementErrorBody]:
        """Creates a new donation campaign, to give shoppers the option to donate to a nonprofit organization when
        making a payment. A campaign can be for online payments, in-person payments, or both online and in-person
        payments.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationCampaignRequest | DonationCampaignRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DonationCampaign1],
            error_mapper=post_companies_company_id_campaign_management_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_campaign_management_donation_campaign_id_status_status(
        self,
        company_id: str,
        donation_campaign_id: str,
        status: CampaignStatusTransitionOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody]:
        """Starts or stops the donation campaign specified in the path, by providing a path parameter. Use the path
        parameter **activate** to start an inactive campaign, or **end** to stop an active campaign. Other status
        transitions are not allowed.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to activate or end.
            status: The desired status change. Possible values: **activate** or **end**.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status}"
            ),
            path_params=[
                param[str]("companyId", company_id),
                param[str]("donationCampaignId", donation_campaign_id),
                param[CampaignStatusTransitionOrStr]("status", status),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[DonationCampaign1],
            error_mapper=post_companies_company_id_campaign_management_donation_campaign_id_status_status_error_mapper,
            request_options=request_options,
        )

    def post_companies_company_id_nonprofits(
        self,
        company_id: str,
        *,
        search_term: str | None = None,
        page_number: int | None = None,
        page_size: int | None = 10,
        goal: list[str] | None = None,
        body: ListNonprofitsRequest | ListNonprofitsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListNonprofitsResponse, PostCompaniesCompanyIdNonprofitsErrorBody]:
        """Returns a list of supported nonprofit organizations to choose from when creating a donation campaign. The
        list only contains nonprofits that are compatible with all the account holders specified in the request.

        Args:
            company_id: The unique identifier of the company account.
            search_term: A query to return nonprofit organizations for, maximum 100 characters. For example,
                ``&searchTerm=clean%20water``.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            goal: One or more United Nations Sustainable Development Goals to return nonprofit organizations for.
                Format: ``unsdg_<number>``, for example, ``&goal=unsdg_6&goal=unsdg_2``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/nonprofits"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("searchTerm", search_term),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[list[str] | None]("goal", goal),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListNonprofitsRequest | ListNonprofitsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListNonprofitsResponse],
            error_mapper=post_companies_company_id_nonprofits_error_mapper,
            request_options=request_options,
        )


class AsyncDonationCampaignsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_companies_company_id_campaign_management_donation_campaign_id(
        self, company_id: str, donation_campaign_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]:
        """Removes the donation campaign specified in the path. This request is only allowed if the campaign has the
        status **inactive**.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be deleted.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement/{donationCampaignId}"),
            path_params=[param[str]("companyId", company_id), param[str]("donationCampaignId", donation_campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=delete_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_campaign_management_account_holders_account_holder_id(
        self,
        company_id: str,
        account_holder_id: str,
        *,
        status: str | None = None,
        page_number: int | None = 1,
        page_size: int | None = 10,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[
        ListDonationCampaignsResponse, GetCompaniesCompanyIdCampaignManagementAccountHoldersAccountHolderIdErrorBody
    ]:
        """Returns a paginated list of donation campaigns associated with the account holder specified in the path. You
        can filter the list by campaign status.

        To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            account_holder_id: The unique identifier of the account holder.
            status: The campaign status to return campaigns that match. Allowed values: **inactive**, **active**, or
                **ended**.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9(
                "/companies/{companyId}/campaignManagement/accountHolders/{accountHolderId}"
            ),
            path_params=[param[str]("companyId", company_id), param[str]("accountHolderId", account_holder_id)],
            query_params=[
                param[str | None]("status", status),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ListDonationCampaignsResponse],
            error_mapper=get_companies_company_id_campaign_management_account_holders_account_holder_id_error_mapper,
            request_options=request_options,
        )

    async def patch_companies_company_id_campaign_management_donation_campaign_id(
        self,
        company_id: str,
        donation_campaign_id: str,
        *,
        body: DonationCampaignUpdate | DonationCampaignUpdateDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PatchCompaniesCompanyIdCampaignManagementDonationCampaignIdErrorBody]:
        """Updates the properties of the donation campaign specified in the path. Note the following restrictions:

        * You cannot use a PATCH request to update the campaign status. To activate or end a campaign, make a POST
            request to the ``/campaignManagement/{campaignId}/status/{status}`` endpoint.
        * You get a validation error if you add account holders that are not compatible with the nonprofit.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to be updated.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement/{donationCampaignId}"),
            path_params=[param[str]("companyId", company_id), param[str]("donationCampaignId", donation_campaign_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationCampaignUpdate | DonationCampaignUpdateDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DonationCampaign1],
            error_mapper=patch_companies_company_id_campaign_management_donation_campaign_id_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_campaign_management(
        self,
        company_id: str,
        *,
        body: DonationCampaignRequest | DonationCampaignRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementErrorBody]:
        """Creates a new donation campaign, to give shoppers the option to donate to a nonprofit organization when
        making a payment. A campaign can be for online payments, in-person payments, or both online and in-person
        payments.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/campaignManagement"),
            path_params=[param[str]("companyId", company_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DonationCampaignRequest | DonationCampaignRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DonationCampaign1],
            error_mapper=post_companies_company_id_campaign_management_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_campaign_management_donation_campaign_id_status_status(
        self,
        company_id: str,
        donation_campaign_id: str,
        status: CampaignStatusTransitionOrStr,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[DonationCampaign1, PostCompaniesCompanyIdCampaignManagementDonationCampaignIdStatusStatusErrorBody]:
        """Starts or stops the donation campaign specified in the path, by providing a path parameter. Use the path
        parameter **activate** to start an inactive campaign, or **end** to stop an active campaign. Other status
        transitions are not allowed.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Campaign Management read and write

        Args:
            company_id: The unique identifier of the company account.
            donation_campaign_id: The unique identifier of the donation campaign to activate or end.
            status: The desired status change. Possible values: **activate** or **end**.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/companies/{companyId}/campaignManagement/{donationCampaignId}/status/{status}"
            ),
            path_params=[
                param[str]("companyId", company_id),
                param[str]("donationCampaignId", donation_campaign_id),
                param[CampaignStatusTransitionOrStr]("status", status),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[DonationCampaign1],
            error_mapper=post_companies_company_id_campaign_management_donation_campaign_id_status_status_error_mapper,
            request_options=request_options,
        )

    async def post_companies_company_id_nonprofits(
        self,
        company_id: str,
        *,
        search_term: str | None = None,
        page_number: int | None = None,
        page_size: int | None = 10,
        goal: list[str] | None = None,
        body: ListNonprofitsRequest | ListNonprofitsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListNonprofitsResponse, PostCompaniesCompanyIdNonprofitsErrorBody]:
        """Returns a list of supported nonprofit organizations to choose from when creating a donation campaign. The
        list only contains nonprofits that are compatible with all the account holders specified in the request.

        Args:
            company_id: The unique identifier of the company account.
            search_term: A query to return nonprofit organizations for, maximum 100 characters. For example,
                ``&searchTerm=clean%20water``.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 10 items on a page.
            goal: One or more United Nations Sustainable Development Goals to return nonprofit organizations for.
                Format: ``unsdg_<number>``, for example, ``&goal=unsdg_6&goal=unsdg_2``.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/companies/{companyId}/nonprofits"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[str | None]("searchTerm", search_term),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[list[str] | None]("goal", goal),
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ListNonprofitsRequest | ListNonprofitsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ListNonprofitsResponse],
            error_mapper=post_companies_company_id_nonprofits_error_mapper,
            request_options=request_options,
        )
