# instagram

[virsail mbagaya](https://github.com/virsail)  
  
# Description  
This is a clone of  Instagram that allows users to upload their  images ,follow other users like others users pictures and leave comments ,users also sign up and get to search for their followers.

##  Live Link  
 View App site [View Site](https://nofucks.herokuapp.com/)  
  
 
## User Story  
  
* Sign up and login to the application  
* Upload their pictures to the application
* Search for different users 
* See their profile with all their pictures they uploaded
* Follow other users and see their activities on my timeline.  



## Search Results
![Screenshot from 2020-10-29 18-19-45](https://user-images.githubusercontent.com/66640798/97595593-e2b34680-1a14-11eb-85d4-25a6e5f3f9a0.png)

## Home Feeds

![Screenshot from 2020-10-29 18-19-20](https://user-images.githubusercontent.com/66640798/97594828-1a6dbe80-1a14-11eb-86d1-5f4f2f0d04ad.png)

###  Profile

![Screenshot from 2020-10-29 18-17-28](https://user-images.githubusercontent.com/66640798/97594299-99162c00-1a13-11eb-85e1-3fb6a58197c4.png)


  
## Setup and Installation  
Clone the repository
##### Cloning the repository:  
 ``` git clone 
 https://github.com/Virsail/Instagram.git 
```
##### Navigate into the folder and install requirements  
 ```bash 
cd instagram then pip install -r requirements.txt 
```
##### Install and activate Virtual  
 ```bash 
- python3 -m venv virtual - source virtual/bin/activate  
```  

 ##### Setup Database  
  SetUp your database User,Password, Host then make migrate  
 ```bash 
python manage.py makemigrations insta
 ``` 
 Now Migrate  
 ```bash 
 python manage.py migrate 
```
##### Run the application  
 ```bash 
 python manage.py runserver 
``` 
##### Testing the application  
 ```bash 
 python manage.py test 
```
Open the application on your browser `127.0.0.1:8000`.  
  
  
## Technology used  
  
* [Python3.8](https://www.python.org/)  
* [Django 1.11.7](https://docs.djangoproject.com/en/2.2/)  
* [Heroku](https://heroku.com)  
  
  
## Contact Information   
ericmbagaya@gmail.com 
  

### License
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](https://opensource.org/licenses/MIT) 
* Copyright (c) 2020 **Virsail Mbagaya**
