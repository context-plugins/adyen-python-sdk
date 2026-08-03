
# Getting Started with Adyen

## Introduction

The A2A payments API provides endpoints for A2A payment flows, enabling issuers to facilitate direct payments through Adyen for users with an Adyen business account.

With these endpoints, you can:

- **Retrieve payment details**: Retrieve transaction information for specific payments.
- **Confirm payments**: Confirm payments with Strong Customer Authentication (SCA).
- **Cancel payments**: Cancel pending transactions.

### Authentication

Each request made to the A2A Payments API must be signed with an API key. Generate an API key in your Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

### Roles and permissions

To use the A2A Payments API, your API credential must have the following roles:

- **Role for A2A Issuer payments - API**

Reach out to your Adyen contact to set up these roles.

### Going live

When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca). You can then use the API key to send requests to `https://balanceplatform-api-live.adyen.com/a2aissuer-api/v{version}/payments`.

## Building

You must have Python `3.7+` installed on your system to install and run this SDK. This SDK package depends on other Python packages like pytest, etc. These dependencies are defined in the `requirements.txt` file that comes with the SDK. To resolve these dependencies, you can use the PIP Dependency manager. Install it by following steps at [https://pip.pypa.io/en/stable/installing/](https://pip.pypa.io/en/stable/installing/).

Python and PIP executables should be defined in your PATH. Open command prompt and type `pip --version`. This should display the version of the PIP Dependency Manager installed if your installation was successful and the paths are properly defined.

* Using command line, navigate to the directory containing the generated files (including `requirements.txt`) for the SDK.
* Run the command `pip install -r requirements.txt`. This should install all the required dependencies.

![Building SDK - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&step=installDependencies)

## Installation

The following section explains how to use the adyen library in a new project.

### 1. Open Project in an IDE

Open up a Python IDE like PyCharm. The basic workflow presented here is also applicable if you prefer using a different editor or IDE.

![Open project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&step=pyCharm)

Click on `Open` in PyCharm to browse to your generated SDK directory and then click `OK`.

![Open project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&step=openProject0)

The project files will be displayed in the side bar as follows:

![Open project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&step=openProject1)

### 2. Add a new Test Project

Create a new directory by right clicking on the solution name as shown below:

![Add a new project in PyCharm - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&step=createDirectory)

Name the directory as "test".

![Add a new project in PyCharm - Step 2](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&step=nameDirectory)

Add a python file to this project.

![Add a new project in PyCharm - Step 3](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&step=createFile)

Name it "testSDK".

![Add a new project in PyCharm - Step 4](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&step=nameFile)

In your python file you will be required to import the generated python library using the following code lines

```python
from adyen.adyen_client import AdyenClient
```

![Add a new project in PyCharm - Step 5](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&libraryName=adyen.adyen_client&className=AdyenClient&step=projectFiles)

After this you can write code to instantiate an API client object, get a controller object and  make API calls. Sample code is given in the subsequent sections.

### 3. Run the Test Project

To run the file within your test project, right click on your Python file inside your Test project and click on `Run`

![Run Test Project - Step 1](https://apidocs.io/illustration/python?workspaceFolder=Adyen-Python&projectName=adyen&libraryName=adyen.adyen_client&className=AdyenClient&step=runProject)

## Initialize the API Client

**_Note:_** Documentation for the client can be found [here.](doc/client.md)

The following parameters are configurable for the API Client:

| Parameter | Type | Description |
|  --- | --- | --- |
| merchant_account | `str` | *Default*: `"merchantAccountDefaultValue"` |
| device_id | `str` | *Default*: `"deviceIdDefaultValue"` |
| environment | [`Environment`](README.md#environments) | The API environment. <br> **Default: `Environment.PRODUCTION`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| logging_configuration | [`LoggingConfiguration`](doc/logging-configuration.md) | The SDK logging configuration for API calls |
| api_key_auth_credentials | [`ApiKeyAuthCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| basic_auth_credentials | [`BasicAuthCredentials`](doc/auth/basic-authentication.md) | The credential object for Basic Authentication |
| client_key_credentials | [`ClientKeyCredentials`](doc/auth/custom-query-parameter.md) | The credential object for Custom Query Parameter |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
import logging

from adyen.adyen_client import AdyenClient
from adyen.configuration import Environment
from adyen.http.auth.api_key_auth import ApiKeyAuthCredentials
from adyen.http.auth.basic_auth import BasicAuthCredentials
from adyen.http.auth.client_key import ClientKeyCredentials
from adyen.logging.configuration.api_logging_configuration import LoggingConfiguration
from adyen.logging.configuration.api_logging_configuration import RequestLoggingConfiguration
from adyen.logging.configuration.api_logging_configuration import ResponseLoggingConfiguration

client = AdyenClient(
    api_key_auth_credentials=ApiKeyAuthCredentials(
        x_api_key='X-API-Key'
    ),
    basic_auth_credentials=BasicAuthCredentials(
        username='Username',
        password='Password'
    ),
    client_key_credentials=ClientKeyCredentials(
        client_key='clientKey'
    ),
    environment=Environment.PRODUCTION,
    merchant_account='merchantAccountDefaultValue',
    device_id='deviceIdDefaultValue',
    logging_configuration=LoggingConfiguration(
        log_level=logging.INFO,
        request_logging_config=RequestLoggingConfiguration(
            log_body=True
        ),
        response_logging_config=ResponseLoggingConfiguration(
            log_headers=True
        )
    )
)
```

### Environment-Based Client Initialization

```python
from adyen.adyen_client import AdyenClient

# Specify the path to your .env file if it’s located outside the project’s root directory.
client = AdyenClient.from_environment(dotenv_path='/path/to/.env')
```

See the [Environment-Based Client Initialization](doc/environment-based-client-initialization.md) section for details.

## Environments

The SDK can be configured to use a different environment for making API calls. Available environments are:

### Fields

| Name | Description |
|  --- | --- |
| PRODUCTION | **Default** Test Environment |
| ENVIRONMENT2 | Test Environment |
| ENVIRONMENT3 | Test Environment |
| ENVIRONMENT4 | Test Environment |
| ENVIRONMENT5 | Test Environment |
| ENVIRONMENT6 | Test Environment |
| ENVIRONMENT7 | Test Environment |
| ENVIRONMENT8 | Test Environment |
| ENVIRONMENT9 | Test Environment |
| ENVIRONMENT10 | Test Environment |
| ENVIRONMENT11 | Test Environment |
| ENVIRONMENT12 | Test Environment |
| ENVIRONMENT13 | Test Environment |
| ENVIRONMENT14 | Test Environment |
| ENVIRONMENT15 | Test Environment |
| ENVIRONMENT16 | Test Environment |
| ENVIRONMENT17 | Test Environment |
| ENVIRONMENT18 | Test Environment |
| ENVIRONMENT19 | Test Environment |
| ENVIRONMENT20 | Test Environment |
| ENVIRONMENT21 | Test Environment |
| ENVIRONMENT22 | Test Environment |
| ENVIRONMENT23 | Test Environment |
| ENVIRONMENT24 | Test Environment |
| ENVIRONMENT25 | Test Environment |
| ENVIRONMENT26 | Test Environment |
| ENVIRONMENT27 | Test Environment |
| ENVIRONMENT28 | Test Environment |
| ENVIRONMENT29 | Test Environment |
| ENVIRONMENT30 | Test Environment |
| ENVIRONMENT31 | Live Environment |
| ENVIRONMENT32 | Live Environment |
| ENVIRONMENT33 | Live Environment |
| ENVIRONMENT34 | Live Environment |
| ENVIRONMENT35 | Live Environment |
| ENVIRONMENT36 | Live Environment |
| ENVIRONMENT37 | Live Environment |
| ENVIRONMENT38 | Live Environment |
| ENVIRONMENT39 | Live Environment |
| ENVIRONMENT40 | Live Environment |
| ENVIRONMENT41 | Live Environment |
| ENVIRONMENT42 | Live Environment |
| ENVIRONMENT43 | Live Environment |
| ENVIRONMENT44 | Live Environment |
| ENVIRONMENT45 | Live Environment |
| ENVIRONMENT46 | Live Environment |
| ENVIRONMENT47 | Live Environment |
| ENVIRONMENT48 | Live Environment |
| ENVIRONMENT49 | Live Environment |
| ENVIRONMENT50 | Live Environment |
| ENVIRONMENT51 | Live Environment |
| ENVIRONMENT52 | Live Environment |
| ENVIRONMENT53 | Live Environment |
| ENVIRONMENT54 | Live Environment |
| ENVIRONMENT55 | Live Environment |
| ENVIRONMENT56 | Live Environment |
| ENVIRONMENT57 | Live Environment |
| ENVIRONMENT58 | Live Environment |
| ENVIRONMENT59 | Live Environment |
| ENVIRONMENT60 | Live Environment |
| ENVIRONMENT61 | Live environment for East Asia |
| ENVIRONMENT62 | Live environment for East Asia |
| ENVIRONMENT63 | Live environment for East Asia |
| ENVIRONMENT64 | Live environment for East Asia |
| ENVIRONMENT65 | Live environment for East Asia |
| ENVIRONMENT66 | Live environment for East Asia |
| ENVIRONMENT67 | Live environment for East Asia |
| ENVIRONMENT68 | Live environment for East Asia |
| ENVIRONMENT69 | Live environment for East Asia |
| ENVIRONMENT70 | Live environment for East Asia |
| ENVIRONMENT71 | Live environment for East Asia |
| ENVIRONMENT72 | Live environment for East Asia |
| ENVIRONMENT73 | Live environment for East Asia |
| ENVIRONMENT74 | Live environment for East Asia |
| ENVIRONMENT75 | Live environment for East Asia |
| ENVIRONMENT76 | Live environment for East Asia |
| ENVIRONMENT77 | Live environment for East Asia |
| ENVIRONMENT78 | Live environment for East Asia |
| ENVIRONMENT79 | Live environment for East Asia |
| ENVIRONMENT80 | Live environment for East Asia |
| ENVIRONMENT81 | Live environment for East Asia |
| ENVIRONMENT82 | Live environment for East Asia |
| ENVIRONMENT83 | Live environment for East Asia |
| ENVIRONMENT84 | Live environment for East Asia |
| ENVIRONMENT85 | Live environment for East Asia |
| ENVIRONMENT86 | Live environment for East Asia |
| ENVIRONMENT87 | Live environment for East Asia |
| ENVIRONMENT88 | Live environment for East Asia |
| ENVIRONMENT89 | Live environment for East Asia |
| ENVIRONMENT90 | Live environment for East Asia |
| ENVIRONMENT91 | Live environment for Europe |
| ENVIRONMENT92 | Live environment for Europe |
| ENVIRONMENT93 | Live environment for Europe |
| ENVIRONMENT94 | Live environment for Europe |
| ENVIRONMENT95 | Live environment for Europe |
| ENVIRONMENT96 | Live environment for Europe |
| ENVIRONMENT97 | Live environment for Europe |
| ENVIRONMENT98 | Live environment for Europe |
| ENVIRONMENT99 | Live environment for Europe |
| ENVIRONMENT100 | Live environment for Europe |
| ENVIRONMENT101 | Live environment for Europe |
| ENVIRONMENT102 | Live environment for Europe |
| ENVIRONMENT103 | Live environment for Europe |
| ENVIRONMENT104 | Live environment for Europe |
| ENVIRONMENT105 | Live environment for Europe |
| ENVIRONMENT106 | Live environment for Europe |
| ENVIRONMENT107 | Live environment for Europe |
| ENVIRONMENT108 | Live environment for Europe |
| ENVIRONMENT109 | Live environment for Europe |
| ENVIRONMENT110 | Live environment for Europe |
| ENVIRONMENT111 | Live environment for Europe |
| ENVIRONMENT112 | Live environment for Europe |
| ENVIRONMENT113 | Live environment for Europe |
| ENVIRONMENT114 | Live environment for Europe |
| ENVIRONMENT115 | Live environment for Europe |
| ENVIRONMENT116 | Live environment for Europe |
| ENVIRONMENT117 | Live environment for Europe |
| ENVIRONMENT118 | Live environment for Europe |
| ENVIRONMENT119 | Live environment for Europe |
| ENVIRONMENT120 | Live environment for Europe |
| ENVIRONMENT121 | Live environment for United States of America |
| ENVIRONMENT122 | Live environment for United States of America |
| ENVIRONMENT123 | Live environment for United States of America |
| ENVIRONMENT124 | Live environment for United States of America |
| ENVIRONMENT125 | Live environment for United States of America |
| ENVIRONMENT126 | Live environment for United States of America |
| ENVIRONMENT127 | Live environment for United States of America |
| ENVIRONMENT128 | Live environment for United States of America |
| ENVIRONMENT129 | Live environment for United States of America |
| ENVIRONMENT130 | Live environment for United States of America |
| ENVIRONMENT131 | Live environment for United States of America |
| ENVIRONMENT132 | Live environment for United States of America |
| ENVIRONMENT133 | Live environment for United States of America |
| ENVIRONMENT134 | Live environment for United States of America |
| ENVIRONMENT135 | Live environment for United States of America |
| ENVIRONMENT136 | Live environment for United States of America |
| ENVIRONMENT137 | Live environment for United States of America |
| ENVIRONMENT138 | Live environment for United States of America |
| ENVIRONMENT139 | Live environment for United States of America |
| ENVIRONMENT140 | Live environment for United States of America |
| ENVIRONMENT141 | Live environment for United States of America |
| ENVIRONMENT142 | Live environment for United States of America |
| ENVIRONMENT143 | Live environment for United States of America |
| ENVIRONMENT144 | Live environment for United States of America |
| ENVIRONMENT145 | Live environment for United States of America |
| ENVIRONMENT146 | Live environment for United States of America |
| ENVIRONMENT147 | Live environment for United States of America |
| ENVIRONMENT148 | Live environment for United States of America |
| ENVIRONMENT149 | Live environment for United States of America |
| ENVIRONMENT150 | Live environment for United States of America |
| ENVIRONMENT151 | Live environment for United States of America |
| ENVIRONMENT152 | Live environment for United States of America |
| ENVIRONMENT153 | Live environment for United States of America |
| ENVIRONMENT154 | Live environment for United States of America |
| ENVIRONMENT155 | Live environment for United States of America |
| ENVIRONMENT156 | Live environment for United States of America |
| ENVIRONMENT157 | Live environment for United States of America |
| ENVIRONMENT158 | Live environment for United States of America |
| ENVIRONMENT159 | Live environment for United States of America |
| ENVIRONMENT160 | Live environment for United States of America |
| ENVIRONMENT161 | Live environment for United States of America |
| ENVIRONMENT162 | Live environment for United States of America |
| ENVIRONMENT163 | Live environment for United States of America |
| ENVIRONMENT164 | Live environment for United States of America |
| ENVIRONMENT165 | Live environment for United States of America |
| ENVIRONMENT166 | Live environment for United States of America |
| ENVIRONMENT167 | Live environment for United States of America |
| ENVIRONMENT168 | Live environment for United States of America |
| ENVIRONMENT169 | Live environment for United States of America |
| ENVIRONMENT170 | Live environment for United States of America |
| ENVIRONMENT171 | Live environment for United States of America |
| ENVIRONMENT172 | Live environment for United States of America |
| ENVIRONMENT173 | Live environment for United States of America |
| ENVIRONMENT174 | Live environment for United States of America |
| ENVIRONMENT175 | Live environment for United States of America |
| ENVIRONMENT176 | Live environment for United States of America |
| ENVIRONMENT177 | Live environment for United States of America |
| ENVIRONMENT178 | Live environment for United States of America |
| ENVIRONMENT179 | Live environment for United States of America |
| ENVIRONMENT180 | Live environment for United States of America |

## Authorization

This API uses the following authentication schemes.

* [`ApiKeyAuth (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`BasicAuth (Basic Authentication)`](doc/auth/basic-authentication.md)
* [`clientKey (Custom Query Parameter)`](doc/auth/custom-query-parameter.md)

## List of APIs

* [I DEA Lprofiles](doc/controllers/i-dea-lprofiles.md)
* [Accountholders](doc/controllers/accountholders.md)
* [Balancesoverview](doc/controllers/balancesoverview.md)
* [Balancetransfers](doc/controllers/balancetransfers.md)
* [Balanceaccounts](doc/controllers/balanceaccounts.md)
* [Managedpayoutschedules](doc/controllers/managedpayoutschedules.md)
* [Custompayoutschedules Sweeps](doc/controllers/custompayoutschedules-sweeps.md)
* [Authorizedcardusers](doc/controllers/authorizedcardusers.md)
* [Recurringtopups](doc/controllers/recurringtopups.md)
* [Paymentinstruments](doc/controllers/paymentinstruments.md)
* [Paymentinstrumentgroups](doc/controllers/paymentinstrumentgroups.md)
* [Transactionrules](doc/controllers/transactionrules.md)
* [Bankaccountvalidation](doc/controllers/bankaccountvalidation.md)
* [Networktokens](doc/controllers/networktokens.md)
* [Grantaccounts](doc/controllers/grantaccounts.md)
* [Grantoffers](doc/controllers/grantoffers.md)
* [Cardorders](doc/controllers/cardorders.md)
* [Directdebitmandates](doc/controllers/directdebitmandates.md)
* [Managecard PIN](doc/controllers/managecard-pin.md)
* [Transferroutes](doc/controllers/transferroutes.md)
* [SC Adevicemanagement](doc/controllers/sc-adevicemanagement.md)
* [Transferlimits-Balanceaccountlevel](doc/controllers/transferlimits-balanceaccountlevel.md)
* [Transferlimits-Balanceplatformlevel](doc/controllers/transferlimits-balanceplatformlevel.md)
* [Manage SC Adevices](doc/controllers/manage-sc-adevices.md)
* [SC Aassociationmanagement](doc/controllers/sc-aassociationmanagement.md)
* [Dynamicoffers](doc/controllers/dynamicoffers.md)
* [Paymentlinks](doc/controllers/paymentlinks.md)
* [Cloudendpointsandconnection](doc/controllers/cloudendpointsandconnection.md)
* [Hosted Onboarding Page](doc/controllers/hosted-onboarding-page.md)
* [PCI Compliance Questionnaire Page](doc/controllers/pci-compliance-questionnaire-page.md)
* [Legalentities](doc/controllers/legalentities.md)
* [Transferinstruments](doc/controllers/transferinstruments.md)
* [Businesslines](doc/controllers/businesslines.md)
* [Termsof Service](doc/controllers/termsof-service.md)
* [PC Iquestionnaires](doc/controllers/pc-iquestionnaires.md)
* [Taxe Deliveryconsent](doc/controllers/taxe-deliveryconsent.md)
* [Hosted Onboarding](doc/controllers/hosted-onboarding.md)
* [Account-Companylevel](doc/controllers/account-companylevel.md)
* [Account-Merchantlevel](doc/controllers/account-merchantlevel.md)
* [Account-Storelevel](doc/controllers/account-storelevel.md)
* [Payoutsettings-Merchantlevel](doc/controllers/payoutsettings-merchantlevel.md)
* [Users-Companylevel](doc/controllers/users-companylevel.md)
* [Users-Merchantlevel](doc/controllers/users-merchantlevel.md)
* [My AP Icredential](doc/controllers/my-ap-icredential.md)
* [AP Icredentials-Companylevel](doc/controllers/ap-icredentials-companylevel.md)
* [AP Icredentials-Merchantlevel](doc/controllers/ap-icredentials-merchantlevel.md)
* [AP Ikey-Companylevel](doc/controllers/ap-ikey-companylevel.md)
* [AP Ikey-Merchantlevel](doc/controllers/ap-ikey-merchantlevel.md)
* [Clientkey-Companylevel](doc/controllers/clientkey-companylevel.md)
* [Clientkey-Merchantlevel](doc/controllers/clientkey-merchantlevel.md)
* [Allowedorigins-Companylevel](doc/controllers/allowedorigins-companylevel.md)
* [Allowedorigins-Merchantlevel](doc/controllers/allowedorigins-merchantlevel.md)
* [Webhooks-Companylevel](doc/controllers/webhooks-companylevel.md)
* [Webhooks-Merchantlevel](doc/controllers/webhooks-merchantlevel.md)
* [Paymentmethods-Merchantlevel](doc/controllers/paymentmethods-merchantlevel.md)
* [Terminals-Terminallevel](doc/controllers/terminals-terminallevel.md)
* [Terminalactions-Companylevel](doc/controllers/terminalactions-companylevel.md)
* [Terminalactions-Terminallevel](doc/controllers/terminalactions-terminallevel.md)
* [Terminalorders-Companylevel](doc/controllers/terminalorders-companylevel.md)
* [Terminalorders-Merchantlevel](doc/controllers/terminalorders-merchantlevel.md)
* [Terminalsettings-Companylevel](doc/controllers/terminalsettings-companylevel.md)
* [Terminalsettings-Merchantlevel](doc/controllers/terminalsettings-merchantlevel.md)
* [Terminalsettings-Storelevel](doc/controllers/terminalsettings-storelevel.md)
* [Terminalsettings-Terminallevel](doc/controllers/terminalsettings-terminallevel.md)
* [Androidfiles-Companylevel](doc/controllers/androidfiles-companylevel.md)
* [Splitconfiguration-Merchantlevel](doc/controllers/splitconfiguration-merchantlevel.md)
* [Donationcampaigns](doc/controllers/donationcampaigns.md)
* [Account Verification](doc/controllers/account-verification.md)
* [Payments App](doc/controllers/payments-app.md)
* [Instantpayouts](doc/controllers/instantpayouts.md)
* [Dispute Attachments](doc/controllers/dispute-attachments.md)
* [Raise Disputes](doc/controllers/raise-disputes.md)
* [Sessionauthentication](doc/controllers/sessionauthentication.md)
* [API](doc/controllers/api.md)
* [Payments](doc/controllers/payments.md)
* [Accounts](doc/controllers/accounts.md)
* [Verification](doc/controllers/verification.md)
* [Platform](doc/controllers/platform.md)
* [Balances](doc/controllers/balances.md)
* [General](doc/controllers/general.md)
* [Grants](doc/controllers/grants.md)
* [Donations](doc/controllers/donations.md)
* [Modifications](doc/controllers/modifications.md)
* [Recurring](doc/controllers/recurring.md)
* [Orders](doc/controllers/orders.md)
* [Utility](doc/controllers/utility.md)
* [Rates](doc/controllers/rates.md)
* [Documents](doc/controllers/documents.md)
* [Initialization](doc/controllers/initialization.md)
* [Reviewing](doc/controllers/reviewing.md)
* [Transfers](doc/controllers/transfers.md)
* [Transactions](doc/controllers/transactions.md)
* [Capital](doc/controllers/capital.md)
* [Cash Out](doc/controllers/cash-out.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)
* [AbstractLogger](doc/abstract-logger.md)
* [LoggingConfiguration](doc/logging-configuration.md)
* [RequestLoggingConfiguration](doc/request-logging-configuration.md)
* [ResponseLoggingConfiguration](doc/response-logging-configuration.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiResponse](doc/api-response.md)
* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

