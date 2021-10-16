pytest -v -s -m "sanity" --html=Reports\reports.html Testcases/ --browser chrome

rem pytest -v -s -m "sanity" --html=Reports\reports.html Testcases/ --browser firefox

rem pytest -v -s -m "sanity and regression" --html=Reports\reports.html Testcases/ --browser chrome

rem pytest -v -s -m "sanity or regression" --html=Reports\reports.html Testcases/ --browser chrome

rem pytest -v -s -m "regression" --html=Reports\reports.html Testcases/ --browser chrome

rem pytest -v -s -m "sanity" --html=Reports\reports.html Testcases/ --browser firefox

rem pytest -v -s -m "sanity and regression" --html=Reports\reports.html Testcases/ --browser firefox

rem pytest -v -s -m "sanity or regression" --html=Reports\reports.html Testcases/ --browser firefox

rem pytest -v -s -m "regression" --html=Reports\reports.html Testcases/ --browser firefox