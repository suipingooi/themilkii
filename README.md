## themlkiiway

The goal of this project is lauch and deploy an e-commerce site for @themlkiiway.

The targetted main users of this site are:
1. 
2. Clients and general public / new clients:
    - learn more about TGR and its offering.
    - on-line payment for products esp. for repeat customers.

<hr>

![@themlkiiway]() <br>

### UX - User Experience

Wireframe of the build design includes:

![Wireframe]()

<hr>

![Color Chart]()<br>


<img src="#" alt="black" width="20px"> Black: symbolizes elegance and sophistication. <br>


![Font Glyphs]()<br>
1. font-family: 'Chicle', cursive;
2. font-family: 'Lato', sans-serif;
3. font-family: 'Montserrat', sans-serif;
4. font-family: 'Open Sans', sans-serif;

<hr>

## Built With 
### Technologies
1. HTML 5.0 + CSS
2. Bootstrap 5.0 - CSS & JS [https://getbootstrap.com/](https://getbootstrap.com/)
3. Python + Django
4. JQuery 
5. Toastr [https://codeseven.github.io/toastr/](https://codeseven.github.io/toastr/)
6. Uploadcare [https://uploadcare.com/](https://uploadcare.com/)
7. Heroku [https://www.heroku.com/](https://www.heroku.com/) as deployment host.


### Styling
1. Google Fonts [https://fonts.google.com/](https://fonts.google.com/) for font-family pairings.
2. Fontawesome [https://fontawesome.com/](https://fontawesome.com/) for icons.
3. Gimp 2.10 [https://www.gimp.org/](https://www.gimp.org/) for image manipulation.
4. Adobe Color [https://color.adobe.com/](https://color.adobe.com/) to extract TGR base color chart.


### Testing
[W3C Validator](https://validator.w3.org/) for html validation. All errors dealt with save for Jinja templating errors/ warnings. Specifically uploadcare input.

[Jigsaw CSS Validator](https://jigsaw.w3.org/css-validator/) for css validation. no errors found.

<hr>

| Action (development testing)             | Results                       | Status      |
| -----------------------------------------|:-----------------------------:|-------------|
| Submission of empty forms                | Unable to submit as expected  | COMPLETED   |
| Submission of invalid data in forms      | Alert and error trigger fixed | COMPLETED   |
| Loading in Chrome                        | Margin issues noted, fixed    | COMPLETED   |                         
| Loading in Firefox                       | Time widget not supported     |    nil      |
| Trolley add & stripe checkout            | Webhook issues fixed          | COMPLETED   |         
| Rezising of viewport widths              | Flexbox issues fixed          | COMPLETED   |
| Checkout / Client request autogen emails | message string issue fixed    | COMPLETED   |

| <h3>**User Features Tests during development**                                                                                                                                                                                                                                                                                                                                                                                                                                                                                               |
| :------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Test 1: Hyperlinks of navigation tabs / hamburger dropdowns with multiple screen size.**                                                                                                                                                                                                          |
| **Expected:** 1. Navbar brings me to different specified pages. 2. Navbar turns to hamburger dropdown when screensize drops. <br> **Test:** Clicking on all different links to reload multiple times. <br/>**Result:** Multiple issues with some images noted; margins and flex issues noted; navigation controls works as expected.<br/>                                                                                                                                                           |
| **Test 2: Admin console navigation and functions**                                                                                                                                                                                                          |
| **Expected:** 1. on button click brings me to desired pages for CRUD actions where available <br/>**Test:** Clicking on all different buttons to reload table or forms multiple times. <br/>**Result:** page loads and reloads as expected<br/>                                                                                                                                                           |
| **Test 3: Admin CRUD**
| **Expected:** create reflected immediately in read; update forms display values to be edited; delete warning prior to action. form validation and error triggers for invalid data  <br/>**Test:** added new pricing to price list, added new space product to space listing; attempted invalid data submission, edited the info in each entry; deleted the entry<br/>**Result:** multiple issues with display size and margins esp. for smaller viewport width<br/>
| **Test 4: Authentication**                                                                                                                                                                                                          |
| **Expected:** all links and follow-on on screen instructions loads and responds to user. <br> **Test:** Clicking on all different links to sign-up, sign-in, forget password, change password multiple times following on screen instructions  <br>**Results:** all responds as expected except for sign-in link on password changed page that does not respond. Fixed path.                                                                                                                                                             |
| **Test 5: Trolley and Checkout**                                                                                                                                                                                                          |
| **Expected:** items to be able to add, price automatically adjusted; successful stripe payment triggers 1. transacted data storage 2. email notification to admin and client confirmation email. <br> **Test:** add item to trolley, proceed with stripe payment testing  <br>**Results:** multiple failed attempts. found error in port set to private. Fixed.                                                                                                                                            |
| **Test 6: Emails**                                                                                                                                                                                                          |
| **Expected:** receive email with confirmation of payment made <br> **Test:** add items to trolley, stripe checkout  <br>**Results:** email received as expected when stripe is successful and port setting is correct.                                                                                                                                            |
<hr>

**User Features Testing (HEROKU Deployment)** <br>
[Heroku Deployment User Tests detailed documentation]()

<hr>

## Features
### Existing Features
1. 
2. 
3. 


### Features left to Implement
1. 
2. 
3. 


## Deployment
Steps taken to deploy on HEROKU: <br>

## Acknowledgements

### References
1. 

### Credits

### Special Thanks
1. 
2. 
3. 
