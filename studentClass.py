#!/usr/bin/env python3
# this is a class containing student information
class Student:
    #Personal data
    idNum = 0
    name = "default_name"
    schoolEmail = "default@gmail.com"
    
    #Pronouns
    pronouns = "default/defaults" #string representing the pronoun
    preferSame = 1 #does the person prefer someone of their same gender.

    #Meet the times (starting [sunday] [midnight])
    meetingTimes = [[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1],[1, 1, 1, 1, 1, 1]]
    preferAsy = 0 # 3 values, 0 = sync, 1= no preference, 2=async

    #Contact Infonrmation
    contactPreference = [False, False, False, True]  #Discord, Phone Number, Email, Canvas Groups 0 = no, 1= no preference, 2= yes
    contactInformation = ["defaultDiscordName#2424", "(000) 000-0000", "deafultEmail@gmail.com"]

    #Preferred Leader or Follower
    preferLeader = False

    #Country of Origin if US then false?
    countryOfOrigin = "United States of America"
    preferCountry = False

    # international student preference
    international = 0
         
    #Language Preference
    language = "English"
    
    #Preffered Stuff to Do
    option1 = "default"
    option2 = "default"
    freeResponse = "default"

    #Priority
    priorityList = ["default", "default", "default", "default", "default"]

    #confidence
    confidence = "default"
    
    def __init__(self, idNumInput = 0, nameInput = "default_name", emailInput = "default_email"):
        self.name = nameInput
        self.idNum = idNumInput
        self.schoolEmail = emailInput
