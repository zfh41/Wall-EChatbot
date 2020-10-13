# Set up React  
0. `cd ~/environment && git clone https://github.com/NJIT-CS490/project2-m1-zfh4.git && cd project2-m1-zfh4`    
1. Install your stuff!    
  a) `npm install`    
  b) `pip install flask-socketio`    
  c) `pip install eventlet`    
  d) `npm install -g webpack`    
  e) `npm install --save-dev webpack`    
  f) `npm install socket.io-client --save`
:warning: :warning: :warning: If you see any error messages, make sure you use `sudo pip` or `sudo npm`. If it says "pip cannot be found", run `which pip` and use `sudo [path to pip from which pip] install` :warning: :warning: :warning:    
  
# Getting PSQL to work with Python  
  
1. Update yum: `sudo yum update`, and enter yes to all prompts    
2. Upgrade pip: `sudo /usr/local/bin/pip install --upgrade pip`  
3. Get psycopg2: `sudo /usr/local/bin/pip install psycopg2-binary`    
4. Get SQLAlchemy: `sudo /usr/local/bin/pip install Flask-SQLAlchemy==2.1`    
  
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
1. The first known problem that I had was having trouble configuring conditional design in React.
I was trying to implement a certain style when the bot replies to the message that the dialogue would appear bold. I was looking through a lot of internet sites to find how to implement the conditional. All in all, it took more time than I warranted because a lot of commands hadn't worked. Eventually, the most succinct and basic command ended up being the solution to the problem. I scoured through stack overflow to find a solution that seemed to fit the previous formatting that I found for styling in JSX and I came across a few posts. I tried the first few and it resulted
in a blank rendered page. I tried the next few and it resulted with no change in the styling. I then looked at one that seemed to be very correct in its syntax and logically simplistic: https://stackoverflow.com/questions/35762351/correct-way-to-handle-conditional-styling-in-react. Styling is easier to be done in the header rather than having to abstrusely put it in a seperate CSS file or code in the main JSX syntax. It was good to note that JSX in-line styling syntax when rendering is different than HTML's.
2. Another issue that I encountered was trying to implement the client-server connection. I felt this wasn't thoroughly explained in the lecture and had to use a lot of independant research. If I had more time I could've cleaned the code a bit and figured out how to implement this more properly. I wasn't able to test the connection more effectively and check if the user count was updating or not.
3. Another issue that I had was displaying the user onto the correct page. This took a lot of logic and playing around with code on my part. I started off by taking the dbuser variable and trying to pass it into the JSX form and printing it from there. I then realized this was silly logic, because the same user would display for every dialogue.
Since I needed the bot to respond and its user to display when provoked, I needed to figure another way to display the user in the list mode. I found JSX render to be intuitively more difficult to format than HTML and found myself wasting time trying to display the user variable next to address variable in a different list. By then,
I decided to use a different logic and decided to pass in the conditionals for dbuser in my python file itself. I changed dbuser whenever the message that was being sent started with '!!' to bot. For simiplicity sake, I decided to concantenate the user string with the message string to make things easier. I am not sure if that is a good coding habit, but it worked perfectly for this project. This made things more easier to render on the JSX rather than creating a whole bunch of list structures and passing it in to JSX.


# Unresolved Issues:

As mentioned before, I was having issues understanding how to change the number of members in the room. I was confused on how to implement the chat room features that socketio had. If I had more time I would have implemented it better and have done the stretch features for it.  


