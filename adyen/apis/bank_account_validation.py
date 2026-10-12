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
    empty_response,
    json_body,
    param,
    unwrap,
)
from ..errors.post_validate_bank_account_identification_error import (
    PostValidateBankAccountIdentificationErrorBody,
    post_validate_bank_account_identification_error_mapper,
)
from ..models.bank_account_identification_validation_request import (
    BankAccountIdentificationValidationRequest,
    BankAccountIdentificationValidationRequestDict,
)
from ..server.server import Server


class BankAccountValidation:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = BankAccountValidationWithRawResponse(client, server, auth)

    def post_validate_bank_account_identification(
        self,
        *,
        body: BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Validates bank account identification details. You can use this endpoint to validate bank account details
        before you `make a transfer <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ or `create
        a transfer instrument <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            self._with_raw_response.post_validate_bank_account_identification(
                body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> BankAccountValidationWithRawResponse:
        return self._with_raw_response


class AsyncBankAccountValidation:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncBankAccountValidationWithRawResponse(client, server, auth)

    async def post_validate_bank_account_identification(
        self,
        *,
        body: BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Validates bank account identification details. You can use this endpoint to validate bank account details
        before you `make a transfer <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ or `create
        a transfer instrument <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return unwrap(
            await self._with_raw_response.post_validate_bank_account_identification(
                body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncBankAccountValidationWithRawResponse:
        return self._with_raw_response


class BankAccountValidationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_validate_bank_account_identification(
        self,
        *,
        body: BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostValidateBankAccountIdentificationErrorBody]:
        """Validates bank account identification details. You can use this endpoint to validate bank account details
        before you `make a transfer <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ or `create
        a transfer instrument <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/validateBankAccountIdentification"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None
            ](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=post_validate_bank_account_identification_error_mapper,
            request_options=request_options,
        )


class AsyncBankAccountValidationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_validate_bank_account_identification(
        self,
        *,
        body: BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, PostValidateBankAccountIdentificationErrorBody]:
        """Validates bank account identification details. You can use this endpoint to validate bank account details
        before you `make a transfer <https://docs.adyen.com/api-explorer/transfers/latest/post/transfers>`__ or `create
        a transfer instrument <https://docs.adyen.com/api-explorer/legalentity/latest/post/transferInstruments>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/validateBankAccountIdentification"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[
                BankAccountIdentificationValidationRequest | BankAccountIdentificationValidationRequestDict | None
            ](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_empty_response,
            error_mapper=post_validate_bank_account_identification_error_mapper,
            request_options=request_options,
        )
