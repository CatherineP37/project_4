# Medical Appointment Booking App

This is an app that helps to make it easy for patients to book appointments at
a medical centre. The app helps to reduce the number of calls coming through to
the medical centre. This means that the patients who do call in don't have to
wait as long for their call to be answered.

## Scope

The following must be included in the app:

- Patient log in screen
- Sign up form for new account
- Booking form
- List of available appointments
- Ability to view booked appointments
- Ability to cancel appointments

It's not necessary to include the following in the app:

- Doctor log in screen
- Patient notes

## Sitemap

![Sitemap](images/map.png)

## User Stories

Epic - patient account

- As a patient I want to set up an account so that I can easily book appointments online.
- As a patient I want to be able to sign in and out of my account easily.
  
Epic - booking an appointment online

- As a patient I want to book an appointment easily online.
- As a patient I want to see a list of available appointments.
- As a patient I don't want to book an appointment that someone else has booked.

Epic - managing my appointments

- As a patient I want the option to see the appointments that I've booked.
- As a patient I want the option of updating my booking.
- As a patient I want the option of cancelling my booking.

## Wireframes

These are wireframes for the mobile screens.

![wireframes](images/wireframes.png)

## Database Schema

![database schema](images/database.png)

## Features

## Bugs

There was an issue with trying to get the dropdown menu to work. By mistake I hadn't put the link to the JavaScript file in the html file. After I added the link, the dropdown menu worked but was only showing the dropdown part while it was being pressed. Also the words were not visible and the width of the dropdown was very narrow and that's probably why the words weren't on it. I solved the issue by changing the css.

The header was set to position: fixed and was covering the content. To solve this I increased the size of the margin at the top of the main section.

I had problems deploying my project to Heroku. This was solved by adding the correct Config Vars to Heroku.

The navigation menu was showing the same things for signed in users as signed out users. This was solved by changing the urls.

The text on the buttons was not fitting in the mobile view so I set the font size in percentage instead of pixels.

I was trying to prevent double bookings by filtering out appointments that had been booked. It wasn't working and the booked appointments were still showing up on the list of available appointments. This was solved by editing the booking view.


## Testing

## Deployment

This project was deployed using Heroku.

A Procfile and a requirements.txt was added to the project.

A new app was set up in Heroku and the config vars were added to the app.

GitHub was selected as the deployment menthod and the GitHub repository was linked to Heroku.

"Deploy Branch" was selected to manually deploy the project.

## Credits






