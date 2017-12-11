# Hasura-Product-development-Fellowship
follow this instruction to run this code on your local machine

1. Install python 3.6.3 on your machine from https://www.python.org/downloads/

2. Then go to the root folder of python in your mahine. for me it is C:/Users/User/AppData/Local/programs/Python/Python36/scripts
(In windows system,Folder AppData remains hidden hence enable show hidden file)

3.Go to Control Panel>System>Advanced system settings>Advanced. Click on Environment variables>Path(system variables)>Edit> add " C:/Users/User/AppData/Local/programs/Python/Python36/scripts" >Ok>Ok>Ok

4.Go to command prompt Now first we will install Virtual Environment. Type ->pip install virtualenv

5.The Environment is ready Now. We will go to any disk in which we want to create our project. For ex. C:\>mkdir myproject ---->> C:\cd myproject. Then type C:\myproject>virtualenv flask now Installing setuptools,pip,wheel is done.

6.Go to  C:\myproject\flask\scripts and type pip install flask. Now our flask package is installed.

7.Go to C:\myproject\flask\scripts and type activate. Flask is activated.

8.Go to the folder where you have saved your python file. for ex. C:\Myproject\app. Type python app.py and your local server is activated now.

9. Go to your Favourite Browser and type the link as shown in command prompt.(Not Necessarily localhost:5000 always)
   
      Now Go to the respective URL to get the result of respective task.
      
      #Task1
       http://localhost:5000/
       
      #Task2
       http://localhost:5000/authors
       
      #Task3
      1.http://localhost:5000/form
      2.http://localhost:5000/setcookie
      
      #Task4
      http://localhost:5000/getcookie
      
      #Task5
      http://localhost:5000/robots.txt
      
      #Task6
      1.http://localhost:5000/html
      2.http://localhost:5000/image
      
      #Task7
      1.http://localhost:5000/input
      2.http://localhost:5000/result
      
