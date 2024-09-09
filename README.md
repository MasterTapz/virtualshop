# VirtualShop

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, I created a new folder called VirtualShop, then set up the environment and installed the required libraries from the requirements.txt file. Once the setup was complete, I started a new Django project and created the main app. Now, I had two folders, main and VirtualShop, which I connected through urls.py and settings.py. Next, I created the product model, giving it attributes like name, price, description, and status. Since I was using a model, I created an admin account so I could manage products through the admin interface at "http://127.0.0.1:8000/admin/". After that, I updated views.py to display the products and created the templates/main.html file to render them. Once everything worked, I created a new GitHub repository to connect it to PWS. After using git add, commit, and push, my program was ready to be deployed on PWS, and my website was successfully launched. 

## Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.




## Explain the use of git in software development!


Git is a tool used in software development to track code changes and help developers work together smoothly. It allows multiple people to work on a project at the same time without interfering with each other's work. Git keeps a record of all changes, making it easy to go back to earlier versions if needed and see who made updates. It also has features like branching and merging, which let developers work on new features or fix bugs separately before combining them into the main project, making teamwork and project management easier.


## In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

In my opinion, Django is a great starting point for learning software development because it simplifies complex tasks, letting you focus on core concepts. It comes with built-in tools like authentication and an admin panel. I love how its structure guides you into best practices, making it easier to understand web development fundamentals.

## Why is the Django model called an ORM?

Because Django models allow you to work with databases using Python code rather than SQL, they are also known as ORMs. In Django, every model is a table, with the fields mapping to the columns of the table. Because you can add or update records using straightforward Python commands rather than using SQL queries, this makes database management much simpler. It really improves the entire working with database.









LINKS TO MY ASSIGNMENT 2: http://muhammad-brian31-virtualshop.pbp.cs.ui.ac.id/