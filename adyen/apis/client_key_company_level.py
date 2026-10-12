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
    async_json_decoder,
    json_decoder,
    param,
    unwrap,
)
from ..errors.post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error import (
    PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody,
    post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error_mapper,
)
from ..models.generate_client_key_response import GenerateClientKeyResponse
from ..server.server import Server


class ClientKeyCompanyLevel:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ClientKeyCompanyLevelWithRawResponse(client, server, auth)

    def post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
        self, company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateClientKeyResponse:
        """Returns a new `client key
        <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__ for the API credential
        identified in the path. You can use the new client key a few minutes after generating it. The old client key
        stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            company_id: The unique identifier of the company account.
            api_credential_id: Unique identifier of the API credential.
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
            self._with_raw_response.post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
                company_id, api_credential_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ClientKeyCompanyLevelWithRawResponse:
        return self._with_raw_response


class AsyncClientKeyCompanyLevel:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncClientKeyCompanyLevelWithRawResponse(client, server, auth)

    async def post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
        self, company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GenerateClientKeyResponse:
        """Returns a new `client key
        <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__ for the API credential
        identified in the path. You can use the new client key a few minutes after generating it. The old client key
        stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            company_id: The unique identifier of the company account.
            api_credential_id: Unique identifier of the API credential.
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
            await self._with_raw_response.post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
                company_id, api_credential_id, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncClientKeyCompanyLevelWithRawResponse:
        return self._with_raw_response


class ClientKeyCompanyLevelWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
        self, company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        GenerateClientKeyResponse, PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody
    ]:
        """Returns a new `client key
        <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__ for the API credential
        identified in the path. You can use the new client key a few minutes after generating it. The old client key
        stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            company_id: The unique identifier of the company account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey"
            ),
            path_params=[param[str]("companyId", company_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenerateClientKeyResponse],
            error_mapper=post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error_mapper,
            request_options=request_options,
        )


class AsyncClientKeyCompanyLevelWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_companies_company_id_api_credentials_api_credential_id_generate_client_key(
        self, company_id: str, api_credential_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[
        GenerateClientKeyResponse, PostCompaniesCompanyIdApiCredentialsApiCredentialIdGenerateClientKeyErrorBody
    ]:
        """Returns a new `client key
        <https://docs.adyen.com/development-resources/client-side-authentication#how-it-works>`__ for the API credential
        identified in the path. You can use the new client key a few minutes after generating it. The old client key
        stops working 24 hours after generating a new one.

        To make this request, your API credential must have the following `roles
        <https://docs.adyen.com/development-resources/api-credentials#api-permissions>`__:
        * Management API—API credentials read and write

        Args:
            company_id: The unique identifier of the company account.
            api_credential_id: Unique identifier of the API credential.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default9(
                "/companies/{companyId}/apiCredentials/{apiCredentialId}/generateClientKey"
            ),
            path_params=[param[str]("companyId", company_id), param[str]("apiCredentialId", api_credential_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[GenerateClientKeyResponse],
            error_mapper=post_companies_company_id_api_credentials_api_credential_id_generate_client_key_error_mapper,
            request_options=request_options,
        )
