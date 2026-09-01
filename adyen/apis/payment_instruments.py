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
from ..errors.get_payment_instruments_id_error import (
    GetPaymentInstrumentsIdErrorBody,
    get_payment_instruments_id_error_mapper,
)
from ..errors.get_payment_instruments_id_network_token_activation_data_error import (
    GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody,
    get_payment_instruments_id_network_token_activation_data_error_mapper,
)
from ..errors.get_payment_instruments_id_network_tokens_error import (
    GetPaymentInstrumentsIdNetworkTokensErrorBody,
    get_payment_instruments_id_network_tokens_error_mapper,
)
from ..errors.get_payment_instruments_id_reveal_error import (
    GetPaymentInstrumentsIdRevealErrorBody,
    get_payment_instruments_id_reveal_error_mapper,
)
from ..errors.get_payment_instruments_id_transaction_rules_error import (
    GetPaymentInstrumentsIdTransactionRulesErrorBody,
    get_payment_instruments_id_transaction_rules_error_mapper,
)
from ..errors.patch_payment_instruments_id_error import (
    PatchPaymentInstrumentsIdErrorBody,
    patch_payment_instruments_id_error_mapper,
)
from ..errors.post_payment_instruments_error import (
    PostPaymentInstrumentsErrorBody,
    post_payment_instruments_error_mapper,
)
from ..errors.post_payment_instruments_id_network_token_activation_data_error import (
    PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody,
    post_payment_instruments_id_network_token_activation_data_error_mapper,
)
from ..errors.post_payment_instruments_reveal_error import (
    PostPaymentInstrumentsRevealErrorBody,
    post_payment_instruments_reveal_error_mapper,
)
from ..models.list_network_tokens_response import ListNetworkTokensResponse
from ..models.network_token_activation_data_request import (
    NetworkTokenActivationDataRequest,
    NetworkTokenActivationDataRequestDict,
)
from ..models.network_token_activation_data_response import NetworkTokenActivationDataResponse
from ..models.payment_instrument1 import PaymentInstrument1
from ..models.payment_instrument_info import PaymentInstrumentInfo, PaymentInstrumentInfoDict
from ..models.payment_instrument_reveal_info import PaymentInstrumentRevealInfo
from ..models.payment_instrument_reveal_request import (
    PaymentInstrumentRevealRequest,
    PaymentInstrumentRevealRequestDict,
)
from ..models.payment_instrument_reveal_response import PaymentInstrumentRevealResponse
from ..models.payment_instrument_update_request import (
    PaymentInstrumentUpdateRequest,
    PaymentInstrumentUpdateRequestDict,
)
from ..models.transaction_rules_response import TransactionRulesResponse
from ..models.update_payment_instrument import UpdatePaymentInstrument
from ..server.server import Server


class PaymentInstruments:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = PaymentInstrumentsWithRawResponse(client, server, auth)

    def get_payment_instruments_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrument1:
        """Returns the details of a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_payment_instruments_id(id, request_options=request_options).unwrap()

    def get_payment_instruments_id_network_token_activation_data(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NetworkTokenActivationDataResponse:
        """Get the network token activation data for a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_payment_instruments_id_network_token_activation_data(
            id, request_options=request_options
        ).unwrap()

    def get_payment_instruments_id_network_tokens(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListNetworkTokensResponse:
        """List the network tokens connected to a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_payment_instruments_id_network_tokens(
            id, request_options=request_options
        ).unwrap()

    def get_payment_instruments_id_reveal(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrumentRevealInfo:
        """Returns the primary account number (PAN) of a payment instrument.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/issuing/manage-access/api-credentials-web-service#api-permissions>`__:

        * Balance Platform BCL PCI role

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_payment_instruments_id_reveal(id, request_options=request_options).unwrap()

    def get_payment_instruments_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_payment_instruments_id_transaction_rules(
            id, request_options=request_options
        ).unwrap()

    def patch_payment_instruments_id(
        self,
        id: str,
        *,
        body: PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentInstrument:
        """Updates a payment instrument. Once a payment instrument is already active, you can only update its status.
        However, for cards created with **inactive** status, you can still update the balance account associated with
        the card.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_payment_instruments_id(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_payment_instruments(
        self,
        *,
        body: PaymentInstrumentInfo | PaymentInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrument1:
        """Creates a payment instrument to issue a physical card, a virtual card, or a business account to your user.

        For more information, refer to `Issue cards <https://docs.adyen.com/issuing/create-cards>`__ or `Issue business
        accounts <https://docs.adyen.com/platforms/business-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_payment_instruments(body=body, request_options=request_options).unwrap()

    def post_payment_instruments_id_network_token_activation_data(
        self,
        id: str,
        *,
        body: NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NetworkTokenActivationDataResponse:
        """Create provisioning data for a network token. Use the provisioning data to add a user's payment instrument to
        their digital wallet.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_payment_instruments_id_network_token_activation_data(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_payment_instruments_reveal(
        self,
        *,
        body: PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrumentRevealResponse:
        """Returns the encrypted data of a specified payment instrument. These data include:

        - The primary account number (PAN)
        - The card verification code (CVC)
        - The expiry date

        You can decrypt the data to reveal it in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PAN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_payment_instruments_reveal(
            body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> PaymentInstrumentsWithRawResponse:
        return self._with_raw_response


class AsyncPaymentInstruments:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncPaymentInstrumentsWithRawResponse(client, server, auth)

    async def get_payment_instruments_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrument1:
        """Returns the details of a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (await self._with_raw_response.get_payment_instruments_id(id, request_options=request_options)).unwrap()

    async def get_payment_instruments_id_network_token_activation_data(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> NetworkTokenActivationDataResponse:
        """Get the network token activation data for a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_payment_instruments_id_network_token_activation_data(
                id, request_options=request_options
            )
        ).unwrap()

    async def get_payment_instruments_id_network_tokens(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ListNetworkTokensResponse:
        """List the network tokens connected to a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_payment_instruments_id_network_tokens(id, request_options=request_options)
        ).unwrap()

    async def get_payment_instruments_id_reveal(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> PaymentInstrumentRevealInfo:
        """Returns the primary account number (PAN) of a payment instrument.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/issuing/manage-access/api-credentials-web-service#api-permissions>`__:

        * Balance Platform BCL PCI role

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_payment_instruments_id_reveal(id, request_options=request_options)
        ).unwrap()

    async def get_payment_instruments_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> TransactionRulesResponse:
        """Returns a list of transaction rules associated with a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_payment_instruments_id_transaction_rules(
                id, request_options=request_options
            )
        ).unwrap()

    async def patch_payment_instruments_id(
        self,
        id: str,
        *,
        body: PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdatePaymentInstrument:
        """Updates a payment instrument. Once a payment instrument is already active, you can only update its status.
        However, for cards created with **inactive** status, you can still update the balance account associated with
        the card.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.patch_payment_instruments_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_payment_instruments(
        self,
        *,
        body: PaymentInstrumentInfo | PaymentInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrument1:
        """Creates a payment instrument to issue a physical card, a virtual card, or a business account to your user.

        For more information, refer to `Issue cards <https://docs.adyen.com/issuing/create-cards>`__ or `Issue business
        accounts <https://docs.adyen.com/platforms/business-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payment_instruments(body=body, request_options=request_options)
        ).unwrap()

    async def post_payment_instruments_id_network_token_activation_data(
        self,
        id: str,
        *,
        body: NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> NetworkTokenActivationDataResponse:
        """Create provisioning data for a network token. Use the provisioning data to add a user's payment instrument to
        their digital wallet.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payment_instruments_id_network_token_activation_data(
                id, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_payment_instruments_reveal(
        self,
        *,
        body: PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaymentInstrumentRevealResponse:
        """Returns the encrypted data of a specified payment instrument. These data include:

        - The primary account number (PAN)
        - The card verification code (CVC)
        - The expiry date

        You can decrypt the data to reveal it in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PAN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.post_payment_instruments_reveal(body=body, request_options=request_options)
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncPaymentInstrumentsWithRawResponse:
        return self._with_raw_response


class PaymentInstrumentsWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_payment_instruments_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrument1, GetPaymentInstrumentsIdErrorBody]:
        """Returns the details of a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrument1],
            error_mapper=get_payment_instruments_id_error_mapper,
            request_options=request_options,
        )

    def get_payment_instruments_id_network_token_activation_data(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetworkTokenActivationDataResponse, GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]:
        """Get the network token activation data for a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokenActivationData"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[NetworkTokenActivationDataResponse],
            error_mapper=get_payment_instruments_id_network_token_activation_data_error_mapper,
            request_options=request_options,
        )

    def get_payment_instruments_id_network_tokens(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListNetworkTokensResponse, GetPaymentInstrumentsIdNetworkTokensErrorBody]:
        """List the network tokens connected to a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokens"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListNetworkTokensResponse],
            error_mapper=get_payment_instruments_id_network_tokens_error_mapper,
            request_options=request_options,
        )

    def get_payment_instruments_id_reveal(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrumentRevealInfo, GetPaymentInstrumentsIdRevealErrorBody]:
        """Returns the primary account number (PAN) of a payment instrument.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/issuing/manage-access/api-credentials-web-service#api-permissions>`__:

        * Balance Platform BCL PCI role

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/reveal"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentRevealInfo],
            error_mapper=get_payment_instruments_id_reveal_error_mapper,
            request_options=request_options,
        )

    def get_payment_instruments_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetPaymentInstrumentsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_payment_instruments_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    def patch_payment_instruments_id(
        self,
        id: str,
        *,
        body: PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentInstrument, PatchPaymentInstrumentsIdErrorBody]:
        """Updates a payment instrument. Once a payment instrument is already active, you can only update its status.
        However, for cards created with **inactive** status, you can still update the balance account associated with
        the card.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/paymentInstruments/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdatePaymentInstrument],
            error_mapper=patch_payment_instruments_id_error_mapper,
            request_options=request_options,
        )

    def post_payment_instruments(
        self,
        *,
        body: PaymentInstrumentInfo | PaymentInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrument1, PostPaymentInstrumentsErrorBody]:
        """Creates a payment instrument to issue a physical card, a virtual card, or a business account to your user.

        For more information, refer to `Issue cards <https://docs.adyen.com/issuing/create-cards>`__ or `Issue business
        accounts <https://docs.adyen.com/platforms/business-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentInfo | PaymentInstrumentInfoDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrument1],
            error_mapper=post_payment_instruments_error_mapper,
            request_options=request_options,
        )

    def post_payment_instruments_id_network_token_activation_data(
        self,
        id: str,
        *,
        body: NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NetworkTokenActivationDataResponse, PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]:
        """Create provisioning data for a network token. Use the provisioning data to add a user's payment instrument to
        their digital wallet.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokenActivationData"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[NetworkTokenActivationDataResponse],
            error_mapper=post_payment_instruments_id_network_token_activation_data_error_mapper,
            request_options=request_options,
        )

    def post_payment_instruments_reveal(
        self,
        *,
        body: PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrumentRevealResponse, PostPaymentInstrumentsRevealErrorBody]:
        """Returns the encrypted data of a specified payment instrument. These data include:

        - The primary account number (PAN)
        - The card verification code (CVC)
        - The expiry date

        You can decrypt the data to reveal it in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PAN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/reveal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentRevealResponse],
            error_mapper=post_payment_instruments_reveal_error_mapper,
            request_options=request_options,
        )


class AsyncPaymentInstrumentsWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_payment_instruments_id(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrument1, GetPaymentInstrumentsIdErrorBody]:
        """Returns the details of a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrument1],
            error_mapper=get_payment_instruments_id_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instruments_id_network_token_activation_data(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[NetworkTokenActivationDataResponse, GetPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]:
        """Get the network token activation data for a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokenActivationData"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[NetworkTokenActivationDataResponse],
            error_mapper=get_payment_instruments_id_network_token_activation_data_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instruments_id_network_tokens(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[ListNetworkTokensResponse, GetPaymentInstrumentsIdNetworkTokensErrorBody]:
        """List the network tokens connected to a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokens"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListNetworkTokensResponse],
            error_mapper=get_payment_instruments_id_network_tokens_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instruments_id_reveal(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[PaymentInstrumentRevealInfo, GetPaymentInstrumentsIdRevealErrorBody]:
        """Returns the primary account number (PAN) of a payment instrument.

        To make this request, your API credential must have the following `role
        <https://docs.adyen.com/issuing/manage-access/api-credentials-web-service#api-permissions>`__:

        * Balance Platform BCL PCI role

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/reveal"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentRevealInfo],
            error_mapper=get_payment_instruments_id_reveal_error_mapper,
            request_options=request_options,
        )

    async def get_payment_instruments_id_transaction_rules(
        self, id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[TransactionRulesResponse, GetPaymentInstrumentsIdTransactionRulesErrorBody]:
        """Returns a list of transaction rules associated with a payment instrument.

        Args:
            id: The unique identifier of the payment instrument.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/paymentInstruments/{id}/transactionRules"),
            path_params=[param[str]("id", id)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[TransactionRulesResponse],
            error_mapper=get_payment_instruments_id_transaction_rules_error_mapper,
            request_options=request_options,
        )

    async def patch_payment_instruments_id(
        self,
        id: str,
        *,
        body: PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdatePaymentInstrument, PatchPaymentInstrumentsIdErrorBody]:
        """Updates a payment instrument. Once a payment instrument is already active, you can only update its status.
        However, for cards created with **inactive** status, you can still update the balance account associated with
        the card.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/paymentInstruments/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentUpdateRequest | PaymentInstrumentUpdateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdatePaymentInstrument],
            error_mapper=patch_payment_instruments_id_error_mapper,
            request_options=request_options,
        )

    async def post_payment_instruments(
        self,
        *,
        body: PaymentInstrumentInfo | PaymentInstrumentInfoDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrument1, PostPaymentInstrumentsErrorBody]:
        """Creates a payment instrument to issue a physical card, a virtual card, or a business account to your user.

        For more information, refer to `Issue cards <https://docs.adyen.com/issuing/create-cards>`__ or `Issue business
        accounts <https://docs.adyen.com/platforms/business-accounts>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentInfo | PaymentInstrumentInfoDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrument1],
            error_mapper=post_payment_instruments_error_mapper,
            request_options=request_options,
        )

    async def post_payment_instruments_id_network_token_activation_data(
        self,
        id: str,
        *,
        body: NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[NetworkTokenActivationDataResponse, PostPaymentInstrumentsIdNetworkTokenActivationDataErrorBody]:
        """Create provisioning data for a network token. Use the provisioning data to add a user's payment instrument to
        their digital wallet.

        Args:
            id: The unique identifier of the payment instrument.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/{id}/networkTokenActivationData"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[NetworkTokenActivationDataRequest | NetworkTokenActivationDataRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[NetworkTokenActivationDataResponse],
            error_mapper=post_payment_instruments_id_network_token_activation_data_error_mapper,
            request_options=request_options,
        )

    async def post_payment_instruments_reveal(
        self,
        *,
        body: PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaymentInstrumentRevealResponse, PostPaymentInstrumentsRevealErrorBody]:
        """Returns the encrypted data of a specified payment instrument. These data include:

        - The primary account number (PAN)
        - The card verification code (CVC)
        - The expiry date

        You can decrypt the data to reveal it in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PAN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/paymentInstruments/reveal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PaymentInstrumentRevealRequest | PaymentInstrumentRevealRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaymentInstrumentRevealResponse],
            error_mapper=post_payment_instruments_reveal_error_mapper,
            request_options=request_options,
        )
