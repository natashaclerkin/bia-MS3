# Bia.ie

## Code Institute MS3 Project in Backend Development 
The brief was to develop a full-stack site that allows users to manage a common dataset about a particular domain. Users make use of the site to share their own data with the community, and benefit from having convenient access to the data provided by all other members. This website is created for educational purposes.
 

# Contents

1. [Project Overview](#project-overview)
2. [UX](#ux)
3. [Features](#features)
4. [Information Architecture](#information-architecture)
5. [Technologies Used](#technologies-used)
6. [Testing](#testing)
7. [Deployment](#deployment)
8. [Credits](#credits)



# Project Overview

## [Bia.ie Online Cookbook](http://bia-ms3.herokuapp.com/)


![Am I Responsive Image](https://res.cloudinary.com/nclerkin/image/upload/v1620756623/amiresponsive_urcfgx.png "Am I Responsive Image") 

[View website](http://bia-ms3.herokuapp.com/) 
 
[Bia.ie](http://bia-ms3.herokuapp.com/) is an online cookbook and community for Irish food-lovers. For any non-native Irish speakers who may be slightly confused re the website name, 'bia' is Gaeilge for the word 'food'! 

The idea for Bia was conceived in the midst of the Covid 19 Pandemic where many industries became decimated as a result of the virus and life as we once knew it changed forever. 
With the nation ordered to remain socially distanced from one another and stay confined in their homes, people turned to the two things that were constant in this new normal: food and the internet!
Enter the avalanche of tutorials and baking recipes with everyone claiming to hold the ultimate banana bread recipe!
The challenge? To fulfil this new demand for online recipes and create a community around it. Also, to boost the economy by supporting struggling Irish businesses. Bia was the obvious solution. 
Unlike any other online cookbook, the website showcases recipes utilising locally-produced ingredients & products and allows the promotion of these homegrown food producers by displaying ingredients or brands with direct links to their website.
Users of Bia make use of the site by sharing their own recipes with the community, and benefit from having convenient access to recipes provided by all other members all whilst promoting local Irish food businesses.

My own goals as a developer creating this project were to: 
- Develop a web application that allowed users to store and easily access cooking recipes. 
- Create an app which is highly accessibile, responsive and simplistic in design.
- Create the backend code and frontend forms allowing users to add new recipes to the site, view them, edit them and delete them using CRUD operations.
- Create the backend and frontend functionality for users to locate recipes based on the recipe's fields providing full search functionality on the site.
- Provide these search results in a manner that is visually appealing and user-friendly.

[^ Back To Top ](#contents)

# UX


## Goals

### External user’s goal:
- Locate: To easily find inspiration for a future meal or locate a specific recipe based on a past meal or from a personal wishlist. To find recipes from other members by: meal type, by specific ingredients and by dietary requirement. 
- Share: To share knowledge from a homemade recipe or a successful recipe used in the past. To share by adding recipes to the community and providing details by ingredients, cook & prep time, dietary requirements relevant to the recipes and being able to edit and delete them when I no longer want to share with the community.
- Create: To create a list of recipes and store as a customised online cookback to refer back to in the future.

### Site owner's goal:
- Provide a simple, easy to use online cookbook and space where food-lovers can find and share recipes using Irish ingredients with the community. 
- Promote homegrown irish food producers online.
- Provide an enjoyable experience for users to encourage them to return to the site by featuring intuitive prompts and witty Irish banter through the content. 
- To benefit from the collection of the recipes in the community to operate as a content incubator for the website.
- Earn revenue through affiliate marketing by directing potential customers towards featured food producers websites. 

### Brand owner's goal:
- Create awareness for the brand on the website.
- Gain potential new customers.
- Show versatility of products by creating recipes on the site.


## User Stories

### External Users

As a new user, I would like to:
- View a visually clean and appealing homepage so that I can instantly understand the purpose of the site and navigate it's offering easily.
- Access the site from any mobile, tablet or desktop devices so that I can have an equally enjoyable experience regardless of the selected device/platform.
- Register a profile easily without the requirement to provide a lot of info so that I can join the community and add my own recipes. 
- View content without requiring to register so that I can quickly locate a specific recipe.
- Browse and filter recipes by meal or dietary category so that I can easily find inspiration for a future meal.
- View a list of recipes by ingredient/meal/dietary keyword search criteria so that I can quickly locate a specific meal/dish.
- View the featured food producers so that I can see any connected recipes that use their products. 
- Learn more about the food producers on the site so that I can support them by purchasing their products.

As a returning user, I would like to:
- Log in and out without encountering issues so that I can have an enjoyable user experience.
- View all the recipes I have stored in a specific area so that I can review my current collection at any time and refer back to them when needed.
- Create a new recipe providing necessary details so that I can share knowledge from a homemade/successful recipe used in the past with the community.
- Edit one of my current recipes so that I can improve the recipe for other members or users.
- Remove one of my current recipes so I that I can choose to no longer share it with the community.
- To have access to all recipes provided by the community so that I can view content from other members.
- To browse recipes from other members so that I can get inspiration for future meals based on meal type, specific ingredients used and by dietary requirement. 

As a brand owner user, I would like to:

- Create recipes to share with the community so that I can highlight our products from the brand.
- Get the products in as many locations on the website so that I can create awareness for the brand.
- Offer discount to community users so that I can gain potential new customers for the brand. 
- View analytics/reports for the quantity of users that have clicked through to our site to value potential customer acquisition.

### Business/Admin Users

As a business/admin user, I would like to have access to all of the above as well as:

- The ability to edit or remove recipes created by users so that I can vet the content and ensure it's appropriate for users.
- The ability to add, edit or remove recipe categories so that I can keep the categories relevant to what users are searching for.
- The ability to add, edit or remove brands as required to maintain relevance between the recipes and brands currently in the community.
- View the amount of clicks from the featured business page and linked ingredient URLs so that I can gauge potential success of affiliate marketing. 
- Ensure witty helper/success text is present when users add recipes in the community to convey a great sense of Irish humour and provide an enjoyable user experience.


## Design

![Data Success messaging](https://res.cloudinary.com/nclerkin/image/upload/v1620829925/data-success_qvjnaj.png "Data Success messaging")

### Typography
I wanted to use [Montserrat](https://fonts.google.com/specimen/Montserrat#about) for the headings and [Open Sans](https://fonts.google.com/specimen/Open+Sans/#about) as a supporting body font to achieve the desired clean-cut image.

### Icons
Font Awesome icons has been used for this project.

### Color Scheme
The Bia brand monochrome colour scheme was implemented along with pops of green to reflect the Irish fresh products represented throughout the site.
I wanted to keep the color palette simplistic and clean to allow for the imagery from the recipes to stand out and inject the site with colour.
However the colour red is used for error messages for the Signup and Login pages to highlight a warning to the user.

I ended up creating and using the below palette once it had passed rigorous Accessibility testing in **A11y's Color Contrast Accessibility Validator**. 

![Bia Color Palette](https://res.cloudinary.com/nclerkin/image/upload/v1620756644/bia-color-palette_wfndir.png "Bia Color Palette")


## Wireframes

This folder contains [Wireframes](wireframes/wireframes.pdf "Bia Wireframes") including mockups of the homepage, an individual recipe page, submit recipe page, featured business page and account creation page designed at the beginning of the project for desktop, tablet and mobile devices. I have also included the projected [sitemap](https://res.cloudinary.com/nclerkin/image/upload/v1620756692/bia-sitemap_iqzi13.png "Bia Sitemap") and data [schema](https://res.cloudinary.com/nclerkin/image/upload/v1620758330/schema_ufevtk.png "Bia Schema").
**Please note the finalised project contains slight variations to the original wireframes**

[^ Back To Top ](#contents)

# Features

![Admin Profile](https://res.cloudinary.com/nclerkin/image/upload/v1620780109/profile_t2gq79.png "Admin Profile")
## Existing Features
- A clean, simplistic responsive website.
- Clear, fixed navigation which is available to the user if exessive scrolling is required and UI with reused template structure across profile, brand and recipe sections.
- Monochrome palette to allow for recipe and brand sections to focus and capture the user’s attention.
- Header with information about the website and it’s purpose.
- ‘Trending’ section of recipes on the homepage for recipe inspiration.
- ‘Featured Brand’ section to highlight a particular brand and it’s products which links to it’s individual brand profile.
- Footer with social media links, email and website information and icon to propel user back to the top of the page.
- ‘All recipes’ page which can be filtered by category and also has search functionality which pulls from the data in the recipe description and recipe name. Users are also advised to feature brands when adding their recipe so this should pick up brand names also. 
- ‘Bia Brands’ section compiles all brands added by the admin and links to their individual brand page with an about section and related recipes.
- An individual recipe page contains a short description, image, featured brand info, ingredients and recipe info.
- Simple user-friendly register & login pages with Regex defensive programming to ensure registration/login forms are not submitted unless usernames and passwords are between 4-15 characters in length. 
- Confirm deletion modals for defensive programming.
- Route protections to keep pages secure and redirect users that shouldn't have access.
- Personalised Username profile heading 
- User profile with access to any submitted recipes, the ability to add a new recipe to the community, edit it or remove it with delete confirmation popups. 
- Admin user has access to all recipes and can edit or remove them, they also have access to manage categories, brands as well as edit them, remove them or add new ones.
- Flash messaging upon login and CRUD actions.
- 404 & 500 custom built error pages to keep the user on the site when an error appears and to guide them back to the content.

![Custom 404 Page](https://res.cloudinary.com/nclerkin/image/upload/v1620758927/404_rxtgcf.png "Custom 404 Page")

## Features Left to Implement
- Bia newsletter sign up form to update users of new recipes and possible discounts from on-site brands.
- Pagination for inspiration browsing when more users submit recipes to the community 
- Google Sign-in to allow users to sign in quicker and more securely
- Additional brands, recipes & categories as more recipes are submitted to the community.
- Automated recipe/brand review for admin before they are published live on the community or smart filtering for inappropriate content.
- Full user authentication functionality.
- Server side credential validation.
- Ability to favourite recipes/brands
- Submission verification for recipe image URLS and implement a placeholder image if an URL gets broken.
- Enable comments and social media sharing functionality on each recipe.
- Public facing user profiles for general users and brand owners in the style of a social media account such as Instagram so other users can see the recipes created and their favourite recipes/brands.
- Expand the admin profile to include usage and analytics reports to validate possible affiliate marketing.
- Upload image functionality for better UX pictured below but due to time constraints could not implement fully before the stated deadline.
- Individual ingredient fields in the ‘Add recipe’ form so more than one brand can be linked to a recipe.
- Contact form for brand owner users to learn more about promoting their brand on the site.
![Image Upload feature](https://res.cloudinary.com/nclerkin/image/upload/v1620833192/imageupload_uiamfz.png "Image Upload feature")

[^ Back To Top ](#contents)

# Information Architecture

![Bia Sitemap](https://res.cloudinary.com/nclerkin/image/upload/v1620756692/bia-sitemap_iqzi13.png "Bia Sitemap")


## Database Choice
In order to fulfil the project requirements, the NoSQL database MongoDB was utilised to store the data.

This non-relational database structure suits Bia as there are only a few relationships between the various collections. 

![Mongo DB Bia Collections](https://res.cloudinary.com/nclerkin/image/upload/v1620782460/mongodb_s0znhx.png "Mongo DB Bia Collections")

## Data Modeling
The project currently relies on four database collections:

#### Categories collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|category_name|string|The Recipe Category title selected by the admin. This can be edited or deleted in the admin profile.|

#### Recipe collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|recipe_name|string|Name of the recipe inputted by the user. Data used in the search functionality|
|category_name|string|The categories available to the user to select on the addition of their recipe.|
|image_url|string|This is a link to a relevant recipe image.Image upload to be implemented in next release.|
|serves|string|The user to input a number of servings. Could possibly use int in future updates.|
|prep_time|string|The user to input a number related to the time taken to prep the dish as minutes is hard-coded. Could possibly use int in future updates.|
|cook_time|string|The user to input a number related to the time taken to cook the dish as minutes is hard-coded. Could possibly use int in future updates.|
|ingredients|string|All ingredients stored as a string with the user advised to enter each ingrdient on a separate line. Should use an array in the next release when updating each single ingredient to appear in individual fields.|
|method|string|All instructions stored as a string with the user advised to enter each ingrdient on a separate line. Should use an array in the next release when updating each single step to appear in individual fields.|
|recipe_description|string|Short description on the recipe. Data used in the search functionality.|
|brand_name|string|Name of Irish brand featured in the recipe.|
|brand_url|string|This is a link to a brand's website which is displayed at the top of the recipe page above the ingredients.|
|created_by|string|The user in session.|


#### Users collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|username|string|Selected by user on account creation. Cannot be changed.|
|password|string|Selected by user on creation of the account and hashed using Werkzeug Security.|


#### Brands collection

|**Key**|**Type**|**Notes**|
|:-----|:-----|:-----|
|_id|ObjectId||
|brand_name|string| This is connected to the brands inputted at the time of recipe creation. Web display controlled by admin in the admin profile.|
|brand_description|string|Short description about the brand. To appear at the top of individual brand pages.Admin to control this.|
|brand_url|string|The link to the brand's website.Admin to control this.|
|brand_img|string|The url to the brand's logo. Image upload to be implemented in next release.Admin to control this.|


![Bia Schema](https://res.cloudinary.com/nclerkin/image/upload/v1620758330/schema_ufevtk.png "Bia Schema")

[^ Back To Top ](#contents)

# Technologies Used
## Languages
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/) with [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

## Libraries and Frameworks

- [Flask](https://palletsprojects.com/p/flask/)
- [jQuery](https://jquery.com/) 
- [Materialize](https://materializecss.com/)

## Extensions and kits

- [Flask](https://pythonhosted.org/Flask)
- [Werkzeug](https://palletsprojects.com/p/werkzeug/)

## Project management & Databases

- [GitHub](https://github.com/)
- [GitPod](https://gitpod.io/)
- [Balsamiq](https://balsamiq.com)
- [Heroku](https://www.heroku.com)
- [MongoDB](https://www.mongodb.com/)
- [Cloudinary](https://cloudinary.com/)

## Tools
- [Autoprefixer](https://autoprefixer.github.io/) to parse my CSS and add vendor prefixes to allow cross-browser compatibility and support.
- [Freeformatter CSS Beautify](https://www.freeformatter.com/css-beautifier.html) to format and automatically indent my CSS file.
- [Freeformatter HTML Formatter](https://www.freeformatter.com/html-formatter.html) to format the HTML in the project.
- [Freeformatter JS Formatter](https://www.freeformatter.com/javascript-beautifier.html) to format the JS file.      
- [Unicorn Revealer Chrome Extension](https://chrome.google.com/webstore/detail/unicorn-revealer/lmlkphhdlngaicolpmaakfmhplagoaln) to inspect and locate where overflow was located in order to simplify the debugging process. 
- [Favicon.io](https://favicon.io//) to generate the favicons for the site.
- [Font Awesome](https://fontawesome.com/) to define signup, login and nav elements by a visual means.
- [Google Fonts](https://fonts.google.com/) to style the website fonts.
- [Figma](https://figma.com) to create the wireframes for the project and customize images for the homepage.
- [Chrome Dev Tools](https://developers.google.com/web/tools/chrome-devtools) to consistently test the site and run reports from Lighthouse.
- [Color Hex](https://www.color-hex.com/) to create the color palette for my project and help structure the UI for the site. 
- [Color Contrast Accessibility Validator](https://color.a11y.com/) to test for colour contrast on the project.
- [W3C Markup Validation Service](https://validator.w3.org/) to check the markup validity of Web documents in HTML.
- [W3C CSS Validation Service](https://jigsaw.w3.org/css-validator/) to check the validity of my CSS in the project.
- [JS Hint Validator](https://jshint.com/) to analyze and ensure the source code complies with coding rules. 
- [Pep8 Online](http://pep8online.com/) to check code for PEP8 requirements in Python.
- [WAVE Web Accessibility Evaluation Tool](https://wave.webaim.org/) to check the site for Accessibility compatibility and highlight any potenial issues.
- [Am I Responsive?](http://ami.responsivedesign.is/) to provide a preview of the site across a variety of popular devices.  


[^ Back To Top ](#contents)

# Testing
The Testing process has been documented in this [testing.md file](TESTING.md "TESTING.md File")

[^ Back To Top ](#contents)

# Deployment

## Local Deployment

### Requirements:
- [Python 3](https://www.python.org) 
- [PIP](https://pypi.org/project/pip/) 
- [Git](https://git-scm.com/) 
- [MongoDB](https://www.mongodb.com/)


### How to clone Bia:

![Local Deployment](https://res.cloudinary.com/nclerkin/image/upload/v1620783586/deploy_w39xv3.png "Local Deployment")
1. Log in to GitHub and go to [this repository](https://github.com/natashaclerkin/bia-MS3).
2. At the top of the repository, select **Code** and copy the **Clone URL**.
3. In your IDE, open a Terminal window and change to the directory where you want the cloned directory to be made and type `git clone` and paste in `https://github.com/natashaclerkin/bia-MS3.git`.
4. Click enter and the project will be created and cloned locally.

### Working with the local copy:

1. Install all the project dependencies from the terminal window of your IDE by typing: pip3 install -r requirements.txt.
2. Register or login to your [MongoDB](https://www.mongodb.com/) account to create a database. First create a cluster, then a database and the four collections as displayed [here](https://res.cloudinary.com/nclerkin/image/upload/v1620758330/schema_ufevtk.png).
3. Create an env.py file to contain the environment variables, which should include the following:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "**secret key goes here**")
os.environ.setdefault("MONGO_URI", "**mongo uri goes here**")
os.environ.setdefault("MONGO_DBNAME", "**database name goes here**")
```
4. Create a .gitignore file in the root directory of the project and add the env.py to the .gitignore file to prevent the environment variables being made public.
5. Type `python3 app.py` into the terminal to run the app locally. 



## Heroku Deployment

1. Set up local workspace for Heroku by typing `pip3 freeze -- local > requirements.txt` into the terminal to inform Heroku of the files required and then `python app.py > Procfile` to setup the Procfile. 
2. Set up [Heroku](https://www.heroku.com) by signing in or registering an account to create the app. To create the app, you must select the local region and the app must have a unique name.
3. Link the app to the GitHub repository by going to the **Deploy** tab in the main app menu, search for your correct repository and select to connect.
4. Add the corresponding Config Variables by selecting **Config Vars** and click on **Reveal Config Vars**. Input the variables from the IDE created in earlier steps to the **Settings** tab:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`secret key goes here`|
|MONGO_URI|`mongo uri goes here`|
|MONGO_DBNAME|`database name goes here`|

5. Push the requirements.txt and Procfile to repository.
```console
$ git add requirements.txt
$ git commit -m "Add requirements.txt"

$ git add Procfile 
$ git commit -m "Add Procfile"
```

6. Go back to the **Deploy** tab and under **Automatic deploys** select **Enable Automatic Deploys** and under **Manual deploy**, select **master** and click **Deploy Branch**.
7. Once the app has completed the build from Github using the required packages, click **Open app** to reveal the live URL.

[^ Back To Top ](#contents)

# Credits
## Code
I took inspiration from the following sources however I did implement my own custom code:

- I undertook a significant amount of research into backend development in preparation for the project. As well as the Code Institute's walkthrough tutorials by [Tim Nelson](https://github.com/TravelTimN) which provided great guidance for the project, I also watched a significant amount of Youtube tutorials notably [Corey Schafer](https://www.youtube.com/user/schafer5) 



## Content and Media
The Bia logo and main content for the site was created by myself however brand profile descriptions and recipes as well as their images were obtained from their own websites or Roz Purcell's Natural Born Feeder recipes. 

- Lifeforce brand description & logo - [Lifeforce Website](www.lifeforce.ie)
- Dr Coy's brand description & logo - [Dr Coy's Website](wwww.drcoys.ie)
- Strong Roots brand description & logo - [Strong Roots Website](www.strongroots.com)
- Fulfil brand description & logo - [Fulfil Website](www.fulfilnutrition.com)
- Flahavans brand description & logo - [Flahavans Website](www.flahavans.ie)
- Bunalun Organic brand description & logo - [Bunalun Organic Website](www.nationalorganic.com)

- PB Chocolate Cups recipe & image - [Lifeforce Website](www.lifeforce.ie/recipes/peanut-butter-chocolate-cups)
- No Bake PB Fudge Bars recipe & image - [Lifeforce Website](www.lifeforce.ie/recipes/no-bake-peanut-butter-fudge-bars)
- Muesli Flapjack Bars recipe & image - [Lifeforce Website](www.lifeforce.ie/recipes/muesli-flapjack-bars)
- Red Pepper Soup recipe & image - [Lifeforce Website](www.lifeforce.ie/recipes/roasted-red-pepper-almond-butter-soup)
- Protein Brownies recipe & image - [Natural Born Feeder Website](www.naturalbornfeeder.com/brownies-with-white-chocolate-chunks)
- Cookie Dough Balls recipe & image - [Natural Born Feeder Website](https://wwww.naturalbornfeeder.com/cookie-dough-balls)
- Pad Thai recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/peanut-butter-pad-thai-style-noodles)
- Carrot Cake recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/carrot-cake)
- Vegan Stew recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/irish-vegan-stew)
- French Toast recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/french-toast)
- Banana Bread recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/marbled-banana-bread)
- Vegan Wellington recipe & image - [Natural Born Feeder Website](https://www.naturalbornfeeder.com/vegan-christmas-wellington-with-strong-roots)

- 404 & 500 pages spilled sugar background image - [Julie Blanner](https://julieblanner.com/wp-content/uploads/2019/10/how-to-make-cinnamon-sugar-2.jpeg)
- About Bia hero image - [Mamasezz.com](https://www.mamasezz.com/blogs/news/seasonings-without-salt)
- Homepage Lifeforce featured brand image (manipulated in Figma)- [Lifeforce Website](www.lifeforce.ie)


## Acknowledgements

I would like to thank my fellow student Boris Gersic for his help with testing and of course my mentor Guido Cecilio for his continued support and overall guidance throughout the project. 

[^ Back To Top ](#contents) 

# Disclaimer

If there are any issues with copyright of content, please contact me directly and I will amend as soon as possible. This project is for educational purposes only.

[^ Back To Top ](#contents) 