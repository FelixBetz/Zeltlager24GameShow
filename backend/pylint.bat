@ECHO OFF
python -m coverage run -m unittest discover tests  && python -m coverage  report --omit=tests\*.py && python -m coverage html --omit=tests\*.py >NUL  
echo:
echo: 
echo --------------------pylint--------------------

python -m   pylint --recursive=y app.py src/ tests/ --ignore=*.pyc,*.docx,frontend_build/ 


python -m coverage report --omit=tests\*.py -m > tests/coverage_report.txt

set cov_score=
for /f "tokens=3" %%i in ('findstr /r /c:"^TOTAL.*100%%$"  %~dp0tests\coverage_report.txt') do (
    set cov_score=%%i
)


if  "%cov_score%" == "" (
    start firefox file:///%~dp0/htmlcov/index.html
)