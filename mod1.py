from mod2 import *

def amount(tuition,sf,dev,adol,labfee,nstp,iD,other,misc,sched):
 layout3 = "{0:>0}{1:<0}{2:>20}"
 if len(sched) == 0:
     misc = 0
     dev = 0
     adol = 0
     iD = 0
     other = 0
 print(layout3.format("", "\nTuition\t\t\t\t", format(tuition, '.2f')))
 print(layout3.format("", "Miscellaneous\t\t", format(misc, '.2f')))
 print(layout3.format("", "Special Fees\t\t", format(sf, '.2f')))
 print(layout3.format("", "Development Fees\t", format(dev, '.2f')))
 print(layout3.format("", "Adolescent Pers Test", format(adol, '.2f')))
 print(layout3.format("", "Laboratory Fees\t\t", format(labfee, '.2f')))
 print(layout3.format("", "NSTP/ROTC Fee\t\t", format(nstp, '.2f')))
 print(layout3.format("", "ID Validation\t\t", format(iD, '.2f')))
 print(layout3.format("", "Other Fees\t\t\t", format(other, '.2f')))
 total = tuition + misc + sf + dev + adol + labfee + nstp + iD + other
 print("\n-------------------------------------------")
 print(layout3.format("", "Overall Balance\t\t", format(total, '.2f')))
 return

def regular(file_name):
 term = int(input("Term 1 / 2 / 3:\t"))
 print("\n")
 if term == 1:
     fp = open("regsched1.txt", "r")
     subj = fp.read()
     print(subj)
     filenames = ["Student Data.txt", "regsched1.txt"]
     with open(file_name, "w") as newfile:
         for files in filenames:
             with open(files) as allfiles:
                 newfile.write(allfiles.read())
 elif term == 2:
     fp = open("regsched2.txt", "r")
     subj = fp.read()
     print(subj)
     filenames = ["Student Data.txt", "regsched2.txt"]
     with open(file_name, "w") as newfile:
         for files in filenames:
             with open(files) as allfiles:
                 newfile.write(allfiles.read())
 elif term == 3:
     fp = open("regsched3.txt", "r")
     subj = fp.read()
     print(subj)
     filenames = ["Student Data.txt", "regsched3.txt"]
     with open(file_name, "w") as newfile:
         for files in filenames:
             with open(files) as allfiles:
                 newfile.write(allfiles.read())
 return

def irregular(chosen,cls,sched,layout1,layout3, off_limits, inchosen, file_name):
 menu = open("irregsmenu.txt", "r")
 lines = menu.readlines()
 for i in lines:
     print(i, end="")
 menu.close()
 fp = open("irregsched.txt", "w")
 fp.write(lines[0])
 print("\nType the number of the chosen course:\t\t Type[0] to finalize\n")

 tuition = 0
 labfee = 0
 misc = 6782
 sf = 0
 dev = 50
 adol = 500
 nstp = 0
 iD = 46
 other = 16
 unit = 0

 while True:
     irreg = input("\nSelect a Subject: ")
     cls()
     print("\n")
     try:
         irreg = int(irreg)
         if 0 < irreg < 27:
             prereq(off_limits, inchosen, chosen)
             if irreg in chosen:
                 print("Subject already taken")
             elif irreg in off_limits:
                 print("Subject Cannot Be Taken")
             elif irreg not in off_limits:
                 norm_checker(irreg, off_limits)
                 if irreg <= 6:
                     tuition = tuition + 3400
                     sched.append(lines[irreg])
                     chosen.append(irreg)
                     unit = unit + 1
                     if irreg == 1 or irreg == 3 or irreg == 4 or irreg == 6 or irreg == 7:
                         labfee = labfee + 3600
                 elif irreg >= 25:
                     tuition = tuition + 3400
                     sched.append(lines[irreg])
                     chosen.append(irreg)
                 elif irreg >= 7 and irreg <= 11:
                     tuition = tuition + 6800
                     sched.append(lines[irreg])
                     chosen.append(irreg)
                     unit = unit + 2
                     if irreg == 10 or irreg == 11:
                         labfee = labfee + 3600
                 elif irreg >= 12 and irreg <= 23:
                     tuition = tuition + 10200
                     sched.append(lines[irreg])
                     chosen.append(irreg)
                     unit = unit + 3
                     if irreg == 18 or irreg == 19:
                         nstp = nstp + 5100
                 elif irreg == 24:
                     sched.append(lines[irreg])
                     chosen.append(irreg)
                     unit = unit + 5
                     tuition = tuition + 17000
             print(layout1.format("", "Courses Taken", "\n"))
             for i in sched:
                 print(i, end="")
             print("\nTotal Units: \t\t", unit)
             print("---------------------------------------------------------------------------------------------------------")
             print(layout1.format("", "Available Courses", "\n"))
             for i in lines:
                 if i not in sched:
                     print(i, end="")
             print("\n\n")
         elif irreg >= 28:
             print("Input Error\n")
             print(layout1.format("", "Courses Taken", "\n"))
             for i in sched:
                 print(i, end="")
             print("\nTotal Units: \t\t", unit)
             print(
                 "---------------------------------------------------------------------------------------------------------")
             print(layout1.format("", "Available Courses", "\n"))
             for i in lines:
                 if i not in sched:
                     print(i, end="")
             print("\n\n")
         elif irreg == 0:
             amount(tuition, sf, dev, adol, labfee, nstp, iD, other, misc,sched)
             for i in sched:
                 fp.write(i)
             if len(sched) == 0:
                 misc = 0
                 dev = 0
                 adol = 0
                 iD = 0
                 other = 0
             fp.write(layout3.format("\n", "Total Units: \t", format(unit, ".2f")))
             fp.write("\n- - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -")
             fp.write("\n")
             fp.write(layout3.format("", "\nTuition\t\t\t\t", format(tuition, '.2f')))
             fp.write(layout3.format("", "\nMiscellaneous\t\t", format(misc, '.2f')))
             fp.write(layout3.format("", "\nSpecial Fees\t\t", format(sf, '.2f')))
             fp.write(layout3.format("", "\nDevelopment Fees\t", format(dev, '.2f')))
             fp.write(layout3.format("", "\nAdolescent Pers Test", format(adol, '.2f')))
             fp.write(layout3.format("", "\nLaboratory Fees\t\t", format(labfee, '.2f')))
             fp.write(layout3.format("", "\nNSTP/ROTC Fee\t\t", format(nstp, '.2f')))
             fp.write(layout3.format("", "\nID Validation\t\t", format(iD, '.2f')))
             fp.write(layout3.format("", "\nOther Fees\t\t\t", format(other, '.2f')))
             total = tuition + misc + sf + dev + adol + labfee + nstp + iD + other
             fp.write("\n-------------------------------------------")
             fp.write(layout3.format("", "\nOverall Balance\t\t", format(total, '.2f'), ))
             fp.close()
             filenames = ["Student Data.txt", "irregsched.txt"]
             with open(file_name, "w") as newfile:
                 for files in filenames:
                     with open(files) as allfiles:
                         newfile.write(allfiles.read())
             break
         elif irreg == 27:
             print("\n[REMOVE MENU]:")
             for i in sched:
                 print(i, end="")
             print("\nTotal Units: \t\t", unit)
             irreg = int(input(
                 "\nWhat subject would you like to remove? \t\t\t\t Type[0] to return to Schedule Selection \n"))
             while True:
                 cls()
                 remove = lines[irreg]
                 print("\n[REMOVE MENU]:")
                 if remove in sched:
                     rem_checker(irreg, off_limits)
                     sched.remove(remove)
                     chosen.remove(irreg)
                     if irreg <= 6:
                         tuition = tuition - 3400
                         unit = unit - 1
                         if irreg == 1 or irreg == 3 or irreg == 4 or irreg == 6 or irreg == 7:
                             labfee = labfee - 3600
                     elif irreg >= 26:
                         tuition = tuition - 3400
                     elif 7 <= irreg <= 11:
                         tuition = tuition - 6800
                         unit = unit - 2
                         if irreg == 10 or irreg == 11:
                             labfee = labfee - 3600
                     elif 12 <= irreg <= 23:
                         tuition = tuition - 10200
                         unit = unit - 3
                         if irreg == 18 or irreg == 19:
                             nstp = nstp - 5100
                     elif irreg == 24:
                         tuition = tuition - 17000
                         unit = unit - 5
                 elif irreg == 0:
                     cls()
                     print(layout1.format("", "Courses Taken", "\n"))
                     for i in sched:
                         print(i, end="")
                     print("\nTotal Units: \t\t", unit)
                     print(
                         "---------------------------------------------------------------------------------------------------------")
                     print(layout1.format("", "Available Courses", "\n"))
                     for i in lines:
                         if i not in sched:
                             print(i, end="")
                     break
                 else:
                     print("Course not Selected")
                 for i in sched:
                     print(i, end="")
                 print("\nTotal Units: \t\t", unit)
                 print(
                     "---------------------------------------------------------------------------------------------------------")
                 irreg = int(
                     input(
                         "\nWhat subject would you like to remove? \t\t\t\t Type[0] to return to Schedule Selection \n"))
         print(
             "Type the number of the chosen course:\t\t Type[0] to finalize\t\t  Press Enter to view estimated cost\t\t Type[27] to remove courses\n")

     except:
         irreg = str(irreg)
         if irreg == "":
             amount(tuition, sf, dev, adol, labfee, nstp, iD, other, misc,sched)
             print(
                 "\nPress Enter to return to Schedule Selection\n")
             irreg = input("\n")
             cls()
             if irreg == "":
                 print(layout1.format("", "Courses Taken", "\n"))
                 for i in sched:
                     print(i, end="")
                 print("\nTotal Units: \t\t", unit)
                 print(
                     "---------------------------------------------------------------------------------------------------------")
                 print(layout1.format("", "Available Courses", "\n"))
                 for i in lines:
                     if i not in sched:
                         print(i, end="")
                 print("Type the number of the chosen course:\t\t Type[0] to finalize\t\t  Press Enter to view estimated cost\t\t Type[27] to remove courses\n")

 return
