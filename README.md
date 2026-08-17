
# Getting Started with Adyen

## Introduction

Adyen Checkout API provides a simple and flexible way to initiate and authorise online payments. You can use the same integration for payments made with cards (including 3D Secure), mobile wallets, and local payment methods (for example, iDEAL and Sofort).

This API reference provides information on available endpoints and how to interact with them. To learn more about the API, visit [online payments documentation](https://docs.adyen.com/online-payments).

### Authentication

Each request to Checkout API must be signed with an API key. For this, [get your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) from your Customer Area, and set this key to the `X-API-Key` header value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

### Versioning

Checkout API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://checkout-test.adyen.com/v72/payments
```

### Server-side API libraries

We provide open-source [server-side API libraries](https://docs.adyen.com/development-resources/libraries/) in several languages:

- PHP
- Java
- Node.js
- .NET
- Go
- Python
- Ruby
- Apex (beta)

See our [integration examples](https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples) for example uses of the libraries.

### Developer resources

Checkout API is available through a Postman collection. Click the button below to create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25716737-46ad970e-dc9e-4246-bac2-769c6083e7b5?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-46ad970e-dc9e-4246-bac2-769c6083e7b5%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

### Going live

To access the live endpoints, you need an API key from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account, for example:

```
https://{PREFIX}-checkout-live.adyenpayments.com/checkout/v72/payments
```

Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**.

When preparing to do live transactions with Checkout API, follow the [go-live checklist](https://docs.adyen.com/online-payments/go-live-checklist) to make sure you've got all the required configuration in place.

### Release notes

Have a look at the [release notes](https://docs.adyen.com/online-payments/release-notes?integration_type=api&version=72) to find out what changed in this version!, A set of API endpoints that allow you to initiate, settle, and modify payments on the Adyen payments platform. You can use the API to accept card payments (including One-Click and 3D Secure), bank transfers, ewallets, and many other payment methods.

> This API is [inactive](https://docs.adyen.com/online-payments/upgrade-your-integration#checkout-api-lifecycle).
> 
> * If you are building a new integration, use the [Checkout API](https://docs.adyen.com/api-explorer/Checkout/latest/overview) instead.
> * If you have an existing integration using this API, reach out to your Adyen contact and [migrate to the Checkout API](https://docs.adyen.com/online-payments/upgrade-your-integration/migrate-to-checkout-api).
>   The Checkout API enables your [online payments](https://docs.adyen.com/online-payments) integration to accept all supported payment methods, use the latest features, and access more benefits.

To learn more about the API, visit [Classic integration](https://docs.adyen.com/classic-integration).

### Authentication

You need an [API credential](https://docs.adyen.com/development-resources/api-credentials) to authenticate to the API.

If using an API key, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

Alternatively, you can use the username and password to connect to the API using basic authentication, for example:

```
curl
-u "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

### Versioning

Payments API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://pal-test.adyen.com/pal/servlet/Payment/v68/authorise
```

### Going live

To authenticate to the live endpoints, you need an [API credential](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payment/v68/authorise
```

Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**., > The Recurring API is a legacy API for managing tokens. We strongly recommend to use [Checkout API recurring endpoints](https://docs.adyen.com/api-explorer/Checkout/71/post/storedPaymentMethods) instead when possible.

The Recurring API allows you to manage and remove your tokens or stored payment details. Tokens should be created with validation during a payment request.

For more information, refer to our [Tokenization documentation](https://docs.adyen.com/online-payments/tokenization).

### Authentication

You need an [API credential](https://docs.adyen.com/development-resources/api-credentials) to authenticate to the API.

If using an API key, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

Alternatively, you can use the username and password to connect to the API using basic authentication, for example:

```
curl
-u "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

### Versioning

Recurring API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://pal-test.adyen.com/pal/servlet/Recurring/v68/disable
```

### Server-side API libraries

We provide open-source [server-side API libraries](https://docs.adyen.com/development-resources/libraries/) in several languages:

- PHP
- Java
- Node.js
- .NET
- Go
- Python
- Ruby
- Apex (beta)

See our [integration examples](https://github.com/adyen-examples#%EF%B8%8F-official-integration-examples) for example uses of the libraries.

### Developer resources

Recurring API is available through a Postman collection. Click the button below to create a fork, then set the environment variables at **Environments**&nbsp;>&nbsp;**Adyen&nbsp;APIs**.

[![Run in Postman](https://run.pstmn.io/button.svg)](https://god.gw.postman.com/run-collection/25716737-0d1ef0da-f5a1-4004-b24a-c5152c51dc7b?action=collection%2Ffork&source=rip_markdown&collection-url=entityId%3D25716737-0d1ef0da-f5a1-4004-b24a-c5152c51dc7b%26entityType%3Dcollection%26workspaceId%3Da8d63f9f-cfc7-4810-90c5-9e0c60030d3e#?env%5BAdyen%20APIs%5D=W3sia2V5IjoiWC1BUEktS2V5IiwidmFsdWUiOiIiLCJlbmFibGVkIjp0cnVlLCJ0eXBlIjoic2VjcmV0In0seyJrZXkiOiJZT1VSX01FUkNIQU5UX0FDQ09VTlQiLCJ2YWx1ZSI6IiIsImVuYWJsZWQiOnRydWUsInR5cGUiOiJkZWZhdWx0In0seyJrZXkiOiJZT1VSX0NPTVBBTllfQUNDT1VOVCIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifSx7ImtleSI6IllPVVJfQkFMQU5DRV9QTEFURk9STSIsInZhbHVlIjoiIiwiZW5hYmxlZCI6dHJ1ZSwidHlwZSI6ImRlZmF1bHQifV0=)

### Going live

To authenticate to the live endpoints, you need an [API credential](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Recurring/v68/disable
```

Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**., > The **Payout API is deprecated** and no longer supports new integrations. Do one of the following:

> - If you are building a new integration, use the [Transfers API](https://docs.adyen.com/api-explorer/transfers/latest/overview) instead.
> - If you are already using the Payout API, reach out to your Adyen contact to learn how to migrate to the Transfers API.
> 
> With the Transfers API, you can:
> 
> - Handle multiple payout use cases with a single API.
> - Use new payout functionalities, such as instant payouts to bank accounts.
> - Receive webhooks with more details and defined transfer states.
> 
> For more information about the payout features of the Transfers API, see our [Payouts](https://docs.adyen.com/payouts/payout-service) documentation.

A set of API endpoints that allow you to store payout details, confirm, or decline a payout.

For more information, refer to [Online payouts](https://docs.adyen.com/online-payments/online-payouts).

### Authentication

To use the Payout API, you need to have [two API credentials](https://docs.adyen.com/online-payments/online-payouts#payouts-to-bank-accounts-and-wallets): one for storing payout details and submitting payouts, and another one for confirming or declining payouts. If you don't have the required API credentials, contact our [Support Team](https://www.adyen.help/hc/en-us/requests/new).

If using an API key, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

Alternatively, you can use the username and password to connect to the API using [basic authentication](https://docs.adyen.com/development-resources/api-credentials#basic-authentication).

The following example shows how to authenticate your request with basic authentication when submitting a payout:

```
curl
-u "storePayout@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

### Versioning

Payout API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://pal-test.adyen.com/pal/servlet/Payout/v68/payout
```

### Going live

To authenticate to the live endpoints, you need [API credentials](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/Payout/v68/payout
```

Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**., The BIN Lookup API provides endpoints for retrieving information, such as cost estimates, and 3D Secure supported version based on a given BIN.

### Authentication

You need an [API credential](https://docs.adyen.com/development-resources/api-credentials) to authenticate to the API.

If using an API key, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

Alternatively, you can use the username and password to connect to the API using basic authentication, for example:

```
curl
-u "ws@Company.YOUR_COMPANY_ACCOUNT":"YOUR_BASIC_AUTHENTICATION_PASSWORD" \
-H "Content-Type: application/json" \
...
```

### Versioning

The BinLookup API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://pal-test.adyen.com/pal/servlet/BinLookup/v54/get3dsAvailability
```

### Going live

To authenticate to the live endpoints, you need an [API credential](https://docs.adyen.com/development-resources/api-credentials) from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account:

```
https://{PREFIX}-pal-live.adyenpayments.com/pal/servlet/BinLookup/v54/get3dsAvailability
```

Get your `{PREFIX}` from your live Customer Area under **Developers** > **API URLs** > **Prefix**., A set of API endpoints to manage stored value products., Adyen Data Protection API provides a way for you to process [Subject Erasure Requests](https://gdpr-info.eu/art-17-gdpr/) as mandated in GDPR.

Use our API to submit a request to delete shopper's data, including payment details and other related information (for example, delivery address or shopper email).## Authentication
Each request to the Data Protection API must be signed with an API key. Get your API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the `X-API-Key` header value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...
```

Note that when going live, you need to generate a new API Key to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

### Versioning

Data Protection Service API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://ca-test.adyen.com/ca/services/DataProtectionService/v1/requestSubjectErasure
```, The Foreign Exchange API allows you to manage and convert the currencies that are enabled for your integration.
## Authentication
We recommend that you use an API key to connect to the Foreign Exchange API. You can generate an API key in your Customer Area. If you have an Adyen Issuing integration, generate an API key in your Balance Platform Customer Area.
### Credential format
* For the `rates/calculate` endpoint: Generate an API key for the credential with the format **ws@BalancePlatform.[YourBalancePlatform]**.

### Header format
To connect to the Foreign Exchange API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: ADYEN_API_KEY' \
...

```
## Versioning

The Foreign Exchange API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

https://balanceplatform-api-test.adyen.com/fx/v1/rates/calculate

## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca/). If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your [live Balance Platform Customer Area](https://balanceplatform-live.adyen.com/balanceplatform/). You can then use the API key to send requests to `https://balanceplatform-api-test.adyen.com/fx/v1`., The Test Cards API provides endpoints for generating custom test card numbers. For more information, refer to [Custom test cards](https://docs.adyen.com/development-resources/testing/create-test-cards) documentation., Configure and manage your Adyen company and merchant accounts, stores, and payment terminals.
## Authentication
Each request to the Management API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.

To access the live endpoints, you need to generate a new API key in your live Customer Area.
## Versioning

Management API handles versioning as part of the endpoint URL. For example, to send a request to this version of the `/companies/{companyId}/webhooks` endpoint, use:

```text
https://management-test.adyen.com/v3/companies/{companyId}/webhooks
```

### Going live

To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:

```text
https://management-live.adyen.com/v3
```

### Release notes

Have a look at the [release notes](https://docs.adyen.com/release-notes/management-api) to find out what changed in this version!, This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/adyen-for-platforms-model) instead.

The Account API provides endpoints for managing account-related entities on your platform. These related entities include account holders, accounts, bank accounts, shareholders, and verification-related documents. The management operations include actions such as creation, retrieval, updating, and deletion of them.

For more information, refer to our [documentation](https://docs.adyen.com/classic-platforms).

### Authentication

Your Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example:

```
curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...
```

Alternatively, you can use the username and password to connect to the API using basic authentication. For example:

```
curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...
```

When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

### Versioning

The Account API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:

```
https://cal-test.adyen.com/cal/services/Account/v6/createAccountHolder
```, The Balance Control API allows you to view and manage the balances in your company and merchant accounts.
## Authentication
We recommend that you use an API key to connect to the Balance Control API. You can [generate an API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in your Customer Area.
### Header format
To connect to the Balance Control API, add an `X-API-Key` header with the API key as the value. For example:
```

curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: ADYEN_API_KEY' \
...

```
## Versioning

The Balance Control API handles versioning as part of the endpoint URL. For example, to send a request to version 2 of the `/balanceOverview/companies/{companyId}/balances` endpoint, use:

https://balance-control-test.adyen.com/balance-control/api/v2/balanceOverview/companies/{companyId}/balances

## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca/). You can then use the API key to send requests to `https://balance-control-live.adyen.com/api/v2`., This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/adyen-for-platforms-model) instead.

The Notification Configuration API provides endpoints for setting up and testing notifications that inform you of events on your platform, for example when a verification check or a payout has been completed.

For more information, refer to our [documentation](https://docs.adyen.com/classic-platforms/notifications).
## Authentication
Your Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
Alternatively, you can use the username and password to connect to the API using basic authentication. For example:
```

curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...

```
When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Versioning
The Notification Configuration API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://cal-test.adyen.com/cal/services/Notification/v6/createNotificationConfiguration

```,
## Authentication
Each request to the Configuration API must be signed with an API key. Generate an API key in your Customer Area if you have a [platform setup](https://docs.adyen.com/platforms/manage-access/api-credentials-web-service/#generate-api-key) or [marketplace setup](https://docs.adyen.com/marketplaces/manage-access/api-credentials-web-service/#generate-api-key).

 If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your Balance Platform Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
## Versioning
The Configuration API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://balanceplatform-api-test.adyen.com/bcl/v2/accountHolders

```
## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca/) if you have an Adyen for Platforms integration or [live Balance Platform Customer Area](https://balanceplatform-live.adyen.com/balanceplatform/) if you have an Adyen Issuing integration.You can then use the API key to send requests to `https://balanceplatform-api-live.adyen.com/bcl/v2`., >Versions 1 and 2 of the Transfers API are deprecated. If you are just starting your implementation, use the latest version.

The Transfers API provides endpoints that you can use to transfer funds, whether when paying out to a transfer instrument for [marketplaces](https://docs.adyen.com/marketplaces/payout-to-users/on-demand-payouts) or [platforms](https://docs.adyen.com/platforms/payout-to-users/on-demand-payouts), [sending funds to third parties](https://docs.adyen.com/platforms/business-accounts/send-receive-funds) for users with business bank accounts, or to [request a payout for a grant offer](https://docs.adyen.com/platforms/capital). The API also supports use cases for [getting transactions for business bank accounts](https://docs.adyen.com/platforms/business-accounts/transactions-api) and getting [outstanding balances](https://docs.adyen.com/platforms/capital#get-balances) for one or more grants on your platform. 

## Authentication
Each request to the Transfers API must be signed with an API key. Generate an API key in your Customer Area if you have a [platform setup](https://docs.adyen.com/platforms/manage-access/api-credentials-web-service/#generate-api-key) or [marketplace setup](https://docs.adyen.com/marketplaces/manage-access/api-credentials-web-service/#generate-api-key).

If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your Balance Platform Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
## Roles and permissions
To use the Transfers API, you need an additional role for your API credential. Transfers must also be enabled for the source balance account. Your Adyen contact will set up the roles and permissions for you.
## Versioning
The Transfers API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://balanceplatform-api-test.adyen.com/btl/v4/transfers

```
## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca/) if you have an Adyen for Platforms integration or [live Balance Platform Customer Area](https://balanceplatform-live.adyen.com/balanceplatform/) if you have an Adyen Issuing integration. You can then use the API key to send requests to `https://balanceplatform-api-live.adyen.com/btl/v4`., The Capital API provides endpoints for embedding [Adyen Capital](https://docs.adyen.com/capital) into your marketplace or platform. With Capital, you can offer business financing to your users as grants. When a user receives a grant, they must repay the grant amount in a specified term, in addition to paying a fee for using this service.

With these endpoints, you can:
- **Get available financing offers**: You can get a list of offers with fixed amounts or a range of available financing for your users. Adyen configures the financing amount, the fee, and the repayment conditions for each offer. These configurations are based on proactive risk analyses that Adyen performs on your users.
- **Make requests for grants**: When a user selects a financing offer, you can make a request for the grant on their behalf.
- **Get information about your grant account**: Your grant account tracks the information of all grants in your marketplace or platform.

## Authentication
Each request made to the Capital API must be signed with an API key. Generate an API key in your Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
## Roles and permissions
To use the Capital API, your API credential must have the following roles:
- **Balance_Platform_Capital_Configuration_Role**
- **Balance_Platform_Capital_Grant_Initiation_Role**

Reach out to your Adyen contact to set up these roles.
## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca). You can then use the API key to send requests to `https://balanceplatform-api-live.adyen.com/capital/v{version}`., This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/adyen-for-platforms-model) instead.

The Fund API provides endpoints for managing the funds in the accounts on your platform. These management operations include, for example, the transfer of funds from one account to another, the payout of funds to an account holder, and the retrieval of balances in an account.

For more information, refer to our [documentation](https://docs.adyen.com/classic-platforms).
## Authentication
Your Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
Alternatively, you can use the username and password to connect to the API using basic authentication. For example:
```

curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...

```
When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Versioning
The Fund API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://cal-test.adyen.com/cal/services/Fund/v6/accountHolderBalance

```,
## Authentication
We recommend that you use an API key to connect to the Session authentication API. Generate an API key in your Customer Area if you have a [platform setup](https://docs.adyen.com/platforms/manage-access/api-credentials-web-service/#generate-api-key) or [marketplace setup](https://docs.adyen.com/marketplaces/manage-access/api-credentials-web-service/#generate-api-key). If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your Balance Platform Customer Area.

To connect to the Session authentication API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H 'Content-Type: application/json' \
-H 'X-API-Key: YOUR_API_KEY' \
...

```
## Roles and permissions
To create a token, you must meet specific requirements. These requirements vary depending on the type of component. For more information, see the documentation for [Onboarding](https://docs.adyen.com/platforms/onboard-users/components) and [Platform Experience](https://docs.adyen.com/platforms/build-user-dashboards) components.

## Going live
To access the live endpoint, generate an API key in your live Customer Area if you have a [platform](https://docs.adyen.com/platforms/) or [marketplace setup](https://docs.adyen.com/marketplaces/). If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your Balance Platform Customer Area. You can then use the API key to send requests to `https://authe-live.adyen.com/authe/api/v1`., The Legal Entity Management API enables you to manage legal entities that contain information required for verification.

## Authentication
Each request to the Legal Entity Management API must be signed with an API key. Generate an API key in your Customer Area if you have a [platform setup](https://docs.adyen.com/platforms/manage-access/api-credentials-web-service/#generate-api-key) or [marketplace setup](https://docs.adyen.com/marketplaces/manage-access/api-credentials-web-service/#generate-api-key).

 If you have an Adyen Issuing integration, [generate an API key](https://docs.adyen.com/issuing/manage-access/api-credentials-web-service/#generate-api-key) in your Balance Platform Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value. For example:
```

curl
-H "X-API-Key: YOUR_API_KEY" \
-H "Content-Type: application/json" \
...

```
## Versioning
The Legal Entity Management API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://kyc-test.adyen.com/lem/v4/legalEntities

```
## Rate limits
We enforce rate limits on Legal Entity Management API endpoints. When the number of requests you send exceeds a threshold within a time frame, additional requests are blocked until the time frame ends. Current limits:

- Live environments: 700 requests per 5 seconds.

- Test environments: 200 requests per 5 seconds.

- Failed requests are subject to a limit of 5 failures per 10 seconds.

## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca/) if you have an Adyen for Platforms integration or [live Balance Platform Customer Area](https://balanceplatform-live.adyen.com/balanceplatform/) if you have an Adyen Issuing integration.You can then use the API key to send requests to `https://kyc-live.adyen.com/lem/v4`., This API is used for the classic integration. If you are just starting your implementation, refer to our [new integration guide](https://docs.adyen.com/adyen-for-platforms-model) instead.

The Hosted onboarding API provides endpoints that you can use to generate links to Adyen-hosted pages, such as an [onboarding page](https://docs.adyen.com/classic-platforms/hosted-onboarding-page) or a [PCI compliance questionnaire](https://docs.adyen.com/classic-platforms/platforms-for-partners). You can provide these links to your account holders so that they can complete their onboarding.

## Authentication
Your Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
Alternatively, you can use the username and password to connect to the API using basic authentication. For example:
```

curl
-U "ws@MarketPlace.YOUR_PLATFORM_ACCOUNT":"YOUR_WS_PASSWORD" \
-H "Content-Type: application/json" \
...

```
When going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Versioning
The Hosted onboarding API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://cal-test.adyen.com/cal/services/Hop/v6/getOnboardingUrl

```,
With these endpoints, you can:
- **Retrieve payment details**: Retrieve transaction information for specific payments.
- **Confirm payments**: Confirm payments with Strong Customer Authentication (SCA).
- **Cancel payments**: Cancel pending transactions.

## Authentication
Each request made to the A2A Payments API must be signed with an API key. Generate an API key in your Customer Area.

To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
## Roles and permissions
To use the A2A Payments API, your API credential must have the following roles:
- **Role for A2A Issuer payments - API**

Reach out to your Adyen contact to set up these roles.
## Going live
When going live, generate an API key in your [live Customer Area](https://ca-live.adyen.com/ca). You can then use the API key to send requests to `https://balanceplatform-api-live.adyen.com/a2aissuer-api/v{version}/payments`., The Open Banking API provides secure endpoints to share financial data and services with third parties. This API offers quick and reliable user verification.

With these endpoints, you can:

- **Create a list of available account verification routes**: Create a list of Account Information Service Providers (AISPs) for third-party individual account verification. Successful connections generate a unique code used for requesting bank reports and verifying identity.
- **Verify bank account ownership**: Get the account verification report using the unique code from a successful open banking connection. This report provides identity verification and bank account details.
## Authentication
Each request made to the Open Banking API must be signed with an API key. Generate an API key in your Customer Area.

To connect to the API, add an X-API-Keyheader with the API key as the value, for example:
```

curl
-H "Content-Type: application/json"
-H "X-API-Key: YOUR_API_KEY"
...

```
## Roles and permissions
To use the Open Banking API, your API credential must have the following roles:
- **Role for OpenBanking account verification use case: EXTERNAL**

Reach out to your Adyen contact to set up these roles., You can use the [Disputes API](https://docs.adyen.com/risk-management/disputes-api) to automate the dispute handling process so that you can respond to disputes and chargebacks as soon as they are initiated. The Disputes API lets you retrieve defense reasons, supply and delete defense documents, and accept or defend disputes.

## Authentication
Each request to the Disputes API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the `X-API-Key` header value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...

```
Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Versioning
Disputes API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://ca-test.adyen.com/ca/services/DisputeService/v30/defendDispute

```,
## Authentication
Your Adyen contact will provide your API credential and an API key. To connect to the API, add an `X-API-Key` header with the API key as the value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: YOUR_API_KEY" \
...

```
Alternatively, you can use the username and password to connect to the API using basic authentication. For example:
```

curl
-H "Content-Type: application/json" \
-U "ws@BalancePlatform.YOUR_BALANCE_PLATFORM":"YOUR_WS_PASSWORD" \
...

```
## Roles and permissions
To use the Disputes API, you need an additional role for your API credential. Your Adyen contact will set up the roles and permissions for you.
## Versioning
The Disputes API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://balanceplatform-api-test.adyen.com/btl/api/v{version}/disputes

```
## Going live
When going live, your Adyen contact will provide your API credential for the live environment. You can then use the username and password to send requests to `https://balanceplatform-api-live.adyen.com/btl/api/v{version}`., The Adyen [Terminal API](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/) lets you make payments, issue refunds, collect shopper information, and perform other shopper-device interactions using a payment terminal supplied by Adyen. The Terminal API is also used for transactions in [Adyen Mobile solutions](https://docs.adyen.com/point-of-sale/ipp-mobile/).

## API structure
The architecture of Terminal API is determined by the [nexo Sale to POI Protocol Specifications](https://www.nexo-standards.org/standards/nexo-retailer-protocol).

A Terminal API request is a JSON message consisting of a `SaleToPOIRequest` object with:
- [`MessageHeader`](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/#request-message-header): identifies the type of transaction, the terminal or Mobile SDK instance being used, and unique transaction identifiers.
- **Request body**: content depending on the type of transaction or operation, for example, a `PaymentRequest`.

A Terminal API response is a JSON message consisting of a `SaletoPOIResponse`with:
* [`MessageHeader`](https://docs.adyen.com/point-of-sale/design-your-integration/terminal-api/#response-message-header): echoes the values provided in the request, except for `MessageType`, which is always **Response**.
* Response body: content depending on the type of transaction or operation, for example, a `PaymentResponse`.

## Sending and receiving
In an integration with Ayden payment terminals, you can send and receive Terminal API messages in the following ways:
- [Local communications](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/local/): using your local network, your POS system sends the request directly to the IP address of the terminal, and receives the result synchronously.
- [Cloud communications](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/cloud/): using the internet to access the cloud, your POS system sends the request to an Adyen endpoint, and Adyen forwards the request to the terminal. Your POS system either keeps the connection open and receives the response synchronously, or closes the connection and receives the response asynchronously in an event notification.

## Using local communications
To learn how to set up and protect local communications, refer to [Building a local integration](https://docs.adyen.com/point-of-sale/design-your-integration/choose-your-architecture/local/).

## Endpoints for cloud communications
If your POS system is cloud-based, you POST your Terminal API requests to a **Cloud device API** endpoint, using path and query parameters to identify the device that you want to send the request to.
- If your POS system is designed to keep the connection open to wait for the response, use the endpoints ending in `/sync`.
- If your POS system is designed to close the connection so that it can initiate a new request, use the endpoints ending in `/async`.

### Test endpoints
- `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/sync`
- `https://device-api-test.adyen.com/v1/merchants/{merchantAccount}/devices/{deviceId}/async`

### Live endpoints
The live endpoints differ per region. In addition to using a regional endpoint, you must select the geographically closest data center in your live Customer Area.

**Australia**
- `https://device-api-live-au.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync`
- `https://device-api-live-au.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async`

**East Asia**
- `https://device-api-live-apse.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync`
- `https://device-api-live-apse.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async`

**Europe**
- `https://device-api-live.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync`
- `https://device-api-live.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async`

**United States**
- `https://device-api-live-us.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/sync`
- `https://device-api-live-us.adyen.com/v1/merchants/{merchantId}/devices/{deviceId}/async`

 ### Old endpoints
If you currently use endpoints with a base URL that includes `terminal-api`, we strongly recommend migrating to Cloud device API endpoints, for the following reasons:
- When using Cloud device API, the API logs in the Customer Area include the Terminal API requests and responses.
- Cloud device API endpoints offer technical advantages such as versioning and better routing.
- Future enhancements and features will be based on Cloud device API.

There will be no future development on the old endpoints, but we continue to support them.

**Old test endpoints**:
- `https://terminal-api-test.adyen.com/sync` and `https://terminal-api-test.adyen.com/async`

**Old live endpoints Australia**:
- `https://terminal-api-live-au.adyen.com/sync` and `https://terminal-api-live-au.adyen.com/async`

**Old live endpoints East Asia**:
- `https://terminal-api-live-apse.adyen.com/sync` and `https://terminal-api-live-apse.adyen.com/async`

**Old live endpoints Europe**:
- `https://terminal-api-live.adyen.com/sync` and `https://terminal-api-live.adyen.com/async`

**Old live endpoints United States**:
- `https://terminal-api-live-us.adyen.com/sync` and `https://terminal-api-live-us.adyen.com/async`

## Authentication for cloud communications
Each request to a **Cloud device API** endpoint must be signed with an API key that has the **Cloud Device API role**. [Generate your API Key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and set this key to the `X-API-Key` header value of the Cloud device API request.

When going live, generate a new API key in the live Customer Area.

## Available Terminal API requests, The SoftPOS configuration API is used in the mutual authentication flow between an Adyen Android or iOS [Mobile SDK](https://docs.adyen.com/point-of-sale/ipp-mobile/) and the Adyen payments platform.
The Mobile SDK for Android or iOS devices enables businesses to accept in-person payments using a commercial off-the-shelf (COTS) device like a phone. 
For example, Tap to Pay transactions, or transactions on a mobile device in combination with a card reader.

## Authentication
Each request to the POS Mobile API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.
You also need to have a [client key](https://docs.adyen.com/development-resources/client-side-authentication/). The client key is part of the setup but you will not need to use it in your integration later. Therefore, when you set up the client key, you do not need to specify allowed origins, and you do not need to store the key in your system. 
To access the live endpoints, you need to generate a new API key and client key in your live Customer Area.
## Versioning

The POS Mobile API handles versioning as part of the endpoint URL.

For example:
```

https://softposconfig-test.adyen.com/softposconfig/v{version}/auth/certificate

```
## Going live
To access the live endpoints, you need an API key and client key from your live Customer Area, and switch to the live endpoint that is geographically closest to your location.
### Australia:
https://softposconfig-live-au.adyen.com/softposconfig/v{version}/auth/certificate
### Asia Pacific South East:
https://softposconfig-live-apse.adyen.com/softposconfig/v{version}/auth/certificate
### Europe:
https://softposconfig-live.adyen.com/softposconfig/v{version}/auth/certificate
### North East Asia:
https://softposconfig-live-nea.adyen.com/softposconfig/v{version}/auth/certificate
### United States:
https://softposconfig-live-us.adyen.com/softposconfig/v3/auth/certificate
## Methods, Board and manage the Adyen Payments App on your Android mobile devices.
## Authentication
Each request to the Payments App API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.

## Versioning

Payments App API handles versioning as part of the endpoint URL. For example, to send a request to this version of the `/merchants/{merchantId}/generatePaymentsAppBoardingToken` endpoint, use:

```text
https://management-test.adyen.com/v1/merchants/{merchantId}/generatePaymentsAppBoardingToken
```

### Going live

To access the live endpoints, you need an API key from your live Customer Area. Use this API key to make requests to:

```text
https://management-live.adyen.com/v{version}
```, >This API is deprecated. Use the [SoftPOS configuration API](https://docs.adyen.com/api-explorer/softpos-configuration-api/latest/overview) instead.

The POS Mobile API is used in the mutual authentication flow between an Adyen Android or iOS [POS Mobile SDK](https://docs.adyen.com/point-of-sale/ipp-mobile/) and the Adyen payments platform.
The POS Mobile SDK for Android or iOS devices enables businesses to accept in-person payments using a commercial off-the-shelf (COTS) device like a phone. For example, Tap to Pay transactions, or transactions on a mobile device in combination with a card reader.

## Authentication
Each request to the POS Mobile API must be signed with an API key. [Generate your API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key) in the Customer Area and then set this key to the `X-API-Key` header value.
You also need to have a [client key](https://docs.adyen.com/development-resources/client-side-authentication/). The client key is part of the setup but you won't need to use it in your integration later. Therefore, you don't need to specify allowed origins, and you don't need to store the key in your system. 
To access the live endpoints, you need to generate a new API key and client key in your live Customer Area.
## Versioning

The POS Mobile API handles versioning as part of the endpoint URL.

For example:
```

https://checkout-test.adyen.com/checkout/possdk/v68/sessions

```
## Going live

To access the live endpoints, you need an API key and client key from your live Customer Area.

The live endpoint URLs contain a prefix which is unique to your company account, for example:
```

https://{PREFIX}-checkout-live.adyenpayments.com/checkout/possdk/v68/sessions

```,
For more information, refer to [Classic assign terminals](https://docs.adyen.com/point-of-sale/automating-terminal-management/assign-terminals-api/classic-assign-terminals-api/).

>From January 1, 2025 POS Terminal Management API is deprecated and support stops on April 1, 2025. To automate the management of your terminal fleet, use our [Management API](https://docs.adyen.com/api-explorer/Management/latest/overview).

## Authentication
Each request to the Terminal Management API must be signed with an API key. For this, obtain an API Key from your Customer Area, as described in [How to get the API key](https://docs.adyen.com/development-resources/api-credentials#generate-api-key). Then set this key to the `X-API-Key` header value, for example:
```

curl
-H "Content-Type: application/json" \
-H "X-API-Key: Your_API_key" \
...

```
Note that when going live, you need to generate new web service user credentials to access the [live endpoints](https://docs.adyen.com/development-resources/live-endpoints).

## Roles and permissions
To use the POS Terminal Management API, you need the **POS Terminal Management API role** added to your API credential. Your Adyen contact will set up the roles for you.
## Versioning
Terminal Management API supports [versioning](https://docs.adyen.com/development-resources/versioning) using a version suffix in the endpoint URL. This suffix has the following format: "vXX", where XX is the version number.

For example:
```

https://postfmapi-test.adyen.com/postfmapi/terminal/v1/getTerminalsUnderAccount

```
When using versioned endpoints, Boolean response values are returned in string format: `"true"` or `"false"`.
If you omit the version from the endpoint URL, Boolean response values are returned like this: `true` or `false`.
## Going live
To access the live endpoints, you need an API key from your live Customer Area.
Use this API key to make requests to:

```text
https://postfmapi-live.adyen.com/postfmapi/terminal/v1
```

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
| environment | [`Environment`](README.md#environments) | The API environment. <br> **Default: `Environment.TEST`** |
| http_client_instance | `Union[Session, HttpClientProvider]` | The Http Client passed from the sdk user for making requests |
| override_http_client_configuration | `bool` | The value which determines to override properties of the passed Http Client from the sdk user |
| http_call_back | `HttpCallBack` | The callback value that is invoked before and after an HTTP call is made to an endpoint |
| timeout | `float` | The value to use for connection timeout. <br> **Default: 30** |
| max_retries | `int` | The number of times to retry an endpoint call if it fails. <br> **Default: 0** |
| backoff_factor | `float` | A backoff factor to apply between attempts after the second try. <br> **Default: 2** |
| retry_statuses | `Array of int` | The http statuses on which retry is to be done. <br> **Default: [408, 413, 429, 500, 502, 503, 504, 521, 522, 524, 408, 413, 429, 500, 502, 503, 504, 521, 522, 524]** |
| retry_methods | `Array of string` | The http methods on which retry is to be done. <br> **Default: ["GET", "PUT", "GET", "PUT"]** |
| proxy_settings | [`ProxySettings`](doc/proxy-settings.md) | Optional proxy configuration to route HTTP requests through a proxy server. |
| api_key_auth_credentials | [`ApiKeyAuthCredentials`](doc/auth/custom-header-signature.md) | The credential object for Custom Header Signature |
| basic_auth_credentials | [`BasicAuthCredentials`](doc/auth/basic-authentication.md) | The credential object for Basic Authentication |
| client_key_credentials | [`ClientKeyCredentials`](doc/auth/custom-query-parameter.md) | The credential object for Custom Query Parameter |

The API client can be initialized as follows:

### Code-Based Client Initialization

```python
from adyen.adyen_client import AdyenClient
from adyen.configuration import Environment
from adyen.http.auth.api_key_auth import ApiKeyAuthCredentials
from adyen.http.auth.basic_auth import BasicAuthCredentials
from adyen.http.auth.client_key import ClientKeyCredentials

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
    environment=Environment.TEST
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
| TEST | **Default** Adyen test environment. Adyen's live endpoints are merchant-prefixed ({prefix}-checkout-live.adyenpayments.com), so no static live URL is correct here - point the client's BaseUrl at the merchant's own live host instead. |

## Authorization

This API uses the following authentication schemes.

* [`ApiKeyAuth (Custom Header Signature)`](doc/auth/custom-header-signature.md)
* [`BasicAuth (Basic Authentication)`](doc/auth/basic-authentication.md)
* [`clientKey (Custom Query Parameter)`](doc/auth/custom-query-parameter.md)

## List of APIs

* [Paymentlinks](doc/controllers/paymentlinks.md)
* [Instantpayouts](doc/controllers/instantpayouts.md)
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
* [Sessionauthentication](doc/controllers/sessionauthentication.md)
* [Legalentities](doc/controllers/legalentities.md)
* [Transferinstruments](doc/controllers/transferinstruments.md)
* [Businesslines](doc/controllers/businesslines.md)
* [Termsof Service](doc/controllers/termsof-service.md)
* [PC Iquestionnaires](doc/controllers/pc-iquestionnaires.md)
* [Taxe Deliveryconsent](doc/controllers/taxe-deliveryconsent.md)
* [Hosted Onboarding](doc/controllers/hosted-onboarding.md)
* [Hosted Onboarding Page](doc/controllers/hosted-onboarding-page.md)
* [PCI Compliance Questionnaire Page](doc/controllers/pci-compliance-questionnaire-page.md)
* [I DEA Lprofiles](doc/controllers/i-dea-lprofiles.md)
* [Account Verification](doc/controllers/account-verification.md)
* [Dispute Attachments](doc/controllers/dispute-attachments.md)
* [Raise Disputes](doc/controllers/raise-disputes.md)
* [API](doc/controllers/api.md)
* [Payments App](doc/controllers/payments-app.md)
* [Payments](doc/controllers/payments.md)
* [Donations](doc/controllers/donations.md)
* [Modifications](doc/controllers/modifications.md)
* [Recurring](doc/controllers/recurring.md)
* [Orders](doc/controllers/orders.md)
* [Utility](doc/controllers/utility.md)
* [General](doc/controllers/general.md)
* [Initialization](doc/controllers/initialization.md)
* [Reviewing](doc/controllers/reviewing.md)
* [Rates](doc/controllers/rates.md)
* [Accounts](doc/controllers/accounts.md)
* [Verification](doc/controllers/verification.md)
* [Platform](doc/controllers/platform.md)
* [Balances](doc/controllers/balances.md)
* [Transfers](doc/controllers/transfers.md)
* [Transactions](doc/controllers/transactions.md)
* [Capital](doc/controllers/capital.md)
* [Cash Out](doc/controllers/cash-out.md)
* [Grants](doc/controllers/grants.md)
* [Documents](doc/controllers/documents.md)

## SDK Infrastructure

### Configuration

* [ProxySettings](doc/proxy-settings.md)
* [Environment-Based Client Initialization](doc/environment-based-client-initialization.md)

### HTTP

* [HttpResponse](doc/http-response.md)
* [HttpRequest](doc/http-request.md)

### Utilities

* [ApiHelper](doc/api-helper.md)
* [HttpDateTime](doc/http-date-time.md)
* [RFC3339DateTime](doc/rfc3339-date-time.md)
* [UnixDateTime](doc/unix-date-time.md)

