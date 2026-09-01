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
from ..errors.post_check_account_holder_error import (
    PostCheckAccountHolderErrorBody,
    post_check_account_holder_error_mapper,
)
from ..errors.post_delete_bank_accounts_error import (
    PostDeleteBankAccountsErrorBody,
    post_delete_bank_accounts_error_mapper,
)
from ..errors.post_delete_legal_arrangements_error import (
    PostDeleteLegalArrangementsErrorBody,
    post_delete_legal_arrangements_error_mapper,
)
from ..errors.post_delete_payout_methods_error import (
    PostDeletePayoutMethodsErrorBody,
    post_delete_payout_methods_error_mapper,
)
from ..errors.post_delete_shareholders_error import (
    PostDeleteShareholdersErrorBody,
    post_delete_shareholders_error_mapper,
)
from ..errors.post_delete_signatories_error import PostDeleteSignatoriesErrorBody, post_delete_signatories_error_mapper
from ..errors.post_get_uploaded_documents_error import (
    PostGetUploadedDocumentsErrorBody,
    post_get_uploaded_documents_error_mapper,
)
from ..errors.post_upload_document_error import PostUploadDocumentErrorBody, post_upload_document_error_mapper
from ..models.delete_bank_account_request import DeleteBankAccountRequest, DeleteBankAccountRequestDict
from ..models.delete_legal_arrangement_request import DeleteLegalArrangementRequest, DeleteLegalArrangementRequestDict
from ..models.delete_payout_method_request import DeletePayoutMethodRequest, DeletePayoutMethodRequestDict
from ..models.delete_shareholder_request import DeleteShareholderRequest, DeleteShareholderRequestDict
from ..models.delete_signatories_request import DeleteSignatoriesRequest, DeleteSignatoriesRequestDict
from ..models.generic_response import GenericResponse
from ..models.get_uploaded_documents_request import GetUploadedDocumentsRequest, GetUploadedDocumentsRequestDict
from ..models.get_uploaded_documents_response import GetUploadedDocumentsResponse
from ..models.perform_verification_request import PerformVerificationRequest, PerformVerificationRequestDict
from ..models.update_account_holder_response import UpdateAccountHolderResponse
from ..models.upload_document_request import UploadDocumentRequest, UploadDocumentRequestDict
from ..server.server import Server


class Verification:
    def __init__(self, client: RawClient, server: Server, auth: AuthSchemes) -> None:
        self._with_raw_response = VerificationWithRawResponse(client, server, auth)

    def post_check_account_holder(
        self,
        *,
        body: PerformVerificationRequest | PerformVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Triggers the verification of an account holder even if the checks are not yet required for the volume that
        they are currently processing.

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
        return self._with_raw_response.post_check_account_holder(body=body, request_options=request_options).unwrap()

    def post_delete_bank_accounts(
        self,
        *,
        body: DeleteBankAccountRequest | DeleteBankAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes bank accounts associated with an account holder.

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
        return self._with_raw_response.post_delete_bank_accounts(body=body, request_options=request_options).unwrap()

    def post_delete_legal_arrangements(
        self,
        *,
        body: DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

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
        return self._with_raw_response.post_delete_legal_arrangements(
            body=body, request_options=request_options
        ).unwrap()

    def post_delete_payout_methods(
        self,
        *,
        body: DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes payout methods associated with an account holder.

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
        return self._with_raw_response.post_delete_payout_methods(body=body, request_options=request_options).unwrap()

    def post_delete_shareholders(
        self,
        *,
        body: DeleteShareholderRequest | DeleteShareholderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes shareholders associated with an account holder.

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
        return self._with_raw_response.post_delete_shareholders(body=body, request_options=request_options).unwrap()

    def post_delete_signatories(
        self,
        *,
        body: DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes signatories associated with an account holder.

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
        return self._with_raw_response.post_delete_signatories(body=body, request_options=request_options).unwrap()

    def post_get_uploaded_documents(
        self,
        *,
        body: GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetUploadedDocumentsResponse:
        """Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the
        `verification process <https://docs.adyen.com/classic-platforms/verification-process>`__.

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
        return self._with_raw_response.post_get_uploaded_documents(body=body, request_options=request_options).unwrap()

    def post_upload_document(
        self,
        *,
        body: UploadDocumentRequest | UploadDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountHolderResponse:
        """Uploads a document for an account holder. Adyen uses the documents during the `verification process
        <https://docs.adyen.com/classic-platforms/verification-process>`__.

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
        return self._with_raw_response.post_upload_document(body=body, request_options=request_options).unwrap()

    @property
    def with_raw_response(self) -> VerificationWithRawResponse:
        return self._with_raw_response


class AsyncVerification:
    def __init__(self, client: AsyncRawClient, server: Server, auth: AsyncAuthSchemes) -> None:
        self._with_raw_response = AsyncVerificationWithRawResponse(client, server, auth)

    async def post_check_account_holder(
        self,
        *,
        body: PerformVerificationRequest | PerformVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Triggers the verification of an account holder even if the checks are not yet required for the volume that
        they are currently processing.

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
            await self._with_raw_response.post_check_account_holder(body=body, request_options=request_options)
        ).unwrap()

    async def post_delete_bank_accounts(
        self,
        *,
        body: DeleteBankAccountRequest | DeleteBankAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes bank accounts associated with an account holder.

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
            await self._with_raw_response.post_delete_bank_accounts(body=body, request_options=request_options)
        ).unwrap()

    async def post_delete_legal_arrangements(
        self,
        *,
        body: DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

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
            await self._with_raw_response.post_delete_legal_arrangements(body=body, request_options=request_options)
        ).unwrap()

    async def post_delete_payout_methods(
        self,
        *,
        body: DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes payout methods associated with an account holder.

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
            await self._with_raw_response.post_delete_payout_methods(body=body, request_options=request_options)
        ).unwrap()

    async def post_delete_shareholders(
        self,
        *,
        body: DeleteShareholderRequest | DeleteShareholderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes shareholders associated with an account holder.

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
            await self._with_raw_response.post_delete_shareholders(body=body, request_options=request_options)
        ).unwrap()

    async def post_delete_signatories(
        self,
        *,
        body: DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GenericResponse:
        """Deletes signatories associated with an account holder.

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
            await self._with_raw_response.post_delete_signatories(body=body, request_options=request_options)
        ).unwrap()

    async def post_get_uploaded_documents(
        self,
        *,
        body: GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> GetUploadedDocumentsResponse:
        """Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the
        `verification process <https://docs.adyen.com/classic-platforms/verification-process>`__.

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
            await self._with_raw_response.post_get_uploaded_documents(body=body, request_options=request_options)
        ).unwrap()

    async def post_upload_document(
        self,
        *,
        body: UploadDocumentRequest | UploadDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> UpdateAccountHolderResponse:
        """Uploads a document for an account holder. Adyen uses the documents during the `verification process
        <https://docs.adyen.com/classic-platforms/verification-process>`__.

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
        return (await self._with_raw_response.post_upload_document(body=body, request_options=request_options)).unwrap()

    @property
    def with_raw_response(self) -> AsyncVerificationWithRawResponse:
        return self._with_raw_response


class VerificationWithRawResponse(SecuredRawResponse[RawClient, Server, AuthSchemes]):
    def post_check_account_holder(
        self,
        *,
        body: PerformVerificationRequest | PerformVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostCheckAccountHolderErrorBody]:
        """Triggers the verification of an account holder even if the checks are not yet required for the volume that
        they are currently processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/checkAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PerformVerificationRequest | PerformVerificationRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_check_account_holder_error_mapper,
            request_options=request_options,
        )

    def post_delete_bank_accounts(
        self,
        *,
        body: DeleteBankAccountRequest | DeleteBankAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteBankAccountsErrorBody]:
        """Deletes bank accounts associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteBankAccounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteBankAccountRequest | DeleteBankAccountRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_bank_accounts_error_mapper,
            request_options=request_options,
        )

    def post_delete_legal_arrangements(
        self,
        *,
        body: DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteLegalArrangementsErrorBody]:
        """Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteLegalArrangements"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_legal_arrangements_error_mapper,
            request_options=request_options,
        )

    def post_delete_payout_methods(
        self,
        *,
        body: DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeletePayoutMethodsErrorBody]:
        """Deletes payout methods associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deletePayoutMethods"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_payout_methods_error_mapper,
            request_options=request_options,
        )

    def post_delete_shareholders(
        self,
        *,
        body: DeleteShareholderRequest | DeleteShareholderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteShareholdersErrorBody]:
        """Deletes shareholders associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteShareholders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteShareholderRequest | DeleteShareholderRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_shareholders_error_mapper,
            request_options=request_options,
        )

    def post_delete_signatories(
        self,
        *,
        body: DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteSignatoriesErrorBody]:
        """Deletes signatories associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteSignatories"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_signatories_error_mapper,
            request_options=request_options,
        )

    def post_get_uploaded_documents(
        self,
        *,
        body: GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetUploadedDocumentsResponse, PostGetUploadedDocumentsErrorBody]:
        """Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the
        `verification process <https://docs.adyen.com/classic-platforms/verification-process>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getUploadedDocuments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetUploadedDocumentsResponse],
            error_mapper=post_get_uploaded_documents_error_mapper,
            request_options=request_options,
        )

    def post_upload_document(
        self,
        *,
        body: UploadDocumentRequest | UploadDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountHolderResponse, PostUploadDocumentErrorBody]:
        """Uploads a document for an account holder. Adyen uses the documents during the `verification process
        <https://docs.adyen.com/classic-platforms/verification-process>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/uploadDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadDocumentRequest | UploadDocumentRequestDict | None](body),
            auth_scheme=AnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountHolderResponse],
            error_mapper=post_upload_document_error_mapper,
            request_options=request_options,
        )


class AsyncVerificationWithRawResponse(SecuredRawResponse[AsyncRawClient, Server, AsyncAuthSchemes]):
    async def post_check_account_holder(
        self,
        *,
        body: PerformVerificationRequest | PerformVerificationRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostCheckAccountHolderErrorBody]:
        """Triggers the verification of an account holder even if the checks are not yet required for the volume that
        they are currently processing.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/checkAccountHolder"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[PerformVerificationRequest | PerformVerificationRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_check_account_holder_error_mapper,
            request_options=request_options,
        )

    async def post_delete_bank_accounts(
        self,
        *,
        body: DeleteBankAccountRequest | DeleteBankAccountRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteBankAccountsErrorBody]:
        """Deletes bank accounts associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteBankAccounts"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteBankAccountRequest | DeleteBankAccountRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_bank_accounts_error_mapper,
            request_options=request_options,
        )

    async def post_delete_legal_arrangements(
        self,
        *,
        body: DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteLegalArrangementsErrorBody]:
        """Deletes legal arrangements and/or legal arrangement entities associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteLegalArrangements"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteLegalArrangementRequest | DeleteLegalArrangementRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_legal_arrangements_error_mapper,
            request_options=request_options,
        )

    async def post_delete_payout_methods(
        self,
        *,
        body: DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeletePayoutMethodsErrorBody]:
        """Deletes payout methods associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deletePayoutMethods"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeletePayoutMethodRequest | DeletePayoutMethodRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_payout_methods_error_mapper,
            request_options=request_options,
        )

    async def post_delete_shareholders(
        self,
        *,
        body: DeleteShareholderRequest | DeleteShareholderRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteShareholdersErrorBody]:
        """Deletes shareholders associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteShareholders"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteShareholderRequest | DeleteShareholderRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_shareholders_error_mapper,
            request_options=request_options,
        )

    async def post_delete_signatories(
        self,
        *,
        body: DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GenericResponse, PostDeleteSignatoriesErrorBody]:
        """Deletes signatories associated with an account holder.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/deleteSignatories"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[DeleteSignatoriesRequest | DeleteSignatoriesRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GenericResponse],
            error_mapper=post_delete_signatories_error_mapper,
            request_options=request_options,
        )

    async def post_get_uploaded_documents(
        self,
        *,
        body: GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[GetUploadedDocumentsResponse, PostGetUploadedDocumentsErrorBody]:
        """Returns documents that were previously uploaded for an account holder. Adyen uses the documents during the
        `verification process <https://docs.adyen.com/classic-platforms/verification-process>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/getUploadedDocuments"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[GetUploadedDocumentsRequest | GetUploadedDocumentsRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[GetUploadedDocumentsResponse],
            error_mapper=post_get_uploaded_documents_error_mapper,
            request_options=request_options,
        )

    async def post_upload_document(
        self,
        *,
        body: UploadDocumentRequest | UploadDocumentRequestDict | None = None,
        request_options: RequestOptionsOrDict | None = None,
    ) -> ApiResult[UpdateAccountHolderResponse, PostUploadDocumentErrorBody]:
        """Uploads a document for an account holder. Adyen uses the documents during the `verification process
        <https://docs.adyen.com/classic-platforms/verification-process>`__.

        Args:
            body: The request body.
            request_options: Per-call overrides for this one request, such as a timeout or extra headers.

        Returns:
            An ``ApiResult`` holding the deserialized response or the error body."""
        return await self._client.execute(
            http_method="POST",
            url_template=self._server.default10("/uploadDocument"),
            headers=[param[UUID]("Idempotency-Key", uuid4())],
            body=json_body[UploadDocumentRequest | UploadDocumentRequestDict | None](body),
            auth_scheme=AsyncAnySchemes(self._auth.basic_auth, self._auth.api_key_auth),
            decoder=json_decoder[UpdateAccountHolderResponse],
            error_mapper=post_upload_document_error_mapper,
            request_options=request_options,
        )
