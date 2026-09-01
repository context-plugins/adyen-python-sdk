from __future__ import annotations

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RequestOptionsOrDict,
    SecuredRawResponse,
    json_decoder,
    param,
)
from ..errors.get_companies_company_id_terminal_actions_action_id_error import (
    GetCompaniesCompanyIdTerminalActionsActionIdErrorBody,
    get_companies_company_id_terminal_actions_action_id_error_mapper,
)
from ..errors.get_companies_company_id_terminal_actions_error import (
    GetCompaniesCompanyIdTerminalActionsErrorBody,
    get_companies_company_id_terminal_actions_error_mapper,
)
from ..models.external_terminal_action import ExternalTerminalAction
from ..models.list_external_terminal_actions_response import ListExternalTerminalActionsResponse
from ..server.server import Server


class TerminalActionsCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalActionsCompanyLevelWithRawResponse(client, server, auth)

    def get_companies_company_id_terminal_actions(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExternalTerminalActionsResponse:
        """Returns the `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ that have been
        scheduled for the company identified in the path.The response doesn't include actions that are scheduled by
        Adyen. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            status: Returns terminal actions with the specified status. Allowed values: **pending**, **successful**,
                **failed**, **cancelled**, **tryLater**.
            type_: Returns terminal actions of the specified type. Allowed values: **InstallAndroidApp**,
                **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_terminal_actions(
            company_id,
            page_number=page_number,
            page_size=page_size,
            status=status,
            type_=type_,
            request_options=request_options,
        ).unwrap()

    def get_companies_company_id_terminal_actions_action_id(
        self, company_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExternalTerminalAction:
        """Returns the details of the `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ identified in the
        path. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            action_id: The unique identifier of the terminal action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_companies_company_id_terminal_actions_action_id(
            company_id, action_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> TerminalActionsCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalActionsCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalActionsCompanyLevelWithRawResponse(client, server, auth)

    async def get_companies_company_id_terminal_actions(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListExternalTerminalActionsResponse:
        """Returns the `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ that have been
        scheduled for the company identified in the path.The response doesn't include actions that are scheduled by
        Adyen. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            status: Returns terminal actions with the specified status. Allowed values: **pending**, **successful**,
                **failed**, **cancelled**, **tryLater**.
            type_: Returns terminal actions of the specified type. Allowed values: **InstallAndroidApp**,
                **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_terminal_actions(
                company_id,
                page_number=page_number,
                page_size=page_size,
                status=status,
                type_=type_,
                request_options=request_options,
            )
        ).unwrap()

    async def get_companies_company_id_terminal_actions_action_id(
        self, company_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ExternalTerminalAction:
        """Returns the details of the `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ identified in the
        path. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            action_id: The unique identifier of the terminal action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_companies_company_id_terminal_actions_action_id(
                company_id, action_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncTerminalActionsCompanyLevelWithRawResponse:
        return self._with_raw_response


class TerminalActionsCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_companies_company_id_terminal_actions(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExternalTerminalActionsResponse, GetCompaniesCompanyIdTerminalActionsErrorBody]:
        """Returns the `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ that have been
        scheduled for the company identified in the path.The response doesn't include actions that are scheduled by
        Adyen. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            status: Returns terminal actions with the specified status. Allowed values: **pending**, **successful**,
                **failed**, **cancelled**, **tryLater**.
            type_: Returns terminal actions of the specified type. Allowed values: **InstallAndroidApp**,
                **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalActions"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("status", status),
                param[str | None]("type", type_),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListExternalTerminalActionsResponse],
            error_mapper=get_companies_company_id_terminal_actions_error_mapper,
            request_options=request_options,
        )

    def get_companies_company_id_terminal_actions_action_id(
        self, company_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExternalTerminalAction, GetCompaniesCompanyIdTerminalActionsActionIdErrorBody]:
        """Returns the details of the `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ identified in the
        path. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            action_id: The unique identifier of the terminal action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalActions/{actionId}"),
            path_params=[param[str]("companyId", company_id), param[str]("actionId", action_id)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ExternalTerminalAction],
            error_mapper=get_companies_company_id_terminal_actions_action_id_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalActionsCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_companies_company_id_terminal_actions(
        self,
        company_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        status: str | None = None,
        type_: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListExternalTerminalActionsResponse, GetCompaniesCompanyIdTerminalActionsErrorBody]:
        """Returns the `terminal actions
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ that have been
        scheduled for the company identified in the path.The response doesn't include actions that are scheduled by
        Adyen. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            status: Returns terminal actions with the specified status. Allowed values: **pending**, **successful**,
                **failed**, **cancelled**, **tryLater**.
            type_: Returns terminal actions of the specified type. Allowed values: **InstallAndroidApp**,
                **UninstallAndroidApp**, **InstallAndroidCertificate**, **UninstallAndroidCertificate**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalActions"),
            path_params=[param[str]("companyId", company_id)],
            query_params=[
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
                param[str | None]("status", status),
                param[str | None]("type", type_),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListExternalTerminalActionsResponse],
            error_mapper=get_companies_company_id_terminal_actions_error_mapper,
            request_options=request_options,
        )

    async def get_companies_company_id_terminal_actions_action_id(
        self, company_id: str, action_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ExternalTerminalAction, GetCompaniesCompanyIdTerminalActionsActionIdErrorBody]:
        """Returns the details of the `terminal action
        <https://docs.adyen.com/point-of-sale/automating-terminal-management/terminal-actions-api>`__ identified in the
        path. To make this request, your API credential must have one of the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Terminal actions read
        * Management API—Terminal actions read and write

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            company_id: The unique identifier of the company account.
            action_id: The unique identifier of the terminal action.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/companies/{companyId}/terminalActions/{actionId}"),
            path_params=[param[str]("companyId", company_id), param[str]("actionId", action_id)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ExternalTerminalAction],
            error_mapper=get_companies_company_id_terminal_actions_action_id_error_mapper,
            request_options=request_options,
        )
