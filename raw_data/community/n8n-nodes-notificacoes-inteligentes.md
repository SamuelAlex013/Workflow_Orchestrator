# Notificações Inteligentes

## What is Notificações Inteligentes?

[Notificações Inteligentes](https://notificacoesinteligentes.com/) is a company founded in 2015, focused on transforming the relationship between businesses and customers through message automation, especially via WhatsApp and other intelligent tools.

With almost 10 years in the market, it is part of Grupo GPM Participações e Tecnologias Ltda, offering robust automated communication solutions for thousands of clients across Brazil.

## Mission, Vision, and Values

The mission of Notificações Inteligentes is to empower companies with accessible and intelligent technology, helping them sell more, provide better service, and grow efficiently. The company believes in practical innovation that generates real value from the first customer contact.

The values are centered on:
*   **Effective and intuitive solutions**
*   **Focus on sustainable growth of client businesses**
*   **Excellence in service and continuous innovation**

---

## How the Platform Works and Its Usefulness

Notificações Inteligentes uses automation technology to transform data into strategic alerts, anticipate risks, automate processes, and ensure no sale is lost due to lack of communication.

The main products and features include:

*   [**GPT Chatbot**](https://notificacoesinteligentes.com/funcionalidades/chatbot-gpt): Intelligent chatbots using AI for automated interactions.
*   [**Automated Workflows**](https://notificacoesinteligentes.com/funcionalidades/workflow): Automate flows and send messages at the right time to engage leads.
*   [**Intelligent Recovery Tools**](https://notificacoesinteligentes.com/funcionalidades/recuperadores-inteligentes): Recover lost sales with automatic reminders.
*   [**Ad Platforms**](https://notificacoesinteligentes.com/funcionalidades/plataformas-de-anuncio): Optimize conversion sending and maximize ad performance.
*   [**Service Center**](https://notificacoesinteligentes.com/funcionalidades/central-de-atendimento): Centralize customer service, automate responses, and track metrics.
*   [**Chatbot**](https://notificacoesinteligentes.com/funcionalidades/chatbot): Provide 24/7 service with chatbots, capture leads, and scale your support.
*   [**Intelligent Lead Management**](https://notificacoesinteligentes.com/funcionalidades/gestao-de-leads): Store, manage, and track leads in the cloud conveniently.
*   [**Intelligent Redirectors**](https://notificacoesinteligentes.com/funcionalidades/redirecionadores-inteligentes): Redirect leads to multiple active WhatsApp numbers and track the origin.
*   [**Intelligent Notifications**](https://notificacoesinteligentes.com/funcionalidades/notificacoes-inteligentes): Send automatic notifications and boost engagement.
*   [**Campaigns**](https://notificacoesinteligentes.com/funcionalidades/campanhas): Schedule campaigns, segment contacts, and increase your conversions.
*   [**Pipeline Management**](https://notificacoesinteligentes.com/funcionalidades/pipelines): Manage your sales funnel and track negotiations in real-time.
*   [**Link Creation (URL Builder)**](https://notificacoesinteligentes.com/funcionalidades/url-builder): Create trackable URLs and enhance your marketing strategies.

The platform processes thousands of messages daily and is already a national reference in the automated communication segment, with over 15,000 companies served, using the solution to streamline processes, improve customer service, and increase operational efficiency.

---

## Why is Notificações Inteligentes Useful?

*   **Automates and scales** customer relationships, preventing lost sales due to lack of communication.
*   **Increases efficiency and agility** for sales, support, and marketing teams.
*   Facilitates **personalization and monitoring of interactions**, enabling faster and safer decisions.
*   Offers a **variety of integrations** with major market platforms, facilitating implementation in any business.
*   Operates **end-to-end**: from first contact to post-sale, including campaigns, notifications, automated service, and more.
*   Is **nationally recognized**, with a high volume of clients and success cases.

---

## Summary in One Sentence

Notificações Inteligentes is a leading platform in message automation and relationship management via WhatsApp, helping businesses of all sizes sell more, serve better, and grow with practical and intelligent technology.

---
# NI NODE AUTHENTICATION GUIDE

Welcome to the **Notificações Inteligentes Custom Node**!
This guide will help you **generate and configure your API Key (Bearer Token)** to authenticate and securely use all functionalities of your Custom Node.

## Accessing the Notificações Inteligentes Panel

1.  Open your browser and go to the [Notificações Inteligentes](https://notificacoesinteligentes.com) website.
2.  Click **Entrar (Login)** and log in with your account.

> Ensure you use the correct account that has access to the **Organizations** you want to manage via API.

---

## Generating the API Key (Bearer Token)

1.  After logging in, click **Organizações (Organizations)** in the top menu.
2.  Select the desired organization.
3.  Access **Configurações (Settings)**.
4.  Look for the **Chave de API (API Key)** section.
5.  Click **Gerar nova chave (Generate new key)**.

<img src="readme.img/generate_key.png" width="800" alt="Application Screenshot - Generate Key">

6.  A dialog box will be displayed:

<img src="readme.img/token.png" width="800" alt="Application Screenshot - Token">

   *   **Check the box** confirming you have saved the key in a secure location.
   *   Click **Concluir (Finish)**.

> The generated key will be used as the **Bearer Token** for Custom Node authentication.
> **Attention:** Keep this key secure! Do not share it publicly.

---

## Configuring the Custom Node

1.  In your integration environment (n8n), open the **Custom Node**.
2.  Locate the **Create new Credential / Bearer Token** field.

<img src="readme.img/credential_field.png" width="800" alt="Application Screenshot - Credential Field">

3.  Paste the key generated on the Notificações Inteligentes website.
4.  Save the settings.

<img src="readme.img/success_example.png" width="800" alt="Application Screenshot - Success">

5.  If there is any problem with the API key, an error message will appear.

<img src="readme.img/error_example.png" width="800" alt="Application Screenshot - Error">

> Your Custom Node is now ready to communicate securely with the API.

6.  If you have more than one organization, you can add more keys and organize the credentials according to each organization. To make identification easier, simply rename each credential.

<img src="readme.img/credential_rename.png" width="800" alt="Application Screenshot - Rename Credential">

---

## Testing the Connection

1.  Create a test action in the Custom Node, such as **Get All Integrations**.
2.  Execute the action.
3.  If everything is correct, you will see the data returned from the API.

<img src="readme.img/testing_token.png" width="800" alt="Application Screenshot - Testing Token">

> If any authentication error occurs, check if:
> *   The **Bearer Token** was copied correctly.
> *   The key has not expired.
> *   Your account has permission to access the chosen organization.

---

## ✅ Ready!

You can now use your **Custom Node** to create, edit, delete, or query custom variables securely using your **API Key (Bearer Token)**.

---

## **Node Idea: How it Works and What to Expect**

*   The **NI (Notificações Inteligentes) Custom Node** is a tool that allows you to integrate and automate some functionalities of your NI account directly into your workflows.
*   The **central idea** is that you can manipulate data from your NI platform (such as Integrations, Leads, Lists, Events, and Variables) using standardized operations (CRUD: Create, Read, Update, Delete). The key to this manipulation are **Unique Identifiers (IDs)**.

### Main Concepts:

*   **Operation Base:** Almost all operations in the Node revolve around an **ID**.
    *   To manage an **Integration**, you need its `ID`.
    *   To edit a **Lead**, you need the `Lead ID`.
    *   To add leads to a **List**, you need the `List ID` and the `Lead IDs`.
    *   And so on for Variables and Groups.

*   **Typical Workflow:**
    *   **Search/Search All:** You will often start by using an operation like "Get All Integrations" or "Get All Leads" to get a list of items and their respective **IDs**.
    *   **Use the ID:** Then, you will use this **ID** in a subsequent operation in the same flow (like "Edit Lead", "Rename an Integration", or "Add Leads to List") to perform the desired action on the specific item.

*   **Error Handling and Confirmations:**

    *   **Success Confirmation:** All creation, editing, and deletion operations are validated by the platform. When successful, they return an explicit confirmation message, ensuring the user that the action was completed as expected.

    <img src="readme.img/success_message.png" width="800" alt="Application Screenshot - Success Message">
    <img src="readme.img/update_message.png" width="800" alt="Application Screenshot - Update Message">
    <img src="readme.img/create_message.png" width="800" alt="Application Screenshot - Create Message">

    *   **Error Handling:** In case of failure, the node provides detailed and structured error responses, including:
        *   **Error Description:** A readable message explaining the nature of the problem.
        *   **HTTP Error Code:** The standard status code, allowing efficient technical debugging and the construction of robust conditional logic within the n8n flow.
    *   When related to an API-specific rule, in most cases it returns the detailed reason for the error, making it even clearer.

    <img src="readme.img/detailed_message_error.png" width="800" alt="Application Screenshot - Detailed Error">

    *   All errors return the error code. In the example below, it returned 404 (Not Found) because it didn't find any ID related to what we tried to delete in the account.

    <img src="readme.img/error_message.png" width="800" alt="Application Screenshot - Error Message">

*   **Additional Data:**
    *   Besides IDs, the Node allows working with a range of complementary (optional) data to enrich your automations, such as **Tags**, **Custom Variables**, **Filters**, and **Relationships**.
    *   In search fields, for example, where plausible, there is an option to receive additional data in the request.
    *   **Filters** allow filtering of data to be received. You can filter by one or more filters at the same time.

    <img src="readme.img/filters_example.png" width="800" alt="Application Screenshot - Filters Example">

    *   **Include Relationships** allows adding more data to be received by the API. More than one option can also be used for the search.

    <img src="readme.img/include_example.png" width="800" alt="Application Screenshot - Include Example">

In summary, the Node transforms the NI API into visual and intuitive blocks in n8n, where the main currency of operation are **IDs**, allowing you to build complex and personalized automations to manage your communication and contact base efficiently.

---

# NI NODE FUNCTIONS GUIDE

## Usage Guide - Integration (n8n)

The Integration resource allows you to create, search, update, and list integrations connected to your account directly from n8n.

### Available Operations

#### Create New Integration
Creates a new integration connecting your platform to the system.

**Required Fields:**
-   **Name:** Give a friendly name to identify the integration (e.g., "My Shopify Store").
-   **Platform:** Specify the platform (e.g., shopify-next, hotmart-v2, wooocommerce, etc). See the list of supported platforms in the field description. **Note:** Only integrations created with the `api-next` platform can add or remove leads from your lead list via the API.

**How to use:**
Select the "Create New Integration" operation, fill in the name and platform, and execute.
The integration will be created and listed in your panel.

#### Get All Integrations
Lists all integrations already registered in your account.

**No fields need to be filled in.**

Returns a list with all registered names and platforms.

**How to use:**
Select "Get All Integrations" and execute.
You will see the complete list of integrations.

#### Get Integration
Allows querying the detailed data of a specific integration.

**Required Fields:**
-   **ID:** The unique identifier of the integration you want to query (you can copy this ID when listing all integrations).

**Additional Parameters (optional):**
-   You can choose to include extra fields in the response, such as "Available Events", "Setup Fields", or "Checklist".
-   Just mark the ones you want detailed.

**How to use:**
Select "Get an Integration", enter the ID, select (if desired) any additional parameters, and execute.

#### Edit Integration Name
Updates the name of an existing integration.

**Required Fields:**
-   **ID:** The identifier of the integration you want to rename.
-   **New Name:** The new name to display in the panel.

**How to use:**
Select "Edit Integration Name", enter the ID and the new name, and execute.

#### Delete Integration
Permanently removes a Integration from the system.

**Required Field:**
-   **Lead ID:** Identifier of the integration to be removed.

**How to use:**
Select "Delete Integration", enter the Lead ID, and execute.
A confirmation message will be displayed if the operation is successful.

#### Special Fields
-   **Name:** Integration name (up to 100 characters).
-   **Platform:** Integration platform (consult the list in the field description).
-   **ID:** Unique integration identifier, usually provided when creating or listing integrations.
-   **Additional Parameters:** Check to include extra information in the integration search.

#### Tips
-   Use "Get All Integrations" to find the ID of the integration you want to edit or query.
-   Always check the required fields (marked with `*`) before executing.
-   For platforms, consult the examples in the field description to avoid typing errors.

[Additional information about Integrations in NI](https://ajuda.notificacoesinteligentes.com/pt-br/article/como-conectar-mrlog2/)

---

## Usage Guide - Leads (n8n)

The Leads resource allows you to register, search, edit, delete, and manage lists of leads (contacts) on your platform directly from n8n, with support for custom variables, tags, and advanced filters.

### Available Operations

#### Create Lead
Creates a new lead (contact) in the system.

**REQUIRED FIELDS:**
-   **Name:** Full name of the lead.
-   **Phone:** Phone number, including area code (DDD).
-   **Email:** Lead's email address.

**OPTIONAL FIELDS:**
-   **Notes:** Additional observations about the lead.
-   **Custom Variables:** Allows adding extra personalized variables for each lead (e.g., CPF, date of birth, etc.).
-   **Tags:** Add keywords to group or categorize leads (e.g., "VIP client", "prospect").

**HOW TO USE:**
Select the "Lead" Resource, then "Create". Fill in the required fields and, if desired, include notes, tags, or custom variables. Execute to register the lead.

**IMPORTANT POINTS:**
If you wish to add a custom variable, both the SLUG and VALUE are required. Both values can be accessed by searching for custom variables (Resource "Custom Variable" and Operation "Get All Custom Variables").

**ATTENTION:**
The `value` field of the custom variable must always be of the correct type for the custom variable. A custom variable of type CPF must contain a CPF, it cannot contain text.

#### Update Lead
Allows updating data of an existing lead.

**REQUIRED FIELDS:**
-   **Lead ID:** Identifier of the lead to be edited.
-   **Name:** Updated name of the lead.
-   **Email:** Updated email of the lead.

**OPTIONAL FIELDS:**
-   **Notes:** Update or add observations.
-   **Custom Variables:** Change or add custom variables.

**HOW TO USE:**
Select the "Lead" Resource, then "Update Lead". Fill in the required fields and, if desired, include notes or custom variables. Execute to update the lead.

#### Create or Update
Allows creating or updating data of an existing lead.

The API analyzes the provided phone number to determine if the lead exists or not. If the lead doesn't exist, a new lead is created. If the lead exists, it is updated with the new data provided.

**REQUIRED FIELDS:**
-   **Name:** Name of the lead.
-   **Phone:** Phone number of the lead.

**OPTIONAL FIELDS:**
-   **Email:** Email of the lead.
-   **Notes:** Update or add observations.
-   **Custom Variables:** Change or add custom variables.
-   **Tags:** Add tags to the lead. Attention: If the lead already exists, the update operation will not add tags to it.

**HOW TO USE:**
Select the "Lead" Resource, then "Create or Update". Fill in the required fields and, if desired, include notes, tags, or custom variables. Execute to create or update the lead.

#### Get All Leads
Lists all leads registered in the system.

**Optional Fields:**
-   **Filters:** Allows filtering by name, phone, email, or tag.
-   **Include Relationships:** Check to bring related data, such as lists, tags or list sources.

**How to use:**
Select "Get All Leads", define the desired filters (or leave blank to list all) and execute.

#### Get Lead by ID
Returns the complete data of a specific lead from its unique identifier.

**Required Fields:**
-   **Lead ID:** Enter the ID of the desired lead (can be obtained by listing all).

**Optional Fields:**
-   **Include Relationships:** Choose to bring related lists or tags.

**How to use:**
Select "Get Lead by ID", enter the Lead ID, and if desired, mark the relationships to include. Execute to see complete details.

#### Delete Lead
Permanently removes a lead from the system.

**Required Field:**
-   **Lead ID:** Identifier of the lead to be removed.

**How to use:**
Select "Delete Lead", enter the Lead ID, and execute.
A confirmation message will be displayed if the operation is successful.

#### Add Lists to a Lead
Associates one or more lists with the specified lead.

**Required Fields:**
-   **Lead ID:** Lead identifier.
-   **List ID(s):** IDs of the lists to associate (e.g., 1234, 5678).

**How to use:**
Select "Add Lists to a Lead", enter the Lead ID and the lists (separated by commas). Execute to associate.

#### Remove Lists from a Lead
Removes one or more lists associated with the lead.

**Required Fields:**
-   **Lead ID:** Lead identifier.
-   **List ID(s):** IDs of the lists to remove (e.g., 1234, 5678).

**How to use:**
Select "Remove Lists from a Lead", enter the Lead ID and the list IDs. Execute to remove.

### Special Fields
-   **Custom Variables:** Allows adding slug/value pairs to the lead (e.g., slug="cpf", value="123.456.789-00").
-   **Tags:** Keywords for grouping leads, entered as a list.
-   **Filters:** Search fields to filter leads by name, phone, email, or tag.
-   **Include Relationships:** Choose to bring along lists, tags, users, and other information connected to the lead.
-   **List ID(s):** List IDs separated by commas, used to add or remove multiple lists at once.

### Tips
-   Use "Get All Leads" to find a lead's ID.
-   For fields like lists, separate IDs by commas and do not use extra spaces.
-   The system requires mandatory fields, but take advantage of optional fields to better detail your lead and facilitate automations.
-   Custom variables are ideal for your business-specific data.
-   Always review data before performing deletion actions, as they are irreversible.

[Additional information about Leads in NI](https://ajuda.notificacoesinteligentes.com/pt-br/article/gerenciamento-de-leads-1x8lj7m/)

---

---

## Usage Guide - Events (n8n)

The Events resource allows creating and sending different types of events to integrations, such as: abandoned cart, invoices, payments, cancellations, deliveries, NPS, member access, and password reset, among others. Ideal for automations and intelligent notifications in your flow.

### Available Operations

#### Create Abandoned Cart Event
Sends an event to notify about an abandoned shopping cart.

**Required Fields:**
-   Integration ID
-   Customer data (name, phone)
-   Order products (name, quantity, value)

**Optional Field:**
-   Cart/checkout data (URL, ID)

#### Create Printed Billet Event
Notifies that an invoice was generated and printed for the customer.

**Required Fields:**
- Customer data (name, phone)
- Order data (ID, values, status, discounts, products)

**Optional Field:**
-   Address data

#### Create Event for Canceled, Paid, Refunded, Delivered, Dispatched, Processing, Out for Delivery, Status Updated, Awaiting Pickup, or Awaiting Payment Order
Each event records a different order status, always including:

**Required Fields:**
-   Customer data
-   Order data (ID, values, status, discounts, products)
-   Payment details (billet, pix, etc.) according to the event type

**Optional Field:**
-   Address and delivery data

#### Create Member Access Granted Event
Sends access data for members.

**Required Fields:**
-   Customer data
-   Member page URL, login, and temporary password
-   Products associated with the access

#### Create Password Reset Event
Notifies the customer with the link to reset their password.

**Required Fields:**
-   Customer data
-   Password reset URL

#### Create NPS (Satisfaction Survey) Event
Involves two separate events:

##### Create NPS Response Event
Records the score, comment, and date of the customer's satisfaction response after they answer an NPS survey.

**Required Fields:**
-   Customer data
-   Score given by the customer
-   (Optional: comment and response date)

##### Create NPS Survey Event
Sends an event to trigger the NPS survey link to the customer.

**Required Fields:**
-   Customer data
-   Survey URL (surveyurl)

### Important Common Fields
-   **Customer Data:** Always include first name, phone, email, CPF/CNPJ, currency, gender, date of birth, IP.
-   **Products:** Name, quantity, and value of products (can add several).
-   **Address:** City, country, neighborhood, number, ZIP code, state, street, complement.
-   **Order:** ID, values (total, discount, products_total), status.
-   **Delivery:** Shipping cost, description, tracking code, tracking URL, estimated delivery date, message.
-   **Payment (invoice/Pix):** Links, codes, values, and specific dates.
-   **NPS:** Score, comment, response date, or survey URL.
-   **Member Access:** URLs, login, password, and access products.
-   **Password Reset:** URL to reset.

### Tips
-   Always fill in all required fields for each operation, respecting suggested formats (e.g., dates, currency).
-   For product or address lists, use the "Add product data" or "Additional Parameters" option.
-   The system validates: blank required fields block execution!
-   In the case of PIX events, check the correct payment method option to show specific fields.
-   Grouped fields (like "checkout", "addressparameter", "deliveryparameter") must be expanded to enter detailed data.
-   Use the event corresponding to the actual order/action status.

[Additional information about Events in NI](https://ajuda.notificacoesinteligentes.com/pt-br/article/eventos-1n02369/)

#### If you haven't found what you're looking for, take a look at our [Help Center](https://ajuda.notificacoesinteligentes.com/pt-br/).
