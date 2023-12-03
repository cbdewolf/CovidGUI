import tkinter 
import PIL

from tkinter import *

#make the window
root = Tk()

#make the size 600 wide 1000 long 2/100
root.geometry('600x1000')

#window title 4/100
root.title('COVID VACCINATION INFORMATION')

#confidential label, make sure this is the biggest text on screen 6/100
conf_label = Label(root, text='All information will be kept confidential', width=30, font=('bold',25))
conf_label.place(x=60,y=75)

#create a name label and text box 9/100 
name_label = Label(root, text='Name: ', width=20, font=('bold',15))
name_label.place(x=-20,y=150)

userName = StringVar()
userName.set('')
#userName.set('Type Name Here')
nameEntry = Entry(root, textvariable= userName)
nameEntry.configure(width=20)
nameEntry.place(x=110,y=150)

#phone number label and text box 12/100
phone_label = Label(root, text='Phone Number: ', width=20, font=('bold',15))
phone_label.place(x=11, y=200)

phoneNum = StringVar()
phoneNum.set('')
#phoneNum.set('Type Phone Number Here')
phoneEntry = Entry(root, textvariable= phoneNum)
phoneEntry.configure(width=20)
phoneEntry.place(x=168,y=200)

#email address label and text box 15/100
email_label = Label(root, text='Email Address: ', width=20, font=('bold',15))
email_label.place(x=8, y=250)

emailAdd = StringVar()
emailAdd.set('')
#emailAdd.set('Type Email Address Here')
emailEntry = Entry(root, textvariable= emailAdd)
emailEntry.configure(width=20)
emailEntry.place(x=166,y=250)

#vaccine label and drop down menu 19/100
whichVax = Label(root, text='Which Vaccine Did You Receive?', width=30, font=('bold',15))
whichVax.place(x=18,y=300)

vaccineList = ['Pfizer', 'Moderna', 'Johnson & Johnson']
vaccine = StringVar()
vaccine.set('Choose Here')
vaxDrop = OptionMenu(root, vaccine, *vaccineList)
vaxDrop.place(x=290,y=300)

#shot number label and drop down menu 23/100
numVax = Label(root, text='First, Second, or Booster Vaccine?', width=40, font=('bold',15))
numVax.place(x=-26,y=350)

numList = ['first','second','booster']
num = StringVar()
num.set('Choose Here')
numDrop = OptionMenu(root, num, *numList)
numDrop.place(x=300,y=350)

#side effect check boxes 33/100 
#need to make so none disselects the others ? ****************

# **********
sideEffects = Label(root, text='Choose Any Side Effects That Apply:', width=40, font=('bold',15))
sideEffects.place(x=-20,y=400)

pain = IntVar()
painBox = Checkbutton(root, text='Pain at injection site', var = pain)
painBox.place(x=52,y=450)

armPain = IntVar()
armBox = Checkbutton(root, text='Pain down arm', var = armPain)
armBox.place(x=205,y=450)

fever = IntVar()
feverBox = Checkbutton(root, text='Fever', var = fever)
feverBox.place(x=325,y=450)

headache = IntVar()
headBox = Checkbutton(root, text='Headache', var = headache)
headBox.place(x=390,y=450)

nausea = IntVar()
nauseaBox = Checkbutton(root, text='Nausea', var = nausea)
nauseaBox.place(x=52,y=500)

rash = IntVar()
rashBox = Checkbutton(root, text='Rash', var = rash)
rashBox.place(x=125,y=500)

hives = IntVar()
hivesBox = Checkbutton(root, text='Hives', var = hives)
hivesBox.place(x=180,y=500)

swell = IntVar()
swellBox = Checkbutton(root, text='Swelling', var = swell)
swellBox.place(x=243,y=500)

chills = IntVar()
chillsBox = Checkbutton(root, text='Chills', var = chills)
chillsBox.place(x=320,y=500)

bodyache = IntVar()
bodyacheBox = Checkbutton(root, text='Body ache', var = bodyache)
bodyacheBox.place(x=380,y=500)

none = IntVar()
noneBox = Checkbutton(root, text='None', var = none)
noneBox.place(x=52,y=550)

#phone number checker, if it is valid, return the 'valid phone number extracted from user input', or boolean False 
#43/100

def validPhoneNumber(myString):
    
    numbers = []
    #convert to list so i can iterate

    myList = list(myString)
    #check for digits
    for x in myList:
        if x.isdigit():
            numbers.append(x)
        else:
            return False
    #check for length
    if len(numbers) == 10:
        return myString
    else:
        return False
    
pass

#email checker, if valid, return the entered email address, else, return boolean False
#53/100

def validEmail(myString):
    myList = list(myString)
    new = myString.split('@')
    
    #check for only 1 @
    counter = 0
    for j in myList:
        if j == '@':
            counter = counter + 1
    if counter == 0:
        return False
    elif counter > 1:
        return False
    #check for an empty string 
    for x in new:
        if len(x) == 0:
            return False

    return myString

pass

#info submitted label 57/100

infosubmit = StringVar()
infosubmit.set('')
infolabel = Label(root, width=20, font=('bold',15), textvariable=infosubmit)
infolabel.place(x=200,y=575)

#feedback label
feedback = StringVar()
feedback.set('')
feedbackLabel = Label(root, font=('bold',18), width=25, textvariable=feedback)
feedbackLabel.place(x=162,y=625)

#need more info label
needinfo = StringVar()
needinfo.set('')
needinfoLabel = Label(root, font=('bold', 18), textvariable=needinfo)
needinfoLabel.place(x=165,y=625)

def submitPressed():
    #Boolean True for whether or not the user can submit 
    canSubmit = True
    
    global validPhoneNumber
    global validEmail
    global nameEntry
    global emailEntry
    global phoneEntry
    global vaccine
    global whichVax
    global num 
    global feedback
    global feedbackLabel
    global needinfo
    global needinfoLabel
    global infosubmit
    
    #verify the name 
    buttonname = nameEntry.get()
    if str(buttonname) == '':
        canSubmit = False
    
    #verify the phone number
    buttonphone = phoneEntry.get()
    if validPhoneNumber(str(buttonphone)) == False:
        #print(validPhoneNumber(str(buttonphone)))
        canSubmit = False
        
    #else:
        #print(validPhoneNumber(str(buttonphone)))
    
    #verify email
    buttonemail = emailAdd.get()
    if validEmail(str(buttonemail)) == False:
        #print(validEmail(str(buttonemail)))
        canSubmit = False
    #else:
        #print(validEmail(str(buttonemail)))
    
    #verify a vaccine manufacturer 
    
    manuString = ''
    
    buttonvax = vaccine.get()
    if str(buttonvax) == 'Choose Here': 
        manuString = 'None'
        canSubmit = False
    elif str(buttonvax) == 'Pfizer':
        manuString = 'Pfizer'
    elif str(buttonvax) == 'Moderna':
        manuString = 'Moderna'
    elif str(buttonvax) == 'Johnson & Johnson':
        manuString = 'Johnson & Johnson'
        
    #which number vax 
    
    numberVax = ''
    
    buttonwhich = num.get()
   
    if str(buttonwhich) == 'Choose Here':
        numberVax = 'None'
        canSubmit = False
    elif str(buttonwhich) == 'first':
        numberVax = 'first'
    elif str(buttonwhich) == 'second':
        numberVax = 'second'
    elif str(buttonwhich) == 'booster':
        numberVax = 'booster' 
    
    #build the string for reactions
    symptoms = ''
    #might need a counter to get rid of the last semicolon 
    if pain.get() == 1:
        symptoms = symptoms + 'Pain at injection site'  
    if armPain.get() == 1:
        if symptoms == '':
            symptoms = symptoms + 'Pain down arm'
        else:
            symptoms = symptoms + '; Pain down arm'
        
        
    if fever.get() == 1: 
        if symptoms == '':
            symptoms = symptoms + 'Fever'
        else:
            symptoms = symptoms + '; Fever'        
    if headache.get() == 1:
        if symptoms == '':
            symptoms = symptoms + 'Headache'
        else:
            symptoms = symptoms + '; Headache'
    if nausea.get() == 1:
        if symptoms == '':
            symptoms = symptoms + 'Nausea'
        else:
            symptoms = symptoms + '; Nausea'        
    if rash.get() == 1:
        if symptoms == '':
            symptoms = symptoms + 'Rash'
        else:
            symptoms = symptoms + '; Rash'
    if hives.get() ==1:
        if symptoms == '':
            symptoms = symptoms + 'Hives'
        else:
            symptoms = symptoms + '; Hives'
    if swell.get() ==1:
        if symptoms == '':
            symptoms = symptoms + 'Swelling'
        else:
            symptoms = symptoms + '; Swelling'        
    if chills.get() ==1:
        if symptoms == '':
            symptoms = symptoms + 'Chills'
        else:
            symptoms = symptoms + '; Chills'
    if bodyache.get() == 1:
        if symptoms == '':
            symptoms = symptoms + 'Body ache'
        else:
            symptoms = symptoms + '; Body ache'
    if none.get() == 1:
        symptoms = symptoms + 'None'
        if symptoms != 'None':
            canSubmit = False
    if symptoms == '':
        canSubmit = False
    
    #print(canSubmit)
    
    #if all checks pass, open the file to append 
    if canSubmit == True:
        
        file = open('ShotReactions.txt','a')
        #GET ALL THE DATA
        namefile = userName.get()
        phonefile = phoneNum.get()
        emailfile = emailAdd.get()

        #writing the stuff to the file 
        file.write(str(namefile)+'\n')
        file.write(str(phonefile)+'\n')
        file.write(str(emailfile)+'\n')
        file.write((manuString) + '\n')
        file.write((numberVax) + '\n')
        file.write((symptoms) + '\n')
        
        #close the file 
        file.close() 
        
        #reset all the widgets 
        userName.set('')
        phoneNum.set('')
        emailAdd.set('')
        #userName.set('Type Name Here')
        #phoneNum.set('Type Phone Number Here')
        #emailAdd.set('Type Email Address Here')        
        
        vaccine.set('Choose Here') 
        num.set('Choose Here')        
        #vaccine.set('Which Vaccine Did You Receive?') 
        #num.set('First, Second, or Booster Vaccine?')
        
        pain.set(0)
        armPain.set(0)
        fever.set(0)
        headache.set(0)
        nausea.set(0)
        rash.set(0)
        hives.set(0)
        swell.set(0)
        chills.set(0)
        bodyache.set(0)
        none.set(0)
        
        #thankyou message
        #feedback = StringVar()
        feedback.set('Thank you for your submission.')
        #feedbackLabel = Label(root, textvariable=feedback)
        #feedbackLabel.place(x=100,y=600)
        
        submit['state'] = DISABLED
        
        needinfo.set('')
        #needinfoLabel = Label(root, textvariable=needinfo)
        #needinfoLabel.place(x=150,y=400)     
        
        infosubmit.set('Information Submitted.')
        
    else:
        #needinfo = Label(root, text='All information must be provided.', width=25, font=('bold', 15))
        needinfo.set('All information must be provided.')
        #needinfoLabel = Label(root, textvariable=needinfo)
        #needinfoLabel.place(x=150,y=400)         
    
    return

#start/clear button 92/100
def startPressed():
    
    global feedback
    global feedbackLabel
    global needinfo
    global infosubmit
    
    #clear any info in the window
    
    #clear the name, number, email, and gratitide label
    userName.set('')
    phoneNum.set('')
    emailAdd.set('')
    #userName.set('Type Name Here')
    #phoneNum.set('Type Phone Number Here')
    #emailAdd.set('Type Email Address Here')    
    
    #clears the check boxes, manufacturer section, and which vaccine it was 
    vaccine.set('Choose Here') 
    num.set('Choose Here')
    
    feedback.set('')
    #vaccine.set('Which Vaccine Did You Receive?') 
    #num.set('First, Second, or Booster Vaccine?') 
    
    feedback.set('')
    #feedbackLabel = Label(root, textvariable=feedback)
    
    needinfo.set('')
    
    infosubmit.set('')
    
    #feedbackLabel.place(x=100,y=400)    
    
    pain.set(0)
    armPain.set(0)
    fever.set(0)
    headache.set(0)
    nausea.set(0)
    rash.set(0)
    hives.set(0)
    swell.set(0)
    chills.set(0)
    bodyache.set(0)
    none.set(0)
    
    submit['state'] = NORMAL
    
    pass

#place the button, on the left of the screen 96/100 
startclear = Button(root, text='Start/Clear', width=10, bg='white', fg='black', command=startPressed)
startclear.place(x=70,y=700)
    
#submit button 100/100
submit = Button(root, text='Submit', width=10, bg='white', fg='black', command=submitPressed)
submit.place(x=400,y=700)
    
root.mainloop()