# The AirBnB Clone Project
![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

## Project Description
This project is broken into fragments or steps, and this is the first part of the AirBnB clone project. We interacted with the backend of the project, using a console developed by importing the cmd module in python. The console gave us the priviledge to manipulate different class instances, store them using file storage (.json file) and extracted date from the file.


## The console
The console has similar features with the bash shell except that the console is designed or developed towards achieving limited specific functions such as for manipulating project data without a visual interface, in this case, the AirBnB project (its classes, storage e.t.c). The console is good for debugging and development.

Some of the commands in the console:

* show - Retrieves an object/instance from a file or a database storage etc.
* create - Creates new objects/instances. Example, create a new User or a new Place class.
* update - Updating the attributes of an object/instance either by modifying existing or adding new attributes.
* count - Count number objects/instances of a particular class that's be created.
* destroy - Destroying an object.

## Installing the console for the AirBnB
The steps below shows step-by-step procedure on how to install the console:

* Step 1: Clone the repository of this project from Github. Cloning this project contains the console program and all of its dependencies.

```
git clone https://github.com/Topsurpass/AirBnB_clone.git

```
Below are the description of the program and all its dependencies:

> /console.py : The main executable of the project, the command interpreter.
>
> models/engine/file_storage.py: This module contains a class that serializes and deserializes instances to and from a JSON file.
> 
> models/__ init __.py:  A unique `FileStorage` instance for the application that ensures the storage is up-to-date once imported.
> 
> models/base_model.py: This module contains class that defines all common attributes (methods and fields) for other classes.
> 
> models/user.py: This module contains User class that inherits from BaseModel.
> 
>models/state.py: This module contains State class that inherits from BaseModel.
>
>models/city.py: This module contains City class that inherits from BaseModel.
>
>models/amenity.py: This module contains Amenity class that inherits from BaseModel.
>
>models/place.py: This module contains Place class that inherits from BaseModel.
>
>models/review.py: This module contains Review class that inherits from BaseModel.


## How to use it
It can work in two different modes:


**Interactive** and **Non-interactive**.

In **Interactive mode**, the console will display a prompt (hbnb) indicating that the user can write and execute a command. After the command is run, the prompt will appear again a wait for a new command. This can go indefinitely as long as the user does not exit the program.

```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) 
(hbnb) 
(hbnb) quit
$
```

In **Non-interactive mode**, the shell will need to be run with a command input piped into its execution so that the command is run as soon as the Shell starts. In this mode no prompt will appear, and no further input will be expected from the user.


```
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 
$
```

## Console commands format

In order to give commands to the console, these will need to be piped through an echo in case of  **Non-interactive mode**.

In  **Interactive Mode**  the commands will need to be written with a keyboard when the prompt appears and will be recognized when an enter key is pressed (new line). As soon as this happens, the console will attempt to execute the command through several means or will show an error message if the command didn't run successfully. In this mode, the console can be exited using the **CTRL + D** combination,  **CTRL + C**, or the command **quit** or **EOF**.

## Arguments

Most commands have several options or arguments that can be used when executing the program. In order for the console to recognize those parameters, the user must separate everything with spaces.

Example:

```

vagrant@ubuntu-focal:~/AirBnB$ ./console.py
(hbnb) create BaseModel
49du8f9a-6018-451f-836d-910505c55907
vagrant@ubuntu-focal:~/AirBnB$ ./console.py

```
or

```
vagrant@ubuntu-focal:~/AirBnB$ ./console.py $ echo "create BaseModel" | ./console.py
(hbnb)
r37f19d3-gde1-9g1f-8095-7a0190753872
(hbnb)
vagrant@ubuntu-focal:~/AirBnB$ ./console.py
```

## Console commands

The recognizable commands by the console are the following:

|Command| Description |
|--|--|
| **quit or EOF** | Exits the program |
| **Usage** | By itself |
| **-----** | **-----** |
| **help** | Provides a text describing how to use a command.  |
| **Usage** | By itself --or-- **help <command\>** |
| **-----** | **-----** |
| **create** | Creates a new instance of a valid `Class`, saves it (to the JSON file) and prints the `id`.  Valid classes are: BaseModel, User, State, City, Amenity, Place, Review. |
| **Usage** | **create <class name\>**|
| **-----** | **-----** |
| **show** | Prints the string representation of an instance based on the class name and `id`  |
| **Usage** | **show <class name\> <id\>** --or-- **<class name\>.show(<id\>)**|
| **-----** | **-----** |
| **destroy** | Deletes an instance based on the class name and `id` (saves the change into a JSON file).  |
| **Usage** | **destroy <class name\> <id\>** --or-- **<class name>.destroy(<id>)** |
| **-----** | **-----** |
| **all** | Prints all string representation of all instances based or not on the class name.  |
| **Usage** | By itself or **all <class name\>** --or-- **<class name\>.all()** |
| **-----** | **-----** |
| **update** | Updates an instance based on the class name and `id` by adding or updating attribute (saves the changes into a JSON file).  |
| **Usage** | **update <class name\> <id\> <attribute name\> "<attribute value\>"** ---or--- **<class name\>.update(<id\>, <attribute name\>, <attribute value\>)** --or-- **<class name\>.update(<id\>, <dictionary representation\>)**|
| **-----** | **-----** |
| **count** | Retrieve the number of instances of a class.  |
| **Usage** | **<class name\>.count()** |

## Authors

* Olowosuyi Temitope
* Emmanuel Essien
