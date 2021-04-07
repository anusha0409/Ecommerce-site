# OOPS_Project
* Consumers will be looking for the ability to easily filter items by dietary preference 
* category pages and search results to adapt based on their personal browsing and purchase history. 
* (Android/Web based/Stand-alone) for e-marketing that connects customers (individuals who shop
for home purpose) to retailers (people dealing with multiple items who stores items in large
quantities) and retailers to wholesalers (warehouse maintaining people) with the below mentioned
mandatory functionalities
## Hierarchy of Users:
Customers -> Retailers -> Wholesalers
## Roles of Users: (Mandatory but not limited to)
* Customers: selection of items (by search, by using filters or by browsing), adding to cart,
place order, payment of order, feedback/queries.
* Retailers: adding new items, deleting items, deciding the price of items while adding,
maintaining record of each customer (items they have bought, transactions they have done
till now etc..), update item quantities (after every order placed by customer), place order,
order payment, feedback/queries, etc.
* Wholesalers: adding new items, deleting items, deciding the price of items while adding,
adding or deleting retailers, maintaining record of each retailer (items they have bought,
transactions they have done till now etc..), items that they supply to the retailers, update
item quantities (after every order placed by retailer) etc.


Functionalities:
## Module 1: Registration and Sign-Up
Registration and signup using username and password or any social media (Gmail, Facebook login
or Instagram)
Login must be done using OTP verification (phone/email) every time.
A Customer can belong to any one or multiple user categories.
* Registration page should have (but not limited to) following fields:
username, password, retype password, type of user Select one of three, Location (better if
enabled with Google API)
* Signup Page

## Module 2: Dashboards for every type of users
Dashboard should have all categories of items food and other items (Vegetables, Readymade
foods, grocery). Feel free to identify your categories and sub-categories.
When pressed on a category, user must navigate to a page having various options/ items for that
particular category.
Every item should have the following fields: cost, in stock/not in stock, if not in stock will be
available at what date next. (Same as all e-commerce sites)
All categories and items of the category should be represented with appropriate images.

## Module 3: Search Module/Navigation Module
Once the user selects the item with required quantity, API must show all the shops having the
required quantity with location, cost per unit and total cost.
Include a location distance filter and all the shops should be listed area wise. (should have but not
limited to)

## Module 4: Place order and status of order
User (Customer/ Retailer) can make the purchase either online or offline mode.
If purchase is to be made offline mode, the time and date should be stored as an event in calendar
and the event should be notified to the user before 30 minutes. You can think of notifying the
retailer that XYZ customer on XX date would be coming to buy ABC item.
If order is placed in online mode, Tracking details should appear on both the customers and
retailers’ dashboard. Details such as name of the delivery person along with his phone number,
tentative delivery date should appear on both the user and retailers or (retailers and wholesalers)
dashboard.
The same should be sent to the user mobile phone/e-mail.
Once the order is placed by user/retailer there should be an updating of quantities on
retailer/wholesaler pages respectively. Cancellation option can be provided.
After placing the order, the status of the order should be updated periodically (Order placed/ Order
Dispatched/ In transit/ Delivered). The status should be shown and updated periodically on the
dashboard of the users.

# Module 5: Feedback and Queries
After placing the order, the status of the order should be updated periodically (Order placed/ Order
Dispatched/ In transit/ Delivered). The status should be shown and updated periodically on the
dashboard of the Customer/Retailer/Wholesaler.
After delivery of the product, a SMS/e-mail should be sent to the user using the registered mobile
number/e-mail id for feedback of the product and delivery as well.
The feedback of the product has to be updated periodically on the page of the concerned item.
If multiple items are orders, feedback has to be taken for each product individually
