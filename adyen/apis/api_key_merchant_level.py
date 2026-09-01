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
    json_decoder,
    param,
)
from ..errors.post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key_error import (
    PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody,
    post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key_error_mapper,
)
from ..models.generate_api_key_response import GenerateApiKeyResponse
from ..server.server import Server


class ApiKeyMerchantLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ApiKeyMerchantLevelWithRawResponse(client, server, auth)

    def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateApiKeyResponse:
        """Returns a new API key for the API credential. You can use the new API key a few minutes after generating it.
        The old API key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
            merchant_id, api_credential_id, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ApiKeyMerchantLevelWithRawResponse:
        return self._with_raw_response


class AsyncApiKeyMerchantLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncApiKeyMerchantLevelWithRawResponse(client, server, auth)

    async def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateApiKeyResponse:
        """Returns a new API key for the API credential. You can use the new API key a few minutes after generating it.
        The old API key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
                merchant_id, api_credential_id, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncApiKeyMerchantLevelWithRawResponse:
        return self._with_raw_response


class ApiKeyMerchantLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateApiKeyResponse, PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody]:
        """Returns a new API key for the API credential. You can use the new API key a few minutes after generating it.
        The old API key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateApiKeyResponse],
            error_mapper=post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key_error_mapper,
            request_options=request_options,
        )


class AsyncApiKeyMerchantLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key(
        self, merchant_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GenerateApiKeyResponse, PostMerchantsMerchantIdApiCredentialsApiCredentialIdGenerateApiKeyErrorBody]:
        """Returns a new API key for the API credential. You can use the new API key a few minutes after generating it.
        The old API key stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            merchant_id: The unique identifier of the merchant account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/merchants/{merchantId}/apiCredentials/{apiCredentialId}/generateApiKey"
            ),
            path_params=[param[str]("merchantId", merchant_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateApiKeyResponse],
            error_mapper=post_merchants_merchant_id_api_credentials_api_credential_id_generate_api_key_error_mapper,
            request_options=request_options,
        )
