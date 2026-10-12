from __future__ import annotations

from pydantic import Field
from typing_extensions import NotRequired, TypedDict

from ..core import UNSET, Optional, SdkBaseModel
from .admin_response2 import AdminResponse2, AdminResponse2Dict
from .balance_inquiry_response2 import BalanceInquiryResponse2, BalanceInquiryResponse2Dict
from .card_acquisition_response2 import CardAcquisitionResponse2, CardAcquisitionResponse2Dict
from .card_reader_apduresponse2 import CardReaderApduresponse2, CardReaderApduresponse2Dict
from .diagnosis_response2 import DiagnosisResponse2, DiagnosisResponse2Dict
from .display_response2 import DisplayResponse2, DisplayResponse2Dict
from .enable_service_response2 import EnableServiceResponse2, EnableServiceResponse2Dict
from .get_totals_response2 import GetTotalsResponse2, GetTotalsResponse2Dict
from .input_response2 import InputResponse2, InputResponse2Dict
from .login_response2 import LoginResponse2, LoginResponse2Dict
from .logout_response2 import LogoutResponse2, LogoutResponse2Dict
from .loyalty_response2 import LoyaltyResponse2, LoyaltyResponse2Dict
from .message_header import MessageHeader, MessageHeaderDict
from .payment_response21 import PaymentResponse21, PaymentResponse21Dict
from .print_response2 import PrintResponse2, PrintResponse2Dict
from .reconciliation_response2 import ReconciliationResponse2, ReconciliationResponse2Dict
from .reversal_response2 import ReversalResponse2, ReversalResponse2Dict
from .stored_value_response2 import StoredValueResponse2, StoredValueResponse2Dict
from .transaction_status_response2 import TransactionStatusResponse2, TransactionStatusResponse2Dict


class SaleToPoiresponse(SdkBaseModel):
    """The SaleToPOIResponse message pair is a container for the response message content. It contains a MessageHeader
    and a message body."""

    message_header: MessageHeader = Field(alias="MessageHeader")
    """Message header of the Sale to POI protocol message. It conveys Information related to the Sale to POI protocol
    management."""

    balance_inquiry_response: Optional[BalanceInquiryResponse2] = Field(default=UNSET, alias="BalanceInquiryResponse")
    """Content of the Balance Inquiry Response message."""

    card_acquisition_response: Optional[CardAcquisitionResponse2] = Field(
        default=UNSET, alias="CardAcquisitionResponse"
    )
    """Content of the Card Acquisition Response message."""

    admin_response: Optional[AdminResponse2] = Field(default=UNSET, alias="AdminResponse")
    """Content of the Admin Response message."""

    diagnosis_response: Optional[DiagnosisResponse2] = Field(default=UNSET, alias="DiagnosisResponse")
    """Content of the Diagnosis Response message."""

    display_response: Optional[DisplayResponse2] = Field(default=UNSET, alias="DisplayResponse")
    """Content of the Display Response message."""

    enable_service_response: Optional[EnableServiceResponse2] = Field(default=UNSET, alias="EnableServiceResponse")
    """Content of the Enable Service Response message."""

    get_totals_response: Optional[GetTotalsResponse2] = Field(default=UNSET, alias="GetTotalsResponse")
    """Content of the Get Totals Response message."""

    input_response: Optional[InputResponse2] = Field(default=UNSET, alias="InputResponse")
    """Content of the Input Response message."""

    login_response: Optional[LoginResponse2] = Field(default=UNSET, alias="LoginResponse")
    """Content of the Login Response message."""

    logout_response: Optional[LogoutResponse2] = Field(default=UNSET, alias="LogoutResponse")
    """Content of the Logout Response message."""

    loyalty_response: Optional[LoyaltyResponse2] = Field(default=UNSET, alias="LoyaltyResponse")
    """Content of the Loyalty Response message."""

    payment_response: Optional[PaymentResponse21] = Field(default=UNSET, alias="PaymentResponse")
    """Content of the Payment Response message."""

    print_response: Optional[PrintResponse2] = Field(default=UNSET, alias="PrintResponse")
    """Content of the Print Response message."""

    card_reader_apdu_response: Optional[CardReaderApduresponse2] = Field(default=UNSET, alias="CardReaderAPDUResponse")
    """Content of the Card Reader APDU Response message."""

    reconciliation_response: Optional[ReconciliationResponse2] = Field(default=UNSET, alias="ReconciliationResponse")
    """Content of the Reconciliation Response message."""

    reversal_response: Optional[ReversalResponse2] = Field(default=UNSET, alias="ReversalResponse")
    """Content of the Reversal Response message."""

    stored_value_response: Optional[StoredValueResponse2] = Field(default=UNSET, alias="StoredValueResponse")
    """Content of the Stored Value Response message."""

    transaction_status_response: Optional[TransactionStatusResponse2] = Field(
        default=UNSET, alias="TransactionStatusResponse"
    )
    """Content of the TransactionStatus Response message."""


class SaleToPoiresponseDict(TypedDict):
    message_header: MessageHeaderDict
    balance_inquiry_response: NotRequired[BalanceInquiryResponse2Dict]
    card_acquisition_response: NotRequired[CardAcquisitionResponse2Dict]
    admin_response: NotRequired[AdminResponse2Dict]
    diagnosis_response: NotRequired[DiagnosisResponse2Dict]
    display_response: NotRequired[DisplayResponse2Dict]
    enable_service_response: NotRequired[EnableServiceResponse2Dict]
    get_totals_response: NotRequired[GetTotalsResponse2Dict]
    input_response: NotRequired[InputResponse2Dict]
    login_response: NotRequired[LoginResponse2Dict]
    logout_response: NotRequired[LogoutResponse2Dict]
    loyalty_response: NotRequired[LoyaltyResponse2Dict]
    payment_response: NotRequired[PaymentResponse21Dict]
    print_response: NotRequired[PrintResponse2Dict]
    card_reader_apdu_response: NotRequired[CardReaderApduresponse2Dict]
    reconciliation_response: NotRequired[ReconciliationResponse2Dict]
    reversal_response: NotRequired[ReversalResponse2Dict]
    stored_value_response: NotRequired[StoredValueResponse2Dict]
    transaction_status_response: NotRequired[TransactionStatusResponse2Dict]
