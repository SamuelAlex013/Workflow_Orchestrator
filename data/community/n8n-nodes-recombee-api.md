![Banner image](https://user-images.githubusercontent.com/10284570/173569848-c624317f-42b1-45a6-ab09-f0ea3c247648.png)

# n8n-nodes-recombee

This is an n8n community node that lets you integrate [Recombee's AI-powered recommendation engine](https://www.recombee.com/?ref=n8n-nodes-recombee-api) into your n8n workflows. Recombee provides powerful personalization capabilities for various use cases including e-commerce, content recommendations, and more.

[n8n](https://n8n.io/) is a [fair-code licensed](https://docs.n8n.io/reference/license/) workflow automation platform.

[Installation](#installation)  
[Operations](#operations)  
[Credentials](#credentials)  
[Compatibility](#compatibility)  
[Usage](#usage)  
[Resources](#resources)

## Installation

Follow the [installation guide](https://docs.n8n.io/integrations/community-nodes/installation/) in the n8n community nodes documentation.

## Operations

This package includes the following nodes for integrating with Recombee's recommendation engine:

### User Management Nodes

#### Add User [API Ref](https://docs.recombee.com/api#add-user)

Adds a new user to the database with the given userId. Users are specified using unique string identifiers that can contain digits, Latin letters, underscores, colons, minus signs, at signs, and dots. This operation is essential for building user profiles and enabling personalized recommendations.

#### Delete User [API Ref](https://docs.recombee.com/api#delete-user)

Deletes a user of the given userId from the database. If there are any purchases, ratings, bookmarks, cart additions or detail views made by the user present in the database, they will be deleted in cascade.

#### Get User Values [API Ref](https://docs.recombee.com/api#get-user-values)

Gets all the current property values of the given user.

#### List Users [API Ref](https://docs.recombee.com/api#list-users)

Gets a list of IDs of users currently present in the catalog.

#### Set User Values [API Ref](https://docs.recombee.com/api#set-user-values)

Sets/updates (some) property values of the given user. The properties (columns) must be previously created by Add user property. This operation is essential for maintaining up-to-date user profiles.

### Item Management Nodes

#### Add Item [API Ref](https://docs.recombee.com/api#add-item)

Adds new item of the given itemId to the items catalog. Items are specified using unique string identifiers with the same format as user IDs. This operation is fundamental for building your recommendation catalog and enabling item-based recommendations.

#### Delete Item [API Ref](https://docs.recombee.com/api#delete-item)

Deletes an item of the given itemId from the catalog. If there are any purchases, ratings, bookmarks, cart additions, or detail views of the item present in the database, they will be deleted in cascade as well. Also, if the item is present in some series, it will be removed from all the series where present. If an item becomes obsolete/no longer available, it is often meaningful to keep it in the catalog (along with all the interaction data, which are very useful) and only exclude the item from recommendations using a filter.

#### Get Item Values [API Ref](https://docs.recombee.com/api#get-item-values)

Gets all the current property values of the given item.

#### List Items [API Ref](https://docs.recombee.com/api#list-items)

Gets a list of IDs of items currently present in the catalog.

#### Set Item Values [API Ref](https://docs.recombee.com/api#set-item-values)

Sets/updates (some) property values of the given item. The properties (columns) must be previously created by Add item property. This operation is essential for maintaining an up-to-date item catalog.

### Interaction Tracking Nodes

#### Add Bookmark [API Ref](https://docs.recombee.com/api#user-item-interactions-bookmarks-add-bookmark)

Adds a bookmark of the given item made by the given user. Bookmarks indicate strong user interest and help improve recommendation accuracy. This operation is useful for tracking saved or favorited(liked) items.

#### Add Cart Addition [API Ref](https://docs.recombee.com/api#add-cart-addition)

Adds a cart addition of the given item made by the given user. Cart additions indicate purchase intent and help improve recommendation accuracy. This operation is essential for tracking shopping behavior.

#### Add Detail View [API Ref](https://docs.recombee.com/api#add-detail-view)

Adds a detail view of the given item made by the given user. Detail views are crucial for understanding user behavior and improving recommendation accuracy.

#### Add Purchase [API Ref](https://docs.recombee.com/api#add-purchase)

Adds a purchase of the given item made by the given user. Purchases are strong signals for recommendation algorithms and help improve recommendation accuracy. This operation is essential for tracking successful transactions.

#### Add Rating [API Ref](https://docs.recombee.com/api#add-rating)

Adds a rating of the given item made by the given user. Ratings are strong signals for recommendation algorithms and help improve recommendation accuracy. This operation is essential for collecting user feedback.

#### Delete View Portion [API Ref](https://docs.recombee.com/api#delete-view-portion)

Deletes an existing view portion uniquely specified by userId, itemId, sessionId and timestamp or all the view portions with the given userId, itemId and sessionId if timestamp is omitted.

#### Set View Portion [API Ref](https://docs.recombee.com/api#set-view-portion)

Sets viewed portion of an item (for example a video or article) by a user (at a session). If you send a new request with the same (userId, itemId, sessionId), the portion gets updated.

### List Interaction Nodes

#### List Item View Portions [API Ref](https://docs.recombee.com/api#list-item-view-portions)

Lists all the view portions of the given item ever made by different users (with different sessionIds).

#### List User View Portions [API Ref](https://docs.recombee.com/api#list-user-view-portions)

Lists all the view portions of different items ever made by the given user (at given sessionId).

### Recommendation Nodes

#### Recommend Item Segments To User [API Ref](https://docs.recombee.com/api#recommend-item-segments-to-user)

Recommends set of item segments that are the most relevant for a given user.

#### Recommend Items To Item [API Ref](https://docs.recombee.com/api#recommend-items-to-item)

Recommends set of items that are somehow related to one given item, X. Typical scenario is when the user looks at a page of item X and you want to display items somehow related to X to the user on this page. The returned items are sorted by relevance (first item being the most relevant).

#### Recommend Items To User [API Ref](https://docs.recombee.com/api#recommend-items-to-user)

Recommends set of items for a given user (not user segment). Generates personalized item recommendations for a specific user based on their interaction history and preferences. This is the core recommendation operation that powers personalized suggestions.

#### Recommend Next Items [API Ref](https://docs.recombee.com/api#recommend-next-items)

Returns items that shall be shown to a user as next recommendations when the user browsed some items already. It can be used in a scenario when the user watches some TV series, and you want to recommend another episode or movie to the user.

#### Recommend Users To Item [API Ref](https://docs.recombee.com/api#recommend-users-to-item)

Recommends set of users that are somehow related to a given item.

#### Recommend Users To User [API Ref](https://docs.recombee.com/api#recommend-users-to-user)

Recommends set of users that are somehow related to a given user.

### Search Nodes

#### Search Item Segments [API Ref](https://docs.recombee.com/api#search-item-segments)

Full-text personalized search for item segments. The results are based on the provided searchQuery and additionally personalized for the given userId.

#### Search Items [API Ref](https://docs.recombee.com/api#search-items)

Full-text personalized search. The results are based on the provided searchQuery and additionally personalized for the given userId. It searches only among items that were already at least once uploaded with Set item values or Add item. It does not perform any structural filtering like the recommendation endpoints do, so you have to use the filter parameter to restrict the items to those you want to search in.

### Series Management Nodes

#### Add Series [API Ref](https://docs.recombee.com/api#add-series)

Adds new series of the given seriesId. Series are interpreted in Recombee as (possibly ordered) sequences of items.

### Database Management Nodes

#### Reset Database [API Ref](https://docs.recombee.com/api#reset-database)

Completely erases all your data, including items, item properties, series, user database, user properties, and all kinds of interactions (purchases, ratings, bookmarks, detail views, and cart additions).

## Credentials

To use these nodes, you need:

1. A Recombee account (sign up at [recombee.com](https://www.recombee.com/))
2. Your Recombee database ID
3. Your Recombee secret token

You can find these credentials in your Recombee dashboard under the API section.

## Compatibility

- Latest n8n version: 1.96
- Tested with n8n versions: 1.96
- Requires Node.js version 20 or higher

## Usage

### Basic Data Synchronization

#### User Synchronization

This workflow syncs user data from your system to Recombee:

1. Trigger: Schedule (daily sync) or Webhook (when user data changes)
2. Set User Values
   ```json
   {
   	"userId": "user123",
   	"values": {
   		"name": "John Doe",
   		"email": "john@example.com",
   		"preferences": ["electronics", "books"],
   		"lastActive": "2024-03-20T10:00:00Z",
   		"subscriptionTier": "premium"
   	}
   }
   ```

#### Product/Item Synchronization

This workflow syncs product catalog from your system to Recombee:

1. Trigger: Schedule (daily sync) or Webhook (when product data changes)
2. Set Item Values
   ```json
   {
   	"itemId": "product123",
   	"values": {
   		"name": "Wireless Headphones",
   		"category": "electronics",
   		"price": 199.99,
   		"brand": "TechBrand",
   		"inStock": true,
   		"tags": ["audio", "wireless", "bluetooth"],
   		"lastUpdated": "2024-03-20T10:00:00Z"
   	}
   }
   ```

### Basic Recommendation Workflow

1. Add a Recombee credential
2. Use the "Add User" node to create a user
3. Use the "Add Item" node to add items to your catalog
4. Use interaction nodes to record user behavior
5. Use recommendation nodes to get personalized suggestions

### Example Workflows

#### 1. Content Recommendation System

This workflow helps an AI agent recommend relevant content to users:

1. Trigger: Webhook (when user requests content recommendations)
2. Get User (retrieve user profile)
3. Recommend Items to User (get personalized content suggestions)
   - Use `scenario` parameter to specify recommendation context
   - Use `filter` to exclude already viewed content
4. HTTP Request (send recommendations to AI agent)
5. AI Agent processes recommendations and generates personalized response

#### 2. E-commerce Product Discovery

This workflow enables an AI shopping assistant to help users find products:

1. Trigger: Webhook (when user views a product page)
2. Add Detail View (record current product view)
3. Recommend Items to Item (find related products)
   - Use `targetUserId` to personalize based on user history
   - Use `filter` to exclude out-of-stock items
4. AI Agent combines results to provide comprehensive recommendations

#### 3. Content Personalization Engine

This workflow helps an AI agent personalize content delivery:

1. Trigger: Schedule (daily content update)
2. Recommend Items to Item Segment (find content for specific segments)
   - Use `scenario` to specify different recommendation strategies
   - Use `filter` to apply business rules
3. AI Agent analyzes trends and generates personalized content strategy

#### 4. User Behavior Analysis

This workflow helps an AI agent understand user preferences:

1. Trigger: Webhook (when user interacts with content)
2. Add Detail View (record the interaction)
3. Add Rating (if user provides feedback)
4. List User Detail Views (analyze user behavior)
5. AI Agent analyzes behavior patterns and adjusts recommendations

#### 5. Multi-Channel Recommendation System

This workflow enables an AI agent to provide consistent recommendations across platforms:

1. Trigger: Webhook (when user interacts on any platform)
2. Add Detail View (record the interaction)
3. Recommend Items to User (get personalized suggestions)
   - Use `scenario` to specify platform-specific recommendations
   - Use `filter`
