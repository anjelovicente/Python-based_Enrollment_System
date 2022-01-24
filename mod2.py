# CABATO, M., REGACHO, R., VICENTE, J.

def initial(chosen, inchosen):
   req = int(input("Consider Last Term?\t 1 - Yes | 2 - No\n"))
   if req == 1:
       filename = input("Enter Initial Student Document: \n")
       filename = filename+".txt"
       file = open(filename.upper(), "r")
       datafile = file.readlines()
       found = False
       for line in datafile:
           if "LBYEC2B" in line:
               found = True
               if True:
                   chosen.append(1)
                   inchosen.append(1)
               else:
                   found = False
           if "COEDISC" in line:
               found = True
               if True:
                   chosen.append(2)
               else:
                   found = False
           if "LBYCH1A" in line:
               found = True
               if True:
                   chosen.append(3)
               else:
                   found = False
           if "LBYEC2A" in line:
               found = True
               if True:
                   chosen.append(4)
                   inchosen.append(4)
               else:
                   found = False
           if "LCLSONE" in line:
               found = True
               if True:
                   chosen.append(5)
               else:
                   found = False
           if "LBYPH1A" in line:
               found = True
               if True:
                   chosen.append(6)
               else:
                   found = False
           if "GEFTWEL" in line:
               found = True
               if True:
                   chosen.append(7)
               else:
                   found = False
           if "PROLOGI" in line:
               found = True
               if True:
                   chosen.append(8)
               else:
                   found = False
           if "GEDANCE" in line:
               found = True
               if True:
                   chosen.append(9)
               else:
                   found = False
           if "LBYCPA1" in line:
               found = True
               if True:
                   chosen.append(10)
               else:
                   found = False
           if "LBYCPE1" in line:
               found = True
               if True:
                   chosen.append(11)
               else:
                   found = False
           if "BASCHEM" in line:
               found = True
               if True:
                   chosen.append(12)
                   inchosen.append(12)
               else:
                   found = False
           if "BASPHYS" in line:
               found = True
               if True:
                   chosen.append(13)
                   inchosen.append(13)
               else:
                   found = False
           if "FNDSTAT" in line:
               found = True
               if True:
                   chosen.append(14)
               else:
                   found = False
           if "CALENG1" in line:
               found = True
               if True:
                   chosen.append(15)
                   inchosen.append(15)
               else:
                   found = False
           if "ENGCHEM" in line:
               found = True
               if True:
                   chosen.append(16)
                   inchosen.append(16)
               else:
                   found = False
           if "GEMATMW" in line:
               found = True
               if True:
                   chosen.append(17)
               else:
                   found = False
           if "NSTPLT1" in line:
               found = True
               if True:
                   chosen.append(18)
                   inchosen.append(18)
               else:
                   found = False
           if "NSTPLTS2" in line:
               found = True
               if True:
                   chosen.append(19)
                   inchosen.append(19)
               else:
                   found = False
           if "GEFILI1" in line:
               found = True
               if True:
                   chosen.append(20)
               else:
                   found = False
           if "ENGPHYS" in line:
               found = True
               if True:
                   chosen.append(21)
                   inchosen.append(21)
               else:
                   found = False
           if "CALENG2" in line:
               found = True
               if True:
                   chosen.append(22)
                   inchosen.append(22)
               else:
                   found = False
           if "ENGDATA" in line:
               found = True
               if True:
                   chosen.append(23)
               else:
                   found = False
           if "FNDMATH" in line:
               found = True
               if True:
                   chosen.append(24)
                   inchosen.append(24)
               else:
                   found = False
           if "LASARE1" in line:
               found = True
               if True:
                   chosen.append(25)
               else:
                   found = False
           if "SAS1000" in line:
               found = True
               if True:
                   chosen.append(26)
               else:
                   found = False
       print("\n")
   elif req == 2:
       print("\n")
   return


def prereq(off_limits, inchosen, chosen):
   if 1 in inchosen:
       off_limits.append(4)
   if 4 in inchosen:
       off_limits.append(1)
   if 12 in inchosen:
       off_limits.append(16)
   if 16 in inchosen:
       off_limits.append(12)
   if 18 in inchosen:
       off_limits.append(19)
   if 19 in inchosen:
       off_limits.append(18)
   if 13 in inchosen:
       off_limits.append(21)
   if 21 in inchosen:
       off_limits.append(13)
   if 15 in inchosen:
       off_limits.append(22)
       off_limits.append(24)
   if 22 in inchosen:
       off_limits.append(15)
       off_limits.append(24)
   if 24 in inchosen:
       off_limits.append(15)
       off_limits.append(22)
   if 4 in inchosen and chosen:
       off_limits.remove(1)
   if 12 in inchosen and chosen:
       off_limits.remove(16)
   if 18 in inchosen and chosen:
       off_limits.remove(19)
   if 13 in inchosen and chosen:
       off_limits.remove(21)
   if 24 in inchosen and chosen:
       off_limits.remove(15)
   if 15 in inchosen and chosen:
       off_limits.remove(22)

   return


def norm_checker(irreg, off_limits):
   if irreg == 1:
       off_limits.append(4)
   if irreg == 4:
       off_limits.append(1)
   if irreg == 12:
       off_limits.append(16)
   if irreg == 16:
       off_limits.append(12)
   if irreg == 18:
       off_limits.append(19)
   if irreg == 19:
       off_limits.append(18)
   if irreg == 13:
       off_limits.append(21)
   if irreg == 21:
       off_limits.append(13)
   if irreg == 15:
       off_limits.append(22)
       off_limits.append(24)
   if irreg == 22:
       off_limits.append(15)
       off_limits.append(24)
   if irreg == 24:
       off_limits.append(15)
       off_limits.append(22)
   return

def rem_checker(irreg, off_limits):
   if irreg == 1:
       off_limits.remove(4)
   if irreg == 4:
       off_limits.remove(1)
   if irreg == 12:
       off_limits.remove(16)
   if irreg == 16:
       off_limits.remove(12)
   if irreg == 18:
       off_limits.remove(19)
   if irreg == 19:
       off_limits.remove(18)
   if irreg == 13:
       off_limits.remove(21)
   if irreg == 21:
       off_limits.remove(13)
   if irreg == 15:
       off_limits.remove(22)
       off_limits.remove(24)
   if irreg == 22:
       off_limits.remove(15)
       off_limits.remove(24)
   if irreg == 24:
       off_limits.remove(15)
       off_limits.remove(22)
   return