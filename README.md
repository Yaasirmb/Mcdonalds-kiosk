# McDonald Kiosk Project

## What this project does:
This is a project meant to imitate the functionalities of an order taking kiosk.
## Dependencies

The dependencies used are the Tabulate 0.8.6 and Time python modules. 

[Tabulate module](https://pypi.org/project/tabulate/)

The kiosk_functions.py file is where the functions that actually run the kiosk live.
The display.py file is what get's printed to the terminal to display all the menu items.
The menu.py file is where the script goes to see if an item is there and get's the price.
## How to start:

To start this program, navigate to the directory you cloned this folder in and run the order.py file.

```powershell
cd .\the\directory\you cloned this into

python order.py
```


The program will run forever unless you use the "Exit" command listed when you type "Help".

To pay for your order, enter a number that's greater than or equal to the total.

```python
"Your total is $6.23, please enter your card into the terminal."

7.50

"Your change is $1.27...
```

While taking your order, the program isn't case sensitive, however when using any of the "Help" commands, those are case sensitive just to make sure you want to go through with it.

### Secret
The McRib is back ;D

## Author

This script was made by Yaasir M.B.

## Acknowledgements

Thanks to John B. for helping me think things out and supervising the project.

Thanks to David F. for helping me with some python syntax and logical thinking.