# assignment_ch

clone repository
Goto to folder
Install all required libraries:
    pip install -r requirement.text
    
Open command prompt:
Firstly make migrsation:
  python manage.py makemigrations
 
Then migrate
  python manage.py migrate
  
Start server
  python manage.py runserver
  
Open loclhost link:
You can get data from randomuser.me with button 'Get data' and save it to sqlite database
You can fetch saved data from database in paginated manner with button 'Fetch data'
you can filter/search/ordering to fetch data from database
    for search use 'search=female/35/19' for filter use 'gender=female/male or age=21' for ordering use 'ordering=gender/age/name'
