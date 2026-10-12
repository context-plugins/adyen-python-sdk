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
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.get_themes_error import GetThemesErrorBody, get_themes_error_mapper
from ..errors.get_themes_id_error import GetThemesIdErrorBody, get_themes_id_error_mapper
from ..errors.post_legal_entities_id_onboarding_links_error import (
    PostLegalEntitiesIdOnboardingLinksErrorBody,
    post_legal_entities_id_onboarding_links_error_mapper,
)
from ..models.onboarding_link import OnboardingLink
from ..models.onboarding_link_info import OnboardingLinkInfo, OnboardingLinkInfoDict
from ..models.onboarding_theme import OnboardingTheme
from ..models.onboarding_themes import OnboardingThemes
from ..server.server import Server


class HostedOnboarding:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = HostedOnboardingWithRawResponse(client, server, auth)

    def get_themes(self, *, request_options: RequestOptionsOrDict | None = None) -> OnboardingThemes:
        """Returns a list of hosted onboarding page themes.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.get_themes(request_options=request_options))

    def get_themes_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> OnboardingTheme:
        """Returns the details of the theme identified in the path.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the theme
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(self._with_raw_response.get_themes_id(id_, request_options=request_options))

    def post_legal_entities_id_onboarding_links(
        self,
        id_: str,
        *,
        body: OnboardingLinkInfo | OnboardingLinkInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnboardingLink:
        """Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            self._with_raw_response.post_legal_entities_id_onboarding_links(
                id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> HostedOnboardingWithRawResponse:
        return self._with_raw_response


class AsyncHostedOnboarding:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncHostedOnboardingWithRawResponse(client, server, auth)

    async def get_themes(self, *, request_options: RequestOptionsOrDict | None = None) -> OnboardingThemes:
        """Returns a list of hosted onboarding page themes.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.get_themes(request_options=request_options))

    async def get_themes_id(self, id_: str, *, request_options: RequestOptionsOrDict | None = None) -> OnboardingTheme:
        """Returns the details of the theme identified in the path.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the theme
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(await self._with_raw_response.get_themes_id(id_, request_options=request_options))

    async def post_legal_entities_id_onboarding_links(
        self,
        id_: str,
        *,
        body: OnboardingLinkInfo | OnboardingLinkInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> OnboardingLink:
        """Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError1 | RawError``."""
        return unwrap(
            await self._with_raw_response.post_legal_entities_id_onboarding_links(
                id_, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncHostedOnboardingWithRawResponse:
        return self._with_raw_response


class HostedOnboardingWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_themes(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnboardingThemes, GetThemesErrorBody]:
        """Returns a list of hosted onboarding page themes.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/themes"),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[OnboardingThemes],
            error_mapper=get_themes_error_mapper,
            request_options=request_options,
        )

    def get_themes_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnboardingTheme, GetThemesIdErrorBody]:
        """Returns the details of the theme identified in the path.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the theme
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/themes/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[OnboardingTheme],
            error_mapper=get_themes_id_error_mapper,
            request_options=request_options,
        )

    def post_legal_entities_id_onboarding_links(
        self,
        id_: str,
        *,
        body: OnboardingLinkInfo | OnboardingLinkInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnboardingLink, PostLegalEntitiesIdOnboardingLinksErrorBody]:
        """Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/onboardingLinks"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OnboardingLinkInfo | OnboardingLinkInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[OnboardingLink],
            error_mapper=post_legal_entities_id_onboarding_links_error_mapper,
            request_options=request_options,
        )


class AsyncHostedOnboardingWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_themes(
        self, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnboardingThemes, GetThemesErrorBody]:
        """Returns a list of hosted onboarding page themes.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/themes"),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[OnboardingThemes],
            error_mapper=get_themes_error_mapper,
            request_options=request_options,
        )

    async def get_themes_id(
        self, id_: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[OnboardingTheme, GetThemesIdErrorBody]:
        """Returns the details of the theme identified in the path.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the theme
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default18("/themes/{id}"),
            path_params=[param[str]("id", id_)],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[OnboardingTheme],
            error_mapper=get_themes_id_error_mapper,
            request_options=request_options,
        )

    async def post_legal_entities_id_onboarding_links(
        self,
        id_: str,
        *,
        body: OnboardingLinkInfo | OnboardingLinkInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[OnboardingLink, PostLegalEntitiesIdOnboardingLinksErrorBody]:
        """Returns a link to an Adyen-hosted onboarding page where you need to redirect your user.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 700 requests per 5 seconds.

        - Test environments: 200 requests per 5 seconds.

        - Failed requests are subject to a limit of 5 failures per 10 seconds.

        Args:
            id_: The unique identifier of the legal entity
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default18("/legalEntities/{id}/onboardingLinks"),
            path_params=[param[str]("id", id_)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[OnboardingLinkInfo | OnboardingLinkInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=async_json_decoder[OnboardingLink],
            error_mapper=post_legal_entities_id_onboarding_links_error_mapper,
            request_options=request_options,
        )
