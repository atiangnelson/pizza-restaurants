 # 1 Set FLASK_APP environment 
   ## export FLASK_APP=server/app.py 

 # 2 Run migration commands
   ## flask db init
   ## flask db migrate -m "Initial migration"
   ## flask db upgrade

 # 3 Seed the Database
   ## python server/seed.py

 # 4 Run the Application
   ## flask run
