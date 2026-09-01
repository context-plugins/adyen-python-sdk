from __future__ import annotations

from uuid import UUID, uuid4

from ..auth import AsyncAuthSchemes, AuthSchemes
from ..core import (
    AnySchemes,
    ApiResult,
    AsyncAnySchemes,
    AsyncRawClient,
    RawClient,
    RawError,
    RequestOptionsOrDict,
    SecuredRawResponse,
    empty_response,
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..models.checkout_forward_request import CheckoutForwardRequest, CheckoutForwardRequestDict
from ..models.checkout_forward_response import CheckoutForwardResponse
from ..models.list_stored_payment_methods_response import ListStoredPaymentMethodsResponse
from ..models.stored_payment_method_request import StoredPaymentMethodRequest, StoredPaymentMethodRequestDict
from ..models.stored_payment_method_resource import StoredPaymentMethodResource
from ..server.server import Server


class RecurringApi:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = RecurringApiWithRawResponse(client, server, auth)

    def delete_stored_payment_methods_stored_payment_method_id(
        self,
        stored_payment_method_id: str,
        shopper_reference: str,
        merchant_account: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes the token identified in the path. The token can no longer be used with payment requests.

        Args:
            stored_payment_method_id: The unique identifier of the token.
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.delete_stored_payment_methods_stored_payment_method_id(
            stored_payment_method_id, shopper_reference, merchant_account, request_options=request_options
        ).unwrap()

    def get_stored_payment_methods(
        self,
        *,
        shopper_reference: str | None = None,
        merchant_account: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoredPaymentMethodsResponse:
        """Lists the tokens for stored payment details for the shopper identified in the path, if there are any
        available. The token ID can be used with payment requests for the shopper's payment. A summary of the stored
        details is included.

        Args:
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.get_stored_payment_methods(
            shopper_reference=shopper_reference, merchant_account=merchant_account, request_options=request_options
        ).unwrap()

    def post_forward(
        self,
        *,
        idempotency_key: str | None = None,
        body: CheckoutForwardRequest | CheckoutForwardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CheckoutForwardResponse:
        """Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response
        from the third-party. Supports forwarding stored card details or `network tokens
        <https://docs.adyen.com/online-payments/network-tokenization>`__. For more information, see `Forward stored
        payment details <https://docs.adyen.com/online-payments/tokenization/forward-payment-details>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.post_forward(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_stored_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredPaymentMethodResource:
        """Creates a token to store the shopper's payment details. This token can be used for the shopper's future
        payments.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.post_stored_payment_methods(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> RecurringApiWithRawResponse:
        return self._with_raw_response


class AsyncRecurringApi:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncRecurringApiWithRawResponse(client, server, auth)

    async def delete_stored_payment_methods_stored_payment_method_id(
        self,
        stored_payment_method_id: str,
        shopper_reference: str,
        merchant_account: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> None:
        """Deletes the token identified in the path. The token can no longer be used with payment requests.

        Args:
            stored_payment_method_id: The unique identifier of the token.
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.delete_stored_payment_methods_stored_payment_method_id(
                stored_payment_method_id, shopper_reference, merchant_account, request_options=request_options
            )
        ).unwrap()

    async def get_stored_payment_methods(
        self,
        *,
        shopper_reference: str | None = None,
        merchant_account: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ListStoredPaymentMethodsResponse:
        """Lists the tokens for stored payment details for the shopper identified in the path, if there are any
        available. The token ID can be used with payment requests for the shopper's payment. A summary of the stored
        details is included.

        Args:
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.get_stored_payment_methods(
                shopper_reference=shopper_reference, merchant_account=merchant_account, request_options=request_options
            )
        ).unwrap()

    async def post_forward(
        self,
        *,
        idempotency_key: str | None = None,
        body: CheckoutForwardRequest | CheckoutForwardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> CheckoutForwardResponse:
        """Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response
        from the third-party. Supports forwarding stored card details or `network tokens
        <https://docs.adyen.com/online-payments/network-tokenization>`__. For more information, see `Forward stored
        payment details <https://docs.adyen.com/online-payments/tokenization/forward-payment-details>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.post_forward(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_stored_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> StoredPaymentMethodResource:
        """Creates a token to store the shopper's payment details. This token can be used for the shopper's future
        payments.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            Created - the request has been fulfilled and has resulted in one or more new resources being created.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.post_stored_payment_methods(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncRecurringApiWithRawResponse:
        return self._with_raw_response


class RecurringApiWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_stored_payment_methods_stored_payment_method_id(
        self,
        stored_payment_method_id: str,
        shopper_reference: str,
        merchant_account: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Deletes the token identified in the path. The token can no longer be used with payment requests.

        Args:
            stored_payment_method_id: The unique identifier of the token.
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/storedPaymentMethods/{storedPaymentMethodId}"),
            path_params=[param[str]("storedPaymentMethodId", stored_payment_method_id)],
            query_params=[
                param[str]("shopperReference", shopper_reference), param[str]("merchantAccount", merchant_account)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def get_stored_payment_methods(
        self,
        *,
        shopper_reference: str | None = None,
        merchant_account: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoredPaymentMethodsResponse, RawError]:
        """Lists the tokens for stored payment details for the shopper identified in the path, if there are any
        available. The token ID can be used with payment requests for the shopper's payment. A summary of the stored
        details is included.

        Args:
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default("/storedPaymentMethods"),
            query_params=[
                param[str | None]("shopperReference", shopper_reference),
                param[str | None]("merchantAccount", merchant_account),
            ],
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoredPaymentMethodsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_forward(
        self,
        *,
        idempotency_key: str | None = None,
        body: CheckoutForwardRequest | CheckoutForwardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CheckoutForwardResponse, RawError]:
        """Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response
        from the third-party. Supports forwarding stored card details or `network tokens
        <https://docs.adyen.com/online-payments/network-tokenization>`__. For more information, see `Forward stored
        payment details <https://docs.adyen.com/online-payments/tokenization/forward-payment-details>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/forward"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CheckoutForwardRequest | CheckoutForwardRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CheckoutForwardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_stored_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredPaymentMethodResource, RawError]:
        """Creates a token to store the shopper's payment details. This token can be used for the shopper's future
        payments.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/storedPaymentMethods"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredPaymentMethodResource],
            error_mapper=raw_error_response,
            request_options=request_options,
        )


class AsyncRecurringApiWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_stored_payment_methods_stored_payment_method_id(
        self,
        stored_payment_method_id: str,
        shopper_reference: str,
        merchant_account: str,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[None, RawError]:
        """Deletes the token identified in the path. The token can no longer be used with payment requests.

        Args:
            stored_payment_method_id: The unique identifier of the token.
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default("/storedPaymentMethods/{storedPaymentMethodId}"),
            path_params=[param[str]("storedPaymentMethodId", stored_payment_method_id)],
            query_params=[
                param[str]("shopperReference", shopper_reference), param[str]("merchantAccount", merchant_account)
            ],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def get_stored_payment_methods(
        self,
        *,
        shopper_reference: str | None = None,
        merchant_account: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ListStoredPaymentMethodsResponse, RawError]:
        """Lists the tokens for stored payment details for the shopper identified in the path, if there are any
        available. The token ID can be used with payment requests for the shopper's payment. A summary of the stored
        details is included.

        Args:
            shopper_reference: Your reference to uniquely identify this shopper, for example user ID or account ID.
                Minimum length: 3 characters. > Your reference must not include personally identifiable information
                (PII), for example name or email address.
            merchant_account: Your merchant account.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default("/storedPaymentMethods"),
            query_params=[
                param[str | None]("shopperReference", shopper_reference),
                param[str | None]("merchantAccount", merchant_account),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ListStoredPaymentMethodsResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_forward(
        self,
        *,
        idempotency_key: str | None = None,
        body: CheckoutForwardRequest | CheckoutForwardRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[CheckoutForwardResponse, RawError]:
        """Forwards the payment details you stored with Adyen to a third-party that you specify and returns the response
        from the third-party. Supports forwarding stored card details or `network tokens
        <https://docs.adyen.com/online-payments/network-tokenization>`__. For more information, see `Forward stored
        payment details <https://docs.adyen.com/online-payments/tokenization/forward-payment-details>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/forward"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[CheckoutForwardRequest | CheckoutForwardRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[CheckoutForwardResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_stored_payment_methods(
        self,
        *,
        idempotency_key: str | None = None,
        body: StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[StoredPaymentMethodResource, RawError]:
        """Creates a token to store the shopper's payment details. This token can be used for the shopper's future
        payments.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/storedPaymentMethods"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[StoredPaymentMethodRequest | StoredPaymentMethodRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[StoredPaymentMethodResource],
            error_mapper=raw_error_response,
            request_options=request_options,
        )
