# n8n-nodes-_node-sippysoft_

This is an n8n community node. It lets you use _Sippy Software Softswitch_ in your n8n workflows.

*Sippy Software Softswitch provides advanced VoIP billing, smart routing, network protection and border control mechanisms all on a single platform.*

Development of this node has been prioritised for functions required by its author's. If you would like to contribute please feel free to submit a pull request for review.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)
[Operations](#operations)
[Credentials](#credentials)
[Compatibility](#compatibility)
[Usage](#usage)
[Resources](#resources)
[Version history](#version-history)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

The following lists operations and their implementation status. A link to the Sippy Software documentation for each operation is included for convinience.

### Account Manipulation

* [X] List Accounts ([listAccounts](https://support.sippysoft.com/support/solutions/articles/107322-xml-rpc-api-listing-accounts))
* [ ] Create Account ()
* [ ] Update Account ([updateAccount](https://support.sippysoft.com/support/solutions/articles/107320-xml-rpc-api-updating-accounts))
* [X] Get Account Info ([getAccountInfo](https://support.sippysoft.com/support/solutions/articles/107327-xml-rpc-api-retrieving-account-information))
* [X] Get Registration Status ([getRegistrationStatus](https://support.sippysoft.com/support/solutions/articles/107366-xml-rpc-api-get-sip-registration-status-of-an-account))
* [ ] Reset One Time Password ([resetAccountOneTimePassword](https://support.sippysoft.com/support/solutions/articles/107399-xml-rpc-api-resetting-one-time-password-for-web-interface-login-account-))
* [X] Add Account Credit ([accountCredit](https://support.sippysoft.com/support/solutions/articles/107440-xml-rpc-api-refunding-an-account))

#### Incoming Routes

* [ ] Update Incoming Route ([updateIncomingRoute](https://support.sippysoft.com/support/solutions/articles/3000032223-xml-rpc-api-account-incoming-routing-management))
* [ ] Get Incoming Routes List ([getIncomingRoutesList](https://support.sippysoft.com/support/solutions/articles/3000032223-xml-rpc-api-account-incoming-routing-management))

#### Follow Me Management

* [ ] Get Follow Me Options ([getFollowMeOptions](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))
* [ ] Set Follow Me Options ([setFollowMeOptions](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))
* [ ] List Follow Me Entries ([listFollowMeEntries](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))
* [ ] Add Follow Me Entries ([addFollowMeEntry](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))
* [ ] Update Follow Me Entry ([updateFollowMeEntry](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))
* [ ] Delete Follow Me Entry ([getFollowMeOptions](https://support.sippysoft.com/support/solutions/articles/107412-xml-rpc-api-follow-me-feature-management))

#### Trunk Management

* [ ] createTrunk ([createTrunk](https://support.sippysoft.com/support/solutions/articles/3000116551-xml-rpc-api-trunks-management-versions-from-2022-))
* [ ] updateTrunk
* [ ] deleteTrunk
* [ ] getTrunkInfo
* [ ] getTrunksList
* [ ] createTrunkConnection ([createTrunkConnection](https://support.sippysoft.com/support/solutions/articles/3000116552-xml-rpc-api-trunk-connections-management))
* [ ] updateTrunkConnection
* [ ] deleteTrunkConnection
* [ ] getTrunkConnectionInfo
* [ ] getTrunkConnectionsList

#### Rates & Plans

* [ ] getAccountRates ([getAccountRates](https://support.sippysoft.com/support/solutions/articles/107408-xml-rpc-api-getting-rates-of-an-account))
* [ ] matchAccountMinutePlan ([matchAccountMinutePlan](https://support.sippysoft.com/support/solutions/articles/107406-xml-rpc-api-matching-cld-with-account-minute-plans))

#### CLI Mapping

* [ ] Add CLI Mapping ([addCLIMapping](https://support.sippysoft.com/support/solutions/articles/107328-xml-rpc-api-trusted-numbers-manipulation-and-cli-mapping))
* [ ] Update CLI Mapping ([updateCLIMapping](https://support.sippysoft.com/support/solutions/articles/107328-xml-rpc-api-trusted-numbers-manipulation-and-cli-mapping))
* [ ] Delete CLI Mapping ([delCLIMapping](https://support.sippysoft.com/support/solutions/articles/107328-xml-rpc-api-trusted-numbers-manipulation-and-cli-mapping))
* [ ] List CLI Mapping ([listCLIMapping](https://support.sippysoft.com/support/solutions/articles/107328-xml-rpc-api-trusted-numbers-manipulation-and-cli-mapping))
* [ ] Find CLI Mapping ([findCLIMapping](https://support.sippysoft.com/support/solutions/articles/107328-xml-rpc-api-trusted-numbers-manipulation-and-cli-mapping))

#### Smart Dials

* [ ] Add Smart Dial ([addSmartDial](https://support.sippysoft.com/support/solutions/articles/107333-xml-rpc-api-smart-dials-manipulation))
* [ ] Update Smart Dial ([updateSmartDial](https://support.sippysoft.com/support/solutions/articles/107333-xml-rpc-api-smart-dials-manipulation))
* [ ] Delete Smart Dial ([deleteSmartDial](https://support.sippysoft.com/support/solutions/articles/107333-xml-rpc-api-smart-dials-manipulation))
* [ ] List Smart Dial ([listSmartDial](https://support.sippysoft.com/support/solutions/articles/107333-xml-rpc-api-smart-dials-manipulation))

#### Post Authentiaction Rules

* [ ] listPostAuthRules ([listPostAuthRules](https://support.sippysoft.com/support/solutions/articles/3000105881-xml-rpc-api-post-authentication-rules-management))
* [ ] getPostAuthRuleInfo
* [ ] deletePostAuthRule
* [ ] updatePostAuthRule
* [ ] addPostAuthRule

#### Hot Dial Numbers

* [ ] addHotDialNumber ([addHotDialNumber](https://support.sippysoft.com/support/solutions/articles/107330-xml-rpc-api-hot-dial-numbers-manipulation))
* [ ] delHotDialNumber
* [ ] updateHotDialNumber
* [ ] listHotDialNumbers

### Payments

* [ ] getPaymentInfo
* [ ] getPaymentsList
* [ ] rechargeVoucher ([rechargeVoucher](https://support.sippysoft.com/support/solutions/articles/107438-xml-rpc-api-top-up-account-using-recharge-voucher))
* [ ] Make Payment ([makePayment](https://support.sippysoft.com/support/solutions/articles/107443-xml-rpc-api-make-payments-with-a-debit-credit-card))
* [ ] Make Payment By Card

#### Card Manipulation

*Look, it is probably not the best idea to have raw credit card numbers pass through n8n, these calls should probably never be implemented, but have been included here for transparency on the implementation progress.*

* [ ] addDebitCreditCard
* [ ] updateDebitCreditCard
* [ ] deleteDebitCreditCard
* [ ] getDebitCreditCardInfo
* [ ] listDebitCreditCards

#### Account Balance Manipulation

* [ ] accountAddFunds ([accountAddFunds](https://support.sippysoft.com/support/solutions/articles/107440-xml-rpc-api-refunding-an-account))
* [ ] accountDebit ([accountDebit](https://support.sippysoft.com/support/solutions/articles/107440-xml-rpc-api-refunding-an-account))

#### Vendor Balance Manipulation

* [ ] vendorAddFunds
* [ ] vendorCredit
* [ ] vendorDebit

#### Customer Balance Manipulation

* [ ] customerAddFunds
* [ ] customerCredit
* [ ] customerDebit

#### Low Balances

* [ ] getLowBalance
* [ ] setLowBalance

### CDRs Data Retrieving

* [ ] Export Vendor CDRs (Mera) ([exportVendorsCDRs_Mera](https://support.sippysoft.com/support/solutions/articles/107436-xml-rpc-api-exporting-vendors-cdr-to-mera-format))
* [X] Get Customer CDRs ([getCustomerCDRs](https://support.sippysoft.com/support/solutions/articles/107429-xml-rpc-api-get-cdrs-of-a-customer))
* [X] Get Account CDRs ([getAccountCDRs](https://support.sippysoft.com/support/solutions/articles/107367-xml-rpc-api-get-cdrs-of-an-account))
* [ ] Get CDR SDP ([getCDRSDP](https://support.sippysoft.com/support/solutions/articles/3000039695-xml-rpc-api-retrieve-sdp-data-of-a-call))

### DID Management

* [ ] addDID
* [ ] updateDID
* [ ] deleteDID
* [ ] getDIDInfo
* [X] Get DIDs List ([getDIDsList](https://support.sippysoft.com/support/solutions/articles/107502-xml-rpc-api-dids-management))
* [ ] getDIDChargingGroupInfo
* [ ] addDIDDelegation
* [ ] updateDIDDelegation
* [ ] deleteDIDDelegation

### Miscellaneous

* [ ] getMonitoringGraph [getMonitoringGraph](https://support.sippysoft.com/support/solutions/articles/107509-xml-rpc-api-monitoring)
* [ ] Get Monitoring Graph Data ([getMonitoringGraphData](https://support.sippysoft.com/support/solutions/articles/107509-xml-rpc-api-monitoring))

## Credentials

You will need to have your Softswitch API credentials setup and enabled. When setting up the credentials you will be asked to enter your server domain name, please use a domain name that has been setup in your softswitch with a valid SSL certificate.

Please note, these credentials will not work with the standard HTTP Request node due to an issue in compatibility between the default digest authentication n8n uses and the implementation used by the softswitch.

## Compatibility

This node *should* work in any version of n8n, however, has been tested only on versions since 1.0.0.

## Usageincoming_did

* **Trunks Management**
  Due to changes in the Sippy Softswitch API, trunk management calls are only compatible with versions of the softswitch from 2022 onwards.
* **DID Management**
  New features present in 2023 have not yet been implemented such as DID Ranges.

## Resources

* [n8n community nodes documentation](https://docs.n8n.io/integrations/community-nodes/)
* [Sippy Software XML-RPC API documentation](https://support.sippysoft.com/support/solutions/107132)

## Version history

1. This version was only used internally by node authors, once proof of concept was delivered, best practice of versioning nodes was implement. Version 1 has remained purely for backwards compatibility on those existing internal workflows and is not recommended for general use at all.
2. Following best practice of n8n node code directory structure, this version will be used while adding all the Softswitch API calls, of which there are many. Unless a major change to the Sippy API happens before completing that task.
