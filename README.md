# VirtualShop
LINKS TO MY WEBSITE: http://muhammad-brian31-virtualshop.pbp.cs.ui.ac.id/



## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, I created a new folder called VirtualShop, then set up the environment and installed the required libraries from the requirements.txt file. Once the setup was complete, I started a new Django project and created the main app. Now, I had two folders, main and VirtualShop, which I connected through urls.py and settings.py. Next, I created the product model, giving it attributes like name, price, description, and status. Since I was using a model, I created an admin account so I could manage products through the admin interface at "http://127.0.0.1:8000/admin/". After that, I updated views.py to display the products and created the templates/main.html file to render them. Once everything worked, I created a new GitHub repository to connect it to PWS. After using git add, commit, and push, my program was ready to be deployed on PWS, and my website was successfully launched. 

## Create a diagram that contains the request client to a Django-based web application and the response it gives, and explain the relationship between urls.py, views.py, models.py, and the html file.


Client (browser Makes HTTP Request) ---> urls.py (URL routing) ---> models.py(Database) --> HTML Template ---> loop back to urls.py


## Explain the use of git in software development!


Git is a tool used in software development to track code changes and help developers work together smoothly. It allows multiple people to work on a project at the same time without interfering with each other's work. Git keeps a record of all changes, making it easy to go back to earlier versions if needed and see who made updates. It also has features like branching and merging, which let developers work on new features or fix bugs separately before combining them into the main project, making teamwork and project management easier.


## In your opinion, out of all the frameworks available, why is Django used as the starting point for learning software development?

In my opinion, Django is a great starting point for learning software development because it simplifies complex tasks, letting you focus on core concepts. It comes with built-in tools like authentication and an admin panel. I love how its structure guides you into best practices, making it easier to understand web development fundamentals.

## Why is the Django model called an ORM?

Because Django models allow you to work with databases using Python code rather than SQL, they are also known as ORMs. In Django, every model is a table, with the fields mapping to the columns of the table. Because you can add or update records using straightforward Python commands rather than using SQL queries, this makes database management much simpler. It really improves the entire working with database.







# Assignment 3

## Explain why we need data delivery in implementing a platform?

Data delivery is key to making a platform functional because it's what ensures that all the pieces work together, whether it’s a user requesting information, the platform processing data, or syncing with external services. If data isn’t delivered properly, you’re left with a platform that feels slow, unreliable, or downright broken. It’s not just about moving information from one place to another, but doing it efficiently so users can have a seamless experience without delays or errors.

## In your opinion, which is better, XML or JSON? Why is JSON more popular than XML?

Personally, I think JSON is far better than XML for most situations. JSON is easier on the eyes, simpler to write, and works beautifully with JavaScript, which is everywhere nowadays. XML, while powerful, feels bloated and over-complicated for many tasks that JSON handles more cleanly and quickly. JSON's popularity really comes down to its ease of use in web development, especially when you're working with APIs. It gets the job done with less fuss and better performance, which is why most developers prefer it.

## Explain the functional usage of is_valid() method in Django forms. Also explain why we need the method in forms?

The is_valid() method in Django forms is like a checkpoint for your data, making sure that everything is in order before you move forward. It’s there to ensure that the data submitted by users passes the necessary validation checks and that only clean, usable information gets processed. Without it, you'd be risking errors or even security issues caused by faulty or malicious data. It's not just about following the rules; it’s about protecting the integrity of your app and ensuring smooth interactions for everyone involved.

## Why do we need csrf_token when creating a form in Django? What could happen if we did not use csrf_token on a Django form? How could this be leveraged by an attacker?

Using csrf_token in Django forms is crucial because it adds a layer of security that helps protect your app from malicious attacks, specifically CSRF attacks. If we didn’t include it, attackers could easily trick users into performing unwanted actions, like making transactions or changing account settings, without their knowledge. It’s a simple token, but without it, your app is left vulnerable to hackers who could exploit user trust and mess with sensitive data. So, it’s a small but vital piece of security that shouldn’t be overlook.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial).

First, i create a new file called form.py consisting the model and the fields. After that I created the 4 views requested from the assignment. After that, I renew the main.html and make the base.html and create_product_entry.html. Now after all of this I route all of the views in the urls.py. Lastly, I modify settings.py templates, now I could add product through the form in the web


## POSTMAN RESULT


### XML

![](image.png)

### XML ID

![](image-1.png)

### JSON

![](image-2.png)


### JSON ID

![](image-3.png)



# Assignment 4

## What is the difference between HttpResponseRedirect() and redirect()?

HttpResponseRedirect() is a low-level Django class that returns an HTTP 302 response to redirect the user to another URL. It requires the full URL as an argument.

redirect() is a shortcut function in Django that provides higher-level functionality. It can accept a URL, a view name, or arguments for reverse URL lookups, making it more convenient for developers.

 ## Explain how the MoodEntry model is linked with User!

The MoodEntry model can be linked to the User model using a ForeignKey field. This establishes a one-to-many relationship where each mood entry belongs to a specific user.
Example: ForeignKey(User, on_delete=models.CASCADE) links each mood entry to a user, and if a user is deleted, their corresponding mood entries are also deleted.

 ## What is the difference between authentication and authorization, and what happens when a user logs in? Explain how Django implements these two concepts.
 
 Authentication: Verifies the identity of the user, usually through credentials like a username and password. In Django, the authenticate() function checks if the user exists and if their credentials are correct.

Authorization: Determines what actions the user is allowed to perform once authenticated. Django checks the user’s permissions or roles to allow or deny access to specific resources.

When a user logs in, Django authenticates the credentials and, upon success, creates a session, storing the user’s ID server-side and marking the user as logged in via session middleware.
 
 ## How does Django remember logged-in users? Explain other uses of cookies and whether all cookies are safe to use.
 
 Django uses sessions to remember logged-in users. After successful login, Django stores the user's session ID in a cookie on the client’s browser. This session ID is used to retrieve the user's session data on the server, keeping the user logged in across multiple requests.

Cookies can also store user preferences (e.g., theme, language), shopping cart data, and tracking information. While useful, cookies can pose security risks like session hijacking.

To enhance cookie safety, Django allows the use of HttpOnly (to prevent JavaScript access) and Secure (to only send cookies over HTTPS) flags. These flags help protect cookies from security vulnerabilities such as cross-site scripting (XSS) and man-in-the-middle attacks.
 
 ## Explain how did you implement the checklist step-by-step (apart from following the tutorial).

I started by creating the functions for user registration, login, and logout in the `views.py` file. Afterward, I mapped these functions to their respective paths in `urls.py`. Next, I worked on the templates, creating `register.html` and `login.html`, which serve as the user interface for registration and login. For the logout functionality, I added a button in `main.html` so users can easily log out from their accounts. After completing the functions, I created two user accounts, each containing three pieces of data, and ensured that the data for each user can be accessed locally. To achieve this, I used the line `user = models.ForeignKey(User, on_delete=models.CASCADE)` in the model, which links the data to the respective user.

Finally, I applied cookies to track user activity by modifying the `show_main`, `login_user`, and `logout_user` views. Cookies are used to store the last login time, so I updated the `show_main` view to include this information in the context, allowing `main.html` to display the user's last login. In the `login_user` view, I set the cookie when the user logs in, and in `logout_user`, I handled the cookie expiration when the user logs out.


# Assignment 5


## If there are multiple CSS selectors for an HTML element, explain the priority order of these CSS selectors!

Cascading Style Sheets (CSS) provide a way to style HTML elements, allowing developers to create visually appealing web pages. However, when multiple CSS selectors apply to a single HTML element, determining which styles are applied can be complex. The priority order of CSS selectors is essential to understand, as it governs how styles cascade and interact. 

At the top of the priority hierarchy are **inline styles**, which are defined directly within the HTML elements using the `style` attribute. For example, `<div style="color: red;">Hello World</div>` will render the text in red, overriding any other styles applied via external or internal stylesheets. This is because inline styles carry the highest specificity.

Next in line are **IDs**, which are unique selectors that can be applied to a single element on a page. For instance, the CSS rule `#header { background-color: blue; }` will apply to any HTML element with the ID "header." Since IDs have a higher specificity than class selectors, they will take precedence over styles defined by classes.

Following IDs are **classes**, which can be applied to multiple elements on a page. A CSS class selector is denoted with a period (`.`), such as `.button { color: white; }`. Class selectors have a lower specificity than IDs but higher than element selectors, which target specific HTML tags, such as `div`, `p`, or `h1`.

Finally, **element selectors** and **universal selectors** (denoted by the asterisk `*`) have the lowest specificity. They apply styles to all instances of a particular HTML tag or all elements, respectively. For example, the rule `p { margin: 20px; }` applies a margin to all paragraph elements but can easily be overridden by more specific selectors.

In addition to the specificity hierarchy, the order in which CSS rules are declared in the stylesheet can also affect which styles are applied. If two selectors have the same specificity, the latter one will take precedence. This cascading behavior allows developers to fine-tune styles and ensure the desired appearance of elements on the page.

## Why does responsive design become an important concept in web application development? Give examples of applications that have and have not implemented responsive design!

Responsive design has become a crucial concept in modern web application development, reflecting the diverse array of devices and screen sizes used to access the internet. With the rise of smartphones, tablets, and various screen resolutions, ensuring a seamless user experience across devices is paramount. Responsive design allows web applications to adapt their layout and content to fit different screen sizes, orientations, and resolutions.

One of the primary reasons responsive design is important is that it enhances user experience. Users expect web applications to be visually appealing and easy to navigate, regardless of the device they are using. A responsive design ensures that elements are appropriately sized, menus are accessible, and content is readable, regardless of whether the user is on a desktop, tablet, or mobile phone.

Examples of applications that have successfully implemented responsive design include popular platforms like **Amazon** and **Netflix**. These websites automatically adjust their layouts, images, and navigation menus to provide an optimal viewing experience on any device. Conversely, applications that have not implemented responsive design can lead to frustration for users. For instance, websites that are not optimized for mobile may display small text, require horizontal scrolling, or have buttons that are difficult to click. This can deter users and lead to higher bounce rates.

In summary, responsive design is essential for delivering a positive user experience in today’s multi-device landscape. By prioritizing responsive design, developers can ensure that their applications are accessible and usable across various devices, enhancing user satisfaction and engagement.

## Explain the differences between margin, border, and padding, and how to implement these three things!

Understanding the differences between **margin**, **border**, and **padding** is fundamental in CSS as they all play distinct roles in the box model, which is the basis for layout in web design.

**Margin** refers to the space outside an element's border. It creates distance between the element and other surrounding elements. Margins are transparent and can be set using CSS properties such as `margin-top`, `margin-bottom`, `margin-left`, and `margin-right`, or the shorthand `margin`. For example, `margin: 20px;` sets a 20-pixel margin on all sides of an element.

**Border** is the line surrounding an element’s padding and content. It can be styled with various attributes such as thickness, color, and style (solid, dashed, dotted, etc.). The border is part of the element’s box and occupies space, contributing to the overall dimensions of the element. You can set borders using properties like `border-width`, `border-style`, and `border-color`, or use the shorthand `border`. For instance, `border: 1px solid black;` creates a solid black border that is 1 pixel thick.

**Padding** is the space between the content of an element and its border. It creates breathing room inside the element, ensuring that the content does not touch the border. Padding can also be set using properties such as `padding-top`, `padding-bottom`, `padding-left`, and `padding-right`, or the shorthand `padding`. For example, `padding: 15px;` applies a 15-pixel padding to all sides of the element.

In summary, while margin creates space outside an element, padding creates space inside the element, and border is the line that surrounds the padding and content. Understanding how to manipulate these properties is crucial for achieving desired layouts and spacing in web design.

## Explain the concepts of flex box and grid layout along with their uses!

Flexbox and Grid Layout are two powerful CSS layout systems that provide developers with flexible and efficient ways to design web layouts.

**Flexbox**, or the Flexible Box Layout, is designed for one-dimensional layouts. It allows items within a container to align and distribute space dynamically. The main advantage of Flexbox is its ability to control the alignment and spacing of items along a single axis (either horizontally or vertically). With properties like `justify-content`, `align-items`, and `flex-direction`, developers can easily control how items are displayed within a flex container. For example, a navigation bar can be efficiently designed using Flexbox to ensure that menu items are evenly spaced and centered.

On the other hand, **Grid Layout** is a two-dimensional layout system that enables developers to create complex layouts by dividing a page into rows and columns. With Grid, items can be positioned anywhere in the grid, making it ideal for intricate designs that require precise control over both dimensions. Developers can use properties like `grid-template-rows`, `grid-template-columns`, and `grid-area` to define the structure of the grid. For instance, a magazine layout with images, text, and advertisements can be effectively managed using Grid.

In conclusion, while Flexbox is ideal for one-dimensional layouts and simpler designs, Grid Layout excels in creating more complex, two-dimensional layouts. Both systems are essential tools for web developers, offering unique capabilities to create responsive and visually appealing designs.
  
 
 ## Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

Firstly, to have functions to delete and edit products, I need to create two functions in the views.py which are delete_product and edit_product. After that I need to mapped this two functions so It could be used in the templates, to do this I just need to add this two line code
```py
path('edit_product/<uuid:id>', edit_product, name='edit_product'),
path('delete_product/<uuid:id>', delete_product, name='delete_product')
```
After that is done I add this block of code, so I could use CSS and the other framework

``` py
<script src="https://cdn.tailwindcss.com"></script>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">
    <script src="https://code.jquery.com/jquery-3.6.0.min.js" integrity="sha384-KyZXEAg3QhqLMpG8r+J4jsl5c9zdLKaUk5Ae5f5b1bw6AUn5f5v8FZJoMxm6f5cH1" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/@popperjs/core@2.11.8/dist/umd/popper.min.js" integrity="sha384-I7E8VVD/ismYTF4hNIPjVp/Zjvgyol6VFvRkX/vR+Vc4jQkC+hVqc2pM8ODewa9r" crossorigin="anonymous"></script>
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/js/bootstrap.min.js" integrity="sha384-BBtl+eGJRgqQAUMxJ7pMwbEyER4l1g+O15P+16Ep7Q9Q+zqX6gSbd85u4mG4QzX+" crossorigin="anonymous"></script>
    <link rel="stylesheet" href="{% static 'css/global.css' %}"/>

```
After doing that I also create a static\css folder that consist the global.css, this file is used as the baseline of my css design. Since i'm done with the setup, I now modify my login,register, and add product pages to have the neon style look. I also customize the product list so if there is no products it will say no products in the virtual shop, however if there are products it will show the products that is already been added. In each card product I have two button that could edit and delete, this two functions uses the function from earlier. Lastly creating a navbar with a home features so user could easily go back to the main page.



# Assignment 6

## Explain the benefits of using JavaScript in developing web applications!

JavaScript has become a cornerstone in web development due to its extensive capabilities, versatility, and ease of use in developing interactive web applications. By leveraging JavaScript, developers can build dynamic and responsive front-end experiences, making user interactions immediate and intuitive. This language enables the creation of Single Page Applications (SPAs), where users interact with the web page in real time without requiring full-page reloads. JavaScript is essential for handling both basic interactions, such as button clicks and form submissions, and complex, event-driven behaviors like AJAX (Asynchronous JavaScript and XML) requests. These features enable a seamless user experience, helping modern web applications deliver fast, smooth, and efficient interactions while connecting with the server asynchronously to load or save data on the fly.

## Explain why we need to use await when we call fetch()! What would happen if we don't use await?

Using `await` with `fetch()` is crucial for maintaining smooth and predictable workflows when fetching data from servers. The `await` keyword allows JavaScript to "pause" execution of code until the server response arrives, rather than moving on to subsequent lines immediately. If `await` is not used with `fetch()`, JavaScript will proceed to execute the code after `fetch()` before the server responds. This can result in unexpected behaviors, such as trying to manipulate or display data before it has been fully received, potentially causing errors or displaying incorrect or incomplete information to users. By using `await`, developers ensure that subsequent code runs only after the requested data has arrived, creating a more reliable and consistent user experience.

## Why do we need to use the csrf_exempt decorator on the view used for AJAX POST?

In Django, the `csrf_exempt` decorator is necessary for views used for AJAX POST requests because Django, by default, requires a Cross-Site Request Forgery (CSRF) token for any POST request to prevent malicious attacks. AJAX requests often don't include CSRF tokens directly, especially if they originate from JavaScript code rather than from Django forms. By adding `csrf_exempt`, we bypass this CSRF validation step, allowing the AJAX POST request to succeed without requiring a CSRF token. However, this must be done cautiously, as it makes the endpoint more vulnerable to attacks. In practice, for enhanced security, developers usually include CSRF tokens in AJAX requests manually or use a method that embeds CSRF protection into the request.

## On this week's tutorial, the user input sanitization is done in the back-end as well. Why can't the sanitization be done just in the front-end?

While front-end sanitization is valuable for providing immediate feedback to users, it is not sufficient for secure web applications. Data should always be sanitized on the server side because relying solely on front-end validation leaves the application vulnerable to security risks. Users can manipulate JavaScript or send malicious inputs directly to the server by bypassing the front end altogether, which exposes sensitive data and the back-end infrastructure to potential security threats. Server-side sanitization acts as the final line of defense against invalid or malicious data inputs, ensuring that only properly validated data interacts with the system.

## Explain how you implemented the checklist above step-by-step (not just following the tutorial)!

First I create the new functions in the views.py to add product through ajax, I also imported `csrf_exempt` and `require_POST`. After that I mapped this function so through urls.py so it could be used in the main.html. I also have to remove this line in my show_main

``` py
product_entries = Product.objects.filter(user=request.user)
'product_entries': product_entries,
``` 
After that I also remove this line below in my show_json and show_xml

``` py
data = Product.objects.filter(user=request.user)
```
Since I remove the product_entries I also have to remove the code that is in my main.html. Now after all of this was done I create my product_entry_cards, and create a script to get my productEntries. After that I create a script to refreshProductEntries() In this function I also sanitize my data. After All of that I create Modal as a form so I could add new product. After I finished setup my Modal I Protect my application from cross site scripting, this is by using strip_tags where I add to views.py functions add_product_entry_ajax(request)

``` py
name = strip_tags(request.POST.get("name"))
price = strip_tags(request.POST.get("price"))
description = strip_tags(request.POST.get("description"))
status = strip_tags(request.POST.get("status"))
user = request.user
```
After that I also modify my form.py so it also use strip_tags

``` py
def clean_name(self):
        name = self.cleaned_data['name']
        return strip_tags(name)

    def clean_description(self):
        description = self.cleaned_data['description']
        return strip_tags(description)

    def clean_price(self):
        price = self.cleaned_data['price']
        if price <= 0:
            raise forms.ValidationError("Price must be greater than zero.")
        return price

    def clean_status(self):
        status = self.cleaned_data['status']
        valid_status_choices = [choice[0] for choice in Product.STATUS_CHOICES]
        if status not in valid_status_choices:
            raise forms.ValidationError("Invalid status selected.")
        return status
```

