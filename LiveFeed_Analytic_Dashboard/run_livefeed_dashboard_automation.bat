REM python -m pytest -s -v .\tests\run_test_suite_1.py --browser firefox --html=.\Livefeed_Dashboard.html
REM  python -m pytest -v  .\tests\home\login_tests.py  .\tests\tabs\livefeed_tests.py .\tests\tabs\analytics\playback_tests.py --browser=chrome --html-report=./report/report_new_1.html --title='Livefeed_1'

REM python -m pytest -v .\tests\run_test_suite_1.py --browser chrome --html-report=./report/report_new_1.html --title='\Livefeed_Dashboard.html'

python -m pytest -v -s .\tests\run_test_suite_1.py --browser chrome --html=.\reports\Livefeed_Dashboard_Report.html
