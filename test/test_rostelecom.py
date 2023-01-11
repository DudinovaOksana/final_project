from page.registration_form_page import RegistrationFormPage
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from page.rostelecom_authorization_page import RostelecomAuthorizationPage
from page.email_confirmation_page import SubmitEmail
from page.redirect_uri_page import RedirectURI
from test import functions
from page.policy_privacy_page import PolicyPrivacy
from page.VK_page import VK
from page.mail_ru_page import MailRu
from page.gmail_com_page import GmailCom
from page.odnoklassniki_page import Odnoklassniki
from page.yandex_ru_page import YandexRu
from fixtures.fixtures import open_rostelecom_page


# ТК-01
def test_registration_with_valid_password_16_characters(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Як")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Смолин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Петербург")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# ТК-02
def test_authorization_using_mail(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    # шаг 2
    email_input = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email_input.send_keys('ivan-ivanov-2023ivanov@yandex.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('Qwertyuiop_1287')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url


# ТК-03
def test_authorization_using_personal_account_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    personal_account_tab = functions.find(driver, RostelecomAuthorizationPage.PERSONAL_ACCOUNT_TAB)

    # шаг 2
    personal_account = functions.find(driver, RostelecomAuthorizationPage.PERSONAL_ACCOUNT)
    personal_account.send_keys("123456789012")

    # шаг 3
    password = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password.send_keys('Qwertyuiop_1287')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    check_error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert check_error_message.text == "Неверный логин или пароль"


# ТК-04
def test_redirect_policy_privacy(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    policy_privacy_link = functions.find(driver, RostelecomAuthorizationPage.POLICY_PRIVACY)
    policy_privacy_link.click()
    current_url = driver.switch_to.window(driver.window_handles[1])
    check_redirect_to_policy_privacy = functions.find(driver, PolicyPrivacy.POLICY_PRIVACY)
    assert driver.current_url == "https://b2c.passport.rt.ru/sso-static/agreement/agreement.html"


# ТК-05
def test_user_registration_with_name_3_characters_password_14_characters(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Ким")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Смолин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Петербург")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(14)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# ТК-06
def test_registration_with_password_4_characters(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Андрей")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Сусанин')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Санкт-Петербург")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(4)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)
    check_error_message = functions.find(driver, RegistrationFormPage.INVALID_ACCAUNT_NUMBER_ERROR_MESSAGE)
    assert check_error_message.text == "Длина пароля должна быть не менее 8 символов"


# ТК-07
def test_user_registration_with_password_8_characters(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Алексей")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Петербург")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    assert check_phone_text.text == "Подтверждение email"


# ТК-08
def test_user_authorization_using_invalid_telephone_number_negative(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    telephone_tab = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER_TAB)
    telephone_tab.click()

    # шаг 2
    telephone_number = functions.find(driver, RostelecomAuthorizationPage.TELEPHONE_NUMBER)
    telephone_number.send_keys('+79533695289')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('Qwertyuiop0987')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# ТК-09
def test_user_registration_with_name_1_character_negative(open_rostelecom_page):
    driver = open_rostelecom_page
    # шаг 1
    register_link = functions.find(driver, RostelecomAuthorizationPage.REGISTRATION_LINK)
    register_link.click()

    # шаг 2
    name = functions.find(driver, RegistrationFormPage.NAME)
    name.send_keys("Я")

    # шаг 3
    surname = functions.find(driver, RegistrationFormPage.SURNAME)
    surname.send_keys('Андреев')

    # шаг 4
    region = functions.find(driver, RegistrationFormPage.REGION_INPUT)
    region.send_keys("Петербург")
    region_select = functions.find(driver, RegistrationFormPage.REGION_SELECT)
    region_select.click()

    # шаг 5
    email = functions.get_random_string(8) + '@gmail.com'
    email_input = functions.find(driver, RegistrationFormPage.EMAIL_MOB_PHONE)
    email_input.send_keys(email)

    # шаг 6
    password = functions.find(driver, RegistrationFormPage.PASSWORD)
    password_generation = functions.get_random_string(8)
    password.send_keys(password_generation)

    # шаг 7
    password_confirm = functions.find(driver, RegistrationFormPage.PASSWORD_CONFIRM)
    password_confirm.send_keys(password_generation)

    # шаг 8
    register_button = functions.find(driver, RegistrationFormPage.REGISTER_BUTTON).click()
    check_phone_text = functions.find(driver, SubmitEmail.EMAIL_CONFIRMATION)
    check_error_message = functions.find(driver, RegistrationFormPage.NAME_ERROR_MESSAGE)
    assert check_error_message.text == "Необходимо заполнить поле кириллицей. От 2 до 30 символов."


# ТК-10
def test_user_authorization_with_valid_email_and_invalid_password_negative(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    email_tab = functions.find(driver, RostelecomAuthorizationPage.EMAIL_TAB)
    email_tab.click()

    # шаг 2
    email = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email.send_keys('ivan-ivanov-2023ivanov@yandex.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('Wfhvn86dh')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    error_message = functions.find(driver, RostelecomAuthorizationPage.ERROR_MESSAGE)
    assert error_message.text == "Неверный логин или пароль"


# ТК-11
def test_VK_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    vk_icon = functions.find(driver, RostelecomAuthorizationPage.VK_ICON)
    vk_icon.click()
    check_redirect_vk_page = functions.find(driver, VK.VK)
    assert check_redirect_vk_page.text == 'Для продолжения вам необходимо войти ВКонтакте.'


# ТК-12
def test_odnoklassniki_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    odnoklassniki_icon = functions.find(driver, RostelecomAuthorizationPage.ODNOKLASSNIKI_ICON)
    odnoklassniki_icon.click()
    check_redirect_odnoklassniki_page = functions.find(driver, Odnoklassniki.odnoklassniki)
    assert check_redirect_odnoklassniki_page.text == 'Одноклассники'


# ТК-13
def test_mail_ru_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    mail_ru_icon = functions.find(driver, RostelecomAuthorizationPage.MAIL_RU_ICON)
    mail_ru_icon.click()
    check_redirect_mail_ru_page = functions.find(driver, MailRu.MAIL_RU)
    assert check_redirect_mail_ru_page.text == 'Мой Мир@Mail.Ru'


# ТК-14
def test_gmail_com_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    gmail_ru_icon = functions.find(driver, RostelecomAuthorizationPage.GMAIL_COM_ICON)
    gmail_ru_icon.click()
    check_redirect_gmail_com_page = functions.find(driver, GmailCom.GMAIL_COM)
    assert check_redirect_gmail_com_page.text == "Войдите в аккаунт Google"


# ТК-15
def test_yandex_ru_redirect(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    yandex_ru_icon = functions.find(driver, RostelecomAuthorizationPage.YANDEX_RU_ICON)
    yandex_ru_icon.click()
    check_redirect_yandex_ru_page = functions.find(driver, YandexRu.YANDEX_RU)
    assert check_redirect_yandex_ru_page.text == "Войдите с Яндекс ID"


# ТК-16
def test_authorization_using_login(open_rostelecom_page):
    driver = open_rostelecom_page

    # шаг 1
    login_tab = functions.find(driver, RostelecomAuthorizationPage.LOGIN_TAB)
    login_tab.click()

    # шаг 2
    email_input = functions.find(driver, RostelecomAuthorizationPage.EMAIL)
    email_input.send_keys('ivan-ivanov-2023ivanov@yandex.ru')

    # шаг 3
    password_input = functions.find(driver, RostelecomAuthorizationPage.PASSWORD)
    password_input.send_keys('Qwertyuiop_1287')

    # шаг 4
    enter_button = functions.find(driver, RostelecomAuthorizationPage.ENTER_BUTTON)
    enter_button.click()
    assert "https://b2c.passport.rt.ru/account_b2c/page?state=" in driver.current_url
