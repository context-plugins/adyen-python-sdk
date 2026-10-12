from __future__ import annotations

from uuid import UUID, uuid4

from ..core import (
    ApiResult,
    AsyncRawClient,
    BaseRawResponse,
    RawClient,
    RequestOptionsOrDict,
    async_empty_response,
    async_json_decoder,
    empty_response,
    json_body,
    json_decoder,
    param,
    unwrap,
)
from ..errors.delete_sca_devices_device_id_error import (
    DeleteScaDevicesDeviceIdErrorBody,
    delete_sca_devices_device_id_error_mapper,
)
from ..errors.patch_sca_devices_device_id_error import (
    PatchScaDevicesDeviceIdErrorBody,
    patch_sca_devices_device_id_error_mapper,
)
from ..errors.post_sca_devices_device_id_sca_associations_error import (
    PostScaDevicesDeviceIdScaAssociationsErrorBody,
    post_sca_devices_device_id_sca_associations_error_mapper,
)
from ..errors.post_sca_devices_error import PostScaDevicesErrorBody, post_sca_devices_error_mapper
from ..models.begin_sca_device_registration_request import (
    BeginScaDeviceRegistrationRequest,
    BeginScaDeviceRegistrationRequestDict,
)
from ..models.begin_sca_device_registration_response import BeginScaDeviceRegistrationResponse
from ..models.finish_sca_device_registration_request import (
    FinishScaDeviceRegistrationRequest,
    FinishScaDeviceRegistrationRequestDict,
)
from ..models.finish_sca_device_registration_response import FinishScaDeviceRegistrationResponse
from ..models.submit_sca_association_request import SubmitScaAssociationRequest, SubmitScaAssociationRequestDict
from ..models.submit_sca_association_response import SubmitScaAssociationResponse
from ..server.server import Server


class ScaDeviceManagement:
    def __init__(self, client: RawClient, server: Server) -> None:
        self._with_raw_response = ScaDeviceManagementWithRawResponse(client, server)

    def delete_sca_devices_device_id(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The device was deleted successfully.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.delete_sca_devices_device_id(device_id, request_options=request_options))

    def patch_sca_devices_device_id(
        self,
        device_id: str,
        *,
        body: FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinishScaDeviceRegistrationResponse:
        """Finishes the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - Device registration was completed successfully.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.patch_sca_devices_device_id(device_id, body=body, request_options=request_options)
        )

    def post_sca_devices(
        self,
        *,
        body: BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BeginScaDeviceRegistrationResponse:
        """Begins the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - A device resource is created. The initial step of registration is complete, but the device isn't
            ready for use.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Unprocessable
                entity - A request validation error. Internal Server Error - The server could not process the request.
                ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(self._with_raw_response.post_sca_devices(body=body, request_options=request_options))

    def post_sca_devices_device_id_sca_associations(
        self,
        device_id: str,
        *,
        body: SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubmitScaAssociationResponse:
        """Creates an association between an SCA-enabled device and an entity, such as an account holder. This action
        does not guarantee the association is immediately ready for use; its status may be ``pendingApproval`` if the
        account holder has existing devices.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - Association created.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable Entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            self._with_raw_response.post_sca_devices_device_id_sca_associations(
                device_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> ScaDeviceManagementWithRawResponse:
        return self._with_raw_response


class AsyncScaDeviceManagement:
    def __init__(self, client: AsyncRawClient, server: Server) -> None:
        self._with_raw_response = AsyncScaDeviceManagementWithRawResponse(client, server)

    async def delete_sca_devices_device_id(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> None:
        """Deletes a Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            No Content - The device was deleted successfully.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.delete_sca_devices_device_id(device_id, request_options=request_options)
        )

    async def patch_sca_devices_device_id(
        self,
        device_id: str,
        *,
        body: FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> FinishScaDeviceRegistrationResponse:
        """Finishes the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            OK - Device registration was completed successfully.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.patch_sca_devices_device_id(
                device_id, body=body, request_options=request_options
            ),
        )

    async def post_sca_devices(
        self,
        *,
        body: BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> BeginScaDeviceRegistrationResponse:
        """Begins the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - A device resource is created. The initial step of registration is complete, but the device isn't
            ready for use.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Unprocessable
                entity - A request validation error. Internal Server Error - The server could not process the request.
                ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(await self._with_raw_response.post_sca_devices(body=body, request_options=request_options))

    async def post_sca_devices_device_id_sca_associations(
        self,
        device_id: str,
        *,
        body: SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> SubmitScaAssociationResponse:
        """Creates an association between an SCA-enabled device and an entity, such as an account holder. This action
        does not guarantee the association is immediately ready for use; its status may be ``pendingApproval`` if the
        account holder has existing devices.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            Created - Association created.

        Raises:
            ApiError: Bad Request - The request contains invalid input and fails validation. Unauthorized -
                Authentication required. Forbidden - Insufficient permissions to process the request. Not Found - Device
                not found. Unprocessable Entity - A request validation error. Internal Server Error - The server could
                not process the request. ``error`` is ``DefaultErrorResponseEntity | RawError``."""
        return unwrap(
            await self._with_raw_response.post_sca_devices_device_id_sca_associations(
                device_id, body=body, request_options=request_options
            ),
        )

    @property
    def with_raw_response(self) -> AsyncScaDeviceManagementWithRawResponse:
        return self._with_raw_response


class ScaDeviceManagementWithRawResponse(BaseRawResponse[RawClient, Server]):
    def delete_sca_devices_device_id(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteScaDevicesDeviceIdErrorBody]:
        """Deletes a Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/scaDevices/{deviceId}"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=empty_response,
            error_mapper=delete_sca_devices_device_id_error_mapper,
            request_options=request_options,
        )

    def patch_sca_devices_device_id(
        self,
        device_id: str,
        *,
        body: FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinishScaDeviceRegistrationResponse, PatchScaDevicesDeviceIdErrorBody]:
        """Finishes the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/scaDevices/{deviceId}"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None](body),
            decoder=json_decoder[FinishScaDeviceRegistrationResponse],
            error_mapper=patch_sca_devices_device_id_error_mapper,
            request_options=request_options,
        )

    def post_sca_devices(
        self,
        *,
        body: BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BeginScaDeviceRegistrationResponse, PostScaDevicesErrorBody]:
        """Begins the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/scaDevices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None](body),
            decoder=json_decoder[BeginScaDeviceRegistrationResponse],
            error_mapper=post_sca_devices_error_mapper,
            request_options=request_options,
        )

    def post_sca_devices_device_id_sca_associations(
        self,
        device_id: str,
        *,
        body: SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubmitScaAssociationResponse, PostScaDevicesDeviceIdScaAssociationsErrorBody]:
        """Creates an association between an SCA-enabled device and an entity, such as an account holder. This action
        does not guarantee the association is immediately ready for use; its status may be ``pendingApproval`` if the
        account holder has existing devices.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/scaDevices/{deviceId}/scaAssociations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None](body),
            decoder=json_decoder[SubmitScaAssociationResponse],
            error_mapper=post_sca_devices_device_id_sca_associations_error_mapper,
            request_options=request_options,
        )


class AsyncScaDeviceManagementWithRawResponse(BaseRawResponse[AsyncRawClient, Server]):
    async def delete_sca_devices_device_id(
        self, device_id: str, *, request_options: RequestOptionsOrDict | None = None
    ) -> ApiResult[None, DeleteScaDevicesDeviceIdErrorBody]:
        """Deletes a Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device to delete.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="DELETE",
            url_template=self._server.default13("/scaDevices/{deviceId}"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            decoder=async_empty_response,
            error_mapper=delete_sca_devices_device_id_error_mapper,
            request_options=request_options,
        )

    async def patch_sca_devices_device_id(
        self,
        device_id: str,
        *,
        body: FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[FinishScaDeviceRegistrationResponse, PatchScaDevicesDeviceIdErrorBody]:
        """Finishes the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="PATCH",
            url_template=self._server.default13("/scaDevices/{deviceId}"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[FinishScaDeviceRegistrationRequest | FinishScaDeviceRegistrationRequestDict | None](body),
            decoder=async_json_decoder[FinishScaDeviceRegistrationResponse],
            error_mapper=patch_sca_devices_device_id_error_mapper,
            request_options=request_options,
        )

    async def post_sca_devices(
        self,
        *,
        body: BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[BeginScaDeviceRegistrationResponse, PostScaDevicesErrorBody]:
        """Begins the registration process for a new Strong Customer Authentication (SCA) device.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/scaDevices"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[BeginScaDeviceRegistrationRequest | BeginScaDeviceRegistrationRequestDict | None](body),
            decoder=async_json_decoder[BeginScaDeviceRegistrationResponse],
            error_mapper=post_sca_devices_error_mapper,
            request_options=request_options,
        )

    async def post_sca_devices_device_id_sca_associations(
        self,
        device_id: str,
        *,
        body: SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[SubmitScaAssociationResponse, PostScaDevicesDeviceIdScaAssociationsErrorBody]:
        """Creates an association between an SCA-enabled device and an entity, such as an account holder. This action
        does not guarantee the association is immediately ready for use; its status may be ``pendingApproval`` if the
        account holder has existing devices.

        Args:
            device_id: The unique identifier of the SCA device that you are associating with a resource.
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout, extra headers, or its retry
                count and statuses.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default13("/scaDevices/{deviceId}/scaAssociations"),
            path_params=[param[str]("deviceId", device_id)],
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[SubmitScaAssociationRequest | SubmitScaAssociationRequestDict | None](body),
            decoder=async_json_decoder[SubmitScaAssociationResponse],
            error_mapper=post_sca_devices_device_id_sca_associations_error_mapper,
            request_options=request_options,
        )
