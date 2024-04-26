Go back to the [README.md](README.md) file


## Code Validation

### HTML

- [W3C Markup Validator](https://validator.w3.org/)

I used W3C Validator to test all HTML pages. Initially, the validator showed two stray tags on a home page.The remaining errors are a result of using a Jinja template.

Screenshots of the results can be found within the documentation folder. [html validation screenshots](docs/html_validation)


### CSS

- [W3C CSS Validator](https://jigsaw.w3.org/css-validator/)

I used W3C CSS Validator for the CSS. No errors were shown.

Screenshots of the results can be found within the documentation folder. [css validation screenshots](docs/css_validation)






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

### Full Manual Testing

I have performed full manual testing on these devices:

- DELL Inspiron 16 laptop
- DELL Optiplex 2
- Iphone 11
- Samsung Galaxy A52 S

The app has been tested on the following browsers:

- Google Chrome 
- Microsoft Edge
- Safari
- Mozilla Firefox 



| **FEATURE** | **EXPECTED OUTCOME** | **TESTING PERFORMED** | **RESULT** | **PASS/FAIL** |
| --- | --- | --- | --- | --- |
| `Navbar` |
| **Navigation Bar Responsiveness** | Navbar should collapse into a hamburger menu on small screens and expand on larger screens | Resize the browser window to various widths to test responsive behavior | Navbar collapses and expands appropriately at breakpoints | PASS |
| **Home Link in Navbar** | Clicking on the logo redirects to the home page | Clicked on the main logo link | Redirected to the home page | PASS |
| **Search Functionality** | Typing and submitting in the search box should lead to a product search results page | Typed a query into the search box and pressed enter | Redirected to the product results page with relevant product listings | PASS |
| **My Account Dropdown Accessibility** | Dropdown should be accessible and show options based on user authentication status | Checked dropdown both as a guest and as a logged-in user | Correct options displayed under different authentication states | PASS |
| **Register/Login Links** | Clicking on these links should redirect to the respective authentication pages | Clicked on both links | Successfully redirected to the register and login pages | PASS |
| **Logout Functionality** | Clicking 'Logout' should log the user out and redirect them to a page indicating they are logged out | Clicked logout | Logged out and saw a confirmation message | PASS |
| **Wishlist Access** | Authenticated users should be directed to the wishlist page after clicking the 'Wish List'. Unauthenticated users should be redirected to log in.| Clicked on 'Wish List' as authenticated and unauthenticated users. | Authenticated users successfully directed to the wishlist page whereas unauthenticated ones were redirected to log in. | PASS |
| **Shopping Bag Access** | Clicking on the shopping bag icon should direct to the shopping bag | Clicked on the shopping bag icon | Redirected to the shopping bag page | PASS |
| **Responsive Main Nav** | All products and categories dropdowns should work correctly across devices | Tested dropdown functionality on multiple devices | Dropdowns operate correctly in all tested scenarios | PASS |
| **Delivery Banner** | Banner displaying free delivery threshold should be visible on all pages | Navigated through various pages | Delivery banner consistently visible | PASS |
| **Message Toasts Functionality** | Toast messages should appear for user actions like add to wishlist or sign out | Performed actions that trigger toasts | Toast messages appeared appropriately | PASS |
| `Navbar Dropdowns` |
| **All Products Dropdown** | Dropdown should display options for sorting and viewing all products | Clicked on "All Products" to view dropdown menu | Dropdown displayed with options: By Price, By Brand, By Size, By Category, All Products | PASS |
| **All Products - By Price** | Redirect to products sorted by price in ascending order | Selected "By Price" from dropdown | Redirected to product page sorted by price ascending | PASS |
| **All Products - By Brand** | Redirect to products sorted by brand in ascending order | Selected "By Brand" from dropdown | Redirected to product page sorted by brand ascending | PASS |
| **All Products - By Size** | Redirect to products sorted by size in ascending order | Selected "By Size" from dropdown | Redirected to product page sorted by size ascending | PASS |
| **All Products - By Category** | Redirect to products sorted by category in ascending order | Selected "By Category" from dropdown | Redirected to product page sorted by category ascending | PASS |
| **All Products - View All** | Redirect to page displaying all products | Selected "All Products" from dropdown | Redirected to page displaying all products | PASS |
| **Clothing Dropdown** | Dropdown should list specific clothing categories and an option to view all clothing | Clicked on "Clothing" to view dropdown menu | Dropdown displayed with options: Dresses, Tops, Trousers, Coats, All Clothing | PASS |
| **Clothing - Dresses** | Redirect to page displaying dresses | Selected "Dresses" from dropdown | Redirected to dresses category page | PASS |
| **Clothing - Tops** | Redirect to page displaying tops | Selected "Tops" from dropdown | Redirected to tops category page | PASS |
| **Clothing - Trousers** | Redirect to page displaying trousers | Selected "Trousers" from dropdown | Redirected to trousers category page | PASS |
| **Clothing - Coats** | Redirect to page displaying coats | Selected "Coats" from dropdown | Redirected to coats category page | PASS |
| **Clothing - View All Clothing** | Redirect to page displaying all clothing items | Selected "All Clothing" from dropdown | Redirected to page showing all clothing items | PASS |
| **Shoes & Accessories Dropdown** | Dropdown should list specific accessory categories and options to view each | Clicked on "Shoes & Accessories" to view dropdown menu | Dropdown displayed with options: Shoes, Jewellery, Bags, Hats | PASS |
| **Shoes & Accessories - Shoes** | Redirect to page displaying shoes | Selected "Shoes" from dropdown | Redirected to shoes category page | PASS |
| **Shoes & Accessories - Jewellery** | Redirect to page displaying jewellery | Selected "Jewellery" from dropdown | Redirected to jewellery category page | PASS |
| **Shoes & Accessories - Bags** | Redirect to page displaying bags | Selected "Bags" from dropdown | Redirected to bags category page | PASS |
| **Shoes & Accessories - Hats** | Redirect to page displaying hats | Selected "Hats" from dropdown | Redirected to hats category page | PASS |
| **Occasions Dropdown** | Dropdown should list occasion-specific categories like weddings, ball gowns | Clicked on "Occasions" to view dropdown menu | Dropdown displayed with options: Wedding, Ball Gowns | PASS |
| **Occasions - Wedding** | Redirect to page displaying wedding-appropriate items | Selected "Wedding" from dropdown | Redirected to wedding category page | PASS |
| **Occasions - Ball Gowns** | Redirect to page displaying ball gowns | Selected "Ball Gowns" from dropdown | Redirected to ball gowns category page | PASS |
| `Home Page` |
| **Page Load** | The homepage should load without any errors and display all content correctly. | Accessed the website's homepage. | Homepage loaded successfully with all content displayed as expected. | PASS |
| **Navigation Bar** | The navigation bar should function correctly, providing access to all linked pages. | Clicked on each link in the navigation bar. | Each link directed to the correct page. | PASS |
| **Page Heading and Subheading on Small Screens** | Heading and subheading should be visible only on xs to md screens. | Viewed the page on small screens to check visibility. | Heading and subheading are properly displayed only on xs to md screens. | PASS |
| **Shop Now Button** | Clicking the 'Shop Now' button should redirect the user to the products page. | Clicked the 'Shop Now' button. | Redirected to the products page correctly. | PASS |
| **Logo and Button Layout on Large Screens** | On large screens, the logo and the button should be next to each other. | Viewed the homepage on a large screen. | Logo and button are correctly displayed next to each other. | PASS |
| **Interactive Logo Flip on Click** | The logo should flip to reveal text on the back when clicked. | Clicked the logo to activate the flip effect. | Logo flipped correctly, revealing the text on the back. | PASS |
| **Accessibility of Flip Container** | The flip container should be easily clickable and should toggle its state on each click. | Repeatedly clicked the flip container. | Flip action worked correctly with each click. | PASS |
| **Vertical Stacking on Smaller Screens** | On smaller screens, the logo and 'Shop Now' button should stack vertically. | Checked the layout on smaller devices. | Elements are stacking vertically as expected. | PASS |
| **Text Visibility in Flip Container** | Text in the flip container should be clear and legible. | Observed the text in both front and back states of the flip container. | Text is clear and legible in both states. | PASS |
| `Footer` |
| **Footer Visibility** | The footer should always be visible at the bottom of every page. | Scrolled to the bottom on various pages to check visibility. | Footer was consistently visible across all pages. | PASS |
| **Social Media Links** | Links should correctly redirect to the respective social media pages. | Clicked each social link to ensure it opens the correct page. | All links redirected correctly to the specified social media platforms. | PASS |
| **Link Targeting** | Social media links should open in a new tab. | Clicked on social media links to check `target="_blank"`. | Each link opened in a new tab as expected. | PASS |
| **Conditional Styling** | Icons should switch styles between light and dark based on the current path. | Checked icons on the homepage and other pages. | Icons correctly displayed light style on the homepage and dark style on other pages. | PASS
| `Products Page` |
| **Page Load** | The page should load without errors and display products, sorting options, and category links. | Loaded the page and observed for any errors or misloads. | Page loaded successfully with all elements displayed correctly. | PASS |
| **Product Display** | Each product should display an image, name, price, size (if it has one) and available actions (wishlist, add to bag). | Checked several product cards for necessary information. | All products correctly displayed their respective details. | PASS |
| **Sorting Functionality** | Changing the sorting options should reorder products based on the selected criteria. | Selected each sorting option from the dropdown and observed the reordering of product listings. | Products were reordered correctly for each selected sorting option. | PASS |
| **Category Links** | Clicking on a category badge should filter the products according to that category. | Clicked on each category badge and checked if only relevant products are shown. | Products were filtered correctly according to selected categories. | PASS |
| **Product Details Link** | Clicking on a product image or name should redirect to the product's detail page. | Clicked on product images and names. | Correctly redirected to the detailed product page for each selected product. | PASS |
| **Add to Wishlist** | Requires login for unauthenticated users. Clicking the wishlist button should add the item to the user’s wishlist and the button heart icon should change to red. Toast message 'Item added to your wishlist' should appear. Unathenticated users should be directed to the login page  | Clicked the wishlist button as both authenticated and unauthenticated user. | Functioned correctly: redirected to login when not authenticated, and added to wishlist when logged in. The right message appeared and the heart icon color changed to red. | PASS |
| **Remove from Wishlist**| Clicking the wishlist button again for the same product should remove the product from the wishlist and turn the button heart icon back to dark brown. Toast message 'Item removed from your wishlist should appear'| Clicked the wishlist button for the same product again | Item was removed from the wishlist and the correct message appeared. The button heart icon went back to dark brown color. | PASS |
| **Add to Bag** | Clicking the add to bag button should add the item to the shopping bag. | Clicked on the add to bag button for multiple products. | Items were successfully added to the shopping bag. | PASS |
| **Add to Bag - Already Added**     | Clicking the add to bag button for an item already in the bag should should prevent duplication and notify the user that the item is already in the bag.| Clicked the add to bag button for an item already in the shopping bag. | Correctly notified that the item was already in the bag and did not add a duplicate.  | PASS          |
| **Back to Top Button** | Clicking the "Back to Top" button should scroll the page back to the top. | Clicked the button after scrolling down on the page. | Page scrolled back to the top smoothly. | PASS |
| `Product Detail Page` |
| **Page Load** | The page should load without any errors, displaying detailed information about a specific product. | Accessed the product detail page for several products. | All product details loaded correctly without errors. | PASS |
| **Product Image Display** | The product image should be displayed prominently. If clicked, a modal with a larger image should appear. | Clicked on the product image to trigger the modal. | The modal displayed the image correctly and closed without issues. | PASS |
| **Product Information Display** | Product name, brand, description, price, and category should be displayed accurately. | Reviewed the displayed information for accuracy against expected values. | All information was correct and well-formatted. | PASS |
| **Category Link** | Clicking the category link should filter the products page by the selected category. | Clicked on the category link. | Redirected to the filtered products page showing only products from that category. | PASS |
| **Size Display** | If a product has a size, it should be displayed. If not, the size information should be omitted. | Checked products both with and without size information. | Size displayed correctly where applicable; omitted where not applicable. | PASS |
| **Superuser Actions** | Superusers should see "Edit" and "Delete" buttons. Clicking these should lead to respective actions. | Tested with a superuser account. | "Edit" and "Delete" buttons worked as expected. | PASS |
| **Keep Shopping Button** | Clicking this button should take users back to the products page. | Clicked the "Keep Shopping" button. | Redirected to the products page. | PASS |
| **Add to Wishlist** | Authenticated users should be able to add the product to their wishlist directly. Unauthenticated users should be redirected to log in. | Tested with both authenticated and unauthenticated users. | Authenticated users successfully added the item whereas unauthenticated were redirected to log in. | PASS |
| **Add to Wishlist - Already Added**| Clicking the wishlist button for an item already in the wishlist should prevent duplication and notify the user.| Clicked the wishlist button for an item already in the wishlist.| Correctly notified that the item was already in the wishlist and did not add a duplicate. | PASS    |
| **Add to Bag** | Users should be able to add the product to their shopping bag. | Submitted the form to add the product to the bag. | Product was added to the shopping bag without issues. | PASS |
| **Add to Bag - Already Added**     | Clicking the add to bag button for an item already in the bag should should prevent duplication and notify the user that the item is already in the bag.| Clicked the add to bag button for an item already in the shopping bag. | Correctly notified that the item was already in the bag and did not add a duplicate.  | PASS    
| `Add Product Page - superuser access only` |
| **Page Load** | The page should load without any errors and display the form for adding a product. | Accessed the "Add Product" page to check for load issues. | Page loaded successfully with all form elements visible. | PASS |
| **Form Fields Visibility** | All form fields should be visible and labeled correctly. | Inspected each field for visibility and proper labeling. | All fields were visible and correctly labeled. | PASS |
| **Form Submission** | Submitting the form with correct data should successfully add a product. | Filled in the form with valid data and submitted. | Product was added successfully and appeared in the product list. | PASS |
| **Field Validation** | Each field should correctly validate data (e.g., required fields, format constraints). | Submitted the form with missing and incorrect data to test validation. | Form validation worked as expected; could not enter the incorrect format. | PASS |
| **Image Upload** | An image upload field should accept image files and show a preview or filename. | Uploaded an image and checked if the filename or preview was shown. | Image filename was displayed correctly after upload. | PASS |
| **Cancel Button** | The cancel button should redirect users back to the product list without adding a product. | Clicked the "Cancel" button. | Redirected to the product list page without adding a new product. | PASS |
| **JavaScript Functionality** | JavaScript should enhance the usability of the form, like displaying image file names. | Tested JavaScript functionality by changing the image file. | JavaScript updated the display with the new image file name correctly. | PASS |
| **Server-side Processing** | After form submission, the server should process the data correctly and store the new product. | Checked the database or admin panel to confirm the product was added. | New product was correctly added to the database and visible in the admin panel. | PASS |
| `Edit Product Page - superuser access only` |
| **Page Load** | The page should load without any errors and display the edit form pre-filled with the product’s existing details. | Accessed the "Edit Product" page to check for load issues and correct data prefill. | Page loaded successfully with all form elements displaying the current product data. | PASS |
| **Form Fields Visibility** | All form fields should be visible, correctly labeled, and pre-filled with the existing product data. | Inspected each field for visibility, proper labeling, and correct pre-fill. | All fields were visible, correctly labeled, and pre-filled with existing product data. | PASS |
| **Form Submission** | Submitting the form with correct data should successfully update the product. | Modified several fields, submitted the form, and verified updates on the product detail page. | Product updates were saved successfully and reflected on the product detail page. | PASS |
| **Field Validation** | Each field should correctly validate data (e.g., format constraints, required fields). | Submitted the form with missing and incorrect data to test validation. | Form validation worked as expected; could not enter the incorrect format. | PASS |
| **Image Upload** | The image upload field should accept image files and show a preview or filename after upload. | Uploaded a new image and checked if the filename or preview was shown. | Image filename was displayed correctly after upload. | PASS |
| **Cancel Button** | The cancel button should redirect users back to the product list without making any changes. | Clicked the "Cancel" button after making changes to the form fields. | Redirected to the product list page without any changes being saved. | PASS |
| **JavaScript Functionality** | JavaScript should enhance the usability of the form, such as displaying the image file name after upload. | Tested JavaScript functionality by changing the image file. | JavaScript updated the display with the new image file name correctly. | PASS |
| **Server-side Processing** | After form submission, the server should process the data correctly and update the product in the database. | Checked the database or admin panel to confirm the product was updated correctly. | The product was correctly updated in the database and visible in the admin panel. | PASS |
|`Wishlist Page`|
| **Page Load** | The Wishlist page should load without any errors and display all items currently in the wishlist. | Loaded the Wishlist page to check for load issues and correct display of items. | Page loaded successfully with all wishlist items displayed. | PASS |
| **Item Display** | Each item in the wishlist should have an image, name, price, size (if applicable) and a remove option. | Checked each item listed in the wishlist for required information and functionality. | All items displayed with correct details and functional remove buttons. | PASS |
| **Image Modal Functionality**      | Product images should trigger a modal for a larger view if clicked.| Clicked on product images to test modal functionality. | Modal opened with a larger view of the product images correctly.| PASS   |
| **Remove Item** | Clicking the 'Remove' button should immediately remove the item from the wishlist without reloading the page. | Clicked the 'Remove' button for multiple items. | Items were removed instantly and the page updated without a full reload. | PASS |
| **Empty Wishlist Message** | If the wishlist is empty, a message should display indicating that there are no items and provide a link back to the products page. | Emptied the wishlist and checked the message display. | The empty wishlist message displayed correctly with a functional link to keep shopping. | PASS |
| **Add to Wishlist** | Items added to the wishlist from product pages should appear on the wishlist page. | Added items from various product detail pages. | Items appeared in the wishlist as expected. | PASS |
| **Back to Top Button** | Clicking the 'Back to Top' button should smoothly scroll the page to the top. | Tested the 'Back to Top' button after scrolling down. | The button scrolled the page back to the top effectively. | PASS |
|`Shopping Bag Page`|
| **Page Load** | The page should load without errors and display items currently in the shopping bag. | Loaded the Shopping Bag page to check for load issues. | Page loaded successfully with all items displayed as expected. | PASS |
| **Product Information Display** | Each item should show accurate product info including name, price, size (if applicable), and a subtotal. | Checked each item listed for accurate and complete information. | All items displayed with correct details. | PASS |
| **Remove Item** | Clicking the 'Remove' link should instantly remove the item from the bag without needing a page refresh. | Clicked the 'Remove' link for several items. | Items were removed instantly and the total price updated accordingly. | PASS |
| **Image Modal View** | Clicking on a product image should display a larger view in a modal window. | Clicked on product images to trigger the modal. | Modal displayed the images correctly and closed without issues. | PASS |
| **Empty Bag Message** | If the bag is empty, a message should indicate this and provide a link to continue shopping. | Emptied the bag and checked the message display. | The empty bag message displayed correctly with a functional link to the products page. | PASS |
| **Subtotal Calculation** | Each item's subtotal should be calculated correctly based on quantity and price. | Verified the subtotal calculations for various items. | Subtotal calculations were correct for all items. | PASS |
| **Total Calculation** | Total, delivery, and grand total calculations should reflect the current items in the bag. | Added and removed items to test calculation updates. | Total, delivery, and grand total were accurately recalculated as items were added or removed. | PASS |
| **Back to Top Button** | Clicking the 'Back to Top' button should smoothly scroll the page to the top. | Clicked the button after scrolling down on the page. | Page scrolled back to the top effectively. | PASS |
| **Keep Shopping Button** | Clicking 'Keep Shopping' should redirect to the products page. | Clicked 'Keep Shopping'. | Redirected to the products page as expected. | PASS |
| **Checkout Button** | Clicking 'Secure Checkout' should lead to the checkout process. | Clicked 'Secure Checkout'. | Redirected to the checkout page to proceed with the order. | PASS |
|`Checkout Page`|
| **Page Load** | The page should load without errors and display an order summary and checkout form. | Accessed the Checkout page to check for load issues. | Page loaded successfully with all elements displayed correctly. | PASS |
| **Order Summary** | Order summary should correctly list items, quantities, prices, and totals. | Reviewed the order summary for accuracy. | All items, prices, and totals displayed correctly. | PASS |
| **Form Fields Display and Validation** | All checkout form fields should be visible and correctly validate user input. | Filled out the form with both valid and invalid inputs to test validation. | Form fields displayed correctly, and validation worked as expected. | PASS |
| **Save Information Option** | Authenticated users should be able to save their delivery information or opt to create an account. | Tested the save information feature as an authenticated and unauthenticated user. | The option behaved correctly based on user authentication status. | PASS |
| **Stripe Payment Integration** | Stripe elements should be integrated for secure card transactions, with proper error handling. | Entered valid and invalid card details to test Stripe integration and error handling. | Stripe handled payments correctly, and card errors were displayed as expected. | PASS |
| **Successful Transaction** | Completing a successful transaction should redirect to a confirmation page and update order records. | Completed a purchase and checked for redirection and record updates. | Redirected to confirmation page, and records were updated correctly. | PASS |
| **Navigation** | Navigational elements should redirect to the intended pages without losing data. | Clicked on 'Adjust Bag' and other navigational links. | Navigation worked as expected without loss of data. | PASS |
| **Loading Overlay** | A loading overlay should appear during processing to enhance the user experience. | Observed the behavior of the loading overlay during form submission. | The loading overlay displayed correctly during processing. | PASS |
|`Checkout Success Page`|
| **Page Load** | The page should load without errors and display a summary of the order details along with a confirmation message. | Loaded the Checkout Success page after a purchase.  | Page loaded successfully with all elements displayed correctly and the correct order details.    | PASS|
| **Order Details Accuracy**| All displayed order details should match the purchased items, quantities, prices, and totals.| Reviewed the order details for accuracy.| All details matched the order placed including item names, quantities, prices, and totals.| PASS  |
| **Confirmation Email Mention**| The page should inform the user that a confirmation email has been sent.| Checked for the mention of the confirmation email.| The confirmation email was correctly mentioned on the page.                                      | PASS          |
| **Navigation from Profile** | If accessed via a user profile, a 'Back to Profile' button should be visible and functional.| Clicked on 'Back to Profile' if visible.| Button took the user back to their profile without issues.| PASS          |
| **View Other Products Link** A link or button should encourage users to continue shopping, directing them to the products page.| Clicked the 'View other products' button.| The link redirected correctly to the products page.| PASS |
| **Image Modal Functionality**      | Product images should trigger a modal for a larger view if clicked.| Clicked on product images to test modal functionality. | Modal opened with a larger view of the product images correctly.| PASS          |
| **Accuracy of Billing Information**| Billing details displayed should correctly reflect the user’s input from the checkout process.| Verified billing information against what was entered during checkout. | Billing information correctly reflected the user's input.| PASS |
|`Sign In Page`|
| **Page Load**| The page should load without any errors and display the sign-in options clearly.| Accessed the "Sign In" page to check for load issues. | Page loaded successfully with all elements displayed correctly.| PASS          |
| **Form Display**| The sign-in form should be visible with fields for username and password.| Inspected the form for visibility and completeness. | Form displayed correctly with all required fields.| PASS |
| **Form Submission** | Submitting the form with correct credentials should grant access to the user’s account.| Filled in the form with valid credentials and submitted. | Successfully signed in and redirected to the user dashboard or specified page.| PASS          |
| **Form Validation** | Incorrect entries or empty fields should trigger appropriate error messages.| Submitted the form with incorrect and empty fields. | Form validation worked as expected; errors were displayed for incorrect or missing inputs.   | PASS          |
| **Password Recovery** | The "Forgot Password?" link should redirect to a password recovery page.| Clicked the "Forgot Password?" link.| Redirected to the password recovery page correctly.| PASS          |
| **Sign Up Redirection**| The sign-up link should redirect new users to the registration page.                         | Clicked the "sign up" link for new account creation. | Redirected to the sign-up page as expected.                                                  | PASS          |
| **Redirect After Sign-In**| After signing in, users should be redirected to a page specified by the "next" parameter or to a default page. | Signed in with and without the "next" parameter.| Redirected appropriately according to the presence or absence of the "next" parameter.| PASS          |
|`Sign Out Page`|
| **Page Load**| The page should load without errors and display the sign-out confirmation message.| Accessed the "Sign Out" page to check for load issues. | Page loaded successfully with all elements displayed correctly, including the confirmation message. | PASS          |
| **Confirmation Message Display**| A clear message asking if the user is sure they want to sign out should be displayed.| Checked for the presence and clarity of the confirmation message. | The confirmation message was displayed clearly and appropriately.| PASS          |
| **Sign Out Functionality** | Clicking the 'Sign Out' button should securely log the user out.| Clicked the 'Sign Out' button.| Successfully signed out, session ended, and redirected to a specified page or home page.| PASS          |
| **Cancel Button Functionality**       | The cancel button should redirect users back to the home page without logging them out.| Clicked the 'Cancel' button.       | Redirected to the home page without signing out.                                                 | PASS          |
| **Form Submission Security**| The sign-out process should handle CSRF tokens correctly to secure the form submission.| Inspected the form for CSRF token implementation. | CSRF token was present and correctly implemented in the form.                                   | PASS          |
| **Redirect Functionality**| After signing out, users should be redirected to the home page.| Signed out and observed the redirect behavior. | Redirected appropriately to the home page.| PASS          |
| **Responsive Design**| The page should be responsive and display correctly on various devices.| Tested the page on multiple screen sizes and devices. | The layout adjusted correctly and remained functional across all devices.| PASS          |
|`Sign Up Page`|
| **Page Load**                      | The page should load without errors and display the sign-up form.| Accessed the "Sign Up" page to check for load issues. | Page loaded successfully with all elements displayed correctly.                                | PASS          |
| **Form Fields Display**            | All necessary fields for registration should be visible and clearly labeled. | Inspected the form for visibility and completeness. | Form displayed correctly with all required fields. | PASS          |
| **Form Submission**  | Submitting the form with valid data should create a new user account.| Filled in the form with valid data and submitted. | Successfully created a new account and redirected to a welcome page or dashboard.| PASS          |
| **Form Validation** | Form should validate data correctly (e.g., password strength, required fields).| Submitted the form with invalid data.| Form validation worked as expected; errors were displayed for incorrect or missing inputs.| PASS          |
| **Link to Sign In** | The link to the sign-in page should be functional for users who already have an account.| Clicked the "sign in" link.                       | Redirected to the sign-in page as expected.                                                    | PASS          |
| **Security - CSRF Protection**     | The form submission should include CSRF token to protect against CSRF attacks.| Inspected the form for CSRF token presence.   | CSRF token was present and correctly implemented in the form.| PASS          |
| **Back to Login Button** | Clicking 'Back to Login' should redirect users back to the login page.| Clicked the 'Back to Login' button.                | Redirected to the login page without issue.| PASS  |
|`Profile Page`|
| **Page Load** | The page should load without errors and display the profile details and order history.| Accessed the "My Profile" page to check for load issues. | Page loaded successfully with all elements displayed correctly. | PASS          |
| **Profile Update Form**| The form should display all current user information and allow updates.| Reviewed the form for accuracy and editability.   | Form displayed correct information and updates were saved successfully. | PASS|
| **Form Submission** | Submitting updated information should correctly update user details in the database.| Updated various fields in the form and submitted. | Changes were correctly reflected in the user's profile and in the database.| PASS          |
| **Order History Display**| Past orders should be listed with details such as order number, date, items, and total cost. | Checked the display of order history.| Order history displayed correctly with all relevant details. | PASS          |
| **Navigation to Order Details**| Clicking an order number should redirect to a detailed view of that order.| Clicked on order numbers in the history table.    | Successfully redirected to the detailed order history page for each clicked order.| PASS |
| **JavaScript Functionality**| JavaScript used for dynamic elements (e.g., country field updates) should function correctly. | Tested JavaScript-dependent features on the form. | JavaScript features such as dynamic dropdowns worked without errors.| PASS          |
















## Bugs and issues

| No  |  Issue |  Solution |
|---|---|---|
| 1  |![product page not dispalying](./docs/products_page_access.png)  Django template loader could not find the 'products/products.html'   |  Used pathlib path instead of os.path for template DIRS and added '/'. Credit goes to my hackathon teammate Tomislav Dukanez. I remembered him mentioning lack of '/' causing problems in Django and decided to try putting it in the syntax. It worked and the explanation of the pathlib path was found on ChatGPT 4 and [Python Documentation](https://www.python.org)|
| 2 |  Initial products sort correctly by size, but subsequent ones revert to beginning the sort order again  | Changed the size field in your Django model from CharField to IntegerField to make storing data consistent  |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |
|   |   |   |