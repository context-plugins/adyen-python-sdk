from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .abort_request2 import AbortRequest2, AbortRequest2Dict
from .admin_request2 import AdminRequest2, AdminRequest2Dict
from .balance_inquiry_request2 import BalanceInquiryRequest2, BalanceInquiryRequest2Dict
from .card_acquisition_request2 import CardAcquisitionRequest2, CardAcquisitionRequest2Dict
from .card_reader_apdurequest2 import CardReaderApdurequest2, CardReaderApdurequest2Dict
from .diagnosis_request2 import DiagnosisRequest2, DiagnosisRequest2Dict
from .display_request2 import DisplayRequest2, DisplayRequest2Dict
from .enable_service_request2 import EnableServiceRequest2, EnableServiceRequest2Dict
from .event_notification2 import EventNotification2, EventNotification2Dict
from .get_totals_request2 import GetTotalsRequest2, GetTotalsRequest2Dict
from .input_request2 import InputRequest2, InputRequest2Dict
from .input_update2 import InputUpdate2, InputUpdate2Dict
from .login_request2 import LoginRequest2, LoginRequest2Dict
from .logout_request2 import LogoutRequest2, LogoutRequest2Dict
from .message_header import MessageHeader, MessageHeaderDict
from .payment_request21 import PaymentRequest21, PaymentRequest21Dict
from .print_request2 import PrintRequest2, PrintRequest2Dict
from .reconciliation_request2 import ReconciliationRequest2, ReconciliationRequest2Dict
from .reversal_request2 import ReversalRequest2, ReversalRequest2Dict
from .stored_value_request2 import StoredValueRequest2, StoredValueRequest2Dict
from .transaction_status_request2 import TransactionStatusRequest2, TransactionStatusRequest2Dict


class SaleToPoirequest(SdkBaseModel):
    """The SaleToPOIRequest message pair is a container for the request message content. It contains a MessageHeader and
    a message body."""

    message_header: MessageHeader = Field(alias="MessageHeader")
    """Message header of the Sale to POI protocol message. It conveys Information related to the Sale to POI protocol
    management."""

    abort_request: Optional[AbortRequest2] = Field(default=UNSET, alias="AbortRequest")
    """Content of the Abort Request message."""

    balance_inquiry_request: Optional[BalanceInquiryRequest2] = Field(default=UNSET, alias="BalanceInquiryRequest")
    """Content of the Balance Inquiry Request message."""

    card_acquisition_request: Optional[CardAcquisitionRequest2] = Field(default=UNSET, alias="CardAcquisitionRequest")
    """Content of the Card Acquisition Request message."""

    admin_request: Optional[AdminRequest2] = Field(default=UNSET, alias="AdminRequest")
    """Content of the Admin Request message."""

    diagnosis_request: Optional[DiagnosisRequest2] = Field(default=UNSET, alias="DiagnosisRequest")
    """Content of the Diagnosis Request message."""

    display_request: Optional[DisplayRequest2] = Field(default=UNSET, alias="DisplayRequest")
    """Content of the Display Request message."""

    enable_service_request: Optional[EnableServiceRequest2] = Field(default=UNSET, alias="EnableServiceRequest")
    """Content of the Enable Service Request message."""

    event_notification: Optional[EventNotification2] = Field(default=UNSET, alias="EventNotification")
    """Content of the EventNotification message."""

    get_totals_request: Optional[GetTotalsRequest2] = Field(default=UNSET, alias="GetTotalsRequest")
    """Content of the Get Totals Request message."""

    input_request: Optional[InputRequest2] = Field(default=UNSET, alias="InputRequest")
    """Content of the Input Request message."""

    input_update: Optional[InputUpdate2] = Field(default=UNSET, alias="InputUpdate")
    """Content of the Input Update message."""

    login_request: Optional[LoginRequest2] = Field(default=UNSET, alias="LoginRequest")
    """Content of the Login Request message."""

    logout_request: Optional[LogoutRequest2] = Field(default=UNSET, alias="LogoutRequest")
    """Content of the Logout Request message."""

    payment_request: Optional[PaymentRequest21] = Field(default=UNSET, alias="PaymentRequest")
    """Content of the Payment Request message."""

    print_request: Optional[PrintRequest2] = Field(default=UNSET, alias="PrintRequest")
    """Content of the Print Request message."""

    card_reader_apdu_request: Optional[CardReaderApdurequest2] = Field(default=UNSET, alias="CardReaderAPDURequest")
    """Content of the Card Reader APDU Request message."""

    reconciliation_request: Optional[ReconciliationRequest2] = Field(default=UNSET, alias="ReconciliationRequest")
    """Content of the Reconciliation Request message."""

    reversal_request: Optional[ReversalRequest2] = Field(default=UNSET, alias="ReversalRequest")
    """Content of the Reversal Request message."""

    stored_value_request: Optional[StoredValueRequest2] = Field(default=UNSET, alias="StoredValueRequest")
    """Content of the Stored Value Request message."""

    transaction_status_request: Optional[TransactionStatusRequest2] = Field(
        default=UNSET, alias="TransactionStatusRequest"
    )
    """Content of the TransactionStatus Request message."""


class SaleToPoirequestDict(TypedDict):
    message_header: MessageHeader | MessageHeaderDict
    abort_request: NotRequired[AbortRequest2 | AbortRequest2Dict]
    balance_inquiry_request: NotRequired[BalanceInquiryRequest2 | BalanceInquiryRequest2Dict]
    card_acquisition_request: NotRequired[CardAcquisitionRequest2 | CardAcquisitionRequest2Dict]
    admin_request: NotRequired[AdminRequest2 | AdminRequest2Dict]
    diagnosis_request: NotRequired[DiagnosisRequest2 | DiagnosisRequest2Dict]
    display_request: NotRequired[DisplayRequest2 | DisplayRequest2Dict]
    enable_service_request: NotRequired[EnableServiceRequest2 | EnableServiceRequest2Dict]
    event_notification: NotRequired[EventNotification2 | EventNotification2Dict]
    get_totals_request: NotRequired[GetTotalsRequest2 | GetTotalsRequest2Dict]
    input_request: NotRequired[InputRequest2 | InputRequest2Dict]
    input_update: NotRequired[InputUpdate2 | InputUpdate2Dict]
    login_request: NotRequired[LoginRequest2 | LoginRequest2Dict]
    logout_request: NotRequired[LogoutRequest2 | LogoutRequest2Dict]
    payment_request: NotRequired[PaymentRequest21 | PaymentRequest21Dict]
    print_request: NotRequired[PrintRequest2 | PrintRequest2Dict]
    card_reader_apdu_request: NotRequired[CardReaderApdurequest2 | CardReaderApdurequest2Dict]
    reconciliation_request: NotRequired[ReconciliationRequest2 | ReconciliationRequest2Dict]
    reversal_request: NotRequired[ReversalRequest2 | ReversalRequest2Dict]
    stored_value_request: NotRequired[StoredValueRequest2 | StoredValueRequest2Dict]
    transaction_status_request: NotRequired[TransactionStatusRequest2 | TransactionStatusRequest2Dict]
