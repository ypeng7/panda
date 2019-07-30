# File              : build.sh
# Author            : Yue Peng <yuepaang@gmail.com>
# Date              : 2019-07-30 09:22:21
# Last Modified Date: 2019-07-30 09:22:21
# Last Modified By  : Yue Peng <yuepaang@gmail.com>

# Build
python setup.py sdist bdist_wheel

# Upload
python -m twine upload --repository-url https://test.pypi.org/legacy/ dist/*

# Download
pip install --index-url https://test.pypi.org/simple/ --no-deps panda-ypeng7
