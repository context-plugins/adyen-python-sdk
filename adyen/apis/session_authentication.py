from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_json_decoder,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.post_auth_certificate_error import PostAuthCertificateErrorBody, post_auth_certificate_error_mapper
from ..errors.post_sessions2_error import PostSessions2ErrorBody, post_sessions2_error_mapper
from ..models.authentication_session_request import AuthenticationSessionRequest, AuthenticationSessionRequestDict
from ..models.authentication_session_response import AuthenticationSessionResponse
from ..models.certificate_loading_request import CertificateLoadingRequest, CertificateLoadingRequestDict
from ..models.certificate_loading_response import CertificateLoadingResponse
from ..server.server import Server


class SessionAuthentication:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = SessionAuthenticationWithRawResponse(client, server)

    def post_auth_certificate(
        self,
        *,
        x_api_key: str | None = None,
        body: CertificateLoadingRequest | CertificateLoadingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CertificateLoadingResponse:
        """Establishes a secure communication session between the Mobile SDK and the Adyen payments platform, through
        mutual authentication. The request sends a setup token that identifies the SDK and the device. The response
        returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform.

        Args:
            x_api_key: The API key to authenticate API requests.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad request - validation failed. Unauthorized - authentication required. Unprocessable entity -
                session request could not be processed. Internal server error. ``error`` is ``DefaultErrorResponseEntity
                | RawError``."""
        return unwrap(
            self._with_raw_response.post_auth_certificate(
                x_api_key=x_api_key, body=body, request_options=request_options
            ),
        )

    def post_sessions2(
        self,
        body: AuthenticationSessionRequest | AuthenticationSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthenticationSessionResponse:
        """Creates a session token that is required to integrate `components
        <https://docs.adyen.com/platforms/components-overview>`__.

        The response contains encrypted session data. The front end then uses the session data to make the required
        server-side calls for the component.

        To create a token, you must meet specific requirements. These requirements vary depending on the type of
        component. For more information, see the documentation for `Onboarding
        <https://docs.adyen.com/platforms/onboard-users/components>`__ and `Platform Experience
        <https://docs.adyen.com/platforms/build-user-dashboards>`__ components.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_sessions2(body, request_options=request_options))

    @property
    def with_raw_response(self) -> SessionAuthenticationWithRawResponse:
        return self._with_raw_response


class AsyncSessionAuthentication:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncSessionAuthenticationWithRawResponse(client, server)

    async def post_auth_certificate(
        self,
        *,
        x_api_key: str | None = None,
        body: CertificateLoadingRequest | CertificateLoadingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CertificateLoadingResponse:
        """Establishes a secure communication session between the Mobile SDK and the Adyen payments platform, through
        mutual authentication. The request sends a setup token that identifies the SDK and the device. The response
        returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform.

        Args:
            x_api_key: The API key to authenticate API requests.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad request - validation failed. Unauthorized - authentication required. Unprocessable entity -
                session request could not be processed. Internal server error. ``error`` is ``DefaultErrorResponseEntity
                | RawError``."""
        return unwrap(
            await self._with_raw_response.post_auth_certificate(
                x_api_key=x_api_key, body=body, request_options=request_options
            ),
        )

    async def post_sessions2(
        self,
        body: AuthenticationSessionRequest | AuthenticationSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AuthenticationSessionResponse:
        """Creates a session token that is required to integrate `components
        <https://docs.adyen.com/platforms/components-overview>`__.

        The response contains encrypted session data. The front end then uses the session data to make the required
        server-side calls for the component.

        To create a token, you must meet specific requirements. These requirements vary depending on the type of
        component. For more information, see the documentation for `Onboarding
        <https://docs.adyen.com/platforms/onboard-users/components>`__ and `Platform Experience
        <https://docs.adyen.com/platforms/build-user-dashboards>`__ components.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Successful operation

        Raises:
            ApiError: Bad request Unauthorized Forbidden ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_sessions2(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncSessionAuthenticationWithRawResponse:
        return self._with_raw_response


class SessionAuthenticationWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_auth_certificate(
        self,
        *,
        x_api_key: str | None = None,
        body: CertificateLoadingRequest | CertificateLoadingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CertificateLoadingResponse, PostAuthCertificateErrorBody]:
        """Establishes a secure communication session between the Mobile SDK and the Adyen payments platform, through
        mutual authentication. The request sends a setup token that identifies the SDK and the device. The response
        returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform.

        Args:
            x_api_key: The API key to authenticate API requests.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default25("/auth/certificate"),
            headers=[param[str | None]("X-API-Key", x_api_key), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CertificateLoadingRequest | CertificateLoadingRequestDict | None](body),
            decoder=json_decoder[CertificateLoadingResponse],
            error_mapper=post_auth_certificate_error_mapper,
            request_options=request_options,
        )

    def post_sessions2(
        self,
        body: AuthenticationSessionRequest | AuthenticationSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthenticationSessionResponse, PostSessions2ErrorBody]:
        """Creates a session token that is required to integrate `components
        <https://docs.adyen.com/platforms/components-overview>`__.

        The response contains encrypted session data. The front end then uses the session data to make the required
        server-side calls for the component.

        To create a token, you must meet specific requirements. These requirements vary depending on the type of
        component. For more information, see the documentation for `Onboarding
        <https://docs.adyen.com/platforms/onboard-users/components>`__ and `Platform Experience
        <https://docs.adyen.com/platforms/build-user-dashboards>`__ components.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default17("/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthenticationSessionRequest | AuthenticationSessionRequestDict](body),
            decoder=json_decoder[AuthenticationSessionResponse],
            error_mapper=post_sessions2_error_mapper,
            request_options=request_options,
        )


class AsyncSessionAuthenticationWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_auth_certificate(
        self,
        *,
        x_api_key: str | None = None,
        body: CertificateLoadingRequest | CertificateLoadingRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CertificateLoadingResponse, PostAuthCertificateErrorBody]:
        """Establishes a secure communication session between the Mobile SDK and the Adyen payments platform, through
        mutual authentication. The request sends a setup token that identifies the SDK and the device. The response
        returns a session token that the SDK can use to authenticate responses received from the Adyen payments
        platform.

        Args:
            x_api_key: The API key to authenticate API requests.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default25("/auth/certificate"),
            headers=[param[str | None]("X-API-Key", x_api_key), param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CertificateLoadingRequest | CertificateLoadingRequestDict | None](body),
            decoder=async_json_decoder[CertificateLoadingResponse],
            error_mapper=post_auth_certificate_error_mapper,
            request_options=request_options,
        )

    async def post_sessions2(
        self,
        body: AuthenticationSessionRequest | AuthenticationSessionRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AuthenticationSessionResponse, PostSessions2ErrorBody]:
        """Creates a session token that is required to integrate `components
        <https://docs.adyen.com/platforms/components-overview>`__.

        The response contains encrypted session data. The front end then uses the session data to make the required
        server-side calls for the component.

        To create a token, you must meet specific requirements. These requirements vary depending on the type of
        component. For more information, see the documentation for `Onboarding
        <https://docs.adyen.com/platforms/onboard-users/components>`__ and `Platform Experience
        <https://docs.adyen.com/platforms/build-user-dashboards>`__ components.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default17("/sessions"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AuthenticationSessionRequest | AuthenticationSessionRequestDict](body),
            decoder=async_json_decoder[AuthenticationSessionResponse],
            error_mapper=post_sessions2_error_mapper,
            request_options=request_options,
        )
