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
    json_body,
    json_decoder,
    param,
    raw_error_response,
)
from ..errors.post_origin_keys_error import PostOriginKeysErrorBody, post_origin_keys_error_mapper
from ..errors.post_paypal_update_order_error import (
    PostPaypalUpdateOrderErrorBody,
    post_paypal_update_order_error_mapper,
)
from ..errors.post_validate_shopper_id_error import (
    PostValidateShopperIdErrorBody,
    post_validate_shopper_id_error_mapper,
)
from ..models.apple_pay_session_request import ApplePaySessionRequest, ApplePaySessionRequestDict
from ..models.apple_pay_session_response import ApplePaySessionResponse
from ..models.paypal_update_order_request import PaypalUpdateOrderRequest, PaypalUpdateOrderRequestDict
from ..models.paypal_update_order_response import PaypalUpdateOrderResponse
from ..models.utility_request import UtilityRequest, UtilityRequestDict
from ..models.utility_response import UtilityResponse
from ..models.validate_shopper_id_request import ValidateShopperIdRequest, ValidateShopperIdRequestDict
from ..models.validate_shopper_id_response import ValidateShopperIdResponse
from ..server.server import Server


class Utility:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = UtilityWithRawResponse(client, server, auth)

    def post_apple_pay_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: ApplePaySessionRequest | ApplePaySessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApplePaySessionResponse:
        """You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay
        certificate.

        The endpoint returns the Apple Pay session data which you need to complete the `Apple Pay session validation
        <https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return self._with_raw_response.post_apple_pay_sessions(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_origin_keys(
        self,
        *,
        idempotency_key: str | None = None,
        body: UtilityRequest | UtilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UtilityResponse:
        """This operation takes the origin domains and returns a JSON object containing the corresponding origin keys
        for the domains.
        > If you're still using origin key for your Web Drop-in or Components integration, we recommend `switching to
            client key
            <https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key>`__.
            This allows you to use a single key for all origins, add or remove origins without generating a new key, and
            detect the card type from the number entered in your payment form.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_origin_keys(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_paypal_update_order(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaypalUpdateOrderResponse:
        """Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated
        amount and delivery methods based on the delivery address.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return self._with_raw_response.post_paypal_update_order(
            idempotency_key=idempotency_key, body=body, request_options=request_options
        ).unwrap()

    def post_validate_shopper_id(
        self,
        body: ValidateShopperIdRequest | ValidateShopperIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ValidateShopperIdResponse:
        """Validates the shopperId.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``CheckoutErrorResponseEntity | RawError``."""
        return self._with_raw_response.post_validate_shopper_id(body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> UtilityWithRawResponse:
        return self._with_raw_response


class AsyncUtility:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncUtilityWithRawResponse(client, server, auth)

    async def post_apple_pay_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: ApplePaySessionRequest | ApplePaySessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApplePaySessionResponse:
        """You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay
        certificate.

        The endpoint returns the Apple Pay session data which you need to complete the `Apple Pay session validation
        <https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: If the API responds with an error status code. ``error`` is ``RawError``."""
        return (
            await self._with_raw_response.post_apple_pay_sessions(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_origin_keys(
        self,
        *,
        idempotency_key: str | None = None,
        body: UtilityRequest | UtilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UtilityResponse:
        """This operation takes the origin domains and returns a JSON object containing the corresponding origin keys
        for the domains.
        > If you're still using origin key for your Web Drop-in or Components integration, we recommend `switching to
            client key
            <https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key>`__.
            This allows you to use a single key for all origins, add or remove origins without generating a new key, and
            detect the card type from the number entered in your payment form.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_origin_keys(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_paypal_update_order(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PaypalUpdateOrderResponse:
        """Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated
        amount and delivery methods based on the delivery address.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``ServiceError | RawError``."""
        return (
            await self._with_raw_response.post_paypal_update_order(
                idempotency_key=idempotency_key, body=body, request_options=request_options
            )
        ).unwrap()

    async def post_validate_shopper_id(
        self,
        body: ValidateShopperIdRequest | ValidateShopperIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ValidateShopperIdResponse:
        """Validates the shopperId.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``CheckoutErrorResponseEntity | RawError``."""
        return (await self._with_raw_response.post_validate_shopper_id(body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncUtilityWithRawResponse:
        return self._with_raw_response


class UtilityWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_apple_pay_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: ApplePaySessionRequest | ApplePaySessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApplePaySessionResponse, RawError]:
        """You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay
        certificate.

        The endpoint returns the Apple Pay session data which you need to complete the `Apple Pay session validation
        <https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/applePay/sessions"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[ApplePaySessionRequest | ApplePaySessionRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApplePaySessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    def post_origin_keys(
        self,
        *,
        idempotency_key: str | None = None,
        body: UtilityRequest | UtilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UtilityResponse, PostOriginKeysErrorBody]:
        """This operation takes the origin domains and returns a JSON object containing the corresponding origin keys
        for the domains.
        > If you're still using origin key for your Web Drop-in or Components integration, we recommend `switching to
            client key
            <https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key>`__.
            This allows you to use a single key for all origins, add or remove origins without generating a new key, and
            detect the card type from the number entered in your payment form.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/originKeys"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[UtilityRequest | UtilityRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UtilityResponse],
            error_mapper=post_origin_keys_error_mapper,
            request_options=request_options,
        )

    def post_paypal_update_order(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaypalUpdateOrderResponse, PostPaypalUpdateOrderErrorBody]:
        """Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated
        amount and delivery methods based on the delivery address.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paypal/updateOrder"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaypalUpdateOrderResponse],
            error_mapper=post_paypal_update_order_error_mapper,
            request_options=request_options,
        )

    def post_validate_shopper_id(
        self,
        body: ValidateShopperIdRequest | ValidateShopperIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ValidateShopperIdResponse, PostValidateShopperIdErrorBody]:
        """Validates the shopperId.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default("/validateShopperId"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ValidateShopperIdRequest | ValidateShopperIdRequestDict](body),
            decoder=json_decoder[ValidateShopperIdResponse],
            error_mapper=post_validate_shopper_id_error_mapper,
            request_options=request_options,
        )


class AsyncUtilityWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_apple_pay_sessions(
        self,
        *,
        idempotency_key: str | None = None,
        body: ApplePaySessionRequest | ApplePaySessionRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ApplePaySessionResponse, RawError]:
        """You need to use this endpoint if you have an API-only integration with Apple Pay which uses Adyen's Apple Pay
        certificate.

        The endpoint returns the Apple Pay session data which you need to complete the `Apple Pay session validation
        <https://docs.adyen.com/payment-methods/apple-pay/api-only?tab=adyen-certificate-validation_1#complete-apple-pay-session-validation>`__.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/applePay/sessions"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[ApplePaySessionRequest | ApplePaySessionRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[ApplePaySessionResponse],
            error_mapper=raw_error_response,
            request_options=request_options,
        )

    async def post_origin_keys(
        self,
        *,
        idempotency_key: str | None = None,
        body: UtilityRequest | UtilityRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UtilityResponse, PostOriginKeysErrorBody]:
        """This operation takes the origin domains and returns a JSON object containing the corresponding origin keys
        for the domains.
        > If you're still using origin key for your Web Drop-in or Components integration, we recommend `switching to
            client key
            <https://docs.adyen.com/development-resources/client-side-authentication/migrate-from-origin-key-to-client-key>`__.
            This allows you to use a single key for all origins, add or remove origins without generating a new key, and
            detect the card type from the number entered in your payment form.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/originKeys"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[UtilityRequest | UtilityRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UtilityResponse],
            error_mapper=post_origin_keys_error_mapper,
            request_options=request_options,
        )

    async def post_paypal_update_order(
        self,
        *,
        idempotency_key: str | None = None,
        body: PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PaypalUpdateOrderResponse, PostPaypalUpdateOrderErrorBody]:
        """Updates the order for PayPal Express Checkout. This can be used to update the PayPal lightbox with an updated
        amount and delivery methods based on the delivery address.

        Args:
            idempotency_key: A unique identifier for the message with a maximum of 64 characters (we recommend a UUID).
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/paypal/updateOrder"),
            headers=[param[str | None]("Idempotency-Key", idempotency_key)],
            body=json_body[PaypalUpdateOrderRequest | PaypalUpdateOrderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PaypalUpdateOrderResponse],
            error_mapper=post_paypal_update_order_error_mapper,
            request_options=request_options,
        )

    async def post_validate_shopper_id(
        self,
        body: ValidateShopperIdRequest | ValidateShopperIdRequestDict,
        *,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[ValidateShopperIdResponse, PostValidateShopperIdErrorBody]:
        """Validates the shopperId.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default("/validateShopperId"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[ValidateShopperIdRequest | ValidateShopperIdRequestDict](body),
            decoder=json_decoder[ValidateShopperIdResponse],
            error_mapper=post_validate_shopper_id_error_mapper,
            request_options=request_options,
        )
