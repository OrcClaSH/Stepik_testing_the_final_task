# Stepik_testing_the_final_task

Небольшая инструкция по проверке:

1. Скачайте к себе проект, либо скачав и распаковав архив, либо склонировав репозитарий.
Просмотрите содержимое файла README.md, возможно, там будут какие-нибудь полезные комментарии для проверки.
Здесь можно, например, указать ОС и версию Python, с которой Вы работаете. 
2. Деактивируйте текущее виртуальное окружение, если вы в нем находитесь. 
Вспомнить, как работать с виртуальными окружениями можно на этом шаге (для Windows):
https://stepik.org/lesson/25969/step/2?unit=196192
3. Создайте новое виртуальное окружение.
4. Перейдите в папку вновь созданного окружения:
cd \path\to\new_virtual_env\Scripts
5. Активируйте данное виртуальное окружение.
6. Установите пакеты в окружение из файла requirements.txt, который должен быть в скачанном проекте:
pip install -r \path\to\requirements.txt
7. Убедитесь, что путь к chromedriver.exe прописан в PATH, либо скопируйте этот файл в текущую папку Scripts из шага 4.
8. Запустите тесты командой:
pytest -v --tb=line --language=en -m need_review \path\to\test_product_page.py
9. Проверьте, что все тесты прошли успешно.
10. Если же тесты не запускаются, не спешите ставить 0 баллов и с чувством выполненного долга переходить к следующей рецензии.
Попробуйте сначала разобраться, в чем заключается ошибка. Возможно, дело в путях к файлам в импорте -- тогда попробуйте поставить / убрать точку в начале и / или добавить / удалить пустой файл __init__.py в корневой папке и / или подпапках.
Или может проблема в том, что автор перед коммитом случайно добавил какой-нибудь лишний символ файл и не проверил перед отправкой.
Или возможны еще другие варианты.
----------------------------------------------------------------------------
A small verification instruction:

1. Download the project to yourself, either by downloading and unpacking the archive, or by cloning the repository.
Look at the contents of the README.md file, maybe there will be some useful comments to check.
Here you can, for example, specify the OS and version of Python with which you are working.
2. Deactivate the current virtual environment if you are in it.
You can recall how to work with virtual environments at this step (for Windows):
https://stepik.org/lesson/25969/step/2?unit=196192
3. Create a new virtual environment.
4. Go to the folder of the newly created environment:
cd \ path \ to \ new_virtual_env \ Scripts
5. Activate this virtual environment.
6. Install packages into the environment from the requirements.txt file, which should be in the downloaded project:
pip install -r \ path \ to \ requirements.txt
7. Make sure that the path to chromedriver.exe is specified in PATH, or copy this file to the current Scripts folder from step 4.
8. Run the tests with the command:
pytest -v --tb = line --language = en -m need_review \ path \ to \ test_product_page.py
9. Verify that all tests are successful.
10. If the tests do not start, do not rush to put 0 points and move on to the next review with a sense of accomplishment.
Try to figure out what the error is first. Perhaps the matter is in the paths to the files in the import - then try to put / remove the dot at the beginning and / or add / delete the empty __init__.py file in the root folder and / or subfolders.
Or maybe the problem is that the author accidentally added some extra character to the file before committing and did not check it before sending it.
Or other options are possible.

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
