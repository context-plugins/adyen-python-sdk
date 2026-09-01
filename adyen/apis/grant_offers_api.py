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
from ..errors.get_grant_offers1_error import GetGrantOffers1ErrorBody, get_grant_offers1_error_mapper
from ..errors.get_grant_offers_error import GetGrantOffersErrorBody, get_grant_offers_error_mapper
from ..errors.get_grant_offers_grant_offer_id_error import (
    GetGrantOffersGrantOfferIdErrorBody,
    get_grant_offers_grant_offer_id_error_mapper,
)
from ..errors.get_grant_offers_id_error import GetGrantOffersIdErrorBody, get_grant_offers_id_error_mapper
from ..models.grant_offer import GrantOffer
from ..models.grant_offer1 import GrantOffer1
from ..models.grant_offers import GrantOffers
from ..server.server import Server


class GrantOffersApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = GrantOffersApiWithRawResponse(client, server, auth)

    def get_grant_offers(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffers:
        """Returns a list of all `grant offers <https://docs.adyen.com/platforms/capital#grant-offers>`__ available for
        ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_grant_offers(account_holder_id, request_options=request_options).unwrap()

    def get_grant_offers_grant_offer_id(
        self, grant_offer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffer:
        """Returns the details of a single grant offer.

        Args:
            grant_offer_id: The unique identifier of the grant offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_grant_offers_grant_offer_id(
            grant_offer_id, request_options=request_options
        ).unwrap()

    def get_grant_offers_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GrantOffer1:
        """Returns the details of the specified static offer.

        Args:
            id: The unique identifier of the static offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grant_offers_id(id, request_options=request_options).unwrap()

    def get_grant_offers1(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffers:
        """Returns a list of all `static offers <https://docs.adyen.com/capital/get-grant-offers/static-offers>`__
        available for ``accountHolderId`` specified as a query parameter. This also includes static offers created for
        financing amounts that the user selected from `dynamic offers
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Args:
            account_holder_id: The unique identifier of the account holder for which you want to get the available
                static offers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return self._with_raw_response.get_grant_offers1(account_holder_id, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> GrantOffersApiWithRawResponse:
        return self._with_raw_response


class AsyncGrantOffersApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncGrantOffersApiWithRawResponse(client, server, auth)

    async def get_grant_offers(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffers:
        """Returns a list of all `grant offers <https://docs.adyen.com/platforms/capital#grant-offers>`__ available for
        ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_grant_offers(account_holder_id, request_options=request_options)
        ).unwrap()

    async def get_grant_offers_grant_offer_id(
        self, grant_offer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffer:
        """Returns the details of a single grant offer.

        Args:
            grant_offer_id: The unique identifier of the grant offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_grant_offers_grant_offer_id(
                grant_offer_id, request_options=request_options
            )
        ).unwrap()

    async def get_grant_offers_id(self, id: str, *, request_options: RequestOptionsOrDict | None = None) -> GrantOffer1:
        """Returns the details of the specified static offer.

        Args:
            id: The unique identifier of the static offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.get_grant_offers_id(id, request_options=request_options)).unwrap()

    async def get_grant_offers1(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> GrantOffers:
        """Returns a list of all `static offers <https://docs.adyen.com/capital/get-grant-offers/static-offers>`__
        available for ``accountHolderId`` specified as a query parameter. This also includes static offers created for
        financing amounts that the user selected from `dynamic offers
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Args:
            account_holder_id: The unique identifier of the account holder for which you want to get the available
                static offers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Not Found - The entity was not found. Unprocessable Entity - A request validation error. ``error``
                is ``DefaultErrorResponseEntity | RawError``."""
        return (
            await self._with_raw_response.get_grant_offers1(account_holder_id, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncGrantOffersApiWithRawResponse:
        return self._with_raw_response


class GrantOffersApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_grant_offers(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffers, GetGrantOffersErrorBody]:
        """Returns a list of all `grant offers <https://docs.adyen.com/platforms/capital#grant-offers>`__ available for
        ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantOffers"),
            query_params=[param[str]("accountHolderId", account_holder_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GrantOffers],
            error_mapper=get_grant_offers_error_mapper,
            request_options=request_options,
        )

    def get_grant_offers_grant_offer_id(
        self, grant_offer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffer, GetGrantOffersGrantOfferIdErrorBody]:
        """Returns the details of a single grant offer.

        Args:
            grant_offer_id: The unique identifier of the grant offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantOffers/{grantOfferId}"),
            path_params=[param[str]("grantOfferId", grant_offer_id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GrantOffer],
            error_mapper=get_grant_offers_grant_offer_id_error_mapper,
            request_options=request_options,
        )

    def get_grant_offers_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffer1, GetGrantOffersIdErrorBody]:
        """Returns the details of the specified static offer.

        Args:
            id: The unique identifier of the static offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantOffers/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[GrantOffer1],
            error_mapper=get_grant_offers_id_error_mapper,
            request_options=request_options,
        )

    def get_grant_offers1(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffers, GetGrantOffers1ErrorBody]:
        """Returns a list of all `static offers <https://docs.adyen.com/capital/get-grant-offers/static-offers>`__
        available for ``accountHolderId`` specified as a query parameter. This also includes static offers created for
        financing amounts that the user selected from `dynamic offers
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Args:
            account_holder_id: The unique identifier of the account holder for which you want to get the available
                static offers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantOffers"),
            query_params=[param[str]("accountHolderId", account_holder_id)],
            decoder=json_decoder[GrantOffers],
            error_mapper=get_grant_offers1_error_mapper,
            request_options=request_options,
        )


class AsyncGrantOffersApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_grant_offers(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffers, GetGrantOffersErrorBody]:
        """Returns a list of all `grant offers <https://docs.adyen.com/platforms/capital#grant-offers>`__ available for
        ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the grant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantOffers"),
            query_params=[param[str]("accountHolderId", account_holder_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GrantOffers],
            error_mapper=get_grant_offers_error_mapper,
            request_options=request_options,
        )

    async def get_grant_offers_grant_offer_id(
        self, grant_offer_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffer, GetGrantOffersGrantOfferIdErrorBody]:
        """Returns the details of a single grant offer.

        Args:
            grant_offer_id: The unique identifier of the grant offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/grantOffers/{grantOfferId}"),
            path_params=[param[str]("grantOfferId", grant_offer_id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GrantOffer],
            error_mapper=get_grant_offers_grant_offer_id_error_mapper,
            request_options=request_options,
        )

    async def get_grant_offers_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffer1, GetGrantOffersIdErrorBody]:
        """Returns the details of the specified static offer.

        Args:
            id: The unique identifier of the static offer.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantOffers/{id}"),
            path_params=[param[str]("id", id)],
            decoder=json_decoder[GrantOffer1],
            error_mapper=get_grant_offers_id_error_mapper,
            request_options=request_options,
        )

    async def get_grant_offers1(
        self, account_holder_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[GrantOffers, GetGrantOffers1ErrorBody]:
        """Returns a list of all `static offers <https://docs.adyen.com/capital/get-grant-offers/static-offers>`__
        available for ``accountHolderId`` specified as a query parameter. This also includes static offers created for
        financing amounts that the user selected from `dynamic offers
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Args:
            account_holder_id: The unique identifier of the account holder for which you want to get the available
                static offers.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/grantOffers"),
            query_params=[param[str]("accountHolderId", account_holder_id)],
            decoder=json_decoder[GrantOffers],
            error_mapper=get_grant_offers1_error_mapper,
            request_options=request_options,
        )
