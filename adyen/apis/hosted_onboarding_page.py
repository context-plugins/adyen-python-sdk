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
    json_body,
    json_decoder,
    param,
)
from ..errors.post_get_onboarding_url_error import PostGetOnboardingUrlErrorBody, post_get_onboarding_url_error_mapper
from ..models.get_onboarding_url_request import GetOnboardingUrlRequest, GetOnboardingUrlRequestDict
from ..models.get_onboarding_url_response import GetOnboardingUrlResponse
from ..server.server import Server


class HostedOnboardingPage:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = HostedOnboardingPageWithRawResponse(client, server, auth)

    def post_get_onboarding_url(
        self,
        *,
        body: GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOnboardingUrlResponse:
        """Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more
        information on how to use HOP, refer to `Hosted onboarding
        <https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return self._with_raw_response.post_get_onboarding_url(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> HostedOnboardingPageWithRawResponse:
        return self._with_raw_response


class AsyncHostedOnboardingPage:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncHostedOnboardingPageWithRawResponse(client, server, auth)

    async def post_get_onboarding_url(
        self,
        *,
        body: GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetOnboardingUrlResponse:
        """Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more
        information on how to use HOP, refer to `Hosted onboarding
        <https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return (
            await self._with_raw_response.post_get_onboarding_url(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncHostedOnboardingPageWithRawResponse:
        return self._with_raw_response


class HostedOnboardingPageWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_get_onboarding_url(
        self,
        *,
        body: GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOnboardingUrlResponse, PostGetOnboardingUrlErrorBody]:
        """Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more
        information on how to use HOP, refer to `Hosted onboarding
        <https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default19("/getOnboardingUrl"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetOnboardingUrlResponse],
            error_mapper=post_get_onboarding_url_error_mapper,
            request_options=request_options,
        )


class AsyncHostedOnboardingPageWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_get_onboarding_url(
        self,
        *,
        body: GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetOnboardingUrlResponse, PostGetOnboardingUrlErrorBody]:
        """Returns a link to an Adyen-hosted onboarding page (HOP) that you can send to your account holder. For more
        information on how to use HOP, refer to `Hosted onboarding
        <https://docs.adyen.com/classic-platforms/onboard-users/hosted-onboarding-page>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default19("/getOnboardingUrl"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetOnboardingUrlRequest | GetOnboardingUrlRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetOnboardingUrlResponse],
            error_mapper=post_get_onboarding_url_error_mapper,
            request_options=request_options,
        )
