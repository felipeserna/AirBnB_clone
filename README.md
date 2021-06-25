# 0x00. AirBnB clone - The console

## Description

hbnb console is our first approach to a simple clone of the [AirBnB website](http://airbnb.com). The goal of the project is to deploy our server, this first part of the process we coded the console, that is a command interpreter to manipulate data without a visual interface, like in a Shell (perfect for development and debugging).

---

## Usage

* Clone this repository to your local machine:
```sh
git clone https://github.com/felipeserna/AirBnB_clone.git
cd AirBnB
```
### Interactive mode
```sh
./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

(hbnb) help <command name> \#where command is the command you want help with
(hbnb) quit \#to exit the console
```
### Non-interactive mode
```sh
$ echo "help" | ./console.py

(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  all  create  destroy  help  quit  show  update

echo "help <command name>" | ./console.py \#where command is the command you want help with
```
## File structure
[console.py](console.py) - This is the command interpreter or console.
[base_model.py](/models/base_model.py) - Base Model Defines all common attributes/methods for other classes.

Subclasses:
* [amenity.py](/models/amenity.py)
* [city.py](/models/city.py)
* [place.py](/models/place.py)
* [review.py](/models/review.py)
* [state.py](/models/state.py)
* [user.py](/models/user.py)

Engine:
[file_storage.py](/models/engine/file_storage.py) - Serializes instances to a JSON file and deserializes JSON file to instances.

Tests:
[tests](/tests/test_models)

Examples:
```sh
./console.py
(hbnb) all MyModel
** class doesn't exist **
(hbnb) all City
(hbnb) create BaseModel
1cfd66dd-1940-49b5-85cf-92bbf0bc6acf
(hbnb) all BaseModel
[BaseModel] (1cfd66dd-1940-49b5-85cf-92bbf0bc6acf) {'created_at': datetime.datet
ime(2020, 6, 28, 15, 37, 29, 312252), 'id': '1cfd66dd-1940-49b5-85cf-92bbf0bc6ac
f', 'updated_at': datetime.datetime(2020, 6, 28, 15, 37, 29, 312327)}
(hbnb) show BaseModel
** instance id missing **
(hbnb) show BaseModel 1cfd66dd-1940-49b5-85cf-92bbf0bc6acf
[BaseModel] (1cfd66dd-1940-49b5-85cf-92bbf0bc6acf) {'created_at': datetime.datet
ime(2020, 6, 28, 15, 37, 29, 312252), 'id': '1cfd66dd-1940-49b5-85cf-92bbf0bc6ac
f', 'updated_at': datetime.datetime(2020, 6, 28, 15, 37, 29, 312327)}
(hbnb) destroy BaseModel 1cfd66dd-1940-49b5-85cf-92bbf0bc6acf
(hbnb) show BaseModel 1cfd66dd-1940-49b5-85cf-92bbf0bc6acf
** no instance found **
(hbnb) create State
f9bb2624-292b-49bc-ab53-4797c2756eb0
(hbnb) show State f9bb2624-292b-49bc-ab53-4797c2756eb0
[State] (f9bb2624-292b-49bc-ab53-4797c2756eb0) {'created_at': datetime.datetime(
2020, 6, 28, 15, 40, 17, 202882), 'id': 'f9bb2624-292b-49bc-ab53-4797c2756eb0',
'updated_at': datetime.datetime(2020, 6, 28, 15, 40, 17, 203586)}
(hbnb) update State f9bb2624-292b-49bc-ab53-4797c2756eb0 name "California"
(hbnb) show State f9bb2624-292b-49bc-ab53-4797c2756eb0
[State] (f9bb2624-292b-49bc-ab53-4797c2756eb0) {'created_at': datetime.datetime(
2020, 6, 28, 15, 40, 17, 202882), 'id': 'f9bb2624-292b-49bc-ab53-4797c2756eb0',
'updated_at': datetime.datetime(2020, 6, 28, 15, 41, 43, 621970), 'name': 'Calif
ornia'}
(hbnb)
```

## Bugs:
No known bugs at this time. Do not hesitate to report bugs to the authors.

## Authors:
Felipe Serna <1509@holbertonschool.com>

Chemical Engineer with skills in the design of industrial processes for the elaboration of new products with added value, taking into account economic, environmental and safety restrictions. Knowledge in water treatment, integrated management systems HSEQ and GLP. High interest in fats and oils, particularly for the manufacture of biodiesel. In his Chemical Engineering thesis he designed and built the first microreactor in Colombia for manufacturing biodiesel.

[LinkedIn profile](https://www.linkedin.com/in/felipesernabarbosa/)

[Twitter](https://twitter.com/felipesernabar1)

[Porfolio Project repository](https://github.com/skillshare-mentorship/holberton-live-experience)

Santiago Martinez <sntgmtnz@gmail.com>

Advertising professional, technician in graphic arts. Studying software engineering at Holberton School. Facing the capitalist dogma, art lover, follow me @choladito on Twitter. Knowledge in programming languages C & Python, currently learning processing, eager to make generative art and HTML gadgets.

[LinkedIn profile](https://www.linkedin.com/in/choladito/)

[Twitter](https://twitter.com/choladito)
## License:
Public domain. No copyrights protection.
