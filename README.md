# CI_WebAPP_Hahn

This project creates a trivial web application which is designed to be deployed with a CircleCI pipeline. 

The website is single page with a button prompting the user to click the button to ge their 'verb of the day'.
Clicking the button will route the user to a page which replaces the prompt with a random verb.

The `app_test.py` file is made so that the CI pipeline can use it to run a unittest to check the button is working as expected before
deploying the application to Heroku.
