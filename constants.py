TIME_TO_WAIT = 30


USERNAME = "Cerpany"
EMAIL = "somemail@gmail.com"
PASSWORD = "qwerty12345"
WRONGPASSWORD = "qwerty"

LOGIN_URL = "https://account.games2gether.com/login"
LOGIN_INPUT_ID = '[id="UsernameOrEmail"]'
LOGIN_BUTTON = '[type="submit"]'
RESPONSE_FIELD = '[class="field-message-error"]'
USER_NAME_ID = '[class="user-username"]'
PASSWORD_ID = '[id="Password"]'
WELLCOME_CLASS = '[class="dashboard-account-username"]'

EXPECTED_NOT_ENTERED_LOGIN_RESULT = "Please enter your Username or Email."
EXPECTED_ERROR_LOGIN_RESULT = "Your username or email is unknown."
EXPECTED_INCORRECT_PASSWORD = "Your username or password is incorrect."
WELLCOME_TEXT = "Welcome" + '\n'
EXPECTED_TEXT = WELLCOME_TEXT + USERNAME
