# Bia.ie

## Code Institute MS3 Project in Backend Development 
The brief was to develop a full-stack site that allows users to manage a common dataset about a particular domain. Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members. This website is created for educational purposes.

AM I RESPONSIVE IMAGE/GIF

[View website](URL.ie)

--
# Contents

1. [Project Overview](#project-overview)
2. [UX](#ux)
3. [Features](#features)
4. [Information Architecture](#ia)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)



# Project Overview
[^ Back To Top ](#contents) 
## [Bia.ie Online Cookbook](https://LINK.URL) 


WEBSITE IMAGE/BIE. IE LOGO

 
Bia.ie is an online cookbook and community for Irish food-lovers.  
For any non-native Irish speakers who may be slightly confused re the website name, 'bia' is Gaeilge for the word 'food'! 
The idea for Bia.ie was conceived in the midst of the Covid 19 Pandemic where many industries became decimated as a result of the virus and life as we once knew it changed forever. 
With the nation ordered to remain socially distanced from one another and stay confined in their homes, people turned to the two things that were constant in this new normal: food and the internet!
Enter the avalanche of tutorials and baking recipes with everyone claiming to hold the ultimate banana bread recipe!
The challenge? To fulfil this new demand for online recipes and create a community around it. Also, to boost the economy by supporting struggling Irish businesses. Bia.ie was the obvious solution. 
Unlike any other online cookbook, the website showcases recipes utilising locally-produced ingredients & products and allows the promotion of these homegrown food producers by displaying individual ingredients as direct links to their website.
Users of Bia.ie make use of the site by sharing their own recipes with the community, and benefit from having convenient access to recipes provided by all other members all whilst promoting local Irish food businneses.

My own goals as a developer creating this project were to: 
- Develop a web application that allowed users to store and easily access cooking recipes. 
- Create an app which is highly accessibile, responsive and simplistic in design.
- Create the backend code and frontend forms allowing users to add new recipes to the site, view them, edit them and delete them using CRUD operations.
- Create the backend and frontend functionality for users to locate recipes based on the recipe's fields providing full search functionality on the site.
- Provide these search results in a manner that is visually appealing and user-friendly.



# UX
[^ Back To Top ](#contents) 

![alt text](images/wireframes/PNG "Bia.ie Main Website")

## Goals

### External user’s goal:
- To easily find inspiration for a future meal or locate a specific recipe based on a past meal or from a personal wishlist. To find recipes from other members by: meal type, by specific ingredients and by dietary requirement. 
- To share knowledge from a homemade recipe or a successful recipe used in the past. To share by adding recipes to the community and providing details by ingredients, cook & prep time, dietary requirements relevant to the recipes and being able to edit and delete them when I no longer want to share with the community.
- To create a list of recipes and store as a customised online cookback to refer back to in the future.

### Site owner's goal:
- Provide a simple, easy to use online cookbook and space where food-lovers can find and share recipes using Irish ingredients with the community. 
- Promote homegrown irish food producers online.
- To benefit from the collection of the recipes in the community to operate as a content incubator for the website.
- Earn revenue through affiliate marketing by directing potential customers towards featured food producers websites. 

## User Stories

### External Users

As a new user, I would like to:
- View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate it's offering easily.
- Access the site from any mobile, tablets and desktop devices so that I can have an equally enjoyable experience regardless of the selected device/platform.
- Register a profile easily without the requirement to provide a lot of info so that I can join the community and add my own recipes. 
- View content without requiring to register so that I can quickly locate a specific recipe.
- Browse and filter recipes by meal or dietary category so that I can easily find inspiration for a future meal.
- View a list of recipes by ingedient/meal/dietary keyword search criteria so that I can quickly locate a specific meal/dish.
- View the featured food producers so that I can see any connected recipes that I can use their ingredients/products in. 
- Learn more about the food producers on the site so that I can support them by purchasing their products.

As a returning user, I would like to:
- Log in and out without encountering issues so that I can have an enjoyable user experience.
- View all the recipes I have stored in a specific area so that I can review my current collection at any time and refer back to them when needed.
- Create a new recipe providing necessary details so that I can share knowledge from a homemade/successful recipe used in the past with the community.
- Edit one of my current recipes so that I can improve the recipe for other members or users.
- Remove one of my current recipes so I that I can choose to no longer share it with the community.
- To have access to all recipes provided by the community so that I can view content from other members.
- To browse recipes from other members so that I can get inspiration for future meals based on meal type, specific ingredients used and by dietary requirement. 

### Business/Admin Users

As a business/admin user, I would like to do all of the above as well as:
- The ability to edit or remove recipes created by users so that I can vet the content and ensure it's appropriate for users.
- The ability to add, edit or remove recipe categories so that I can keep the categories relevant to what users are searching for
- Edit the linked ingredient URLs so that they divert to the correct business website.
- View the amount of clicks from the featured business page and linked ingredient URLs so that I can gauge potential success of affiliate marketing. 


## Design

### Typography
I wanted to use [Montserrat](https://fonts.google.com/specimen/Montserrat#about) for the headings and [Open Sans](https://fonts.google.com/specimen/Open+Sans/#about) as a supporting body font to achieve the desired clean-cut image.

### Icons
Materialize icons has been used for this project.

### Color Scheme
The Bia.ie brand monochrome colour scheme was implemented along with pops of green to reflect the Irish fresh products represented throughout the site.
I wanted to keep the color palette simplistic and clean to allow for the imagery from the recipes to stand out and inject the site with colour.
However the colour red is used for error messages for the Signup and Login pages to highlight a warning to the user.

I ended up creating and using the below palette once it had passed rigorous Accessibility testing in **A11y's Color Contrast Accessibility Validator**. 

![alt text](static/images/bia-color-palette.PNG "Bia Color Palette")


## Wireframes

The folder contains [Wireframes](wireframes/wireframes.pdf "Bia Wireframes") including mockups of the homepage, an individual recipe page, submit recipe page, featured business page and account creation page designed at the beginning of the project for desktop, tablet and mobile devices. I have also included the projected [sitemap](wireframes/site-map.png "Bia Sitemap") and data [schema](wireframes/schema.PNG "Bia Schema").
**Please note the finalised project contains slight variations to the original wireframe**

# Features
[^ Back To Top ](#contents) 

![alt text](images/wireframes/PNG "wireframe")

## Existing Features
Existing features
Index page informs the user about the site in the eye-catching jumbotron
 Ads for featured businesses
 Signup
 Login
Search: users are able to search for recipes by username, title or any other text. If no results are found message "No results found. Please try again".
 Sorting by category in navigation links.
 Access to user profile with all users recipes
 If user has not added any recipes, the profile reads "X" and has "Submit Recipe" CTA.
 Whenever user has logged in user is greeted with a 5 second flash welcome message
 When user is first registerd user is greeted with 5 second "Signup Successful" flashed message.
 Profile page displays username in banner
 Thank you page with a "Back Home" button that appears after user has edited or submitted a recipe
 Only registered and logged in users allowed to sumbit/edit and delete recipes.
 Only user that posted the recipe or admin can delete and/or edit it.
 Social icons with links in the page footer
 Recipes displayed in list have title, description, cooking time and user information
 Single recipe page have full recipe information, the date and time it was first created, image and list.
 Single recipe page displays tips only if they have been defined. All other fields are required.
 Submit recipe and edit recipe forms have clear instructions and character limits for certain fields.
 If password is too short or email is invalid etc tooltip appears
 Favicon
 Bootstrap input field validation


## Features Left to Implement
newsletter
Future features
Pagination
Google/Facebook login
 Admin recipe review to either accept or reject recipe for it to be public.
 More categories
 Admin able to add/edit/delete categories
 Sort recipes by tags
 Nutrition calculations
 Server side credential validation
 SSL certificate
 Recipe Comments
 Lazy loading images
 Prevent duplicate subscribers
 "Remember me" signup checkbox
 Edit user profiles
 User profiles with description, avatar, post list
 Ability to click on other user profiles and see recipes they posted
 Page loading animation
 Filter emails so that there are no duplicates for subscription letters
 Admin portal
 Contact form and admin to be able to see all received messages directly in the admin console
 Recipe image url validation


# Information Architecture
[^ Back To Top ](#contents)
## Database Choice
In order to fulfil the project requirements, the NoSQL database MongoDB was utilised to store the data.

This non-relational database structure suits Bia.ie as there are only a few relationships between the various collections. 

## Data Modeling
The project currently relies on five database collections:

#### Categories collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string||

#### Recipe collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|title|string||
|category_name|string||
|recipe_description|string||
|image_url|string||
|serves|Array||
|prep|string||
|cooks|string||
|difficulty|string||
|ingredient_name|string||
|instructions|string||
|date_added|string||
|username|string||


#### Users collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string||
|password|string||
|email|string||


#### Businesses collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|business_name|string||
|business_description|string||
|business_url|string||


#### Ingredients collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|ingredient_name|string||
|business_url|string||

# Technologies Used
[^ Back To Top ](#contents)
## Languages
- [CSS](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/)
  - [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

## Libraries and Frameworks

- [Flask](https://palletsprojects.com/p/flask/)
- [jQuery](https://jquery.com/)?????????
- [Materialize](https://materializecss.com/)


## Extensions and kits

- [Boto3](https://boto3.amazonaws.com/v1/documentation/api/latest/index.html)???????
- [Flask Paginate](https://pythonhosted.org/Flask-paginate/)
- [Pillow](https://pillow.readthedocs.io/en/stable/)?????
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)

## Tools
- [Am I Responsive?](http://ami.responsivedesign.is/)
- [Autoprefixer](https://autoprefixer.github.io/)
- [Favicon.io](https://favicon.io//)
- [Font Awesome](https://fontawesome.com/)
- [Google Fonts](https://fonts.google.com/)
- [Amazon AWS](https://aws.amazon.com/) (S3)??????????????
- [Balsamiq](https://balsamiq.com/wireframes/)
- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Heroku](https://www.heroku.com/about)

## Databases
- [MongoDB](https://www.mongodb.com/)


In the construction of this project I have utilised the following languages, frameworks, libraries and tools:
- **HTML5,** **CSS3** and **JavaScript** programming languages
- [Bootstrap v4.5.3](https://getbootstrap.com)
    - The project used **Bootstrap** to simplify the website layout by integrating the Congrats Modal and Navbar. 
- [GitPod](https://www.gitpod.io/)
    - I used **GitPod** as the development environment for my website. I also used Git for Version Control in the project.
- [GitHub](https://www.github.com/)
    - The project used **GitHub** to host my code that was created and pushed from GitPod.
- [Balsamiq](https://balsamiq.com/)
    - I used **Balsamiq**, the rapid low-fidelity UI wireframing tool during the prototyping phase to structure the website and its content following best UX practices.
- [Color Hex](https://www.color-hex.com/)
    - I created the color palette for my project using the theme colours of the main Bia.ie website and **Color Hex** to help structure the UI for the game. 
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools)
    - **Chrome Dev Tools** was used to consistently test the site and run reports from Lighthouse.
- [Google Fonts](https://fonts.google.com)
    - **Google Fonts** was used to style the website fonts.
- [Font Awesome](https://fontawesome.com/)
    - I used the font & icon toolkit Font Awesome in the win modal to define elements by a visual means and break up the larger section of text.
- [Favicon.io](https://favicon.io/)
    - **Favicon.io** was used to generate the favicons for the site.    
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html)
    - I used **CSS Beautify** to format and automatically indent my CSS file.
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html)
    - The **HTML Formatter** was used to format the HTML document.  
- [Freeformatter JS Formatter](https://www.freeformatter.com/javascript-beautifier.html)
    - The **JavaScript Formatter** was used to format the JS file.      
- [Unicorn Revealer](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln)
    - I regularly used the **Unicorn Revealer** Chrome extension to inspect and locate where overflow was located making the debugging process a lot easier. 
- [Autoprefixer](https://autoprefixer.github.io)
    - The project used PostCSS plugin **Autoprefixer** which parsed my CSS and added vendor prefixes to allow cross-browser compatibility and support.
- [Color Contrast Accessibility Validator](https://color.a11y.com/)
    - The **Color Contrast Accessibility Validator** was used to test for colour contrast on the project.
- [W3C Markup Validation Service](https://validator.w3.org/)
    - The **W3C Markup Validation Service** checked the markup validity of Web documents in HTML.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/)
    - **W3C CSS Validation Service** was used to check the validity of my CSS in the project.
- [JS Hint Validator](https://jshint.com/)
    - **JS Hint** was used to analyze and ensure the source code complies with coding rules. 
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/)
    - I used **WAVE** to make my site more accessible to individuals with disabilities by detecting any potential issues.
- [Pep8 Online](http://pep8online.com/)
    - **Pep 8 Online** 
Figma
Python
mongodb
materialise for icons etc

# Testing
[^ Back To Top ](#contents)
The Testing process has been documented in this [testing.md file.](/testing.md "testing.md File")

# Deployment
[^ Back To Top ](#contents)

## Local Deployment
## Heroku Deployment

# Credits
[^ Back To Top ](#contents)

I took inspiration from the following sources however I did implement my own custom code with each snippet also:

## Code
## Content and Media
## Acknowledgements

I would like to thank my mentor Guido Cecilio for his continued support and overall guidance throughout the project. 

[^ Back To Top ](#contents) 

# Disclaimer