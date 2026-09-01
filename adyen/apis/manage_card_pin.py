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
from ..errors.get_public_key_error import GetPublicKeyErrorBody, get_public_key_error_mapper
from ..errors.post_pins_change_error import PostPinsChangeErrorBody, post_pins_change_error_mapper
from ..errors.post_pins_reveal_error import PostPinsRevealErrorBody, post_pins_reveal_error_mapper
from ..models.pin_change_request import PinChangeRequest, PinChangeRequestDict
from ..models.pin_change_response import PinChangeResponse
from ..models.public_key_response import PublicKeyResponse
from ..models.reveal_pin_request import RevealPinRequest, RevealPinRequestDict
from ..models.reveal_pin_response import RevealPinResponse
from ..server.server import Server


class ManageCardPin:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageCardPinWithRawResponse(client, server, auth)

    def get_public_key(
        self,
        *,
        purpose: str | None = None,
        format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicKeyResponse:
        """Get an `RSA <https://en.wikipedia.org/wiki/RSA_(cryptosystem>`__) public key to encrypt or decrypt card data.

        You need the RSA public key to generate the ``encryptedKey`` required to:
        - `Change a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/change>`__.
        - `Reveal a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/reveal>`__.
        - `Reveal a PAN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/paymentInstruments/reveal>`__.

        Args:
            purpose: The purpose of the public key. Possible values: **pinChange**, **pinReveal**, **panReveal**.
                Default value: **pinReveal**.
            format: The encoding format of public key. Possible values: **jwk**, **pem**. Default value: **pem**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.get_public_key(
            purpose=purpose, format=format, request_options=request_options
        ).unwrap()

    def post_pins_change(
        self,
        *,
        body: PinChangeRequest | PinChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinChangeResponse:
        """Changes the personal identification number (PIN) of a specified card.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Change Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.post_pins_change(body=body, request_options=request_options).unwrap()

    def post_pins_reveal(
        self,
        *,
        body: RevealPinRequest | RevealPinRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RevealPinResponse:
        """Returns an encrypted PIN block that contains the PIN of a specified card. You can use the decrypted data to
        reveal the PIN in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return self._with_raw_response.post_pins_reveal(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> ManageCardPinWithRawResponse:
        return self._with_raw_response


class AsyncManageCardPin:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageCardPinWithRawResponse(client, server, auth)

    async def get_public_key(
        self,
        *,
        purpose: str | None = None,
        format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PublicKeyResponse:
        """Get an `RSA <https://en.wikipedia.org/wiki/RSA_(cryptosystem>`__) public key to encrypt or decrypt card data.

        You need the RSA public key to generate the ``encryptedKey`` required to:
        - `Change a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/change>`__.
        - `Reveal a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/reveal>`__.
        - `Reveal a PAN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/paymentInstruments/reveal>`__.

        Args:
            purpose: The purpose of the public key. Possible values: **pinChange**, **pinReveal**, **panReveal**.
                Default value: **pinReveal**.
            format: The encoding format of public key. Possible values: **jwk**, **pem**. Default value: **pem**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_public_key(
                purpose=purpose, format=format, request_options=request_options
            )
        ).unwrap()

    async def post_pins_change(
        self,
        *,
        body: PinChangeRequest | PinChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> PinChangeResponse:
        """Changes the personal identification number (PIN) of a specified card.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Change Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (await self._with_raw_response.post_pins_change(body=body, request_options=request_options)).unwrap()

    async def post_pins_reveal(
        self,
        *,
        body: RevealPinRequest | RevealPinRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RevealPinResponse:
        """Returns an encrypted PIN block that contains the PIN of a specified card. You can use the decrypted data to
        reveal the PIN in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Unauthorized - authentication required. Forbidden - insufficient permissions to process the
                request. Unprocessable Entity - a request validation error. Internal Server Error - the server could not
                process the request. ``error`` is ``RestServiceError | RawError``."""
        return (await self._with_raw_response.post_pins_reveal(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageCardPinWithRawResponse:
        return self._with_raw_response


class ManageCardPinWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def get_public_key(
        self,
        *,
        purpose: str | None = None,
        format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicKeyResponse, GetPublicKeyErrorBody]:
        """Get an `RSA <https://en.wikipedia.org/wiki/RSA_(cryptosystem>`__) public key to encrypt or decrypt card data.

        You need the RSA public key to generate the ``encryptedKey`` required to:
        - `Change a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/change>`__.
        - `Reveal a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/reveal>`__.
        - `Reveal a PAN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/paymentInstruments/reveal>`__.

        Args:
            purpose: The purpose of the public key. Possible values: **pinChange**, **pinReveal**, **panReveal**.
                Default value: **pinReveal**.
            format: The encoding format of public key. Possible values: **jwk**, **pem**. Default value: **pem**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/publicKey"),
            query_params=[param[str | None]("purpose", purpose), param[str | None]("format", format)],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PublicKeyResponse],
            error_mapper=get_public_key_error_mapper,
            request_options=request_options,
        )

    def post_pins_change(
        self,
        *,
        body: PinChangeRequest | PinChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinChangeResponse, PostPinsChangeErrorBody]:
        """Changes the personal identification number (PIN) of a specified card.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Change Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/pins/change"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PinChangeRequest | PinChangeRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PinChangeResponse],
            error_mapper=post_pins_change_error_mapper,
            request_options=request_options,
        )

    def post_pins_reveal(
        self,
        *,
        body: RevealPinRequest | RevealPinRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RevealPinResponse, PostPinsRevealErrorBody]:
        """Returns an encrypted PIN block that contains the PIN of a specified card. You can use the decrypted data to
        reveal the PIN in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/pins/reveal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RevealPinRequest | RevealPinRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RevealPinResponse],
            error_mapper=post_pins_reveal_error_mapper,
            request_options=request_options,
        )


class AsyncManageCardPinWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def get_public_key(
        self,
        *,
        purpose: str | None = None,
        format: str | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PublicKeyResponse, GetPublicKeyErrorBody]:
        """Get an `RSA <https://en.wikipedia.org/wiki/RSA_(cryptosystem>`__) public key to encrypt or decrypt card data.

        You need the RSA public key to generate the ``encryptedKey`` required to:
        - `Change a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/change>`__.
        - `Reveal a PIN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/pins/reveal>`__.
        - `Reveal a PAN <https://docs.adyen.com/api-explorer/balanceplatform/2/post/paymentInstruments/reveal>`__.

        Args:
            purpose: The purpose of the public key. Possible values: **pinChange**, **pinReveal**, **panReveal**.
                Default value: **pinReveal**.
            format: The encoding format of public key. Possible values: **jwk**, **pem**. Default value: **pem**.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/publicKey"),
            query_params=[param[str | None]("purpose", purpose), param[str | None]("format", format)],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PublicKeyResponse],
            error_mapper=get_public_key_error_mapper,
            request_options=request_options,
        )

    async def post_pins_change(
        self,
        *,
        body: PinChangeRequest | PinChangeRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[PinChangeResponse, PostPinsChangeErrorBody]:
        """Changes the personal identification number (PIN) of a specified card.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Change Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/pins/change"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PinChangeRequest | PinChangeRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[PinChangeResponse],
            error_mapper=post_pins_change_error_mapper,
            request_options=request_options,
        )

    async def post_pins_reveal(
        self,
        *,
        body: RevealPinRequest | RevealPinRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RevealPinResponse, PostPinsRevealErrorBody]:
        """Returns an encrypted PIN block that contains the PIN of a specified card. You can use the decrypted data to
        reveal the PIN in your user interface.

        To make this request, your API credential must have the following role:
        * Bank Issuing PIN Reveal Webservice role

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/pins/reveal"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RevealPinRequest | RevealPinRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RevealPinResponse],
            error_mapper=post_pins_reveal_error_mapper,
            request_options=request_options,
        )
