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
    empty_response,
    json_body,
    json_decoder,
    param,
)
from ..errors.delete_registered_devices_id_error import (
    DeleteRegisteredDevicesIdErrorBody,
    delete_registered_devices_id_error_mapper,
)
from ..errors.get_registered_devices_error import GetRegisteredDevicesErrorBody, get_registered_devices_error_mapper
from ..errors.patch_registered_devices_device_id_associations_error import (
    PatchRegisteredDevicesDeviceIdAssociationsErrorBody,
    patch_registered_devices_device_id_associations_error_mapper,
)
from ..errors.patch_registered_devices_id_error import (
    PatchRegisteredDevicesIdErrorBody,
    patch_registered_devices_id_error_mapper,
)
from ..errors.post_registered_devices_device_id_associations_error import (
    PostRegisteredDevicesDeviceIdAssociationsErrorBody,
    post_registered_devices_device_id_associations_error_mapper,
)
from ..errors.post_registered_devices_error import PostRegisteredDevicesErrorBody, post_registered_devices_error_mapper
from ..models.association_finalise_request import AssociationFinaliseRequest, AssociationFinaliseRequestDict
from ..models.association_finalise_response import AssociationFinaliseResponse
from ..models.association_initiate_request import AssociationInitiateRequest, AssociationInitiateRequestDict
from ..models.association_initiate_response import AssociationInitiateResponse
from ..models.register_scafinal_response import RegisterScafinalResponse
from ..models.register_scarequest import RegisterScarequest, RegisterScarequestDict
from ..models.register_scaresponse import RegisterScaresponse
from ..models.search_registered_devices_response import SearchRegisteredDevicesResponse
from ..server.server import Server


class ManageScaDevices:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = ManageScaDevicesWithRawResponse(client, server, auth)

    def delete_registered_devices_id(
        self, id: str, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an SCA device from the list of registered devices of a specific payment instrument.

        Args:
            id: The unique identifier of the SCA device.
            payment_instrument_id: The unique identifier of the payment instrument linked to the SCA device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.delete_registered_devices_id(
            id, payment_instrument_id, request_options=request_options
        ).unwrap()

    def get_registered_devices(
        self,
        payment_instrument_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchRegisteredDevicesResponse:
        """Get a paginated list of the SCA devices you have currently registered for a specific payment instrument.

        Args:
            payment_instrument_id: The unique identifier of a payment instrument. It limits the returned list to SCA
                devices associated to this payment instrument.
            page_number: The index of the page to retrieve. The index of the first page is 0 (zero). Default: 0.
            page_size: The number of items to have on a page. Default: 20. Maximum: 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.get_registered_devices(
            payment_instrument_id, page_number=page_number, page_size=page_size, request_options=request_options
        ).unwrap()

    def patch_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationFinaliseRequest | AssociationFinaliseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssociationFinaliseResponse:
        """Completes an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        To complete the association, this endpoint validates the authentication data of the registered device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_registered_devices_device_id_associations(
            device_id, body=body, request_options=request_options
        ).unwrap()

    def patch_registered_devices_id(
        self,
        id: str,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterScafinalResponse:
        """Completes the registration of an SCA device by validating the authentication data of the device. You can
        register SCA devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk>`__.

        Args:
            id: The unique identifier of the SCA device. You obtain this ``id`` in the response of a
                POST&nbsp;`/registeredDevices
                <https://docs.adyen.com/api-explorer/balanceplatform/2/post/registeredDevices#responses-200-id>`__
                request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.patch_registered_devices_id(
            id, body=body, request_options=request_options
        ).unwrap()

    def post_registered_devices(
        self,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterScaresponse:
        """Initiates the registration of a user's device for Strong Customer Authentication (SCA). You can register SCA
        devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        For a successful request, the device must be eligible for SCA.

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
        return self._with_raw_response.post_registered_devices(body=body, request_options=request_options).unwrap()

    def post_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationInitiateRequest | AssociationInitiateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssociationInitiateResponse:
        """Initiates an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return self._with_raw_response.post_registered_devices_device_id_associations(
            device_id, body=body, request_options=request_options
        ).unwrap()

    @property
    def with_raw_response(self) -> ManageScaDevicesWithRawResponse:
        return self._with_raw_response


class AsyncManageScaDevices:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncManageScaDevicesWithRawResponse(client, server, auth)

    async def delete_registered_devices_id(
        self, id: str, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes an SCA device from the list of registered devices of a specific payment instrument.

        Args:
            id: The unique identifier of the SCA device.
            payment_instrument_id: The unique identifier of the payment instrument linked to the SCA device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            No Content - look at the actual response code for the status of the request.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.delete_registered_devices_id(
                id, payment_instrument_id, request_options=request_options
            )
        ).unwrap()

    async def get_registered_devices(
        self,
        payment_instrument_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SearchRegisteredDevicesResponse:
        """Get a paginated list of the SCA devices you have currently registered for a specific payment instrument.

        Args:
            payment_instrument_id: The unique identifier of a payment instrument. It limits the returned list to SCA
                devices associated to this payment instrument.
            page_number: The index of the page to retrieve. The index of the first page is 0 (zero). Default: 0.
            page_size: The number of items to have on a page. Default: 20. Maximum: 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            OK - the request has succeeded.

        Raises:
            ApiError: Bad Request - a problem reading or understanding the request. Unauthorized - authentication
                required. Forbidden - insufficient permissions to process the request. Unprocessable Entity - a request
                validation error. Internal Server Error - the server could not process the request. ``error`` is
                ``RestServiceError | RawError``."""
        return (
            await self._with_raw_response.get_registered_devices(
                payment_instrument_id, page_number=page_number, page_size=page_size, request_options=request_options
            )
        ).unwrap()

    async def patch_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationFinaliseRequest | AssociationFinaliseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssociationFinaliseResponse:
        """Completes an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        To complete the association, this endpoint validates the authentication data of the registered device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
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
            await self._with_raw_response.patch_registered_devices_device_id_associations(
                device_id, body=body, request_options=request_options
            )
        ).unwrap()

    async def patch_registered_devices_id(
        self,
        id: str,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterScafinalResponse:
        """Completes the registration of an SCA device by validating the authentication data of the device. You can
        register SCA devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk>`__.

        Args:
            id: The unique identifier of the SCA device. You obtain this ``id`` in the response of a
                POST&nbsp;`/registeredDevices
                <https://docs.adyen.com/api-explorer/balanceplatform/2/post/registeredDevices#responses-200-id>`__
                request.
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
            await self._with_raw_response.patch_registered_devices_id(id, body=body, request_options=request_options)
        ).unwrap()

    async def post_registered_devices(
        self,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> RegisterScaresponse:
        """Initiates the registration of a user's device for Strong Customer Authentication (SCA). You can register SCA
        devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        For a successful request, the device must be eligible for SCA.

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
            await self._with_raw_response.post_registered_devices(body=body, request_options=request_options)
        ).unwrap()

    async def post_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationInitiateRequest | AssociationInitiateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> AssociationInitiateResponse:
        """Initiates an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
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
            await self._with_raw_response.post_registered_devices_device_id_associations(
                device_id, body=body, request_options=request_options
            )
        ).unwrap()

    @property
    def with_raw_response(self) -> AsyncManageScaDevicesWithRawResponse:
        return self._with_raw_response


class ManageScaDevicesWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def delete_registered_devices_id(
        self, id: str, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteRegisteredDevicesIdErrorBody]:
        """Deletes an SCA device from the list of registered devices of a specific payment instrument.

        Args:
            id: The unique identifier of the SCA device.
            payment_instrument_id: The unique identifier of the payment instrument linked to the SCA device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/registeredDevices/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_registered_devices_id_error_mapper,
            request_options=request_options,
        )

    def get_registered_devices(
        self,
        payment_instrument_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchRegisteredDevicesResponse, GetRegisteredDevicesErrorBody]:
        """Get a paginated list of the SCA devices you have currently registered for a specific payment instrument.

        Args:
            payment_instrument_id: The unique identifier of a payment instrument. It limits the returned list to SCA
                devices associated to this payment instrument.
            page_number: The index of the page to retrieve. The index of the first page is 0 (zero). Default: 0.
            page_size: The number of items to have on a page. Default: 20. Maximum: 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/registeredDevices"),
            query_params=[
                param[str]("paymentInstrumentId", payment_instrument_id),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SearchRegisteredDevicesResponse],
            error_mapper=get_registered_devices_error_mapper,
            request_options=request_options,
        )

    def patch_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationFinaliseRequest | AssociationFinaliseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssociationFinaliseResponse, PatchRegisteredDevicesDeviceIdAssociationsErrorBody]:
        """Completes an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        To complete the association, this endpoint validates the authentication data of the registered device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/registeredDevices/{deviceId}/associations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociationFinaliseRequest | AssociationFinaliseRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AssociationFinaliseResponse],
            error_mapper=patch_registered_devices_device_id_associations_error_mapper,
            request_options=request_options,
        )

    def patch_registered_devices_id(
        self,
        id: str,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterScafinalResponse, PatchRegisteredDevicesIdErrorBody]:
        """Completes the registration of an SCA device by validating the authentication data of the device. You can
        register SCA devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk>`__.

        Args:
            id: The unique identifier of the SCA device. You obtain this ``id`` in the response of a
                POST&nbsp;`/registeredDevices
                <https://docs.adyen.com/api-explorer/balanceplatform/2/post/registeredDevices#responses-200-id>`__
                request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/registeredDevices/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterScarequest | RegisterScarequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RegisterScafinalResponse],
            error_mapper=patch_registered_devices_id_error_mapper,
            request_options=request_options,
        )

    def post_registered_devices(
        self,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterScaresponse, PostRegisteredDevicesErrorBody]:
        """Initiates the registration of a user's device for Strong Customer Authentication (SCA). You can register SCA
        devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        For a successful request, the device must be eligible for SCA.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/registeredDevices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterScarequest | RegisterScarequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RegisterScaresponse],
            error_mapper=post_registered_devices_error_mapper,
            request_options=request_options,
        )

    def post_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationInitiateRequest | AssociationInitiateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssociationInitiateResponse, PostRegisteredDevicesDeviceIdAssociationsErrorBody]:
        """Initiates an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/registeredDevices/{deviceId}/associations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociationInitiateRequest | AssociationInitiateRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AssociationInitiateResponse],
            error_mapper=post_registered_devices_device_id_associations_error_mapper,
            request_options=request_options,
        )


class AsyncManageScaDevicesWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def delete_registered_devices_id(
        self, id: str, payment_instrument_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteRegisteredDevicesIdErrorBody]:
        """Deletes an SCA device from the list of registered devices of a specific payment instrument.

        Args:
            id: The unique identifier of the SCA device.
            payment_instrument_id: The unique identifier of the payment instrument linked to the SCA device.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/registeredDevices/{id}"),
            path_params=[param[str]("id", id)],
            query_params=[param[str]("paymentInstrumentId", payment_instrument_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=empty_response,
            error_mapper=delete_registered_devices_id_error_mapper,
            request_options=request_options,
        )

    async def get_registered_devices(
        self,
        payment_instrument_id: str,
        *,
        page_number: int | None = None,
        page_size: int | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SearchRegisteredDevicesResponse, GetRegisteredDevicesErrorBody]:
        """Get a paginated list of the SCA devices you have currently registered for a specific payment instrument.

        Args:
            payment_instrument_id: The unique identifier of a payment instrument. It limits the returned list to SCA
                devices associated to this payment instrument.
            page_number: The index of the page to retrieve. The index of the first page is 0 (zero). Default: 0.
            page_size: The number of items to have on a page. Default: 20. Maximum: 100.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="GET",
            url_template=self._server.default13("/registeredDevices"),
            query_params=[
                param[str]("paymentInstrumentId", payment_instrument_id),
                param[int | None]("pageNumber", page_number),
                param[int | None]("pageSize", page_size),
            ],
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[SearchRegisteredDevicesResponse],
            error_mapper=get_registered_devices_error_mapper,
            request_options=request_options,
        )

    async def patch_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationFinaliseRequest | AssociationFinaliseRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssociationFinaliseResponse, PatchRegisteredDevicesDeviceIdAssociationsErrorBody]:
        """Completes an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        To complete the association, this endpoint validates the authentication data of the registered device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/registeredDevices/{deviceId}/associations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociationFinaliseRequest | AssociationFinaliseRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AssociationFinaliseResponse],
            error_mapper=patch_registered_devices_device_id_associations_error_mapper,
            request_options=request_options,
        )

    async def patch_registered_devices_id(
        self,
        id: str,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterScafinalResponse, PatchRegisteredDevicesIdErrorBody]:
        """Completes the registration of an SCA device by validating the authentication data of the device. You can
        register SCA devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk>`__.

        Args:
            id: The unique identifier of the SCA device. You obtain this ``id`` in the response of a
                POST&nbsp;`/registeredDevices
                <https://docs.adyen.com/api-explorer/balanceplatform/2/post/registeredDevices#responses-200-id>`__
                request.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/registeredDevices/{id}"),
            path_params=[param[str]("id", id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterScarequest | RegisterScarequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RegisterScafinalResponse],
            error_mapper=patch_registered_devices_id_error_mapper,
            request_options=request_options,
        )

    async def post_registered_devices(
        self,
        *,
        body: RegisterScarequest | RegisterScarequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[RegisterScaresponse, PostRegisteredDevicesErrorBody]:
        """Initiates the registration of a user's device for Strong Customer Authentication (SCA). You can register SCA
        devices for `business accounts <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or
        `Adyen-issued cards <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        For a successful request, the device must be eligible for SCA.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/registeredDevices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[RegisterScarequest | RegisterScarequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[RegisterScaresponse],
            error_mapper=post_registered_devices_error_mapper,
            request_options=request_options,
        )

    async def post_registered_devices_device_id_associations(
        self,
        device_id: str,
        *,
        body: AssociationInitiateRequest | AssociationInitiateRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[AssociationInitiateResponse, PostRegisteredDevicesDeviceIdAssociationsErrorBody]:
        """Initiates an association between a user's registered SCA device and an Adyen resource. For example, you can
        associate an SCA device with additional `business accounts
        <https://docs.adyen.com/platforms/business-accounts/sca/register-devices>`__ or `Adyen-issued cards
        <https://docs.adyen.com/issuing/3d-secure/oob-auth-sdk/register-devices>`__.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/registeredDevices/{deviceId}/associations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[AssociationInitiateRequest | AssociationInitiateRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.client_key, self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[AssociationInitiateResponse],
            error_mapper=post_registered_devices_device_id_associations_error_mapper,
            request_options=request_options,
        )
