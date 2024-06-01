alias BUILD_USPORTS='python setup.py sdist bdist_wheel'
alias CLEAN='rm -rf build dist usportspy.egg-info'
alias INSTALL='pip install dist/usportspy*.whl --force-reinstall'
alias UPLOAD='twine upload dist/*'
