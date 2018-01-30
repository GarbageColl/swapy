echo Cleaning dist directory...
del -R dist
echo Building packages...
python setup.py sdist
python setup.py wheel
echo Uploading to PyPi...
twine upload dist/*
echo Finished.