## User Stories

### Viewing and Navigation

| User Story | Relevant Feautures | Result |
|------------|----------|--------|
| Easily navigate the site and find the products that I need. | Intuitive site layout, consistent menu placements, and clearly labeled sections. | Users can quickly find what they're looking for with minimal clicks. |
| View a category of products/filter products to find specific items I am interested in. | Filters and sorting options available on products page. | Users can refine their searches and browse relevant products efficiently. |
| View more detail on products and read their descriptions. | Product detailpage with detailed descriptions | Users understand what they're buying and feel confident in their choices. |
| View a close-up of a product image. | Zoom-in functionality | Users see detailed product features and quality up-close to make informed decisions. |
| View my running total of purchases throughout my visit. | Shopping cart widget with a running total displayed on all pages. | Users keep track of spending and manage their budget during their shopping session. |
| View the items I currently have selected for purchase and adjust the shopping bag if needed. | Editable shopping cart with options to modify or remove items. | Users tailor their final order with ease, increasing satisfaction and reducing cart abandonment. |
| Add products to a wishlist. | Wishlist feature allowing users to save items for later. | Users can bookmark items of interest to revisit and purchase at a later time. |


### Registration and User Accounts
| User Story | Relevant Features | Result |
|------------|----------|--------|
| Register for an account and view my profile. | Registration form and user profile page. | Users easily create an account and access their personal dashboard. |
| Receive an email to confirm my registration. | Automated email system that sends confirmation upon successful registration. | Users receive immediate verification of their account setup and can confirm their email address. |
| Log in and out to keep my account information secure. | Secure login/logout functionality with session management. | User sessions are protected, enhancing security and privacy. |
| View a profile page, set a default delivery address, and view previous purchases. | Profile management features that allow users to update personal details and view order history. | Users manage their shipping preferences and track past activities conveniently. |
| Reset my password. | Password reset feature with email verification. | Users recover access to their accounts securely in case of forgotten passwords. |


### Sorting and Searching
| User Story |Relevant Features | Result |
|------------|----------|--------|
| Sort the list of available products by categories, size, price, and brand. | Drop-down menus and sorting options on products page. | Users find products that meet their needs and preferences more quickly. |
| Search for a product by name or description. | Search bar on the top of ech page | Users locate specific items efficiently using intuitive search capabilities. |



### Purchasing and Checkout
| User Story | Relevant Features | Result |
|------------|----------|--------|
| View items in my bag to be purchased. | Detailed shopping bag view page that shows all items and prices. | Users review their intended purchases clearly, reducing errors. |
| Adjust the bag and make changes to my purchase before checkout. | Options to change quantity or remove items directly in the shopping bag. | Users customize their order to their satisfaction before finalizing the purchase. |
| Easily enter my payment information. | Secure payment form with debit/credit card option | Users enter their payment details in a straightforward and secure manner. |
| Feel that my personal and payment information is safe and secure. | SSL certification, secure payment gateways, and privacy policies in place. | Users trust the site with their data|
| View an order confirmation after checkout to verify that I haven't made any mistakes. | Order summary page and confirmation details before final submission. | Users confirm details are correct, reducing post-purchase customer service issues. |
| Receive an email confirmation after checking out. | Automated email system that sends a detailed receipt after purchase. | Users have immediate written confirmation of their purchase for their records. |


### Admin and Store Management

| User Story | Relevant Features | Result |
|------------|----------|--------|
| Add a product - add new items to my store. | Admin panel with a form to submit new product details. | Store administrators can quickly expand their inventory. |
| Edit/update a product - change product prices, descriptions, images, and other product criteria. | Editable product listings within the admin dashboard. | Store administrators keep the product listings up-to-date with minimal effort. |
| Delete a product - remove items that are no longer for sale. | Option to delete products directly in the admin interface. | Store administrators manage and store's products effectively. |











## Bugs and issues

| No  |  Issue |  Solution |
|---|---|---|
| 1  |![product page not dispalying](./docs/products_page_access.png)  Django template loader could not find the 'products/products.html'   |  Used pathlib path instead of os.path for template DIRS and added '/'. Credit goes to my hackathon teammate Tomislav Dukanez. I remembered him mentioning lack of '/' causing problems in Django and decided to try putting it in the syntax. It worked and the explanation of the pathlib path was found on ChatGPT 4 and [Python Documentation](https://www.python.org)|
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |