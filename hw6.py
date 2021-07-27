'''
Author: Christina Elmore
RIN: 661542904
Section: 02
Assignment: Homework 6
Purpose: Given a file containing information about Dr. Who villans, find the 10 most popular villans, finds the villan corresponding to the inputted number and display its information.
'''
import sys

def extract_info(line): #extracts the needed data from each line from the file and returns it as a list
    list_info = line.split('\t')
    num_shows = len(list_info[7].split(','))
    name = list_info[0]
    
    list_shows = list_info[7].split(',')
    i = 0
    while i < len(list_shows):
        list_shows[i] = list_shows[i].strip()
        i += 1
    set_shows = set(list_shows)
    
    list_docs = list_info[4].split(',')
    i = 0
    while i < len(list_docs):
        list_docs[i] = list_docs[i].strip()
        i += 1
    set_docs = set(list_docs) 
    
    return [num_shows, name, set_shows, set_docs]

def display_vill(): #displays the top ten list of villans and asks for user's input
    print ""
    i = 0
    while i < 10:
        print "%d. %s" %(i + 1, list_vill_info[i][1])
        i += 1   
    print ""    
    print "Please enter a number between 1 and 10, or -1 to end"
    villain = raw_input("Enter a villain ==> ")
    print villain
    if ' ' in villain:
        return None
    i = 0
    while i < len(villain):
        if villain[i].isalpha() == True:
            return None
        i += 1    
    return int(villain)

def vill_info(num): #prints out number of stories villian was in, which villians appeared with them, which stories had just that villain, and which doctors they were involved with
    villain = list_vill_info[num]
    stories = villain[2]
    
    #find villians who appear with given villain
    other_vills = []
    i = 0
    while i < len(list_vill_info):
        if len(stories & list_vill_info[i][2]) > 0:
            if list_vill_info[i][1] not in other_vills and list_vill_info[i][1] != villain[1]:
                other_vills.append(list_vill_info[i][1])
        i += 1
    i = 0
    while i < len(other_vills):
        other_vills[i] = other_vills[i].strip()
        if '&' in other_vills[i]:
            fixed = other_vills[i].split('&')
            other_vills[i] = fixed[0]
        i += 1
    other_vills.sort()
    
    #find stories featuring only the given villain
    i = 0
    while i < len(list_vill_info):
        if len(stories - list_vill_info[i][2]) > 0:
            stories = stories - list_vill_info[i][2]
        i += 1
    stories = list(stories)
    stories.sort()
    
    #find doctors involved with given villian
    doctors = list(villain[3])
    doctors.sort()
    
    #prints information on villain
    print ""
    print "%s in %d stories, with the following other villains:" %(villain[1], len(villain[2]))
    print "="*50
    i = 0
    while i < len(other_vills):
        print "%d. %s" %( i + 1, other_vills[i])
        i += 1
    print ''
    if len(stories) == 0:
        print "There are no stories with only this villain"
        print "="*50
    else:
        print "The stories that only features %s are:" %(villain[1])
        print "="*50

        i = 0
        while i < len(stories):
            print "%d. %s" %( i + 1, list(stories)[i])
            i += 1    
    print ""
    print "This villain was foiled by %d doctor(s):" %(len(doctors))
    print "="*50
    i = 0
    while i < len(doctors):
        print "%d. %s" %( i + 1, doctors[i])
        i += 1 

if __name__ == '__main__':
    f = open('DrWhoVillains.tsv')
    all_info = f.read()
    list_all_info = all_info.split('\n')
    
    #creates list of lists for all the info
    list_vill_info = []
    for line in list_all_info:
        if line == '':
            break       
        line_info = extract_info(line)
        list_vill_info.append(line_info)
           
    list_vill_info.pop(0)
    list_vill_info.sort(reverse=True)
    
    #Display top 10 villans 
    villain_num = display_vill()
    
    #asks for user input and fufills request until user enters -1
    while villain_num != -1:
        if villain_num == None or villain_num not in range(1,11,1):
            villain_num = display_vill()
        if villain_num in range(1,11,1):
            vill_info(villain_num-1)
            villain_num = display_vill()
    print "Exiting"
    sys.exit()
        
    