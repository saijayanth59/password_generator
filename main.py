
# installing required modules
import os

os.system("pip install pysimplegui")
os.system("pip install pysimpleguiqt")
os.system("pip install pyperclip")
os.system("pip install cryptography")

# importing gui module
import PySimpleGUIQt as gui
import random
import pyperclip
from cryptography.fernet import Fernet

# setting theme
gui.theme("Default")

# widget options
BTN_SIZE = (100, 30)
MLTLN_SIZE = (40, 4)
NLN_SIZE = (0.3, 0.3)
POPUP_LCTN = (500, 500)

# character strings and lists
lower = "abcdefghijklmnopqrstuvwxyz"
lower_list = list(lower)
upper = lower.upper()
upper_list = list(upper)
alpha_list = lower_list + upper_list
digits = "0123456789"
digits_list = list(digits)
alnum_list = alpha_list + digits_list
special = " !\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
special_list = list(special)
all_list = alnum_list + special_list

# password class
class Password:

    '''
    Password class to represent a password.
    '''

    def __init__(self, password = None, length = 8, contains = [True] * 4, starts_with = [False] * 5,
                    ends_with = [False] * 5, custom_starts_with = None, custom_ends_with = None):
        self.password = password
        self.length = length
        self.contains = contains
        self.starts_with = starts_with
        self.ends_with = ends_with
        self.custom_starts_with = custom_starts_with
        self.custom_ends_with = custom_ends_with

        if self.password == None:
            self.password = self.generate()
        else:
            length = len(self.password)

    def __str__(self):
        return self.password

    def __len__(self):
        return self.length

    # generate functio
    def generate(self):
        l = self.length
        pas = ""

        # if any starts with option is selected
        if any(self.starts_with):
            if self.starts_with[-1]:
                pas += self.custom_starts_with
                l -= len(self.custom_starts_with)
            else:
                if self.starts_with[0]:
                    pas += random.choice(upper_list)
                if self.starts_with[1]:
                    pas += random.choice(lower_list)
                if self.starts_with[2]:
                    pas += random.choice(digits_list)
                if self.starts_with[3]:
                    pas += random.choice(special_list)
                l -= 1

        # if any ends with option is selected
        if any(self.ends_with):
            if self.ends_with[-1]:
                l -= len(self.custom_ends_with)
            else:
                l -= 1

        # if all the check boxes are checked
        if all(self.contains):
            random.shuffle(all_list)
            for _ in range(l):
                pas += random.choice(all_list)
        else:
            char_list = []
            if self.contains[0]:
                char_list += upper_list
            if self.contains[1]:
                char_list += lower_list
            if self.contains[2]:
                char_list += digits_list
            if self.contains[3]:
                char_list += special_list

            random.shuffle(char_list)

            for _ in range(l):
                pas += random.choice(char_list)

        # if any ends with option is selected
        if any(self.ends_with):
            if self.ends_with[-1]:
                pas += self.custom_ends_with
            else:
                if self.ends_with[0]:
                    pas += random.choice(upper_list)
                if self.ends_with[1]:
                    pas += random.choice(lower_list)
                if self.ends_with[2]:
                    pas += random.choice(digits_list)
                if self.ends_with[3]:
                    pas += random.choice(special_list)

        return pas

# open/save layout
open_save = [
    [gui.Frame("Open:", [
        [gui.In(size = (30, 0.8), key = "-FILE-"), gui.FileBrowse(size = BTN_SIZE)]
    ])],
    [gui.Frame("Password:", [
        [gui.Multiline(size = (27, 4), font = ("Courier New", 14, "bold"), key = "-PSWD-")]
    ]), gui.Frame("", [
        [gui.Text("\n", size = (0.15, 0.15))],
        [gui.Button("Open", size = BTN_SIZE, key = "-FOPEN-")],
        [gui.Text("\n", size = (0.1, 0.1))],
        [gui.Button("Copy", size = BTN_SIZE, key = "-PSWDC-")]
    ], element_justification = "center")],
    [gui.Frame("Save:", [
        [gui.DropDown(values = [
            "Select",
            "Quick Generated Password",
            "Generated Password",
            "Encrypted Text",
            "Decrypted Text"
        ], size = (32, 0.8), key = "-SDD-", enable_events = True), gui.Checkbox("Encrypt", key = "-SENCRYPT-")]
    ])],
    [gui.Frame("Save location:", [
        [gui.In(size = (30, 0.8), key = "-FOLDER-"), gui.FolderBrowse(size = BTN_SIZE)]
    ])],
    [gui.Frame("File name:", [
        [gui.In(size = (30, 0.8), key = "-FNAME-"), gui.Button("Save", size = BTN_SIZE, key = "-SB-")]
    ])]
]

# frame layout for quick_generate
quick_generated_password = [
    [gui.Multiline(str(Password()), size = MLTLN_SIZE, font = ("Courier New", 18, "bold"), key = "-QGP-")],
    [gui.Button("Generate", size = BTN_SIZE, key = "-QGB-"), gui.Button("Copy", size = BTN_SIZE, key = "-QGC-")]
]

# quick generate layout
quick_generate = [
    [gui.Frame("Length:", [
        [gui.Spin(values = range(1, 129), initial_value = 8, key = "-QGL-", size = (40, 1))]
    ], element_justification = "center")],
    [gui.Frame("Quick Generated Password:", quick_generated_password, element_justification = "center")]
]

# first column layout
column = [
    [gui.Frame("Open/Save:", open_save, element_justification = "center")],
    [gui.Text("\n", size = (0.15, 0.15))],
    [gui.Frame("Quick Generate", quick_generate)]
]

# frame layouts of generate layout
contains = [
    [gui.Checkbox("Uppercase Characters (A-Z)", default = True, key = "-UPPER-")],
    [gui.Checkbox("Lowercase Characters (a-z)", default = True, key = "-LOWER-")],
    [gui.Checkbox("Digits (0-9)", default = True, key = "-DIGITS-")],
    [gui.Checkbox("Special Characters (" + special + ")", default = True, key = "-SPECIAL-")]
]

starts_with = [
    [gui.Radio("Uppercase Character (A-Z)", group_id = "sw", key = "-SUPPER-")],
    [gui.Radio("Lowercase Character (a-z)", group_id = "sw", key = "-SLOWER-")],
    [gui.Radio("Digit (0-9)", group_id = "sw", key = "-SDIGIT-")],
    [gui.Radio("Special Character (" + special + ")", group_id = "sw", key = "-SSPECIAL-")],
    [gui.Radio("Custom", group_id = "sw", key = "-SCUSTOM-"), gui.InputText(size = (32, 0.8), key = "-SCT-")]
]

ends_with = [
    [gui.Radio("Uppercase Character (A-Z)", group_id = "ew", key = "-EUPPER-")],
    [gui.Radio("Lowercase Character (a-z)", group_id = "ew", key = "-ELOWER-")],
    [gui.Radio("Digit (0-9)", group_id = "ew", key = "-EDIGIT-")],
    [gui.Radio("Special Character (" + special + ")", group_id = "ew", key = "-ESPECIAL-")],
    [gui.Radio("Custom", group_id = "ew", key = "-ECUSTOM-"), gui.InputText(size = (32, 0.8), key = "-ECT-")]
]

generated_password = [
    [gui.Multiline(size = MLTLN_SIZE, font = ("Courier New", 18, "bold"), key = "-GP-")],
    [gui.Button("Generate", size = BTN_SIZE, key = "-GB-"), gui.Button("Copy", size = BTN_SIZE, key = "-GC-")],
    [gui.Text("\nDesigned and Developed by AP20110010005, SRM University, AP.")]
]

# generate layout
generate = [
    [gui.Frame("Length:", [
        [gui.Spin(values = range(1, 129), initial_value = 8, key = "-GL-", size = (40, 1))]
    ], element_justification = "center")],
    [gui.Frame("Contains:", contains)],
    [gui.Text("\n", size = NLN_SIZE)],
    [gui.Frame("Starts with:", starts_with)],
    [gui.Text("\n", size = NLN_SIZE)],
    [gui.Frame("Ends with:", ends_with)],
    [gui.Frame("Generated Password:", generated_password, element_justification = "center")]
]

# frame layouts of encrypt/decrypt layout
encrypt = [
    [gui.Frame("Input text to be encrypted:", [
        [gui.Multiline(size = MLTLN_SIZE, key = "-TE-")],
        [gui.Button("Encrypt", size = BTN_SIZE, key = "-EB-")]
    ], element_justification = "center")],
    [gui.Frame("Key:", [
        [gui.InputText(size = (30, 0.8), key = "-EK-"), gui.Button("Copy", size = BTN_SIZE, key = "-EKC-")]
    ], element_justification = "center")],
    [gui.Frame("Encrypted Text:", [
        [gui.InputText(size = (30, 0.8), key = "-ET-"), gui.Button("Copy", size = BTN_SIZE, key = "-ETC-")]
    ], element_justification = "center")]
]

decrypt = [
    [gui.Frame("Input encrypted text:", [
        [gui.InputText(size = (40, 0.8), key = "-TD-")]
    ], element_justification = "center")],
    [gui.Frame("Input key:", [
        [gui.InputText(size = (40, 0.8), key = "-DK-")]
    ], element_justification = "center")],
    [gui.Button("Decrypt", size = BTN_SIZE, key = "-DB-")],
    [gui.Text("\n", size = NLN_SIZE)],
    [gui.Frame("Decrypted Text:", [
        [gui.Multiline(size = MLTLN_SIZE, key = "-DT-")],
        [gui.Button("Copy", size = BTN_SIZE, key = "-DTC-")]
    ], element_justification = "center")]
]

# encrypt/decrypt layout
encrypt_decrypt = [
    [gui.Frame("Encrypt:", encrypt, element_justification = "center")],
    [gui.Text("\n", size = NLN_SIZE)],
    [gui.Frame("Decrypt:", decrypt, element_justification = "center")]
]

# creating final layout
layout = [
    [
        gui.Frame("Welcome to Unique Password Generator!", column),
        gui.VerticalSeparator(),
        gui.Frame("Generate", generate),
        gui.VerticalSeparator(),
        gui.Frame("Encrypt/Decrypt", encrypt_decrypt)
    ]
]

# creating main window
window = gui.Window("Unique Password Generator", layout, resizable = False)

# event loop
while True:
    event, values = window.read()

    # if exit is clicked or window is closed, loop will break
    if event == "Exit" or event == gui.WIN_CLOSED:
        break

    # if open is clicked
    if event == "-FOPEN-":
        try:
            file_path = values["-FILE-"]

            # if file extension is not password
            if not file_path.endswith(".password"):
                window["-PSWD-"].update("Invalid file!")
                continue

            file = open(file_path, "r")
            contents = file.read().split('\n')

            # if encrypted
            if contents[0] == 'True':
                key = contents[1]
                encrypted_text = contents[2]

                fernet = Fernet(key.encode())

                decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()

                window["-PSWD-"].update(decrypted_text)
            else:
                window["-PSWD-"].update(contents[1])

            file.close()
        except:
            window["-PSWD-"].update("Invalid path!")
    
    # if there is no file path
    if len(values["-FILE-"]) == 0:
        window["-PSWD-"].update("")

    # if copy of password is clicked
    if event == "-PSWDC-":
        pyperclip.copy(values["-PSWD-"])

    # if any from the dropdown list is selected
    if event == "-SDD-":
        if values["-SDD-"] != "Select":
            file_name = "_".join(values["-SDD-"].split()) + "_" + str(Password(length = 5, contains = [1,1,1,0])) + ".password"
            window["-FNAME-"].update(file_name)
        else:
            window["-FNAME-"].update("")

    # if save button is clicked
    if event == "-SB-":

        file_path = values["-FOLDER-"]
        file_name = values["-FNAME-"]

        # if filename does not contain extension
        if not file_name.endswith(".password"):
            file_name = file_name + ".password"
        file_path += "/" + file_name

        content = values["-SDD-"]
        text = None

        try:
            file = open(file_path, "w+")

            if content == "Quick Generated Password":
                text = values["-QGP-"]
            elif content == "Generated Password":
                text = values["-GP-"]
            elif content == "Encrypted Text":
                text = values["-ET-"]
            elif content == "Decrypted Text":
                text = values["-DT-"]
            else:
                gui.PopupError("Invalid path!", title = "Unique Password Generator", location = POPUP_LCTN)

            if len(text) == 0:
                gui.PopupError("Password is empty!", title = "Unique Password Generator", location = POPUP_LCTN)
                file.close()
                os.remove(file_path)
                continue
            else:
                pass

            # if encrypt option is checked
            if values["-SENCRYPT-"]:

                file.write("True\n")

                if content == "Encrypted Text":
                    key = values["-EK-"].encode()
                    encrypted_text = values["-ET-"].encode()

                    if len(key) == 0 or len(encrypted_text) == 0:
                        gui.PopupError("Encrypted Text or Key is empty!", title = "Unique Password Generator", location = POPUP_LCTN)
                        file.close()
                        os.remove(file_path)
                        continue
                    else:
                        pass

                else:
                    key = Fernet.generate_key()
                    fernet = Fernet(key)

                    encrypted_text = fernet.encrypt(text.encode())

                file.write(key.decode())
                file.write("\n")
                file.write(encrypted_text.decode())
            else:

                if content == "Encrypted Text":
                    file.write("True\n")

                    key = values["-EK-"]
                    encrypted_text = values["-ET-"]

                    if len(key) == 0 or len(encrypted_text) == 0:
                        gui.PopupError("Encrypted Text or Key is empty!", title = "Unique Password Generator", location = POPUP_LCTN)
                        file.close()
                        os.remove(file_path)
                        continue
                    else:
                        pass

                    file.write(key + "\n")
                    file.write(encrypted_text)

                else:
                    file.write("False\n")
                    file.write(text)

            file.write("\n\n# This file can be renamed but modifying the contents or extension of the file may cause data loss!")

            gui.Popup("Password saved successfully at\n" + file_path, title = "Unique Password Generator", location = (500, 500))

            file.close()
        except:
            gui.PopupError("Invalid path or file!", title = "Unique Password Generator", location = POPUP_LCTN)
            continue

    # if generate of quick generate is clicked
    if event == "-QGB-":
        window["-QGP-"].update(str(Password(length = values["-QGL-"])))

    # if copy of quick generate is clicked
    if event == "-QGC-":
        pyperclip.copy(values["-QGP-"])

    # if generate of generate password is clicked
    if event == "-GB-":
        l = values["-GL-"]
        csw = values["-SCT-"]
        cew = values["-ECT-"]
        contains_list = [values["-UPPER-"], values["-LOWER-"], values["-DIGITS-"], values["-SPECIAL-"]]
        sw_list = [values["-SUPPER-"], values["-SLOWER-"], values["-SDIGIT-"], values["-SSPECIAL-"], values["-SCUSTOM-"]]
        ew_list = [values["-EUPPER-"], values["-ELOWER-"], values["-EDIGIT-"], values["-ESPECIAL-"], values["-ECUSTOM-"]]

        if not any(contains_list):
            window["-UPPER-"].update(True)
            contains_list[0] = True

        window["-GP-"].update(str(Password(length = l, contains = contains_list, starts_with = sw_list, ends_with = ew_list, custom_starts_with = csw, custom_ends_with = cew)))
    
    # if copy of generate password is clicked
    if event == "-GC-":
        pyperclip.copy(values["-GP-"])

    # if encrypt is clicked
    if event == "-EB-":
        text = values["-TE-"]

        key = Fernet.generate_key()
        fernet = Fernet(key)

        encrypted_text = fernet.encrypt(text.encode())

        window["-EK-"].update(key.decode())
        window["-ET-"].update(encrypted_text.decode())

    # if copy of encrypt key is clicked
    if event == "-EKC-":
        pyperclip.copy(values["-EK-"])

    # if copy of encrypt text is clicked
    if event == "-ETC-":
        pyperclip.copy(values["-ET-"])

    # if decrypt is clicked
    if event == "-DB-":
        key = values["-DK-"]
        encrypted_text = values["-TD-"]

        try:
            fernet = Fernet(key.encode())
            decrypted_text = fernet.decrypt(encrypted_text.encode()).decode()
        except:
            decrypted_text = "Invalid token!"

        window["-DT-"].update(decrypted_text)

    # if copy of decrypt text is clicked
    if event == "-DTC-":
        pyperclip.copy(values["-DT-"])

# closing the window
window.close()