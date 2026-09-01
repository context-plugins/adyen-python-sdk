from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    json_body,
    json_decoder,
    param,
)
from ..errors.get_account_verification_reports_code_error import (
    GetAccountVerificationReportsCodeErrorBody,
    get_account_verification_reports_code_error_mapper,
)
from ..errors.post_account_verification_routes_error import (
    PostAccountVerificationRoutesErrorBody,
    post_account_verification_routes_error_mapper,
)
from ..models.account_verification_report_response import AccountVerificationReportResponse
from ..models.account_verification_routes_request import (
    AccountVerificationRoutesRequest,
    AccountVerificationRoutesRequestDict,
)
from ..models.account_verification_routes_response import AccountVerificationRoutesResponse
from ..server.server import Server


class AccountVerification:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = AccountVerificationWithRawResponse(client, server)

    def get_account_verification_reports_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountVerificationReportResponse:
        """Get the account verification report using a unique code from a successful open banking connection. This
        report provides identity verification and bank account details.

        Args:
            code: The unique code you receive after a successful open banking flow that is included as a query parameter
                in the ``redirectUrl`` callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Not Found - The entity
                was not found. Unprocessable Entity - A request validation error. Too Many Requests - Request rate limit
                exceeded. Internal Service Error - An unrecoverable error occurred while trying to perform the request.
                ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_account_verification_reports_code(
            code, request_options=request_options
        ).unwrap()

    def post_account_verification_routes(
        self,
        body: AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountVerificationRoutesResponse:
        """Create a list of routes for verifying bank accounts of third-party individuals. Successful connections
        generate a unique code used for requesting bank reports and verifying identity.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Unprocessable Entity -
                A request validation error. Too Many Requests - Request rate limit exceeded. Internal Service Error - An
                unrecoverable error occurred while trying to perform the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_account_verification_routes(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> AccountVerificationWithRawResponse:
        return self._with_raw_response


class AsyncAccountVerification:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncAccountVerificationWithRawResponse(client, server)

    async def get_account_verification_reports_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> AccountVerificationReportResponse:
        """Get the account verification report using a unique code from a successful open banking connection. This
        report provides identity verification and bank account details.

        Args:
            code: The unique code you receive after a successful open banking flow that is included as a query parameter
                in the ``redirectUrl`` callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Not Found - The entity
                was not found. Unprocessable Entity - A request validation error. Too Many Requests - Request rate limit
                exceeded. Internal Service Error - An unrecoverable error occurred while trying to perform the request.
                ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_account_verification_reports_code(code, request_options=request_options)
        ).unwrap()

    async def post_account_verification_routes(
        self,
        body: AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AccountVerificationRoutesResponse:
        """Create a list of routes for verifying bank accounts of third-party individuals. Successful connections
        generate a unique code used for requesting bank reports and verifying identity.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not in the expected format. Unauthorized - The API
                credential used in the request is invalid or does not have the right permissions. Unprocessable Entity -
                A request validation error. Too Many Requests - Request rate limit exceeded. Internal Service Error - An
                unrecoverable error occurred while trying to perform the request. ``error`` is
                ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.post_account_verification_routes(body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncAccountVerificationWithRawResponse:
        return self._with_raw_response


class AccountVerificationWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_account_verification_reports_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountVerificationReportResponse, GetAccountVerificationReportsCodeErrorBody]:
        """Get the account verification report using a unique code from a successful open banking connection. This
        report provides identity verification and bank account details.

        Args:
            code: The unique code you receive after a successful open banking flow that is included as a query parameter
                in the ``redirectUrl`` callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default21("/accountVerification/reports/{code}"),
            path_params=[param[str]("code", code)],
            decoder=json_decoder[AccountVerificationReportResponse],
            error_mapper=get_account_verification_reports_code_error_mapper,
            request_options=request_options,
        )

    def post_account_verification_routes(
        self,
        body: AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountVerificationRoutesResponse, PostAccountVerificationRoutesErrorBody]:
        """Create a list of routes for verifying bank accounts of third-party individuals. Successful connections
        generate a unique code used for requesting bank reports and verifying identity.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default21("/accountVerification/routes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict](body),
            decoder=json_decoder[AccountVerificationRoutesResponse],
            error_mapper=post_account_verification_routes_error_mapper,
            request_options=request_options,
        )


class AsyncAccountVerificationWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_account_verification_reports_code(
        self, code: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[AccountVerificationReportResponse, GetAccountVerificationReportsCodeErrorBody]:
        """Get the account verification report using a unique code from a successful open banking connection. This
        report provides identity verification and bank account details.

        Args:
            code: The unique code you receive after a successful open banking flow that is included as a query parameter
                in the ``redirectUrl`` callback.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default21("/accountVerification/reports/{code}"),
            path_params=[param[str]("code", code)],
            decoder=json_decoder[AccountVerificationReportResponse],
            error_mapper=get_account_verification_reports_code_error_mapper,
            request_options=request_options,
        )

    async def post_account_verification_routes(
        self,
        body: AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AccountVerificationRoutesResponse, PostAccountVerificationRoutesErrorBody]:
        """Create a list of routes for verifying bank accounts of third-party individuals. Successful connections
        generate a unique code used for requesting bank reports and verifying identity.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default21("/accountVerification/routes"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AccountVerificationRoutesRequest | AccountVerificationRoutesRequestDict](body),
            decoder=json_decoder[AccountVerificationRoutesResponse],
            error_mapper=post_account_verification_routes_error_mapper,
            request_options=request_options,
        )
