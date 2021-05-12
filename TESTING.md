# Project Testing

# Contents
1. [Responsive Testing](#responsive-testing)
2. [Automated Testing](#automated-testing)
3. [Manual Testing](#manual-testing)
4. [Bugs](#bugs)

[< Take me back to the README file](README.md "README.md File")
# Responsive Testing

Responsiveness of the site is tested with [Chrome DevTools](https://developers.google.com/web/tools/chrome-devtools) and [Responsive Design Checker](https://www.responsivedesignchecker.com/).
The website is tested on Chrome, Firefox, Safari and Edge on the following devices: 
- Desktop: 1024px, 1280px, 1440px, 1600px and 1680px. 
- Mobile & Tablet: Galaxy S5, iPhone 5/SE, iPhone 6/7/8, iPhone 6/7/8 Plus, iPhone X, iPad, iPad Pro and Google Nexus 10.

![Responsive testing](responsive-testing.png)


[^ Back To Top ](#contents) 

# Automated Testing
## Validation Programs
I used the [W3C Markup Validation Service](https://validator.w3.org/) to check the Markup, [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the CSS validity, [JS Hint Validator](https://jshint.com/) to check the JS rules and [PEP8](http://pep8online.com/) to validate Python in the project. After fixing the errors on all testing sites, the sites eventually passed validation.

![HTML Validation Final Results](wireframes/html-validation.PNG "HTML Validation Final Results")

![CSS Validation Final Results](wireframes/css-validation.PNG "CSS Validation Final Results")

![JS Validation Final Results](wireframes/js-validation.PNG "JS Validation Final Results")

![Python validator](testing/python-validator.png)

The [Color Contrast Accessibility Validator](https://color.a11y.com/) was used to test for colour contrast on the project and confirmation that the overall site complies with accessibility standards.

![Color Validation Testing](wireframes/color-validation.PNG "Color Validation Testing")

In order to have optimal user experience, the site needs to be accessible for everyone. I would continually run the URL through **WAVE Web Accessibility Evaluation Tool** to highlight potential issues. I continued until no further errors or alerts were given.

![Wave Accessibility Test results](wireframes/wave-validation-1.PNG "Wave Accessibility Test results")

I constantly tested the code in [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) and often ran Lighthouse audits to identify and fix issues that affected the site's performance, accessibility and user experience. 

![Lighthouse Testing Initial Results](wireframes/lighthouse-audit-1.PNG "Lighthouse Testing Initial Results")

This highlighted the areas that required improvement for validation.
Also, a Cross-Origin security issue pertaining to Best Practices was simply resolved via adding `rel= noreferrer` to all external links. I also ensured all the necessary aria labels, alt tags etc were present to conform to best practices. 
Through constant testing, I was able to achieve almost 100% on all metrics for optimum Performance, Accessibility, SEO and Best Practices.  

![alt text](wireframes/lighthouse-audit-2.PNG "Lighthouse Testing Final Run Results")


[^ Back To Top ](#contents) 



# Manual Testing
## Manual Testing of User Stories
|  USER     | USER STORY TEST      |  EXPECTED OUTCOME    |  RESULT    |
| ----------| -------------------- |  --------------------|  ----------|
| New User | **View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate it's offering easily.**  |         |         |
| New User | **Access the site from any mobile, tablet or desktop devices so that I can have an equally enjoyable experience regardless of the selected device/platform.**  |         |         |
| New User | **Register a profile easily without the requirement to provide a lot of info so that I can join the community and add my own recipes.**  |         |         |
| New User | **View content without requiring to register so that I can quickly locate a specific recipe.**  |         |         |
| New User | **Browse and filter recipes by meal or dietary category so that I can easily find inspiration for a future meal.**  |         |         |
| New User | **View a list of recipes by ingredient/meal/dietary keyword search criteria so that I can quickly locate a specific meal/dish.**  |         |         |
| New User | **View the featured food producers so that I can see any connected recipes that use their products.**  |         |         |
| New User | **Learn more about the food producers on the site so that I can support them by purchasing their products.**  |         |         |
| Returning User | **Log in and out without encountering issues so that I can have an enjoyable user experience.**  |         |         |
| Returning User | **View all the recipes I have stored in a specific area so that I can review my current collection at any time and refer back to them when needed.**  |         |         |
| Returning User | **Create a new recipe providing necessary details so that I can share knowledge from a homemade/successful recipe used in the past with the community.**  |         |         |
| Returning User | **Edit one of my current recipes so that I can improve the recipe for other members or users.**  |         |         |
| Returning User | **Remove one of my current recipes so I that I can choose to no longer share it with the community.**  |         |         |
| Returning User | **To have access to all recipes provided by the community so that I can view content from other members.**  |         |         |
| Returning User | **To browse recipes from other members so that I can get inspiration for future meals based on meal type, specific ingredients used and by dietary requirement.**  |         |         |
| Brand Owner User | **Create recipes to share with the community so that I can highlight our products from the brand.**  |         |         |
| Brand Owner User | **Get the products in as many locations on the website so that I can create awareness for the brand.**  |         |         |
| Brand Owner User | **Offer discount to community users so that I can gain potential new customers for the brand.**  |         |         |
| Brand Owner User | **View analytics/reports for the quantity of users that have clicked through to our site to value potential customer acquisition.** |         |         |
| Business/Admin User | **The ability to edit or remove recipes created by users so that I can vet the content and ensure it's appropriate for users.**  |         |         |
| Business/Admin User | **The ability to add, edit or remove recipe categories so that I can keep the categories relevant to what users are searching for.**  |         |         |
| Business/Admin User | **The ability to add, edit or remove brands as required to maintain relevance between the recipes and brands currently in the community.**  |         |         |
| Business/Admin User | **Ensure witty helper/success text is present when users add recipes in the community to convey a great sense of Irish humour and provide an enjoyable user experience.**  |         |         |
| Business/Admin User | **View the amount of clicks from the featured business page and linked ingredient URLs so that I can gauge potential success of affiliate marketing.**  |         |         |
 

## Manual Back End Testing

|  TEST      |  EXPECTED OUTCOME    |  RESULT    |
| -------------------- |  --------------------|  ----------|
| Flash messaging   |   Flash messaging should be in place when a user registers, logs in/out, enters an incorrect username and/or password. It also should appear when CUD functionality is activated for brands, categories and recipes. Example of flash messaging implemented [here](https://res.cloudinary.com/nclerkin/image/upload/v1620827520/flashmessaging_gehdpp.png)      |  Approved       |
| Password Hashing   |  User's passwords should be hashed by Werkzeug security features installed to provide additional defence against any passwords being accessed should a database has been compromised. Example of password hashing completed in the database [here](https://res.cloudinary.com/nclerkin/image/upload/v1620827151/hashed_passwords_ztjn3p.png)      |  Approved       |
| Form Validation |  The 'Add Recipe/Category', 'Edit Recipe/Category' and 'Login/Register' forms, should have a Regex "min-length" and a "max-length" set on Recipe name, Category name, Username and Password. All Dropdown content should be marked as required and be displayed alphabetically. All forms should not allow the user to submit unless all required fields are completed and should be higlighted in red or green depending if the field is valid or invalid, pattern attributes should be added to most text, number, url and password fields, the majority of fields should have delightful helper text and data-success messaging to aid the user experience. Example of data success messaging in place [here](https://res.cloudinary.com/nclerkin/image/upload/v1620829925/data-success_qvjnaj.png)     |         |
| Buttons  | All buttons should have consistent styling and be standardised sitewide. Non-registered users have access to the CTA's which are all styled with a green background and white text and inverted on hover to enforce the positive association linked to the colour allowing the user to successfully browse through brand/recipe pages. The search bar also has a reset button which should be styled with a black background and white text and invert colours on hover, the action should reset the user's current search filters. This  Non-Admin users should only have access to their own recipes so should only be able to view the 'Add' button styled with a green background and white text which is inverted on hover, the 'Edit' Button which is styled with a white background and green text which is inverted on hover and the 'Delete' button which is styled with a red background and white text which is inverted on hover. The 'Cancel' and 'Edit' buttons on the proceeding page replicate the 'Add' and 'Delete button styling and functionality. The 'Cancel' button should redirect the user back to their profile and the 'Edit button should save the user's changes and update their recipe. As well as the primary buttons available to all users, admin also have access to 'Manage' buttons which are displayed with a black background and white text and invert the colours when hovered. Admin users in session should be the only users able to view these buttons. Once selected, the buttons bring the Admin user to CRUD functionality for Brands and Categories. The Recipes CRUD functionality is readily accessible for the admin on login and should display as [here](https://res.cloudinary.com/nclerkin/image/upload/v1620780109/profile_t2gq79.png)        |         |






[^ Back To Top ](#contents) 




# Bugs

Dropdown bugs:
![Dropdown bug 1](https://res.cloudinary.com/nclerkin/image/upload/v1620833595/bug1_rwvr19.png "Dropdown bug 1")
![Dropdown bug 2](https://res.cloudinary.com/nclerkin/image/upload/v1620833685/bu_rntwoe.png "Dropdown bug 2")



[^ Back To Top ](#contents) 

[< Take me back to the README file](README.md "README.md File")