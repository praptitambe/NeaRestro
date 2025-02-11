# Testing

- Manual testing was carried out throughout the development of the website and bugs fixed as they arose. 

## Manual testing
- Manual testing was carried out on the local and deployed sites.



## Code validators

### HTML Validator
- The [W3C Validator](https://validator.w3.org/) was used to validate the HTML.

#### Home
![Home page validator screenshot](static/images/readme/testing/html-validator-home.png)

#### Chef Page
![Chef page validator screenshot](static/images/readme/testing/html-validator-restro-details.png)

#### Join Us 
![join us validator screenshot](static/images/readme/testing/html-validator-joinus.png)

#### Register 
![Register validator screenshot](static/images/readme/testing/html-validator-register.png)

-When I checked the code that the validator was referring to, it was the code which was integrated by Django for the review functionality and not written by me. I looked for it everywhere in an attempt to fix it but could not find it.

#### Sign-In
![Sign-in validator screenshot](static/images/readme/testing/html-validator-login.png)

#### Sign-out
![Sign-out validator screenshot](static/images/readme/testing/html-validator-signout.png)

### CSS Validator
- The [W3C CSS Validator](https://jigsaw.w3.org/css-validator/) was used to validate the CSS.
![CSS validator screenshot](static/images/readme/testing/css.png)

### Python
- The [CI Python Linter](https://pep8ci.herokuapp.com/) was used to validate the Python files.

#### "Restro" project files
All files were edited according to the suggestions provided by the validator and are now showing no errors.

##### asgi.py
![admin.py](static/images/readme/testing/restro-asgi.png)

##### urls.py
![apps.py](static/images/readme/testing/restro-urls.png)

##### wsgi.py
![forms.py](static/images/readme/testing/restro-wsgi.png)

##### settings.py
![forms.py](static/images/readme/testing/restro-settings.png)



#### "About" app files
All files were edited according to the suggestions provided by the validator and are now showing no errors.

##### admin.py
![admin.py](static/images/readme/testing/python-validator-about-admin-forms.png) 

##### apps.py
![apps.py](static/images/readme/testing/python-validatorabout-apps.png)

##### forms.py
![forms.py](static/images/readme/testing/python-validatorabout-forms.png)

##### models.py
![models.py](static/images/readme/testing/python-validatorabout-models.png)

##### urls.py
![urls.py](static/images/readme/testing/python-validatorabout-urls.png)

##### views.py
![views.py](static/images/readme/testing/python-validatorabout-views.png)

#### "Review" app files
All files were edited according to the suggestions provided by the validator and are now showing no errors.

##### admin.py
![admin.py](static/images/readme/testing/recipe-admin.png)

##### apps.py
![apps.py](static/images/readme/testing/recipe-apps.png)

##### forms.py
![forms.py](static/images/readme/testing/recipe-forms.png)

##### models.py
![models.py](static/images/readme/testing/recipe-models.png)

##### urls.py
![urls.py](static/images/readme/testing/recipe-urls.png)

##### views.py
![views.py](static/images/readme/testing/recipe-views.png)

#### Settings.py
![settings.py](static/images/readme/testing/settings.png)
-Even though some lines were considered too long by PEP8 (highlighted), I decided that the readability of the code was better when left on the same line, since it was very close to the accepted limit. Even though error exists, the app still functions. 

#### Project urls
![project urls.py](static/images/readme/testing/project-urls.png)

## Lighthouse

- The home and detail pages scored low in the best practices. This seemed to be due to the Cloudinary files not producing HTTPS files. Efforts are being made to address this issue to improve the overall score but this is something to be considered as future improvement.

### Desktop Lighthouse

#### Home page
![home page](static/images/readme/testing/lighthouse-desktop-home.png)

#### Chef page
![chef page](static/images/readme/testing/lighthouse-desktop-chef.png)

#### Detail page
![detail page](static/images/readme/testing/lighthouse-desktop-detail.png)

#### Join us page
![join us page](static/images/readme/testing/lighthouse-desktop-joinus.png)

#### Register
![register page](static/images/readme/testing/lighthouse-desktop-register.png)

#### Sign-in page
![sign-in page](static/images/readme/testing/lighthouse-desktop-signin.png)

### Mobile Lighthouse

#### Home page
![home page](static/images/readme/testing/lighthouse-mobile-home.png)

#### Chef page
![chef page](static/images/readme/testing/lighthouse-mobile-chef.png)

#### Detail page
![detail page](static/images/readme/testing/lighthouse-mobile-detail.png)

#### Join us page
![join us page](static/images/readme/testing/lighthouse-mobile-joinus.png)