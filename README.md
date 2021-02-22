# Holberton AirBnB clone project #

![Diagrama en blanco](https://user-images.githubusercontent.com/60363879/108719035-1434ae00-74ed-11eb-8240-e76ac30caf0f.png)

##### In this project, we implement the following: #####

- BaseModel class for instantation of AirBnB clone objects
- User, State, City, Place, Amenity, Review subclasses that inherit from BaseModel
- Serialization/deserialization of instances
- A storage engine for the project: FileStorage

### The Console ###
The code for the command interpreter is in console.py
To start the console, type ./console.py or python3 console.py in the directory console.py is in. This will make the command prompt (hbnb) appear on your terminal.

`
$ ./console.py
`
`
(hbnb)
`

## Environment

Ubuntu 14.04 LTS via Vagrant in VirtualBox and Interpret Python3

## More Info

-   But also in non-interactive mode: (like the Shell project in C)

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