# BobZZ Your Uncle!

## Code Institute - Milestone Project 3


- The purpose of **BobZZ Your Uncle** is to provide an easy to follow, straightforward habit tracking website, to inspire people interested in self-development. Users will be able to follow pre-existent habits, as well as create, edit and delete their own. The simplicity and intuitive UI will ensure that users of different age groups will enjoy continuously using the **BobZZ Your Uncle** website to improve their lives.


## Table of Contents
> - [Overview](#overview)
> - [Description](#description)
> - [Ux](#ux)
> - [User Stories](#user-stories)
> - [Features](#features)
> - [Technologies Used](#technologies-used)
> - [Credits](#credits)
> - [Deployment](#deployment)



## Overview
 As the Pandemic has changed our lives completely, we live in a new reality. More and more people have been looking for an escape and ways to keep themself busy. One of the directions many have ventured into is self-improvement - which is why I have decided to create a website for habit tracking. **BobZZ Your Uncle** focuses on simple and clear usability and offers concise information for forming lasting habits, to inspire users to change their lives. 

 
## Description 

**BobZZ Your Uncle** is simple in use and gives the users the oportunity to follow pre-existing habits, create their own as well as track their progress. A potential user can see Home and All Habits pages, as well as Log In and Sign Up. Where Home Page has a hero image and brief information about habits and invitation to join the self-developement journey. All Habits page has 3 cards with public habits that user can view and once registered can clone. A signed up user can view additional two pages, which are My Habits and Add Habit. Where My Habits page shows the habits that user would create themselves and after be able to edit, delete and track their pogress, besides that user can clone a habit from All Habits page. Add Habit page has form for creating a habit. An admin user has access to Manage Categories page, where they can create, edit and delete categories. As well as admin user is the only one able to edit or delete 3 cards on All Habits page.


---
## UX  

## Strategy

**BobZZ Your Uncle** is targeting all age groups of those who interested in self-devolepement. It's target is to have a simple habit tracking website that anyone can use. This website has all the basic easy to follow funcionality needed for creating and tracking user's habits. There are hardly any websites for habit tracking and for this reason this website is offering cross platform integration.

**User Stories**

#### As a First Time User:
- I want the website to have a visually clear purpose.
- I want to be able intuitively browse through the website and easily find all the pages.
- I want the functionality to be simple with engaging content.

#### As a Returning User: 
- I want to find out more about habit tracking.
- I want to see how this website is different to others like it and what the benefits are.
- I want to sign up, to be able to use all the functions and check how straightforward the usability is.


#### As a Frequent User: 
- I want to easily add new habits and have an option to add a description, once I've logged in.
- I want a simple way to tick off the completed habit/s for the day.
- I want to be able to track my progress.

## Scope

- I have chosen minimalistic and clear design which allows users to focus on habits tracking as this is the main purpose of the website.
- The Home page gives a brief information about forming habits and buttons inviting to Sign Up & check recommended habits. Recommended habits are 3 habits created by admin which could be cloned to add to My Habits page. On My Habits page user can edit, delete and track their progress. The progress can be conviniently seen under the description of the card.
- I have used mixed content of cards with image, buttons and text.

## Structure

This website has different sets of pages, dependant on weather user is logged in or not, or if are an admin. 
**First time user four pages are visible:** 
- Home 
- All Habits 
- Log In
- Sign Up

**For registered User another four pages visible:**
- Home
- All Habits
- My Habits
- Add Habit
Additionally, they have Log Out option

**For Admin User five pages + Log Out:**
- Home
- All Habits
- My Habits
- Add Habit
- Manage categories

## Skeleton

- Home Page: <a href="wireframes/home-wireframe-b.pdf" target="_blank" >Home</a>

- All Habits Page: <a href="wireframes/habits-wireframe-b.pdf" target="_blank" >All Habits</a>

- Add Habit Page: <a href="wireframes/add-habit-wireframe-b.pdf" target="_blank" >Add Habit</a>

- Manage Catefories Page: <a href="wireframes/categories-wireframe-b.pdf" target="_blank" >Manage Catefories</a>
---

## Surface

## Surface

I have used minimalistic design with simple layout. Home page has hero image with text box on top of it, apart from it the rest of elements are done in simplistic design with 3 main colours. Cards have an image in them and underneatch on cyan backroung is habit's elements in white text. All the buttons, forms and cards are following the main colour scheme.


### Images
- Two images have been used for this website. The hero image at the top of the Home page with the text box with the quote are designed to draw user's attention to the purpose of the website. While on All Habits & My Habits pages there is one image on each card at the moment.

-   ### Design
    -   #### Colour Scheme
        - Main colors of the website are - peach, cyan and white. This colourscheme is consistant throughout all pages and is calm without causing any distress or sidtructions from main purpose of the website.
    -   #### Icons
        - Font Awesome was used for icons which are psent on all pages: next to heading of 3 steps on the Home page, on most of the buttons, on the forms for adding & editing habits and ategories, on Signing Up & Log In forms and social links in the footer.

## Features

#### Navbar
- Logo and website name can be clicked on any page and it will take the user to Home page.
- Favicon has been added to show on the tab, matching the logo.
- On a mobile, the navbar is then collapsed to show the toggler which expands when clicked to display the nav elements as sidenav, which can be swiped or removed by clicking on blank space

#### Home
- Contains the hero image of graphic mountains with nearly transparant peach text box with text-shadow accents.
- Grid system used to create 3 columns: for 3 simple steps of forming a habit with icons next to the title of each of them.
- Underneath those steps are two buttons: 1) is inviting to sign up & 2) is inviting to check out recommended habits on All Habits page.

#### All Habits
- Contains pablic cards with habits
- Habits can be cloned once user signed up
- Card reveal allows user to see the description
- Card reveal can be accessed by clicking either on the image or three dots next to habit name
- Card contains prechosen completion time type (i.e. minutes or time of the day) where user can still choose a completion time 
- Done button can be clicked once task is completed and it will add to progress
- Progress updates in the description of the habit after each click of done button
- Progress shows the day of completion and completion time chosen by user
- Search on the top will search only for public habits

#### My Habits
- Contains all the same features as My Habits page apart from clone function
- Once habit added it can be edited and delted if user wishes so
- Edit funcion is redirecting to Edit Habit page where pre-filled fields can be ammended
- Once habit has been edited it will redirect back to My Habits page and flash message will notify of successful update
- When user presses delete button a delete confirmation modal pops up to avoid accidental deletion
- Search on the top will search only for habits created by user

#### Add Habit
- Contains form with fields to fill in (which are required) as well as dropdown for category and completion time typle selection
- Redirects to My Habits page once habit was created, showing flash message for successful creation


#### Sign Up 
- Contains form for signing up
- Checks if username already exists
- Has minimum and maximum length for password
- Checks if password if password is matching
- Redirects to My Habits page once user signed up with "Welcome {username}" message

#### Log In
- Checks if username is in data base (db from now on)
- Checks if password is correct
- If either of them incorrect shows "Incorrect Username and/or Password" message
- Redirects to My Habits page once logged in

#### Footer
- Sign Up button (following the rounded shape of all buttons) can be clicked for user to go straight to sign up page
- Social media icons link to the pages about habits for more inspiration, which will open in seperate tab.

### Features Left to Implement
- Public or Private option when user creates habit.
- Different images choice for habit cards
- Progress page seperate with graphs
---

## Technologies Used

#### Languages:
- [CSS3](https://developer.mozilla.org/en-US/docs/Web/CSS)
- [HTML5](https://developer.mozilla.org/en-US/docs/Web/HTML)
- [Javascript](https://developer.mozilla.org/en-US/docs/Web/JavaScript)
- [Python](https://www.python.org/) with [Jinja](https://jinja.palletsprojects.com/en/2.11.x/)

#### Libraries:
- [Materialize 1.0.0](https://materializecss.com/getting-started.html) - A mobile-first responsive library used to construct various parts of the website, including the All Habits & My Habits cards, Navbar, Footer, Add Habit, Edit Habit, Log In & Sign Up Form, Grid System and Buttons.
- [jQuery](https://jquery.com/) - Used for sidenav, confirm delete modal, for select and password match check.
- [Flask](https://palletsprojects.com/p/flask/) 
- [FontAwesome](https://fontawesome.com/) - Used for icons used for header, footer, in front of titles of three steps on home page, in front of input fields of all forms and in most of buttons.
- [Balsamiq](https://balsamiq.com/wireframes/?gclid=EAIaIQobChMIn-_lgbiJ7QIVn4BQBh1X3Av6EAAYASAAEgL1XfD_BwE) - used for creating the wireframes

#### Version Control:
- [Github](https://github.com/) - Used to store the code and to deploy the website. 
- [Gitpod](https://gitpod.io/) - Used as the primary version control IDE for development to further push and commit code to Gihub.

#### Other:
- [Code Institute Course Content](https://courses.codeinstitute.net/) - Main learning base as well as inspiration for curtain features.
- [ChromeDevTools](https://developers.google.com/web/tools/chrome-devtools) - Used frequently to check layout, responsivness and any malfunctions.
- [W3Schools](https://www.w3schools.com/) - used for CSS coding tips.
- [StackOverFlow](https://stackoverflow.com/) - used as a general resource for both styling and HTML tips as well as python tips.
- [Online Web Tutor](https://onlinewebtutorblog.com/how-to-validate-password-and-confirm-password-using-jquery/) - Used for confirm password (check if password match) functionslity in jQuery.
- [Google Mobile Friendly Test](https://search.google.com/test/mobile-friendly) - Used to test all pages on a mobile device
- [AmIResponsive](http://ami.responsivedesign.is/) - Used to see how the layout of the website looks across different devices- found at the top of this [README](https://github.com/Juliya91/bobzz-your-uncle/blob/main/README.md). 

# Testing
The Testing process has been documented in this [TESTING.md file](TESTING.md "TESTING.md File")

# Deployment

## Local Deployment

### Requirements:
- [Python 3](https://www.python.org) 
- [PIP](https://pypi.org/project/pip/) 
- [Git](https://git-scm.com/) 
- [MongoDB](https://www.mongodb.com/)


### How to clone BobZZ Your Uncle:

- Log in to GitHub and create a new repository by clicking "+" next to my profile avatar and choosing "New repository".
- Go to [this repository](https://github.com/Juliya91/bobzz-your-uncle).
- Once added a Gitpod extention to a browser, on GitHub repository click on the green "Gitpod" button next to code button which will redirect to [Gitpod](https://gitpod.io/)
- Gitpod, an IDE used to write all the code and this README file for this project.

- Install all the project dependencies from the terminal window of your IDE by typing: pip3 install -r requirements.txt.
- Register or login to your [MongoDB](https://www.mongodb.com/) account to create a database. First create a cluster, then a database and the four collections.
- Create an env.py file to contain the environment variables, which should include the following:

```console
import os

os.environ.setdefault("IP", "0.0.0.0")
os.environ.setdefault("PORT", "5000")
os.environ.setdefault("SECRET_KEY", "**secret key goes here**")
os.environ.setdefault("MONGO_URI", "**mongo uri goes here**")
os.environ.setdefault("MONGO_DBNAME", "**database name goes here**")
```
4. Create a .gitignore file in the root directory of the project and add the env.py to the .gitignore file to prevent the environment variables from being made public.
5. Type `python3 app.py` into the terminal to run the app locally. 



## Heroku Deployment

- Set up local workspace for Heroku by typing `pip3 freeze -- local > requirements.txt` into the terminal to inform Heroku of the files required and then `python app.py > Procfile` to setup the Procfile. 
- Set up [Heroku](https://www.heroku.com) by signing in or registering an account to create the app. To create the app, you must select the local region and the app must have a unique name.
- Link the app to the GitHub repository by going to the **Deploy** tab in the main app menu, search for your correct repository and select to connect.
- Add the corresponding Config Variables by selecting **Config Vars** and click on **Reveal Config Vars**. Input the variables from the IDE created in earlier steps to the **Settings** tab:

|**Key**|**Value**|
|:-----|:-----|
|IP|`0.0.0.0`|
|PORT|`5000`|
|SECRET_KEY|`secret key goes here`|
|MONGO_URI|`mongo uri goes here`|
|MONGO_DBNAME|`database name goes here`|

- Push the requirements.txt and Procfile to repository.
```console
$ git add requirements.txt
$ git commit -m "Add requirements.txt"

$ git add Procfile 
$ git commit -m "Add Procfile"
```

- Go back to the **Deploy** tab and under **Automatic deploys** select **Enable Automatic Deploys** and under **Manual deploy**, select **master** and click **Deploy Branch**.
- Once the app has completed the build from Github using the required packages, click **Open app** to reveal the live URL.

## Credits

### Content

- Parts of text for welcome part of Home and page was ispired by YouTube video [The "It Takes 21 Days To Form A Habit" Myth: BUSTED](https://www.youtube.com/watch?v=_bbEviC9qSc)

### Media

- The photos for this project were taken from Adobe Stock and Bing images.
---
### Acknowledgements
- My Mentor **Antonio Rodriguez** for his tremendous help, motivation, inspiration and guidance on the sessions.