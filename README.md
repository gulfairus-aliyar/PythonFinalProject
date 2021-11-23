# PythonFinalProject
## Aliyar Gulfairus, Abuova Izel, SE-2010
### Installation
#### Clone the repository to your local machine:
``git clone your-git-repo``  
#### Install Python 3, if you don't have it installed:
* https://www.python.org/downloads/
#### Create and activate a virtual environment:
> You can take this step using your preferred method.
* `python3 -m venv env`
* `source env/bin/activate`
#### Install necessary packages:
* `pip install -r requirements.txt`
### Usage
1. #### Run the application
    `cd src/`  
    `python app.py`
2. #### Go to browser and type `localhost:5000`
3. #### Available endpoints:
    `localhost:5000/login`  
    `localhost:5000/protected?token=`  
    `localhost:5000/coin`   
Note:
   > If the user has entered a coin name that is not in the database, we turn https://coinmarketcap.com/currencies/ for data. Otherwise, we take the paragraphs from the database.
### Examples

#### Already existing users in the db:
- `login: dummy`
  `password: dummy`
- `login: qwerty`
  `password: qwerty`
- `login: foo`
  `password: bar`

#### Already existing coins in the db:
- bitcoin  
- ethereum  
- binance-coin  
