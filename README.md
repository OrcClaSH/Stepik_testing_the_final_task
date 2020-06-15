# Stepik_testing_the_final_task
Repository for completing the last part of the course at https://stepik.org
----------------------------------------------------------------------------
base_page.py - we store methods that are applied throughout the project, everything is wrapped in a class.

locators.py - store locators in the form of constants. The locators of each individual page are wrapped in a class.

main_page.py - store methods on a specific page, wrapped in a class for this page. This class is a conditional MainPage - an inheritor of the BasePage class, so that you can use the methods described in base_page.py

test_main_page.py - run the tests themselves
Here we will create functions that:
    - give the link you need to check

    - we create the page variable in the function, to which we pass the browser from base_page.py (the BasePage class) and the link from step No. 1

    - next we say "page, open", but using the method from base_page.py (class BasePage)

    - add checks created by methods in main_page.py
