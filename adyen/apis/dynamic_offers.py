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
from ..errors.get_dynamic_offers_error import GetDynamicOffersErrorBody, get_dynamic_offers_error_mapper
from ..errors.post_dynamic_offers_id_calculate_error import (
    PostDynamicOffersIdCalculateErrorBody,
    post_dynamic_offers_id_calculate_error_mapper,
)
from ..errors.post_dynamic_offers_id_grant_offer_error import (
    PostDynamicOffersIdGrantOfferErrorBody,
    post_dynamic_offers_id_grant_offer_error_mapper,
)
from ..models.calculate_grant_offer_request import CalculateGrantOfferRequest, CalculateGrantOfferRequestDict
from ..models.calculated_grant_offer import CalculatedGrantOffer
from ..models.create_grant_offer_request import CreateGrantOfferRequest, CreateGrantOfferRequestDict
from ..models.enums.financing_type import FinancingTypeOrStr
from ..models.get_dynamic_offers_response import GetDynamicOffersResponse
from ..models.grant_offer1 import GrantOffer1
from ..server.server import Server


class DynamicOffers:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = DynamicOffersWithRawResponse(client, server)

    def get_dynamic_offers(
        self,
        account_holder_id: str,
        *,
        financing_type: FinancingTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetDynamicOffersResponse:
        """Returns a list of all `dynamic offers <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__
        available for ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the account holder that the dynamic offer is for.
            financing_type: The type of financing that the offer is for. If the value is not specified, returns all
                available types. Possible values: **businessFinancing**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.get_dynamic_offers(
            account_holder_id, financing_type=financing_type, request_options=request_options
        ).unwrap()

    def post_dynamic_offers_id_calculate(
        self,
        id: str,
        *,
        body: CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculatedGrantOffer:
        """Calculates a preliminary offer for the financing amount that the user selected from a `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__. The preliminary offer is for informational
        purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.post_dynamic_offers_id_calculate(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_dynamic_offers_id_grant_offer(
        self,
        id: str,
        *,
        body: CreateGrantOfferRequest | CreateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GrantOffer1:
        """Creates a static offer for the financing amount that the user selected from the `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return self._with_raw_response.post_dynamic_offers_id_grant_offer(
            id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> DynamicOffersWithRawResponse:
        return self._with_raw_response


class AsyncDynamicOffers:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncDynamicOffersWithRawResponse(client, server)

    async def get_dynamic_offers(
        self,
        account_holder_id: str,
        *,
        financing_type: FinancingTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetDynamicOffersResponse:
        """Returns a list of all `dynamic offers <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__
        available for ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the account holder that the dynamic offer is for.
            financing_type: The type of financing that the offer is for. If the value is not specified, returns all
                available types. Possible values: **businessFinancing**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.get_dynamic_offers(
                account_holder_id, financing_type=financing_type, request_options=request_options
            )
        ).unwrap()

    async def post_dynamic_offers_id_calculate(
        self,
        id: str,
        *,
        body: CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CalculatedGrantOffer:
        """Calculates a preliminary offer for the financing amount that the user selected from a `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__. The preliminary offer is for informational
        purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.post_dynamic_offers_id_calculate(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_dynamic_offers_id_grant_offer(
        self,
        id: str,
        *,
        body: CreateGrantOfferRequest | CreateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GrantOffer1:
        """Creates a static offer for the financing amount that the user selected from the `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - The request has succeeded.

        Raises:
            ApiError: Unprocessable Entity - A request validation error. ``error`` is ``DefaultErrorResponseEntity |
                RawError``."""
        return (
            await self._with_raw_response.post_dynamic_offers_id_grant_offer(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncDynamicOffersWithRawResponse:
        return self._with_raw_response


class DynamicOffersWithRawResponse(BaseRawResponse[RawClient, Server]):
    def get_dynamic_offers(
        self,
        account_holder_id: str,
        *,
        financing_type: FinancingTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetDynamicOffersResponse, GetDynamicOffersErrorBody]:
        """Returns a list of all `dynamic offers <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__
        available for ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the account holder that the dynamic offer is for.
            financing_type: The type of financing that the offer is for. If the value is not specified, returns all
                available types. Possible values: **businessFinancing**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/dynamicOffers"),
            query_params=[
                param[str]("accountHolderId", account_holder_id),
                param[FinancingTypeOrStr | None]("financingType", financing_type),
            ],
            decoder=json_decoder[GetDynamicOffersResponse],
            error_mapper=get_dynamic_offers_error_mapper,
            request_options=request_options,
        )

    def post_dynamic_offers_id_calculate(
        self,
        id: str,
        *,
        body: CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculatedGrantOffer, PostDynamicOffersIdCalculateErrorBody]:
        """Calculates a preliminary offer for the financing amount that the user selected from a `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__. The preliminary offer is for informational
        purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/dynamicOffers/{id}/calculate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None](body),
            decoder=json_decoder[CalculatedGrantOffer],
            error_mapper=post_dynamic_offers_id_calculate_error_mapper,
            request_options=request_options,
        )

    def post_dynamic_offers_id_grant_offer(
        self,
        id: str,
        *,
        body: CreateGrantOfferRequest | CreateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GrantOffer1, PostDynamicOffersIdGrantOfferErrorBody]:
        """Creates a static offer for the financing amount that the user selected from the `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/dynamicOffers/{id}/grantOffer"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGrantOfferRequest | CreateGrantOfferRequestDict | None](body),
            decoder=json_decoder[GrantOffer1],
            error_mapper=post_dynamic_offers_id_grant_offer_error_mapper,
            request_options=request_options,
        )


class AsyncDynamicOffersWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def get_dynamic_offers(
        self,
        account_holder_id: str,
        *,
        financing_type: FinancingTypeOrStr | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetDynamicOffersResponse, GetDynamicOffersErrorBody]:
        """Returns a list of all `dynamic offers <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__
        available for ``accountHolderId`` specified as a query parameter.

        Args:
            account_holder_id: The unique identifier of the account holder that the dynamic offer is for.
            financing_type: The type of financing that the offer is for. If the value is not specified, returns all
                available types. Possible values: **businessFinancing**
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default15("/dynamicOffers"),
            query_params=[
                param[str]("accountHolderId", account_holder_id),
                param[FinancingTypeOrStr | None]("financingType", financing_type),
            ],
            decoder=json_decoder[GetDynamicOffersResponse],
            error_mapper=get_dynamic_offers_error_mapper,
            request_options=request_options,
        )

    async def post_dynamic_offers_id_calculate(
        self,
        id: str,
        *,
        body: CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CalculatedGrantOffer, PostDynamicOffersIdCalculateErrorBody]:
        """Calculates a preliminary offer for the financing amount that the user selected from a `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__. The preliminary offer is for informational
        purposes only and cannot be used to initiate a grant.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 120 requests per minute.

        - Test environments: 120 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/dynamicOffers/{id}/calculate"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CalculateGrantOfferRequest | CalculateGrantOfferRequestDict | None](body),
            decoder=json_decoder[CalculatedGrantOffer],
            error_mapper=post_dynamic_offers_id_calculate_error_mapper,
            request_options=request_options,
        )

    async def post_dynamic_offers_id_grant_offer(
        self,
        id: str,
        *,
        body: CreateGrantOfferRequest | CreateGrantOfferRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GrantOffer1, PostDynamicOffersIdGrantOfferErrorBody]:
        """Creates a static offer for the financing amount that the user selected from the `dynamic offer
        <https://docs.adyen.com/capital/get-grant-offers/dynamic-offers/>`__.

        Requests to this endpoint are subject to rate limits:

        - Live environments: 30 requests per minute.

        - Test environments: 30 requests per minute.

        Args:
            id: The unique identifier of the dynamic offer from which the user selected the financing amount.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default15("/dynamicOffers/{id}/grantOffer"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[CreateGrantOfferRequest | CreateGrantOfferRequestDict | None](body),
            decoder=json_decoder[GrantOffer1],
            error_mapper=post_dynamic_offers_id_grant_offer_error_mapper,
            request_options=request_options,
        )
