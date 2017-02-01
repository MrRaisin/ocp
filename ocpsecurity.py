import json
import time
import random
import urllib.request

class security():
    def __init__(self):
        self._day = time.strftime("%A")
        self.__login = self.__loginGen()
        self.__login = 'Wednesday22017'
        self.__password = self.__setPwd()
        self.__password = 'Password8*'

    def SignIn(self, user_name, password):
        inttime = int(time.strftime("%M"))
        # Checks the user's input against the actual password
        if self.__login.lower() == user_name.lower() and self.__password == password and (inttime % 6) != 0:
            return "Access Granted"
        elif self.__login.lower() == user_name.lower() and self.__password == password and (inttime % 6) == 0:
            print("You forgot the threat of the guard while hacking...\nYou had the right password but got caught\nYou get locked back out\nPassword reset - try again :-)")
            self.__password = self.setPwd()
            return "Password reset"
        else:
            return "Access Denied"
    
    def __loginGen(self):
    # Generates login as a list then joins the list and returns to main.
        login_list = []
        login_list.append(self._day)
        login_list.append(time.strftime("%#m"))
        login_list.append(time.strftime("%Y"))
        login = "".join(login_list)
        return login

    def __setPwd(self):
    # Acts as a hub for 4 functions to put together the password.
        word = self.__genWord()
        character = self.__genChar()
        number = self.__genNum()
        password = self.__makePassword(word, character, number)
        return password
        
    def __genWord(self):
        #Calls out to external API to get a word. The day name is used to slightly change the URL.
        RequestURL = "http://www.setgetgo.com/randomword/get.php?len="
    
        if self._day in ("Monday","Tuesday","Wednesday"):
            RequestURL = RequestURL + "8"

        elif self._day in ("Thursday","Friday"):
            RequestURL = RequestURL + "9"

        elif self._day in ("Saturday","Sunday"):
            RequestURL = RequestURL + "10"

        found = False

        while not found:
            response = urllib.request.urlopen(RequestURL)
            myword = response.read().decode("utf-8")
            found = self.__checkPWD(myword)
            
        return myword.capitalize()

    def __genChar(self):
    #Randomly chooses from a set of characters then returns it.
        charlist = ["!","@","£","$","%","&","*","#"]
        character = random.choice(charlist)
        return character

    def __genNum(self):
    #Randomly generates a number and returns it.
        num = random.randint(0,9)
        num = str(num)
        return num

    def __makePassword(self, word, char, num):
    #Puts together the password as a list then joins it and returns it.
        pass_list = []
        pass_list.append(word)
        pass_list.append(char)
        pass_list.append(num)
        password = "".join(pass_list)
        return password

    def __checkPWD(self, pwd):
    #Checks word from the web against the english dictionary file
        try:
            text_file = open('English_Dictionary_Full.txt', 'r')
            for line in text_file:
                if line.lower().strip('\n') == pwd.lower():
                    return True
            return False
        finally:
            text_file.close()

