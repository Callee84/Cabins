# **The Cabins**

![](./cabin/assets/img/mockup_cabins.png)

This is the fourth milestone project in the Code Institute Full Stack Developer program. The project is a full-stack framework and has been built for educational purposes. The technologies used for this project are HTML, CSS, JavaScript, Python, and Django.

The Cabins is a fictional booking site for two cabins. One in the mountains of Sälen, Sweden and the ohter on the island of Öland, Swenden. 

[Find the live site here.](https://the-cabins-project.herokuapp.com/)

---

## **UX**
While planing this project / site I first started I broke it down to the 5 planes of:

- The Strategy Plane
- The Scope Plane
- The Structure Plane
- The Skeleton Plane
- The Surface Plane
---
### **The Strategy Plane**
Who am  I trying to reach and connect with in this site? The target audiance is hard to define seeing that the to cabins has different attractions. However, users visitng this site a here because they want a vaction...
There are ofcourse a couple of core components for this site.

- The User should have a easily navagated site wich are informative
- The User should be able to book / reserve a cabin on the site.
- The User should be able to log in to their account and manage their reservations 

#### **User Stories**

##### **Admin Goals**
- As a Site Admin I can See all bookings / reservations that's been made so that I can see manage the cabins bookings / reservations.
- As a Site Admin I can see all the bookings / reservations that been made on the front end so that I can overview the bookings / reservations without logging in back end
- As a Site Admin / User I can rely on authentication so that only I edit / delete my own news articles / post.
- As a Site Admin I can delete my news articles/ posts so that I can control my information to the user.
- As a Site Admin I can edit my news articles/posts so that I can control the content that I write for the user/ guest.
- As a Site Admin I can add news articles on the website so that I can keep users/ guests informed.

##### **User Goals**
- As a Site User I can see available dates for the cabins so that I can make a booking / reservation for a cabin on the website.
- As a Site User I can read / get information about the cabins so that I can make a informed decision about which cabin I want to book.
- As a Site User I can delete my posts so that I can control the posts I made on the website.
- As a Site User I can edit my blog posts so that I can control the content of my post.
- As a Site User I can log in to my account so that I can write posts in the guestbook.
- As a Site User I can see pictures of the cabins so that I know what the cabins look like before I make my booking/ reservation.
- As a Site User I can fill put a contact form so that I can contact the site administrators if I have any questions.

---
### **The Scope Plane**
In order to achieve the desired admin and user goals, the following features will be included in this website:

- Responsive navbar that will navigate to the various pages throughout the site
- Landing page with brief information about the cabins and the cabins locations.
- Register/login feature using Django allauth

---

## **The Structure Plane**
This website is made up with 5 apps (4 of which is connected to the front end)
- cabin_web - the core
- news - handles the news articles that admin manages
- guestbook - hadles the user created posts
- contact - handles the contact form
- cabin_reservation

### *The news app*
The Post model class porvides the model for the admin to create news articles which is dispalyed on the /news page. It also hold the form for which provides the form that is accessable though the front end.

### *The guestbook app*
Just like the news app, the guestbook app provides the model for the user to leave a feedback / post for everryone to read.

### *The contact app*
The contact app provides the form for which the user can send an email to the admin (me) with a question or inquiry for a reservation.

### *The cabin_reservation app*
In the cabin_reservation app is the models for Guest, Cabin and Booking. This provide the admin with the ability to handle bookings on the back end. There is also a form that will (in the future) give the user the abilitiy to book a cabin directily on the website




**UserProfile**
- The user profile is connected to the User model created by Allauth on registration.


---

## **The Skeleton Plane**


---

## **The Surface Plane**



## **Technologies Used**

- [Python](https://www.python.org/) 
- *The following Python modules were used on this project,*
    - asgiref==3.5.2
    - cloudinary==1.30.0
    - dj-database-url==0.5.0
    - dj3-cloudinary-storage==0.0.6
    - Django==3.2.16
    - django-allauth==0.51.0    
    - django-reservation==0.2.10
    - django-summernote==0.8.20.0
    - gunicorn==20.1.0
    - oauthlib==3.2.2
    - psycopg2==2.9.5
    - PyJWT==2.6.0
    - python3-openid==3.2.0
    - pytz==2022.6
    - requests-oauthlib==1.3.1
    - sqlparse==0.4.3
- [ElephantSQL](https://www.elephantsql.com/)
- [Bootstrap](https://getbootstrap.com/)
- [Google Fonts](https://fonts.google.com/)
- [Font Awesome](https://fontawesome.com/)
- [Google Developer Tools](https://developers.google.com/web/tools/chrome-devtools)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Heroku](https://dashboard.heroku.com/apps)
- [Cloudinary](https://cloudinary.com/)

---

## Deployment

### Github & Gitpod

I used the Code Institiue student template as a base for this project.

[Code Institute Full Template](https://github.com/Code-Institute-Org/gitpod-full-template)

- Click the *Use This Template* button.
- Give your repository a name, and description if you wish.
- Click the *Create Repository from Template* to create your repository. 
- Click the *Gitpod* button to create a gitpod workspace, this can take a few minutes.
- When working on project using Gitpod, please open the workspace from Gitpod, this will open your previous workspace rather than creating a new one.
Use the following commands to commit your work, 
- `git add . ` - adds all modified files to a staging area.
- `git commit -m "A short message exlaining your commit"` - commits all changes to a local repository.
- `git push` - pushes all your commited changes to your Github repository.

*Forking the GitHub Repository*

If you want to make changes to your repository without affecting it, you can make a copy of it by 'Forking' it. This ensures your original repository remains unchanged.

### Creating an Application with Heroku

I followed the below steps using the Code Institute tutorial, *with the updated information* and [Django Blog cheatsheat](https://codeinstitute.s3.amazonaws.com/fst/Django%20Blog%20Cheat%20Sheet%20v1.pdf)

- The following command in the Gitpod CLI will create the relevant files needed for Heroku to install your project dependencies `pip3 freeze --local > requirements.txt`. 
- A `Procfile` is also required that specifies the commands that are executed by the Heroku app on startup. 

1. Go to [Heroku.com](https://dashboard.heroku.com/apps) and log in; if you do not already have an account then you will need to create one.

![Heroku start app](./cabin/assets/img/heroku_start.jpeg)

2. Click the `New` dropdown and select `Create New App`.

![Heroku start app](./cabin/assets/img/heroku_create.jpeg)

3. Enter a name for your new project, all Heroku apps need to have a unique name, you will be prompted if you need to change it.


4. Select the region you are working in.

*Heroku Settings*
You will need to set your Environment Variables - this is a key step to ensuring your application is deployed properly.

c
- In the Settings tab, click on `Reveal Config Vars` and set the following variables:
    - CLOUDINARY_URL - to be set to your Cloudinary API environment variable
    - DATABASE_URL - to be set to your database *In my the URL to my ElephantSQL database*
    - PORT - 8000
    - SECRET_KEY - to be set to your chosen key
    - DISABLE_COLLECTSTATIC - 1

![Heroku start app](./cabin/assets/img/heroku_config_see.jpg)


*Heroku Deployment*
In the Deploy tab:
1. Connect your Heroku account to your Github Repository following these steps:
    1. Click on the `Deploy` tab and choose `Github-Connect to Github`.
    2. Enter the GitHub repository name and click on `Search`.
    3. Choose the correct repository for your application and click on `Connect`.
2. You can then choose to deploy the project manually or automatically, automatic deployment will generate a new application every time you push a change to Github, whereas manual deployment requires you to push the `Deploy Branch` button whenever you want a change made.
3. Once you have chosen your deployment method and have clicked `Deploy Branch` your application will be built and you should see the below `View` button, click this to open your application:


## Credits

Building this website I've used a lot of different sources to seach for functions & bug fixes. 
I've used boostrap as a core for style. The split image i found as a code along on youtube with credit to Code Instinct.
For the news / post funcitions I've took inspiration from Code Institute's Walkthough project "I Think Therefore I Blog" and John Elder from Codemy.com.


