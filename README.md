
#Intro Web projects

Some basic projects to get used to web programming in Python using the [Flask](http://flask.pocoo.org/) framework.
Each project will have a set of unit tests to prove functionality.

I'm making this as a tool to teach a friend so it will be updated as we go.

###Project 1

A simple Hello World app.

###Project 2

To be made


##Solutions

Located in the `solutions` directory. There are likely many other ways to solve each of these projects.

##Set Up

I suggest using [virtualenv](http://flask.pocoo.org/docs/installation/#virtualenv) to keep your Python packages organized.
The python dependencies are located in `requirements.txt`


    pip install virtualenv            # installling the virtualenv tool
    virtualenv --no-site-packages .   # creating a new virtualenv
    source bin/activate               # entering your new virtualenv
    pip install -r requirements.txt   # installing all dependecies from the requirements.txt list

