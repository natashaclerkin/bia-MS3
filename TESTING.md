# Project Testing

# Contents
1. [Responsive Testing](#responsive-testing)
2. [Automated Testing](#automated-testing)
3. [Manual Testing](#manual-testing)
4. [Bugs](#bugs)

[< Take me back to the README file](README.md "README.md File")
# Responsive Testing

Responsiveness of the site is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools).
The website is tested on Chrome, Firefox, Safari and Edge on the following devices: 
- Desktop: 1024px, 1280px, 1440px, 1600px and 1680px. 
- Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro and Google Nexus 10.


[^ Back To Top ](#contents) 


# Automated Testing
## Validation Programs

I used the [W3C Markup Validation Service](https://validator.w3.org/) to check the Markup, The error 'Consider using h2-h6 elements to add identifying heading to all sections' was cited as a warning because of the flash messaging through the code. I used [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS validity, [JS Hint Validator](https://jshint.com/) to check the JS rules and [PEP8](http://pep8online.com/) to validate Python in the project. After fixing the errors on all testing sites, the sites eventually passed validation.

![HTML Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1620888747/htmlval_qkngqf.png "HTML Validation Final Results")

![CSS Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1620888747/cssval_zufx86.png "CSS Validation Final Results")

![JS Validation Final Results](https://res.cloudinary.com/nclerkin/image/upload/v1620888747/jsval_t9hgjp.png "JS Validation Final Results")

![Python validator](https://res.cloudinary.com/nclerkin/image/upload/v1620888747/pythonval_eqntd4.png "JS Validation Final Results")

I constantly tested the code in [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) and often ran Lighthouse audits to identify and fix issues that affected the site's performance, accessibility and user experience. 



[^ Back To Top ](#contents) 


# Manual Testing
## Manual Testing of User Stories
|  USER     | USER STORY TEST      |  OUTCOME    |  STATUS    |
| ----------| -------------------- |  --------------------|  ----------|
| New User | **View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate its offering easily.**  |   As a new user, when I click the URL, I land on The homepage to view a clean, sleek website with a monochrome design and the main focus on the colourful imagery and bright CTA's. The Nav allows me to select 'all recipes' or select a category, there's also a designated Bia Brands page that displays all promoted brands on the site and a login and register page.  The About info is in the Header image and is the first item I see so the site's purpose is clear. It is followed by an Instagram-worthy grid of recipes which adds to the overall appeal of the page and makes me want to click into each recipe. The featured section highlights a brand and directs the user to their individual brand page. There is contact info and social media links in the footer.  |    Approved     |
| New User | **Access the site from any mobile, tablet or desktop devices so that I can have an equally enjoyable experience regardless of the selected device/platform.**  |  As a new user, when I attempt to navigate the site on multiple devices, I am greeted with a responsive website on all tested devices.       |      Approved     |
| New User | **Register a profile easily without the requirement to provide a lot of info so that I can join the community and add my own recipes.**  |     As a new user, When I try to register an account with Bia, I am only required to fill out a username and password which takes less than 2 minutes and I am then diverted to my new profile where I immediately see the CTA to 'add a new recipe'.      |    Approved       |
| New User | **View content without requiring to register so that I can quickly locate a specific recipe.**  |   As I new non-authenticated user, I can select 'all recipes' from the nav and I have the ability to search recipes by title and short description content.      |   Approved        |
| New User | **Browse and filter recipes by meal or dietary category so that I can easily find inspiration for a future meal.**  |      As a new user, I click filtered categories from the Nav to view a selection of relevant recipes and I can view all recipes from the Recipes link in the navbar  |      Approved     |
| New User | **View a list of recipes by ingredient/meal/dietary keyword search criteria so that I can quickly locate a specific meal/dish.**  |     As a new user, I can select the recipes link which brings me to all available recipes and I have the ability to search recipes by title and short description content. If no results are found a helpful error message is presented. I can reset the search filters to manually search also.   |   Approved        |
| New User | **View the featured food producers so that I can see any connected recipes that use their products.**  |    As a new user, I can view the 'featured brand' section on the homepage which diverts me to the same brand's profile which displays information about the brand, their logo and links to related recipes.     |  Approved         |
| New User | **Learn more about the food producers on the site so that I can support them by purchasing their products.**  |     As a new user, I can select the 'Bia Brands' link in the navbar which returns all the available brands on the site. I can browse each brand and view their individual brand profile page. There is a link to their website where I can find out more info about ordering their products.     |  Approved         |
| Returning User | **Log in and out without encountering issues so that I can have an enjoyable user experience.**  |    As a returning user, I can select the 'log in' link in the navbar which directs me to the login page and when I enter my details correctly, I am diverted to my profile and presented with a personalised welcome message. If I enter incorrect details, I am reminded about the username and password format.     | Approved          |
| Returning User | **View all the recipes I have stored in a specific area so that I can review my current collection at any time and refer back to them when needed.**  |     As a returning user, given that I have logged in successfully, I am brought straight to my profile where I can see all my collection of recipes instantly provided that I have created recipes.     | Approved          |
| Returning User | **Create a new recipe providing necessary details so that I can share knowledge from a homemade/successful recipe used in the past with the community.**  |      As a returning user, given that I have logged in successfully, I can 'add a new recipe' from the profile and share it with the community. When I create the recipe, I am presented with a flash message confirming that the recipe has been created and the recipe appears in the profile.    |  Approved         |
| Returning User | **Edit one of my current recipes so that I can improve the recipe for other members or users.**  |   As a returning user, given that I have logged in successfully, I can select one of my recipes from the dashboard and edit the fields successfully and save the recipe. When I am rediverted to the profile, I am presented with a flash message confirming that the recipe has been updated and the changes to the recipe can be seen in the recipe.       |  Approved         |
| Returning User | **Remove one of my current recipes so that I can choose to no longer share it with the community.**  |    As a returning user, given that I have logged in successfully, I can select a specific recipe from the dashboard and choose the 'delete' action and I am presented with the delete confirmation modal. When I confirm the deletion, I am presented with a flash message confirming that the recipe has been deleted and the recipe disappears from the profile.    | Approved          |
| Returning User | **To have access to all recipes provided by the community so that I can view content from other members.**  |   Feature in next release      | Not Approved          |
| Returning User | **To browse recipes from other members so that I can get inspiration for future meals based on meal type, specific ingredients used and by dietary requirement.**  |      Feature in next release     |  Not Approved         |
| Brand Owner User | **Create recipes to share with the community so that I can highlight our products from the brand.**  |     As a brand owner user, I can register my own profile and add a new recipe to the site allowing our brand to be the brand name and the username. When I create the recipe, I am presented with a flash message confirming that the recipe has been created and the recipe appears in the profile.    |  Approved         |
| Brand Owner User | **View the products in as many locations on the website so that I can create awareness for the brand.**  |  Feature in next release        | Not Approved          |
| Brand Owner User | **Offer a discount to community users so that I can gain potential new customers for the brand.**  |    Feature in next release        | Not Approved          |
| Brand Owner User | **View analytics/reports for the number of users that have clicked through to our site to value potential customer acquisition.** |   Feature in next release         | Not Approved          |
| Business/Admin User | **The ability to edit or remove recipes created by users so that I can vet the content and ensure it's appropriate for users.**  |     As a logged-in Admin user, I can view all recipes on the site from the profile. As well as being able to view the content by expanding the collapsible tabs, there are two additional actions available for 'edit' and 'delete'. I have full functionality to edit or delete the recipe and I am presented with a confirmation modal prior to deleting a recipe. Flash messaging confirms action taken.  |  Approved         |
| Business/Admin User | **The ability to add, edit or remove recipe categories so that I can keep the categories relevant to what users are searching for.**  |  As a logged-in Admin user, I can select 'manage categories' which brings me to a page where I can view the current categories that are present on the site and I have options available to edit or delete these categories as well as the option to create a new category. When I attempt to delete a category I am presented with a modal confirming my action to remove the category from the site.  Flash messaging confirms action taken.        | Approved          |
| Business/Admin User | **The ability to add, edit or remove brands as required to maintain relevance between the recipes and brands currently in the community.**  |    As a logged-in Admin user, I can select 'manage brands' which brings me to a page where I can view the current brands that are present on the site and I have options available to edit or delete these brands as well as the option to create a new brand. When I attempt to delete a brand I am presented with a modal confirming my action to remove the brand from the site.  Flash messaging confirms action taken.    |  Approved         |
| Business/Admin User | **Ensure witty helper/success text is present when users add recipes in the community to convey a great sense of Irish humour and provide an enjoyable user experience.**  |  As a logged-in user, when I select 'add a recipe' I am presented with a form with fields that have friendly 'helper text' and when I fill out a field correctly I feel like I am interacting with a real person as the 'success text' responds to my input.           |  Approved         |
| Business/Admin User | **View the number of clicks from the featured business page and linked ingredient URLs so that I can gauge the potential success of affiliate marketing.**  | Feature in next release         | Not Approved          |
 

## Manual Back End Feature Testing 

|  TEST      |  EXPECTED OUTCOME    |  RESULT    |
| -------------------- |  --------------------|  ----------|
| Flash messaging   |   Flash messaging should be in place when a user registers, logs in/out, enters an incorrect username and/or password. It also should appear when CUD functionality is activated for brands, categories and recipes. Example of flash messaging implemented [here](https://res.cloudinary.com/nclerkin/image/upload/v1620827520/flashmessaging_gehdpp.png)      |  Approved       |
| Password Hashing   |  User's passwords should be hashed by Werkzeug security features installed to provide an additional defence against any passwords being accessed should a database has been compromised. Example of password hashing completed in the database [here](https://res.cloudinary.com/nclerkin/image/upload/v1620827151/hashed_passwords_ztjn3p.png)      |  Approved       |
| Form Validation |  The 'Add Recipe/Category', 'Edit Recipe/Category' and 'Login/Register' forms, should have a Regex "min-length" and a "max-length" set on Recipe name, Category name, Username and Password. All Dropdown content should be marked as required and be displayed alphabetically. All forms should not allow the user to submit unless all required fields are completed and should be highlighted in red or green depending on if the field is valid or invalid, pattern attributes should be added to most text, number, URL  and password fields, the majority of fields should have delightful helper text and data-success messaging to aid the user experience. Example of data success messaging in place [here](https://res.cloudinary.com/nclerkin/image/upload/v1620829925/data-success_qvjnaj.png)       |  Approved       |
| Buttons  | All buttons should have consistent styling and be standardised sitewide. Non-registered users have access to the CTA's which are all styled with a green background and white text to enforce the positive association linked to the colour allowing the user to successfully browse through brand/recipe pages. The search bar also has a reset button which should be styled with a black background and white text, the action should reset the user's current search filters. Non-Admin users should only have access to their own recipes so should only be able to view the 'Add' button styled with a green background and white text, the 'Edit' Button which is styled with a white background and green text and the 'Delete' button which is styled with a red background and white text. The 'Cancel' and 'Edit' buttons on the proceeding page replicate the 'Add' and 'Delete button styling and functionality. The 'Cancel' button should redirect the user back to their profile and the 'Edit button should save the user's changes and update their recipe. As well as the primary buttons available to all users, admin also have access to 'Manage' buttons which are displayed with a black background and white text. Admin users in session should be the only users able to view these buttons. Once selected, the buttons bring the Admin user to CRUD functionality for Brands and Categories. The Recipes CRUD functionality is readily accessible for the admin on login and should display as [here](https://res.cloudinary.com/nclerkin/image/upload/v1620780109/profile_t2gq79.png)        |  Approved       |         
| Protect route validation  | To prevent attacks on brute-forcing routes by exposed IDs, functions need to be protected. Users shouldn't be able to access areas they aren't permitted and shouldn't be able to carry out actions such as Delete on visible IDs, they should be diverted to a custom 404 page as [here](https://res.cloudinary.com/nclerkin/image/upload/v1620870665/deletebugfixed_pf3pks.png)        |  Approved       |         



[^ Back To Top ](#contents) 




# Bugs

Minor bugs were found and resolved with **Devtools** like the below dropdown bugs.

![Dropdown bug 1](https://res.cloudinary.com/nclerkin/image/upload/v1620833685/bu_rntwoe.png "Dropdown bug 1")

![Dropdown bug 2](https://res.cloudinary.com/nclerkin/image/upload/v1620833595/bug1_rwvr19.png "Dropdown bug 2")


However, I did run into issues with the following:


- When attempting to add a recipe and add a brand, the brand name wasn't saving to the database. I figured out the inconsistencies between the input fields and related routes and was able to fix this bug successfully.

![Brand name bug](https://res.cloudinary.com/nclerkin/image/upload/v1620870664/brand-name_cefyxr.png "Brand name bug")

![Brand name bug fix](https://res.cloudinary.com/nclerkin/image/upload/v1620872683/brandnamefix_jhwgse.png "Brand name bug fix")


Also just before the deadline, I noticed that there was an issue with the profile display for new users. I will ensure to implement a 'No recipes yet :(' placeholder message in the next release.
![New user profile bug fix](https://res.cloudinary.com/nclerkin/image/upload/v1620881643/profilebug_ru0uy8.png "New user profile bug fix")



[^ Back To Top ](#contents) 

[< Take me back to the README file](README.md "README.md File")