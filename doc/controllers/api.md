# API

```python
client_api = client.client
```

## Class Name

`API`

## Methods

* [Login Request](../../doc/controllers/api.md#login-request)
* [Logout Request](../../doc/controllers/api.md#logout-request)
* [Enable Service Request](../../doc/controllers/api.md#enable-service-request)
* [Admin Request](../../doc/controllers/api.md#admin-request)
* [Payment Request](../../doc/controllers/api.md#payment-request)
* [Card Acquisition Request](../../doc/controllers/api.md#card-acquisition-request)
* [Stored Value Request](../../doc/controllers/api.md#stored-value-request)
* [Reversal Request](../../doc/controllers/api.md#reversal-request)
* [Reconciliation Request](../../doc/controllers/api.md#reconciliation-request)
* [Get Totals Request](../../doc/controllers/api.md#get-totals-request)
* [Balance Inquiry Request](../../doc/controllers/api.md#balance-inquiry-request)
* [Transaction Status Request](../../doc/controllers/api.md#transaction-status-request)
* [Abort Request](../../doc/controllers/api.md#abort-request)
* [Diagnosis Request](../../doc/controllers/api.md#diagnosis-request)
* [Display Request](../../doc/controllers/api.md#display-request)
* [Input Request](../../doc/controllers/api.md#input-request)
* [Print Request](../../doc/controllers/api.md#print-request)
* [Card Reader APDU Request](../../doc/controllers/api.md#card-reader-apdu-request)


# Login Request

It conveys information related to the session (period between a Login and the following Logout) to process.
Content of the `LoginRequest` message.

```python
def login_request(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LoginRequest`](../../doc/models/login-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the Login to process.
Content of the Login Response message.

[`LoginResponse`](../../doc/models/login-response.md)

## Example Usage

```python
body = LoginRequest(
    date_time=dateutil.parser.parse('2016-03-13T12:52:32.123Z'),
    sale_software=SaleSoftware1(
        manufacturer_id='ManufacturerID4',
        application_name='ApplicationName8',
        software_version='SoftwareVersion0',
        certification_code='CertificationCode4'
    ),
    operator_language='OperatorLanguage2',
    training_mode_flag=False
)

result = client_api.login_request(
    body=body
)
print(result)
```


# Logout Request

Empty.
Content of the Logout Request message.

```python
def logout_request(self,
                  body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`LogoutRequest`](../../doc/models/logout-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the Logout.
Content of the Logout Response message.

[`LogoutResponse`](../../doc/models/logout-response.md)

## Example Usage

```python
body = LogoutRequest(
    maintenance_allowed=False
)

result = client_api.logout_request(
    body=body
)
print(result)
```


# Enable Service Request

It conveys the services that will be enabled for the POI Terminal without the request of the Sale System, and a possible invitation for the Customer to start the services.
Content of the Enable Service Request message.

```python
def enable_service_request(self,
                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`EnableServiceRequest`](../../doc/models/enable-service-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the Enable Service processing.
Content of the Enable Service Response message.

[`EnableServiceResponse`](../../doc/models/enable-service-response.md)

## Example Usage

```python
result = client_api.enable_service_request()
print(result)
```


# Admin Request

Empty.
Content of the Custom Admin Request message.

```python
def admin_request(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AdminRequest`](../../doc/models/admin-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the Custom Admin.
Content of the Custom Admin Response message.

[`AdminResponse`](../../doc/models/admin-response.md)

## Example Usage

```python
result = client_api.admin_request()
print(result)
```


# Payment Request

Request sent to terminal to initiate payment.
It conveys Information related to the Payment transaction to process.
Content of the `PaymentRequest` message.

```python
def payment_request(self,
                   body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PaymentRequest2`](../../doc/models/payment-request-2.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the Payment transaction processed by the POI System.
Content of the Payment Response message.

[`PaymentResponse4`](../../doc/models/payment-response-4.md)

## Example Usage

```python
result = client_api.payment_request()
print(result)
```


# Card Acquisition Request

It conveys Information related to the payment and loyalty cards to read and analyse. This message pair is usually followed by a message pair (e.g. payment or loyalty) which refers to this Card Acquisition message pair.
Content of the Card Acquisition Request message.

```python
def card_acquisition_request(self,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CardAcquisitionRequest`](../../doc/models/card-acquisition-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the payment and loyalty cards read and processed by the POI System and entered by the Customer.
Content of the Card Acquisition Response message.

[`CardAcquisitionResponse`](../../doc/models/card-acquisition-response.md)

## Example Usage

```python
result = client_api.card_acquisition_request()
print(result)
```


# Stored Value Request

It conveys Information related to the Stored Value transaction to process.
Content of the Stored Value Request message.

```python
def stored_value_request(self,
                        body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`StoredValueRequest`](../../doc/models/stored-value-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the Stored Value transaction processed by the POI System.
Content of the Stored Value Response message.

[`StoredValueResponse`](../../doc/models/stored-value-response.md)

## Example Usage

```python
body = StoredValueRequest(
    sale_data=SaleData1(
        sale_transaction_id=TransactionIDType1(
            transaction_id='TransactionID2',
            time_stamp=dateutil.parser.parse('2016-03-13T12:52:32.123Z')
        )
    ),
    stored_value_data=[
        StoredValueData(
            stored_value_transaction_type=StoredValueTransactionType1Enum.RESERVE
        )
    ]
)

result = client_api.stored_value_request(
    body=body
)
print(result)
```


# Reversal Request

It conveys Information related to the reversal of a previous payment or a loyalty transaction.
Content of the Reversal Request message.

```python
def reversal_request(self,
                    body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ReversalRequest`](../../doc/models/reversal-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the reversal processed by the POI System.
Content of the Reversal Response message.

[`ReversalResponse`](../../doc/models/reversal-response.md)

## Example Usage

```python
body = ReversalRequest(
    original_poi_transaction=OriginalPOITransaction2(
        reuse_card_data_flag=True
    ),
    reversal_reason=ReversalReason1Enum.CUSTCANCEL
)

result = client_api.reversal_request(
    body=body
)
print(result)
```


# Reconciliation Request

Content of the Reconciliation Request message.
It conveys Information related to the Reconciliation requested by the Sale System.

```python
def reconciliation_request(self,
                          body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`ReconciliationRequest`](../../doc/models/reconciliation-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys Information related to the Reconciliation transaction processed by the POI System.
Content of the Reconciliation Response message.

[`ReconciliationResponse`](../../doc/models/reconciliation-response.md)

## Example Usage

```python
result = client_api.reconciliation_request()
print(result)
```


# Get Totals Request

It conveys information from the Sale System related to the scope and the format of the totals to be computed by the POI System.
Content of the Get Totals Request message.

```python
def get_totals_request(self,
                      body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`GetTotalsRequest`](../../doc/models/get-totals-request.md) | Body, Optional | - |

## Response Type

**200**: Content of the Reconciliation Response message.
It conveys Information related to the Reconciliation transaction processed by the POI System.

[`GetTotalsResponse`](../../doc/models/get-totals-response.md)

## Example Usage

```python
result = client_api.get_totals_request()
print(result)
```


# Balance Inquiry Request

It conveys Information related to the account for which a Balance Inquiry is requested.
Content of the Balance Inquiry Request message.

```python
def balance_inquiry_request(self,
                           body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`BalanceInquiryRequest`](../../doc/models/balance-inquiry-request.md) | Body, Optional | - |

## Response Type

**200**: Content of the Balance Inquiry Response message.
It conveys the balance and the identification of the associated payment, loyalty or stored value account.

[`BalanceInquiryResponse`](../../doc/models/balance-inquiry-response.md)

## Example Usage

```python
result = client_api.balance_inquiry_request()
print(result)
```


# Transaction Status Request

Content of the TransactionStatus Request message.
It conveys Information requested for status of the last or current Payment, Loyalty or Reversal transaction.

```python
def transaction_status_request(self,
                              body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`TransactionStatusRequest`](../../doc/models/transaction-status-request.md) | Body, Optional | - |

## Response Type

**200**: Content of the TransactionStatus Response message.
It conveys Information related to the status of the last or current Payment, Loyalty or Reversal transaction.

[`TransactionStatusResponse`](../../doc/models/transaction-status-response.md)

## Example Usage

```python
body = TransactionStatusRequest(
    receipt_reprint_flag=False
)

result = client_api.transaction_status_request(
    body=body
)
print(result)
```


# Abort Request

Body of the Abort Request message.
It conveys Information requested for identification of the message request carrying the transaction to abort. A message to display on the CustomerError Device could be sent by the Sale System (DisplayOutput).

```python
def abort_request(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`AbortRequest`](../../doc/models/abort-request.md) | Body, Optional | - |

## Response Type

**200**: A successful `AbortRequest` returns a response with a **200 OK** HTTP status code and no body.

`Any`

## Example Usage

```python
result = client_api.abort_request()
print(result)
```


# Diagnosis Request

It conveys Information related to the target POI for which the diagnosis is requested.
Content of the Diagnosis Request message.

```python
def diagnosis_request(self,
                     body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DiagnosisRequest`](../../doc/models/diagnosis-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the requested diagnosis and a possible message to display on a logical device.
Content of the Diagnosis Response message.

[`DiagnosisResponse`](../../doc/models/diagnosis-response.md)

## Example Usage

```python
body = DiagnosisRequest(
    host_diagnosis_flag=False
)

result = client_api.diagnosis_request(
    body=body
)
print(result)
```


# Display Request

It conveys the data to display and the way to process the display. It contains the complete content to display. It might contain an operation (the DisplayOutput element) per Display Device type.
Content of the Display Request message.

```python
def display_request(self,
                   body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`DisplayRequest`](../../doc/models/display-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the display, parallel to the message request, except if response not required and absent.
Content of the Display Response message.

[`DisplayResponse`](../../doc/models/display-response.md)

## Example Usage

```python
body = DisplayRequest(
    display_output=[
        DisplayOutput(
            device=Device11Enum.CASHIERDISPLAY,
            info_qualify=InfoQualify1Enum.STATUS,
            output_content=OutputContent1(
                output_format=OutputFormat1Enum.XHTML
            ),
            response_required_flag=True,
            minimum_display_time=0
        )
    ]
)

result = client_api.display_request(
    body=body
)
print(result)
```


# Input Request

Content of the `InputRequest` message. It conveys the data to display and how to process it. In addition to the display on the Input Device, it might contain an operation (the `DisplayOutput` element) per Display Device type.

```python
def input_request(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`InputRequest`](../../doc/models/input-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the input or the result of the outputs, parallel to the message request, except if response not required and absent.
Content of the Input Response message.

[`InputResponse`](../../doc/models/input-response.md)

## Example Usage

```python
body = InputRequest(
    input_data=InputData2(
        device=Device2Enum.CASHIERDISPLAY,
        info_qualify=InfoQualify2Enum.CUSTOMERASSISTANCE,
        input_command=InputCommand1Enum.GETANYKEY,
        notify_card_input_flag=False,
        immediate_response_flag=False,
        wait_user_validation_flag=True,
        from_right_to_left_flag=False,
        mask_characters_flag=False,
        beep_key_flag=False,
        global_correction_flag=False,
        disable_cancel_flag=False,
        disable_correct_flag=False,
        disable_valid_flag=False,
        menu_back_flag=False
    )
)

result = client_api.input_request(
    body=body
)
print(result)
```


# Print Request

Content of the Print Request message.
It conveys the complete data to print and how to process the print.

```python
def print_request(self,
                 body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`PrintRequest`](../../doc/models/print-request.md) | Body, Optional | - |

## Response Type

**200**: It conveys the result of the print, parallel to the message request, except if response not required and absent.
Content of the Print Response message.

[`PrintResponse`](../../doc/models/print-response.md)

## Example Usage

```python
body = PrintRequest(
    print_output=PrintOutput2(
        document_qualifier=DocumentQualifier2Enum.CUSTOMERRECEIPT,
        response_mode=ResponseMode1Enum.PRINTEND,
        output_content=OutputContent3(
            output_format=OutputFormat1Enum.XHTML
        ),
        integrated_print_flag=False,
        required_signature_flag=False
    )
)

result = client_api.print_request(
    body=body
)
print(result)
```


# Card Reader APDU Request

It contains the APDU request to send to the chip of the card, and a possible invitation message to display on the CashierInterface or the CustomerInterface.
Content of the Card Reader APDU Request message.

```python
def card_reader_apdu_request(self,
                            body=None)
```

## Authentication

This endpoint requires [BasicAuth](../../doc/auth/basic-authentication.md) **OR** [ApiKeyAuth](../../doc/auth/custom-header-signature.md)

## Parameters

| Parameter | Type | Tags | Description |
|  --- | --- | --- | --- |
| `body` | [`CardReaderAPDURequest`](../../doc/models/card-reader-apdu-request.md) | Body, Optional | - |

## Response Type

**200**: Content of the Card Reader APDU Response message.
It contains the result of the requested service, APDU response sent by the chip of the card in response to the APDU request.

[`CardReaderAPDUResponse`](../../doc/models/card-reader-apdu-response.md)

## Example Usage

```python
result = client_api.card_reader_apdu_request()
print(result)
```

