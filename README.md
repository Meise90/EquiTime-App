
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/powered-by-coffee.svg)](https://forthebadge.com)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
## Table of contents

* [General info](#general)
* [Used technologies](#used-technologies)
* [How to start](#how-to-start)
* [Modules description](#modules-description)

## General info
<details>
<summary>Click here to see more information about <b>EquiTimeApp Project</b>!</summary>
<br>
The application was created in Django and is used to manage an equestrian 
center. It is divided into several minor applications that are designed to 
improve the daily operations of the center and its users. Each application will be 
descriebd below.
<hr>
<strong>The whole project is under constant development</strong>
</details>


## Used technologies

<ul>
<li>Python 3.x</li>
<li>Django</li>
<li>Celery</li>
<li>Django-Celery-Beat</li>
<li>Twilio API</li>
<li>BeautifulSoup</li>
</ul>

## How to start

<ol>
<li>Clone this repo: <b>git clone https://github.com/Meise90/EquiTime-App.git</b></li>
<li>Install dependencies: <b>pip install requirements.txt</b></li>
<li>Install Redis (please note that for MacOS you need to install Homebrew first): <a href="https://redis.io/docs/getting-started/installation/" target="_blank">Redis installation</a></li>
</ol>


## Modules description
### 1. Homepage, registration

<details>
<summary>Click here to see more information about <b>Registration process.</b></summary>
<br>
A new user must sign up to see contents of other tabs and be able to use the features.
After filling out the forms (validation of each data, unique username and email address) the user gets two 
emails: a welcome email and email with one-time generated token to confirm his identity, 
email address and finish the registration process. After that user gets logged in automatically and can start using the app. 
In database he is marked as active user. If user doesn't activate his account in 24 hours by clicking the link he will 
be deleted from the database - Celery and Celery-beat are responsible for this task. Beat is checking the database 
every single hour.
</details>


### 2. Schedule
<details>
<summary>Click here to see more information about <b>Schedule module.</b></summary>
<br>
This tab is visible for all registered and active users. The functionality of this app is
to help organize the occupancy of the indoor arena in the center. The schedule should be
used to enter planned activities with the horse (e.g. jumping, flat work, dressage training etc.).
Indoor arena capacity is limited, it helps to plan the trainings so that there won't be 
20 horses inside at the same hour. The schedule is being cleared every week at 2 AM on Mondays - 
Celery and Celery-beat are responsible for this task as well. 
Schedule can be cleared at any time by the Admin.
</details>

### 3. Noticeboard
<details>
<summary>Click here to see more information about <b>Noticeboard module.</b></summary>
<br>
This tab is visible for all registered and active users. 
The noticeboard helps to communicate important information to all users of 
the stable. 
Each user can pin a note, which is visible to all other active users. 
A note can only be edited or deleted by the user who is the author of 
the note. 
Only the administrator can delete all notes. 
Each note is signed with the author's nickname and the date and time of 
creation.
</details>


### 4. Reminder
<details>
<summary>Click here to see more information about <b>Reminder module.</b></summary>
<br>
This tab is visible for all registered and active users. 
The app allows a logged-in user to add an activity, set its date and time and then set a reminder for a given day and 
time. The reminder is sent to the email address provided by the user during registration. 
The user can also tick a checkbox so that the reminder is also sent to their phone by text message. 
Each logged-in user can only see their own events and cannot access other users' events. 
This module uses the Twilio API (for text message sending) and of course Celery and Celery-Beat.
</details>

### 5. Competitions
<details>
<summary>Click here to see more information about <b>Competitions module.</b></summary>
<br>
This tab is visible for all registered and active users. 
This tab shows a list of the current 100 upcoming equestrian events in Poland and links to them. The tool used here is BeautifulSoup, 
web scraping based on the website www.zawodykonne.com - tab 'Current'.
</details>




