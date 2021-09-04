# BobZZ Your Uncle!

## Code Institute - Milestone Project 3


- The purpose of **BobZZ Your Uncle** is to provide an easy to follow, straightforward habit tracking website, to inspire people interested in self-development. Users will be able to follow pre-existent habits, as well as create, edit and delete their own. The simplicity and intuitive UI will ensure that users of different age groups will enjoy continuously using the **BobZZ Your Uncle** website to improve their lives.


## Table of Contents
> - [Overview](#overview)
> - [Description](#description)
> - [Ux](#ux)
> - [User Stories](#user-stories)
> - [Features](#features)



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