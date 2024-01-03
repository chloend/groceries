# groceries
This Django app allows you to create a weekly mealplan and automatically generates a grocery list.

## Prerequisites
- Python >= 3.11.1
- Pip >= 23.3.2
- Npm >= 10.2.5
- Node JS >= 21.2.0

## Installation
Clone the repository :  
```
git clone https://github.com/chloend/groceries.git
``` 

Navigate to the root project directory :  
```
cd groceries
```

Set up a virtual environment :  
```
python -m venv venv
```

Activate it :  
On Windows :  
```
.\venv\Scripts\activate
```

On Linus/MacOS :  
```
source venv/bin/activate
```

Install Python dependencies :  
```
pip install -r requirements.txt
```

## Configuration
Navigate to the groceries project directory (inside root directory) :  
```
cd groceries
```  

Create a local.py file and declare those variables :  
```
SECRET_KEY = [generate here => (https://djecrety.ir/)]
DEBUG = True (False in production)
ALLOWED_HOSTS = ["127.0.0.1", "localhost", "0.0.0.0"]
```

Apply migrations :  
```
python manage.py migrate
```

Load data from mealplan.json :  
```
python manage.py loaddata mealplan.json
```

Build css styles from Tailwind CSS :  
```
python manage.py tailwind install
python manage.py tailwind start
```

## Running
Start the Django development server :  
```
python manage.py runserver
```  
