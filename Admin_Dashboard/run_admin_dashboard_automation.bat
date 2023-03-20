REM pytest -s -v .\tests\user_management\user_tests.py --browser chrome --html=.\Admin_DashBoard.html
REM pytest -s -v .\tests\run_test_suite_1.py --browser chrome --html=.\Admin_Dashboard.html
pytest -s -v .\tests\run_test_suite_1.py --browser chrome --html=.\reports\Admin_Dashboard.html
REM pytest -s -v .\tests\run_test_suite_1.py --browser firefox --html=.\reports\Admin_Dashboard.html