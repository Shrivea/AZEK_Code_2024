import pandas as pd
import win32com.client
import argparse
import sys
#Create a class
#//Create a function to load the spreadsheet in; THe spreadsheet will be read into by pandas and take in by a sys.argv
# In the command line, they can put a subject 
# In the command line, the user can put an intro
# They can put a body
class email_sender:
    def __init__(self,email_to,intro, subject, body):
        email_to = email_to
        intro = intro
        subject = subject
        body = body
    def get_body(self):
        return body
    def send_email(self):
        try:
            outlook = win32com.client.Dispatch("Outlook.Application")
            mail = outlook.CreateItem(0)
            mail.To = email_to
            #print("Email sent successfully")
            mail.Subject = subject
            mail.Body = body
            mail.Send()
            print("Email(s) sent successfully")
        except Exception as e:
            print(str(e))
if __name__ == '__main__':
    file_name = sys.argv[1]
    print("File name: "+ file_name)
    if not (len(sys.argv) == 2):
        print("Incorrect arguments")
        exit
    intr= input("Enter an introduction: ")
    print("The introduction includes: "+ intr)
    subject  = input("What will be the subject of your emails: ")
    print("The subject is : "+ subject)
    bod = input("Write the rest of your email: ")
    bool = input("Would you like to add a ending to you email? ")
    ending  = ""
    if bool == "Yes":
        ending = input("What would you like your ending to be:  ")
    print("The body includes: "+ bod)
    # Program file, List of recipients, Intro, Subject, Body
    if not (file_name[-4:]==".csv"):
        print("Error, file has to be a csv file")
        print(file_name[-3:])
        exit
    dat = None
    #print("First iteration\n")
    #print(dat)
    try:
        dat = pd.read_csv(file_name)
        #print("Second Iteration\n")
        #print(dat)
        print(f"Data loaded successfully from {file_name}")
    except Exception as e:
        print(f"Error loading data from {file_name}: {str(e)}")
    for i, x in dat.iterrows():
        email_to = str(x['Email'])
        first_name = str(x['First Name'])
        intro = (intr+(first_name))+"\n"
        body = intro+(bod)+"\n"+ending
        emailer = email_sender(email_to,intro,subject,body)
        #print(emailer.get_body())
        emailer.send_email()
    