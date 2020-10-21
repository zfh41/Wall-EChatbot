# Set up React  
0. `cd ~/environment && git clone https://github.com/NJIT-CS490/project2-m1-zfh4.git && cd project2-m1-zfh4`    
1. Install your stuff!    
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`
  g) `sudo pip install requests`
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` :warning: :warning: :warning:    
  
# Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo /usr/local/bin/pip install --upgrade pip`  
3. Get psycopg2: `sudo /usr/local/bin/pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`  

# Set up DB  
0. `sudo service postgresql start` and `cd ~/environment/lect12 && python`  
1. In the python interactive shell, run:  
	`import models`  
	`models.db.create_all()`  
	`models.db.session.commit()`  
  
# Setting up PSQL  
  
1. Install PostGreSQL: `sudo yum install postgresql postgresql-server postgresql-devel postgresql-contrib postgresql-docs`    
    Enter yes to all prompts.    
2. Initialize PSQL database: `sudo service postgresql initdb`    
3. Start PSQL: `sudo service postgresql start`    
4. Make a new superuser: `sudo -u postgres createuser --superuser $USER`    
    :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
5. Make a new database: `sudo -u postgres createdb $USER`    
        :warning: :warning: :warning: If you get an error saying "could not change directory", that's okay! It worked! :warning: :warning: :warning:    
6. Make sure your user shows up:    
    a) `psql`    
    b) `\du` look for ec2-user as a user    
    c) `\l` look for ec2-user as a database    
7. Make a new user:    
    a) `psql` (if you already quit out of psql)    
    ## REPLACE THE [VALUES] IN THIS COMMAND! Type this with a new (short) unique password.   
    b) I recommend 4-5 characters - it doesn't have to be very secure. Remember this password!  
        `create user [some_username_here] superuser password '[some_unique_new_password_here]';`    
    c) `\q` to quit out of sql    
8. `cd` into `lect11` and make a new file called `sql.env` and add `SQL_USER=` and `SQL_PASSWORD=` in it  
9. Fill in those values with the values you put in 7. b)  
  
  
# Enabling read/write from SQLAlchemy  
There's a special file that you need to enable your db admin password to work for:  
1. Open the file in vim: `sudo vim /var/lib/pgsql9/data/pg_hba.conf`
If that doesn't work: `sudo vim $(psql -c "show hba_file;" | grep pg_hba.conf)`  
2. Replace all values of `ident` with `md5` in Vim: `:%s/ident/md5/g`  
3. After changing those lines, run `sudo service postgresql restart`  
4. Ensure that `sql.env` has the username/password of the superuser you created!  
5. Run your code!    
  a) `npm run watch`. If prompted to install webpack-cli, type "yes"    
  b) In a new terminal, `python app.py`    
  c) Preview Running Application (might have to clear your cache by doing a hard refresh)    




## Use the command `sudo service postgresql restart` to restart your database

### If you want to clear your chat of all message history:
1. Type in command `psql`
2. Type in `\c postgres`
3. Type in `delete from <databasename> (in our case usps);`





# Technical Problems:
1. I came across a few problems when working on my code. I had a lot of problems that scaled from front-end to back-end. JSX is an environment that I am not too familiar with, so coding in it took a lot of Google searching. The biggest problems lay in the ambuigity and the specificness of certain features that I wanted to implement. For instance, when working on the front-end content JSX file, I encountered a lot of inconsistincies online as to how to format conditionals appropriately in returning rendered HTML in the script. I had to do a lot of trial and errors to finally figure out how to properly get a conditional line syntax to work. There were a few conditionals that I was having the most difficulty with and that was the ones where I was setting up conditionals for displaying bold font for my bot, or I was changing the profile image from my user to bot. The actual syntax I found to be confusing and took a lot of logical thinking on my part and online investigation. 
2. Another issue I came across was when deploying my app to Heroku, it would display an application error. In order to figure out why it was displaying, I had went to Professor Rengesh's office hours and discussed it with me. What I learned from his session, was that in the heroku app, there is a setting to check your logs. This is really convenient when you are trying to understand why the app is not being deployed properly. I realized that I did not have a particular module added in my requirements text and that was the primary reason why my heroku app wasn't being deployed.

# Unresolved Issues:
1. What I could've improved with this project would definitely be the user interface of both the google login page as well as the chat room. If I had more time I would've decorated the login to be a bit more visually appealing. For the chat room, I would've centered the chat box and made the button and input much bigger. 
2. Another issue I came across was that logged in users would've different users when independantly using the apps, but when together it would show the same person. This will be fixed with the next version of my application hopefully.

