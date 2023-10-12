# AirBnB clone


The goal of this project is to deploy on our server a simple copy of the AirBnB website, as part of the learning program at alx.

All the features will not be implemented at once, only some of them to cover all fundamental concepts of the higher level programming track.

This project is expected to be completed after 4 months as we learn and implement new concepts after which we will have a complete web application composed by:
*A command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging)
*A website (the front-end) that shows the final product to everybody: static and dynamic
*A database or files that store data (data = objects)
*An API that provides a communication interface between the front-end and your data (retrieve, create, delete, update them)


## Execution

  
The shell should work like this in interactive mode:

  
```
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF help quit

(hbnb)
(hbnb)
(hbnb) quit
$
```

But also in non-interactive mode: (like the Shell project in C)

```
$ echo "help" | ./console.py

(hbnb)

Documented commands (type help <topic>):
========================================

EOF help quit
(hbnb)
$
$ cat test_help
help
$
$ cat test_help | ./console.py
(hbnb)

  
Documented commands (type help <topic>):
========================================
EOF help quit
(hbnb)
$

```

