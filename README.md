# Unique-Password-Generator

## About

A python GUI application that can generate, save, encrypt and decrypt your passwords or texts.

This Unique Password Generator can generate endless unique highly secure passwords. It has many features like customizing the password, encrypting and decrypting any text, saving the password and many more. This application is written in python language is made using the latest python gui package called PySimpleGUIQt. One can organize his/her passwords vey comfortably using this application.

About PySimpleGUI:
PySimpleGUI was launched in 2018, so it’s a relatively new package compared with the likes of wxPython or PyQt.

PySimpleGUI has four ports:

1. Tkinter
2. PyQt
3. wxPython
4. Remi

PySimpleGUI wraps portions of each of these other packages and makes them easier to use. However, each of the ports has to be installed separately.
PySimpleGUI wraps the entirety of Tkinter, which comes with Python. PySimpleGUI has wrapped most of PySide2, but only a small portion of wxPython. When you install PySimpleGUI, you get the Tkinter variant by default. For more information about Tkinter, check out Python GUI Programming With Tkinter.
Depending on which variant of PySimpleGUI you use, applications that you create with PySimpleGUI may not look native to their platform. But don’t let this stop you from giving PySimpleGUI a try. PySimpleGUI is still quite powerful and can get most things done with a little work.

Imported Modules:

PySimpleGUIQt:
PySimpleGUIQt is the PyQt version of PySimpleGUI Module.

random:
Python Random module is an in-built module of Python which is used to generate random numbers. These are pseudo-random numbers means these are not truly random. This module can be used to perform random actions such as generating random numbers, print random a value for a list or string, etc.

pyperclip:
Pyperclip is a cross-platform Python module for copy and paste clipboard functions. It works with both Python 2 and 3. This module was created to enable cross-platform copy-pasting in Python which was earlier absent. The pyperclip module has copy() and paste() functions that can send text to and receive text from your computer’s clipboard. Sending the output of your program to the clipboard will make it easy to paste it on an email, word processor, or some other software.

cryptography.fernet:
Cryptography is the practice of securing useful information while transmitting from one computer to another or storing data on a computer. Cryptography deals with the encryption of plaintext into ciphertext and decryption of ciphertext into plaintext. Python supports a cryptography package that helps us encrypt and decrypt data. The fernet module of the cryptography package has inbuilt functions for the generation of the key, encryption of plaintext into ciphertext, and decryption of ciphertext into plaintext using the encrypt and decrypt methods respectively. The fernet module guarantees that data encrypted using it cannot be further manipulated or read without the key.

os:
The OS module in Python provides functions for interacting with the operating system. OS comes under Python’s standard utility modules. This module provides a portable way of using operating system-dependent functionality. The _os_ and _os.path_ modules include many functions to interact with the file system.

Application Theme:
PySimpleGUI Module provide many color themes for the application. We can set a theme using PySimpleGUI.theme() method that takes the theme name as a parameter.

Constants:
BTN_SIZE - Size of the Button widget.
MLTLN_SIZE - Size of the Multiline widget.
NLN_SIZE - Height of the new line character.
POPUP_LCTN - Position of popups from the application on the screen.

Global Variables:
lower - String with all lower case alphabets.
lower_list - List of all lower case alphabets.
upper - String with all upper case alphabets.
upper_list - List of all upper case alphabets.
alpha_list - String with all lower and upper case alphabets.
digits - String with all digits.
digits_list - List of all digits.
alnum_list - List of all alpha-numeric characters.
special - String with all special characters.
special_list - List of all special characters.
all_list - List of all alpha-numeric and special characters.

Classes:

Password:
Docstring - Password class to represent a password. It generates and stores all the characteristics of a password.

Attributes:
self.password - Stores the generated or user given password.
self.length - Length of the generated or user given password.
self.contains - List of 4 boolean values.
1st value is true if password contains Uppercase letter else false.
2nd value is true if password contains lowercase letter else false.
3rd value is true if password contains a digit else false.
4th value is true if password contains a special character else false.
self.starts_with - List of 5 boolean values.
1st value is true if password starts with Uppercase letter else false.
2nd value is true if password starts with lowercase letter else false.
3rd value is true if password starts with a digit else false.
4th value is true if password starts with a special character else false.
5th value is true if password starts with a custom user given string.
self.ends_with - List of 5 boolean values.
1st value is true if password ends with Uppercase letter else false.
2nd value is true if password ends with lowercase letter else false.
3rd value is true if password ends with a digit else false.
4th value is true if password ends with a special character else false.
5th value is true if password ends with a custom user given string.
self.custom_starts_with - If 5th value of self.starts_with is true, this attribute holds the custom string.
self.custom_ends_with - If 5th value of self.ends_with is true, this attribute holds the custom string.

Constructor:
-> Parametrized Constructor with all default values.
-> Initializes all attributes.
-> If password is NoneType, self.generate method is called that generates a new password.

Methods:
--str-- - Returns the password.
--len-- - Returns the length of the password.
generate - Generates a new password according to the customizations given by the user.

Layouts in PySimpleGUI:
Layouts in PySimpleGUI are represented using nested lists. Each of the nested list contains widgets like Buttons, Texts, etc. Widgets in the same list are aligned side by side. Widgets in the different list are aligned in different lines.

Frames in PySimpleGUI:
Frames is a widget which is a container of widgets. It stores the widgets as a layout.

Widgets in PySimpleGUI:
A widget is an element of a graphical user interface (GUI) that displays information or provides a specific way for a user to interact with the operating system or an application.
Widgets include icons, pull-down menus, buttons, selection boxes, progress indicators, on-off checkmarks, scroll bars, windows, window edges (that let you resize the window), toggle buttons, form, and many other devices for displaying information and for inviting, accepting, and responding to user actions.

Window in PySimpleGUI:
PySimpleGUI provides a Window Element that you use to display other Elements in, such as buttons, text, images, and more. These Windows can be made Modal. A Modal Window won't let you interact with any other Windows in your program until you exit it. This is useful when you want to force the user to read something or ask the user a question.

Event Loop:
A graphical user interface needs to run inside a loop and wait for the user to do something. For example, the user might need to press a button in your UI or type something with their keyboard. When they do that, those events are processed by the event loop.
When you use PySimpleGUI, you make an event loop by creating an infinite while loop that reads events from the window object. If the user presses the OK button or the Exit button, then you want the program to end. To accomplish that, you break out of the loop and close() the window.

Window.read():
This method returns two values: a string and a dictionary. String is the event and dictionary is the values.

Event:
Variable Type - String
Every widget is identified using a key. Whenever the user interacts with a widget, the read method returns the key of the widget as a string indicating the user interaction.

Values:
Variable Type - Dictionary
Keys of this dictionary are the key of every widget of the application. The value of the corresponding key is the data stored in the widget with that key. If the widget does not contains any data, the value is set to None.

Exceptions Handled:

1. Invalid open file path
2. Invalid file (file without .password extension)
3. Invalid save location
4. Invalid decrypt key
5. Invalid encrypt text

Thank you for using this software.
