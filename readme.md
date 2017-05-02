## Local development set up
```
virtualenv env
env\Scripts\activate
git clone https://github.com/yezz007/tilawahyuk
cd tilawahyuk
pip install -r requirements.txt
```
You should change the following lines in [settings](https://github.com/yezz007/tilawahyuk/blob/master/tilawahyuk/settings/__init__.py) :
```
from .prod import *
```
to
```
from .dev import *
```
for local development.
Also set up the local database - see [dev.py](https://github.com/yezz007/tilawahyuk/blob/master/tilawahyuk/settings/dev.py)

## Running local development server
```
python manage.py runserver
```


## Info
Your support is very welcome!

## License
This project is licensed under the MIT License - see the [license.txt](https://github.com/yezz007/tilawahyuk/blob/master/license.txt) file for details