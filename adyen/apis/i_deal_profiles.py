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
from ..errors.post_ideal_profile_auth_link_error import (
    PostIdealProfileAuthLinkErrorBody,
    post_ideal_profile_auth_link_error_mapper,
)
from ..errors.post_ideal_profile_authenticate_error import (
    PostIdealProfileAuthenticateErrorBody,
    post_ideal_profile_authenticate_error_mapper,
)
from ..errors.post_ideal_profile_register_error import (
    PostIdealProfileRegisterErrorBody,
    post_ideal_profile_register_error_mapper,
)
from ..models.ideal_auth_link_request import IdealAuthLinkRequest, IdealAuthLinkRequestDict
from ..models.ideal_auth_link_response import IdealAuthLinkResponse
from ..models.ideal_authenticate_request import IdealAuthenticateRequest, IdealAuthenticateRequestDict
from ..models.ideal_authenticate_response import IdealAuthenticateResponse
from ..models.profile_registration_request import ProfileRegistrationRequest, ProfileRegistrationRequestDict
from ..models.profile_registration_response import ProfileRegistrationResponse
from ..server.server import Server


class IDealProfiles:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = IDealProfilesWithRawResponse(client, server)

    def post_ideal_profile_auth_link(
        self,
        body: IdealAuthLinkRequest | IdealAuthLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IdealAuthLinkResponse:
        """Manage an already registered iDEAL profile. Generates a redirection URL to manage the iDEAL profile linked to
        the account holder from the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_ideal_profile_auth_link(body, request_options=request_options))

    def post_ideal_profile_authenticate(
        self,
        body: IdealAuthenticateRequest | IdealAuthenticateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IdealAuthenticateResponse:
        """Generates an redirection URL to finish the authentication flow when requested by iDEAL. Before calling this
        endpoint, make sure that your user has completed multi-factor authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_ideal_profile_authenticate(body, request_options=request_options))

    def post_ideal_profile_register(
        self,
        body: ProfileRegistrationRequest | ProfileRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProfileRegistrationResponse:
        """Register a new iDEAL profile. The profile is linked to the account holder and payment instruments included in
        the request. The user must be redirected to the URL in the response to finish their IDEAL profile registration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_ideal_profile_register(body, request_options=request_options))

    @property
    def with_raw_response(self) -> IDealProfilesWithRawResponse:
        return self._with_raw_response


class AsyncIDealProfiles:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncIDealProfilesWithRawResponse(client, server)

    async def post_ideal_profile_auth_link(
        self,
        body: IdealAuthLinkRequest | IdealAuthLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IdealAuthLinkResponse:
        """Manage an already registered iDEAL profile. Generates a redirection URL to manage the iDEAL profile linked to
        the account holder from the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_ideal_profile_auth_link(body, request_options=request_options))

    async def post_ideal_profile_authenticate(
        self,
        body: IdealAuthenticateRequest | IdealAuthenticateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> IdealAuthenticateResponse:
        """Generates an redirection URL to finish the authentication flow when requested by iDEAL. Before calling this
        endpoint, make sure that your user has completed multi-factor authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_ideal_profile_authenticate(body, request_options=request_options)
        )

    async def post_ideal_profile_register(
        self,
        body: ProfileRegistrationRequest | ProfileRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ProfileRegistrationResponse:
        """Register a new iDEAL profile. The profile is linked to the account holder and payment instruments included in
        the request. The user must be redirected to the URL in the response to finish their IDEAL profile registration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Bad Request - The request is malformed or is not the expected format. Unprocessable Entity - A
                request validation error. Internal Service Error - An unrecoverable error occurred while trying to
                perform the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_ideal_profile_register(body, request_options=request_options))

    @property
    def with_raw_response(self) -> AsyncIDealProfilesWithRawResponse:
        return self._with_raw_response


class IDealProfilesWithRawResponse(BaseRawResponse[RawClient, Server]):
    def post_ideal_profile_auth_link(
        self,
        body: IdealAuthLinkRequest | IdealAuthLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IdealAuthLinkResponse, PostIdealProfileAuthLinkErrorBody]:
        """Manage an already registered iDEAL profile. Generates a redirection URL to manage the iDEAL profile linked to
        the account holder from the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/auth-link"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealAuthLinkRequest | IdealAuthLinkRequestDict](body),
            decoder=json_decoder[IdealAuthLinkResponse],
            error_mapper=post_ideal_profile_auth_link_error_mapper,
            request_options=request_options,
        )

    def post_ideal_profile_authenticate(
        self,
        body: IdealAuthenticateRequest | IdealAuthenticateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IdealAuthenticateResponse, PostIdealProfileAuthenticateErrorBody]:
        """Generates an redirection URL to finish the authentication flow when requested by iDEAL. Before calling this
        endpoint, make sure that your user has completed multi-factor authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/authenticate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealAuthenticateRequest | IdealAuthenticateRequestDict](body),
            decoder=json_decoder[IdealAuthenticateResponse],
            error_mapper=post_ideal_profile_authenticate_error_mapper,
            request_options=request_options,
        )

    def post_ideal_profile_register(
        self,
        body: ProfileRegistrationRequest | ProfileRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProfileRegistrationResponse, PostIdealProfileRegisterErrorBody]:
        """Register a new iDEAL profile. The profile is linked to the account holder and payment instruments included in
        the request. The user must be redirected to the URL in the response to finish their IDEAL profile registration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/register"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRegistrationRequest | ProfileRegistrationRequestDict](body),
            decoder=json_decoder[ProfileRegistrationResponse],
            error_mapper=post_ideal_profile_register_error_mapper,
            request_options=request_options,
        )


class AsyncIDealProfilesWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def post_ideal_profile_auth_link(
        self,
        body: IdealAuthLinkRequest | IdealAuthLinkRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IdealAuthLinkResponse, PostIdealProfileAuthLinkErrorBody]:
        """Manage an already registered iDEAL profile. Generates a redirection URL to manage the iDEAL profile linked to
        the account holder from the request.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/auth-link"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealAuthLinkRequest | IdealAuthLinkRequestDict](body),
            decoder=async_json_decoder[IdealAuthLinkResponse],
            error_mapper=post_ideal_profile_auth_link_error_mapper,
            request_options=request_options,
        )

    async def post_ideal_profile_authenticate(
        self,
        body: IdealAuthenticateRequest | IdealAuthenticateRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[IdealAuthenticateResponse, PostIdealProfileAuthenticateErrorBody]:
        """Generates an redirection URL to finish the authentication flow when requested by iDEAL. Before calling this
        endpoint, make sure that your user has completed multi-factor authentication.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/authenticate"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[IdealAuthenticateRequest | IdealAuthenticateRequestDict](body),
            decoder=async_json_decoder[IdealAuthenticateResponse],
            error_mapper=post_ideal_profile_authenticate_error_mapper,
            request_options=request_options,
        )

    async def post_ideal_profile_register(
        self,
        body: ProfileRegistrationRequest | ProfileRegistrationRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ProfileRegistrationResponse, PostIdealProfileRegisterErrorBody]:
        """Register a new iDEAL profile. The profile is linked to the account holder and payment instruments included in
        the request. The user must be redirected to the URL in the response to finish their IDEAL profile registration.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default20("/ideal/profile/register"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ProfileRegistrationRequest | ProfileRegistrationRequestDict](body),
            decoder=async_json_decoder[ProfileRegistrationResponse],
            error_mapper=post_ideal_profile_register_error_mapper,
            request_options=request_options,
        )
