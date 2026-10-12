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
from ..errors.get_terminals_error import GetTerminalsErrorBody, get_terminals_error_mapper
from ..errors.post_terminals_terminal_id_reassign_error import (
    PostTerminalsTerminalIdReassignErrorBody,
    post_terminals_terminal_id_reassign_error_mapper,
)
from ..models.list_terminals_response import ListTerminalsResponse
from ..models.terminal_reassignment_request import TerminalReassignmentRequest, TerminalReassignmentRequestDict
from ..server.server import Server


class TerminalsTerminalLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = TerminalsTerminalLevelWithRawResponse(client, server, auth)

    def get_terminals(
        self,
        *,
        search_query: str | None = None,
        otp_query: str | None = None,
        countries: str | None = None,
        merchant_ids: str | None = None,
        store_ids: str | None = None,
        brand_models: str | None = None,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTerminalsResponse:
        """Returns the payment terminals that the API credential has access to and that match the query parameters. To
        make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API — Terminal actions read

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            search_query: Returns terminals with an ID that contains the specified string. If present, other query
                parameters are ignored.
            otp_query: Returns one or more terminals associated with the one-time passwords specified in the request. If
                this query parameter is used, other query parameters are ignored.
            countries: Returns terminals located in the countries specified by their `two-letter country code
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__.
            merchant_ids: Returns terminals that belong to the merchant accounts specified by their unique merchant
                account ID.
            store_ids: Returns terminals that are assigned to the `stores
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores>`__ specified by their unique
                store ID.
            brand_models: Returns terminals of the `models
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels>`__
                specified in the format *brand.model*.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.get_terminals(
                search_query=search_query,
                otp_query=otp_query,
                countries=countries,
                merchant_ids=merchant_ids,
                store_ids=store_ids,
                brand_models=brand_models,
                page_number=page_number,
                page_size=page_size,
                request_options=request_options,
            ),
        )

    def post_terminals_terminal_id_reassign(
        self,
        terminal_id: str,
        *,
        body: TerminalReassignmentRequest | TerminalReassignmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Assign Terminal

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_terminals_terminal_id_reassign(
                terminal_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> TerminalsTerminalLevelWithRawResponse:
        return self._with_raw_response


class AsyncTerminalsTerminalLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncTerminalsTerminalLevelWithRawResponse(client, server, auth)

    async def get_terminals(
        self,
        *,
        search_query: str | None = None,
        otp_query: str | None = None,
        countries: str | None = None,
        merchant_ids: str | None = None,
        store_ids: str | None = None,
        brand_models: str | None = None,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListTerminalsResponse:
        """Returns the payment terminals that the API credential has access to and that match the query parameters. To
        make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API — Terminal actions read

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            search_query: Returns terminals with an ID that contains the specified string. If present, other query
                parameters are ignored.
            otp_query: Returns one or more terminals associated with the one-time passwords specified in the request. If
                this query parameter is used, other query parameters are ignored.
            countries: Returns terminals located in the countries specified by their `two-letter country code
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__.
            merchant_ids: Returns terminals that belong to the merchant accounts specified by their unique merchant
                account ID.
            store_ids: Returns terminals that are assigned to the `stores
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores>`__ specified by their unique
                store ID.
            brand_models: Returns terminals of the `models
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels>`__
                specified in the format *brand.model*.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.get_terminals(
                search_query=search_query,
                otp_query=otp_query,
                countries=countries,
                merchant_ids=merchant_ids,
                store_ids=store_ids,
                brand_models=brand_models,
                page_number=page_number,
                page_size=page_size,
                request_options=request_options,
            ),
        )

    async def post_terminals_terminal_id_reassign(
        self,
        terminal_id: str,
        *,
        body: TerminalReassignmentRequest | TerminalReassignmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Assign Terminal

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_terminals_terminal_id_reassign(
                terminal_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncTerminalsTerminalLevelWithRawResponse:
        return self._with_raw_response


class TerminalsTerminalLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_terminals(
        self,
        *,
        search_query: str | None = None,
        otp_query: str | None = None,
        countries: str | None = None,
        merchant_ids: str | None = None,
        store_ids: str | None = None,
        brand_models: str | None = None,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTerminalsResponse, GetTerminalsErrorBody]:
        """Returns the payment terminals that the API credential has access to and that match the query parameters. To
        make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API — Terminal actions read

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            search_query: Returns terminals with an ID that contains the specified string. If present, other query
                parameters are ignored.
            otp_query: Returns one or more terminals associated with the one-time passwords specified in the request. If
                this query parameter is used, other query parameters are ignored.
            countries: Returns terminals located in the countries specified by their `two-letter country code
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__.
            merchant_ids: Returns terminals that belong to the merchant accounts specified by their unique merchant
                account ID.
            store_ids: Returns terminals that are assigned to the `stores
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores>`__ specified by their unique
                store ID.
            brand_models: Returns terminals of the `models
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels>`__
                specified in the format *brand.model*.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals"),
            query_params=[
                param[str | None]("searchQuery", search_query),
                param[str | None]("otpQuery", otp_query),
                param[str | None]("countries", countries),
                param[str | None]("merchantIds", merchant_ids),
                param[str | None]("storeIds", store_ids),
                param[str | None]("brandModels", brand_models),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListTerminalsResponse],
            error_mapper=get_terminals_error_mapper,
            request_options=request_options,
        )

    def post_terminals_terminal_id_reassign(
        self,
        terminal_id: str,
        *,
        body: TerminalReassignmentRequest | TerminalReassignmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostTerminalsTerminalIdReassignErrorBody]:
        """Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Assign Terminal

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/terminals/{terminalId}/reassign"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalReassignmentRequest | TerminalReassignmentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_terminals_terminal_id_reassign_error_mapper,
            request_options=request_options,
        )


class AsyncTerminalsTerminalLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_terminals(
        self,
        *,
        search_query: str | None = None,
        otp_query: str | None = None,
        countries: str | None = None,
        merchant_ids: str | None = None,
        store_ids: str | None = None,
        brand_models: str | None = None,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListTerminalsResponse, GetTerminalsErrorBody]:
        """Returns the payment terminals that the API credential has access to and that match the query parameters. To
        make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API — Terminal actions read

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            search_query: Returns terminals with an ID that contains the specified string. If present, other query
                parameters are ignored.
            otp_query: Returns one or more terminals associated with the one-time passwords specified in the request. If
                this query parameter is used, other query parameters are ignored.
            countries: Returns terminals located in the countries specified by their `two-letter country code
                <https://en.wikipedia.org/wiki/ISO_3166-1_alpha-2>`__.
            merchant_ids: Returns terminals that belong to the merchant accounts specified by their unique merchant
                account ID.
            store_ids: Returns terminals that are assigned to the `stores
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/stores>`__ specified by their unique
                store ID.
            brand_models: Returns terminals of the `models
                <https://docs.adyen.com/api-explorer/#/ManagementService/latest/get/companies/{companyId}/terminalModels>`__
                specified in the format *brand.model*.
            page_number: The number of the page to fetch.
            page_size: The number of items to have on a page, maximum 100. The default is 20 items on a page.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default9("/terminals"),
            query_params=[
                param[str | None]("searchQuery", search_query),
                param[str | None]("otpQuery", otp_query),
                param[str | None]("countries", countries),
                param[str | None]("merchantIds", merchant_ids),
                param[str | None]("storeIds", store_ids),
                param[str | None]("brandModels", brand_models),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[ListTerminalsResponse],
            error_mapper=get_terminals_error_mapper,
            request_options=request_options,
        )

    async def post_terminals_terminal_id_reassign(
        self,
        terminal_id: str,
        *,
        body: TerminalReassignmentRequest | TerminalReassignmentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostTerminalsTerminalIdReassignErrorBody]:
        """Reassigns a payment terminal to a company account, merchant account, merchant account inventory, or a store.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—Assign Terminal

        In the live environment, requests to this endpoint are subject to `rate limits
        <https://docs.adyen.com/point-of-sale/automating-terminal-management#rate-limits-in-the-live-environment>`__.

        Args:
            terminal_id: The unique identifier of the payment terminal.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9("/terminals/{terminalId}/reassign"),
            path_params=[param[str]("terminalId", terminal_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[TerminalReassignmentRequest | TerminalReassignmentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=post_terminals_terminal_id_reassign_error_mapper,
            request_options=request_options,
        )
