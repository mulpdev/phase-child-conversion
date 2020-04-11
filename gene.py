#!/usr/bin/python

import sys

def pad_integer (num, width):
    num = str(num)
    for i in range(len(num), width): #might have set i outside of loop
        sys.stdout.write(" ")

#LOC 16#
def report_SNP (chr_id, chr_number, SNP_position, genotypeA, genotypeB, genotypeC, rsidA, FFvs23):
    if ((chr_number < 10) or (chr_number == 23)):
        sys.stdout.write(" ")

    sys.stdout.write(chr_id)
    comma()
    sys.stdout.write("  ")
    sys.stdout.write(rsidA)
    comma()

    sps = 15-len(rsidA);
    while (sps > 0):
        sys.stdout.write(" ")
        sps=sps-1

    pad_integer(SNP_position, 9)
    print FFvs23
    return
    if (FFvs23 > 0):
        sys.stdout.write("<a href=\"https://www.23andme.com/you/explorer/chr/?chr=")

        if (chr_number < 23):
            sys.stdout.write(chr_number)
        elif (chr_number == 23):
            sys.stdout.write("X")
        elif (chr_number == 24):
            sys.stdout.write("Y")
        elif (chr_number == 25):
            sys.stdout.write("MT")

        tmpout = "%s%d%s" %("&pos_start=", SNP_position, "\" target=\"_new\">")
        sys.stdout.write(tmpout)
        

        sys.stdout.write(SNP_position)

        if (FFvs23 > 0):
            print"</a>"
        comma()
        sys.stdout.write("      ")

        if (len(genotypeB) == 1):
            sys.stdout.write(" ")
        sys.stdout.write(genotypeB)
        comma()
        sys.stdout.write("     ")

        if (len(genotypeA) == 1):
            sys.stdout.write(" ")
        sys.stdout.write(genotypeA)
        comma()
        sys.stdout.write("     ")

        if (len(genotypeC) == 1):
            sys.stdout.write(" ")
        sys.stdout.write(genotypeC)
        comma()
        sys.stdout.write("     ")

        sys.stdout.write("    ")
        print_phased_SNP (chr_number,genotypeA,genotypeB,genotypeC)
        sys.stdout.write("\n\nOOOOOOGABOOOOOOOOGA\n")

#LOC 93#
def comma ():
    #'no literal translation of this function#
    sys.stdout.write(", ")

def print_phased_SNP (chr_number, genotypeA, genotypeB, genotypeC):
    mat = ' '
    pat = ' '
    mat_comp = ' '
    pat_comp = ' '
    annotation = ''

    if (is_discordant_SNP (chr_number, genotypeA, genotypeB, genotypeC)):
        pat = "?"
        mat = "?"
        pat_comp = "?"
        mat_comp = "?"
        annotation = "discordant"

    elif ((genotypeA == "??") or (genotypeB == "??") or (genotypeC == "??")):
        annotation = "No-Call"

        if ((len(genotypeA) == 2) and (len(genotypeB) == 2) and (len(genotypeC) == 2)):
            if ((genotypeC != "??") and (genotypeC[0] == genotypeC[1])):
                pat = genotypeC[0]
                mat = genotypeC[1]

            elif ((genotypeC != "??") and (genotypeA != "??") and (genotypeA[0] == genotypeA[1])):
                if (genotypeA[0] == genotypeC[0]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0]

            elif ((genotypeC != "??") and (genotypeB != "??") and (genotypeB[0] == genotypeB[1])):
                if (genotypeB[0] == genotypeC[1]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0] #loc 130

            elif ((genotypeC != "??") and (genotypeB != "??") and (genotypeB[0] == genotypeB[1])):
                if (genotypeB[0] == genotypeC[1]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0] #loc 142

            elif ((genotypeC != "??") and (genotypeA != "??") and (genotypeA != genotypeC)):
                if (genotypeA[0] == genotypeC[0]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0] #155#

            elif ((genotypeC != "??") and (genotypeB != "??") and (genotypeB != genotypeC)):
                if (genotypeB[0] == genotypeC[1]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0] #168#

            elif ((genotypeC == "??") and (genotypeA != "??") and (genotypeB != "??")):
                if (genotypeA[0] == genotypeA[1]):
                    pat = genotypeA[0]
                else:
                    pat = "?"

                if (genotypeB[0] == genotypeB[1]):
                    mat = genotypeB[0]
                else:
                    mat = "?" #187#

            elif ((genotypeC == "??") and (genotypeA != "??") and (genotypeB == "??")):
                if (genotypeA[0] == genotypeA[1]):
                    pat = genotypeA[0]
                    mat = "?"

                else:
                    pat = "?"
                    mat = "?" #202#

            elif ((genotypeC == "??") and (genotypeA == "??") and (genotypeB != "??")):
                if (genotypeB[0] == genotypeB[1]):
                    pat = "?"
                    mat = genotypeB[0]
                else:
                    pat = "?"
                    mat = "?"
            else:
                pat = "?"
                mat = "?" #loc219#

        elif ((chr_number == 23) and (genotypeC == "??")):
            if (genotypeB[0] == genotypeB[1]):
                pat = "?"
                mat = genotypeB[0]
            else:
                pat = "?"
                mat = "?" #234#

        elif ((chr_number == 23) and (len(genotypeC) == 1)):
             mat = genotypeC[0]

        else:
            pat = "?"
            mat = "?"  #loc242#

    else: #// all three SNPs have values
        if ((len(genotypeA) == 2) and (len(genotypeB) == 2) and (len(genotypeC) == 2)):
            if (genotypeC[0] == genotypeC[1]):
                pat = genotypeC[0]
                mat = genotypeC[1]


            elif (genotypeA[0] == genotypeA[1]):                 
                if (genotypeA[0] == genotypeC[0]):                
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                
                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0]
                
             
            elif (genotypeB[0] == genotypeB[1]):                 
                if (genotypeB[0] == genotypeC[1]):                
                    pat = genotypeC[0]
                    mat = genotypeC[1]
                
                else:                
                    pat = genotypeC[1]
                    mat = genotypeC[0]
                
             
            elif (genotypeA != genotypeC):
                if (genotypeA[0] == genotypeC[0]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]

                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0]
                
             
            elif (genotypeB != genotypeC):
                if (genotypeB[0] == genotypeC[1]):
                    pat = genotypeC[0]
                    mat = genotypeC[1]

                else:
                    pat = genotypeC[1]
                    mat = genotypeC[0]            
             
            else: #// the child is heterozygous and identical to both parents
                pat = "?"
                mat = "?"
                annotation = "indeterminate"         
     
        elif ((len(genotypeA) == 1) and (len(genotypeB) == 2) and (len(genotypeC) == 2)):             
            #// this is probably a female's X
            if (genotypeA[0] == genotypeC[0]):                
                pat = genotypeC[0]
                mat = genotypeC[1]

            else:
                pat = genotypeC[1]
                mat = genotypeC[0]

            if (chr_number != 23):                
                annotation = "something is odd ... X Chromosome was anticipated"


        elif ((len(genotypeB) == 2) and (len(genotypeC) == 1)):             
            #// this is probably a male's X
            mat = genotypeC[0]

            if (chr_number != 23):            
                annotation = "something is odd ... X Chromosome was expected"

        else:        
            annotation = "XXX this needs attention" #loc 344#


    sys.stdout.write("%s, %s" %(mat, pat))

    if (len(annotation) > 19):
        sys.stdout.write("%s\nTerminating.\n" %(annotation))
        return(0)  

    sps = 19-len(annotation)
    tmp =  " " * sps
    sys.stdout.write("%s%s," %(tmp, annotation))

    if (pat_comp != "?"):
     pat_comp = get_comp (genotypeA, pat)

    if (mat_comp != "?"):
     mat_comp = get_comp (genotypeB, mat)

    sys.stdout.write("     %s!  %s" %(mat_comp, pat_comp))


#LOC 383#
def get_comp (genotype, allele):
    result = 'declared'

    if (len(genotype) == 2):
        if (allele == '?'):
            if (genotype[0] == genotype[1]):
                result = genotype[0]
            else:
                result = '?'
        elif (genotype[0] == allele):
            result = genotype[1]
        else:
            result = genotype[0]
    else:
        if (genotype == allele):
            result = ' '
        elif (allele != '?'):
            result = genotype
        else:
            result = '?'
    
    return result


def is_discordant_SNP (chr_number, genotypeA, genotypeB, genotypeC):
    retcode = 0

    if ((chr_number != 23) or (len(genotypeC) == 2)): #// either not X, or else a female X
        if (is_SNP_mutated (genotypeA, genotypeC)):  #i hope python uses 1 for true and 0 for false#
            retcode = 1

    if (retcode == 0):
        if (is_SNP_mutated (genotypeB, genotypeC)):
            retcode = 1

    if (retcode == 0):
        if ((genotypeA != '??') and (genotypeB != '??') and (genotypeC != '??')):
            if ((len(genotypeA) == 2) and (len(genotypeC) == 2) and (len(genotypeC) == 2)):        
                retcode = 1
                if ((is_allele_in_SNP (genotypeC[0], genotypeA)) and (is_allele_in_SNP (genotypeC[1], genotypeB))):
                    retcode = 0
                if ((is_allele_in_SNP (genotypeC[0], genotypeB)) and (is_allele_in_SNP (genotypeC[1], genotypeA))):
                    retcode = 0

    return retcode

def is_allele_in_SNP(allele, SNP):
    result = 0
    if ((SNP[0] == allele) or (SNP[1] == allele)):
        result = 1
    return result

def is_SNP_mutated(genotypeA, genotypeB):
    retcode = 0
    if (genotypeA == genotypeB):
        pass
    elif ((genotypeA == '??') or (genotypeB == '??')):
        pass
    elif ((len(genotypeA) == 1) and (len(genotypeB) == 1)):
        retcode = 1
    elif ((len(genotypeA) == 1) and (len(genotypeB) == 2)):
        if (genotypeA[0] == genotypeB[0]):
            pass
        elif (genotypeA[0] == genotypeB[1]):
            pass
        else:
            retcode = 1
    elif ((len(genotypeA) == 2) and (len(genotypeB) == 1)):
        if (genotypeB[0] == genotypeA[0]):
            pass
        elif (genotypeB[0] == genotypeA[1]):
            pass
        else:
            retcode = 1
    else:
        if (genotypeA[0] == genotypeB[0]):
            pass
        elif (genotypeA[0] == genotypeB[1]):
            pass
        elif (genotypeA[1] == genotypeB[0]):
            pass
        elif (genotypeA[1] == genotypeB[1]):
            pass
        else:
            retcode = 1

    return retcode




def which_file_to_skip (chr_id, chr_idB, chr_idC, SNP_position, SNP_positionB, SNP_positionC):
    file_to_read = 'declared'
    curr_chr_number = 'declared'
    curr_chr_numberB = 'declared'
    curr_chr_numberC = 'declared'        
    #// parent.bottom.document.write(SNP_position + "  " + SNP_positionB + "  " + SNP_positionC +"\n")
    if chr_id == 'MT':
        curr_chr_number = 25
    elif chr_id == 'X':
        curr_chr_number = 23
    elif chr_id == 'Y':
        curr_chr_number == 24
    else:
        curr_chr_number = int(chr_id)

    if chr_idB == 'MT':
        curr_chr_numberB = 25
    elif chr_idB == 'X':
        curr_chr_numberB = 23
    elif chr_idB == 'Y':
        curr_chr_numberB == 24
    else:
        curr_chr_numberB = int(chr_idB)

    if chr_idC == 'MT':
        curr_chr_numberC = 25
    elif chr_idC == 'X':
        curr_chr_numberC = 23
    elif chr_idC == 'Y':
        curr_chr_numberC == 24
    else:
        curr_chr_numberC = int(chr_idC)

    if (curr_chr_number < curr_chr_numberB):
        file_to_read = 1
    elif (curr_chr_number < curr_chr_numberC):
        file_to_read = 1
    elif (curr_chr_numberB < curr_chr_number):
        file_to_read = 2
    elif (curr_chr_numberB < curr_chr_numberC):
        file_to_read = 2
    elif (curr_chr_numberC < curr_chr_number):
        file_to_read = 3
    elif (curr_chr_numberC < curr_chr_numberB):
        file_to_read = 3
    else: # all three are for the same Chromosome
        if (int(SNP_position) < int(SNP_positionB)):
            file_to_read = 1
        elif (int(SNP_position) < int(SNP_positionC)):
            file_to_read = 1
        elif (int(SNP_positionB) < int(SNP_position)):
            file_to_read = 2
        elif (int(SNP_positionB) < int(SNP_positionC)):
            file_to_read = 2
        elif (int(SNP_positionC) < int(SNP_position)):
            file_to_read = 3
        else:
            file_to_read = 3 

    return file_to_read


#ProcessFilesFirefox
#this is the equivilent of main()
if len(sys.argv) < 5:
    sys.stdout.write("usage: .py F M C chr\n")
    sys.exit(-1)

fnameA = sys.argv[1] #father
fnameB = sys.argv[2] #mother
fnameC= sys.argv[3] #child
TargetChr = sys.argv[4]

sys.stdout.write("Files to be processed\nFather: %s\nMother: %s\nChild: %s\n" %(fnameA, fnameB, fnameC))

#ProcessFilesFirefox2#
inA = open(fnameA, 'r')
dataA = inA.read()

#ProcessFilesFirefox3#
inB = open(fnameB, 'r')
dataB = inB.read()

#ProcessFilesFirefox4#
inC = open(fnameC, 'r')
dataC = inC.read()

treat_nocalls_as_math = 1
SNP_cnt = 0

sys.stdout.write("\nChr  RSid             Position     Mother  Father  Child         Child Phased                   Uninherited\n")

i = 'declared' 
within_target_run = 0
run_length = 0
curr_chr_number = 0
curr_chr_numberB = 'declared'
prev_chr_number = -1

FFvs23A = 0
FFvs23B = 0
FFvs23C = 0

line_noA = 1 #ignore first line "RSID,CHROMOSOME,POSITION,RESULT"
line_noB = 1
line_noC = 1

dataA_lines = dataA.split("\n")
dataB_lines = dataB.split("\n")
dataC_lines = dataC.split("\n")

while ((line_noA < len(dataA_lines)-1) and (line_noB < len(dataB_lines)-1) and (line_noC < len(dataC_lines)-1)):
    input_lineA = dataA_lines[line_noA]
    input_lineB = dataB_lines[line_noB]
    input_lineC = dataC_lines[line_noC]


    if (line_noA == 0):
        if (input_lineA[0] == '#'):
            FFvs23A = 23 #// the file is from 23andMe
            
    if (line_noB == 0):
        if (input_lineB[0] == '#'):
            FFvs23B = 23#// the file is from 23andMe

    if (line_noC == 0):
        if (input_lineC[0]== '#'):
            FFvs23C = 23#// the file is from 23andMe


    if (FFvs23A == 23):
        while input_lineA[0] == '#':
            line_noA = line_noA + 1
            input_lineA = dataA_lines[line_noA]

    if (FFvs23B == 23):
        while input_lineB[0] == '#':
            line_noB = line_noB + 1
            input_lineB = dataB_lines[line_noB]
        
    if (FFvs23C == 23):
        while input_lineC[0] == '#':
            line_noC = line_noC + 1
            input_lineC = dataC_lines[line_noC]

    #// the substring stuff below is to compensate for a CarriageReturn that is left at the end of each line
    input_lineA = input_lineA[:-1]
    input_lineB = input_lineB[:-1]
    input_lineC = input_lineC[:-1]


    input_dataA = 'declared'
    input_dataB = 'declared'
    input_dataC = 'declared'
    rsidA = 'declared'
    rsidB = 'declared'
    rsidC = 'declared'
    chr_id = 'declared'
    chr_idB = 'declared'
    chr_idC = 'declared'
    SNP_position = 'declared'
    SNP_positionB = 'declared'
    SNP_positionC = 'declared'
    genotypeA = 'declared'
    genotypeB = 'declared'
    genotypeC = 'declared'

    if (FFvs23A == 23):
        input_dataA = input_lineA.split("\t")
        rsidA = input_dataA[0] #i think this is an array... LOC 740-747
        chr_id = input_dataA[1]
        SNP_position = input_dataA[2]
        genotypeA = input_dataA[3]

    elif (input_lineA[0] == "\""):
        input_dataA = input_lineA.split(",")
        rsidA = input_dataA[0][1:-1] #rsidA = input_dataA[0].substr(1,input_dataA[0].length -2 LOC 752
        chr_id = input_dataA[1][1:-1] 
        SNP_position = input_dataA[2][1:-1] 
        genotypeA = input_dataA[3][1:-1] 

    else:
        input_dataA = input_lineA.split(" ")
        rsidA = input_dataA[0] #i think this is an array... LOC 740-747
        chr_id = input_dataA[1]
        SNP_position = input_dataA[2]
        genotypeA = input_dataA[3] 

    #######################readablity########################       

    if (FFvs23B == 23):
        input_dataB = input_dataB.split("\t")
        rsidB = input_dataB[0] #i think this is an array... LOC 740-747
        chr_idB = input_dataB[1]
        SNP_positionB = input_dataB[2]
        genotypeB = input_dataB[3]

    elif (input_lineB[0] == "\""):
        input_dataB = input_lineB.split(",")
        rsidB = input_dataB[0][1:-1] #rsidB = input_dataB[0].substr(1,input_dataB[0].length -2 
        chr_idB = input_dataB[1][1:-1] 
        SNP_positionB = input_dataB[2][1:-1] 
        genotypeB = input_dataB[3][1:-1] 

    else:
        input_dataB = input_lineB.split(" ")
        rsidB = input_dataB[0] #i think this is an array... 
        chr_idB = input_dataB[1]
        SNP_positionB = input_dataB[2]
        genotypeB = input_dataB[3] 

    #######################readablity########################       

    if (FFvs23C == 23):
        input_dataC = input_dataC.split("\t")
        rsidC = input_dataC[0] #i think this is an array... 
        chr_idC = input_dataC[1]
        SNP_positionC = input_dataC[2]
        genotypeC = input_dataC[3]

    elif (input_lineC[0] == "\""):
        input_dataC = input_lineC.split(",")
        rsidC = [0][1:-1] #rsidC = input_dataC[0].substr(1,input_dataC[0].length -2 
        chr_idC = input_dataC[1][1:-1] 
        SNP_positionC = input_dataC[2][1:-1] 
        genotypeC = input_dataC[3][1:-1] 

    else:
        input_dataC = input_lineC.split(" ")
        rsidC = input_dataC[0] #i think this is an array... 
        chr_idC = input_dataC[1]
        SNP_positionC = input_dataC[2]
        genotypeC = input_dataC[3]



    while ((rsidA != rsidB) or (rsidA != rsidC) or (rsidB != rsidC)):

        file_to_read = which_file_to_skip(chr_id, chr_idB, chr_idC, SNP_position, SNP_positionB, SNP_positionC)

        if (file_to_read == 1):
            line_noA = line_noA + 1
            input_lineA = dataA_lines[line_noA]
            input_lineA = input_lineA[0:] #input_lineA = input_lineA.substr(0, input_lineA.length - 1

            if (FFvs23A == 23):            
                input_dataA = input_lineA.split("\t")  
                rsidA = input_dataA[0]
                chr_id = input_dataA[1]
                SNP_position = input_dataA[2]
                genotypeA = input_dataA[3]

            elif (input_lineA[0] == "\""):
                input_dataA = input_lineA.split(",")  
                rsidA = input_dataA[0][1:-1]
                chr_id = input_dataA[1][1:-1]
                SNP_position = input_dataA[2][1:-1] #HELP FIX ME [1:-2] ???
                genotypeA = input_dataA[3][1:-1]

            else:
                input_dataA = input_lineA.split(" ")  
                rsidA = input_dataA[0]
                chr_id = input_dataA[1]
                SNP_position = input_dataA[2]
                genotypeA = input_dataA[3]


        elif (file_to_read == 2):
            line_noB = line_noB + 1
            input_lineB = dataB_lines[line_noB]
            input_lineB = input_lineB[0:] #input_lineB = input_lineB.substr(0, input_lineB.length - 1

            if (FFvs23B == 23):            
                input_dataB = input_lineB.split("\t")  
                rsidB = input_dataB[0]
                chr_idB = input_dataB[1]
                SNP_positionB = input_dataB[2]
                genotypeB = input_dataB[3]

            elif (input_lineB[0] == "\""):
                input_dataB = input_lineB.split(",")  
                rsidB = input_dataB[0][1:-1]
                chr_idB = input_dataB[1][1:-1]
                SNP_positionB = input_dataB[2][1:-1]
                genotypeB = input_dataB[3][1:-1]

            else:
                input_dataB = input_lineB.split(" ")  
                rsidB = input_dataB[0]
                chr_idB = input_dataB[1]
                SNP_positionB = input_dataB[2]
                genotypeB = input_dataB[3]

        else:
            line_noC = line_noC + 1
            input_lineC = dataC_lines[line_noC]
            input_lineC = input_lineC[0:] #input_lineC = input_lineC.substr(0, input_lineC.length - 1

            if (FFvs23C == 23):            
                input_dataC = input_lineC.split("\t")  
                rsidC = input_dataC[0]
                chr_idC = input_dataC[1]
                SNP_positionC = input_dataC[2]
                genotypeC = input_dataC[3]

            elif (input_lineC[0] == "\""):
                input_dataC = input_lineC.split(",")  
                rsidC = input_dataC[0][1:-1]
                chr_idC = input_dataC[1][1:-1]
                SNP_positionC = input_dataC[2][1:-1]
                genotypeC = input_dataC[3][1:-1]

            else:
                input_dataC = input_lineC.split(" ")  
                rsidC = input_dataC[0]
                chr_idC = input_dataC[1]
                SNP_positionC = input_dataC[2]
                genotypeC = input_dataC[3]

    #// end while... we now have identical rsid's, or we've exhausted the input #LOC 925
    
    #len(dataA_lines)-1 should be len(dataA_lines)???
    if( (line_noA < len(dataA_lines)-1) and (line_noB < len(dataB_lines)-1) and (line_noC < len(dataC_lines)-1) ):

        if (chr_id == "MT"):
            curr_chr_number = 25
        elif (chr_id == "X"):
            curr_chr_number = 23
        elif (chr_id == "Y"):
            curr_chr_number = 24
        else:
            curr_chr_number = chr_id


        if (genotypeA == "---"):        
            genotypeA = "??"
        elif (genotypeA == "--"):
            genotypeA = "??"
        elif (genotypeA == "CA"):
            genotypeA = "AC"
        elif (genotypeA == "GA"):
            genotypeA = "AG"
        elif (genotypeA == "GC"):
            genotypeA = "CG"
        elif (genotypeA == "TA"):
            genotypeA = "AT"
        elif (genotypeA == "TC"):
            genotypeA = "CT"
        elif (genotypeA == "TG"):
            genotypeA = "GT"

        if (genotypeB == "---"):
            genotypeB = "??"
        elif (genotypeB == "--"):
            genotypeB = "??"
        elif (genotypeB == "CA"):
            genotypeB = "AC"
        elif (genotypeB == "GA"):
            genotypeB = "AG"
        elif (genotypeB == "GC"):
            genotypeB = "CG"
        elif (genotypeB == "TA"):
            genotypeB = "AT"
        elif (genotypeB == "TC"):
            genotypeB = "CT"
        elif (genotypeB == "TG"):
            genotypeB = "GT"

        if (genotypeC == "---"):
            genotypeC = "??"
        elif (genotypeC == "--"):
            genotypeC = "??"
        elif (genotypeC == "CA"):
            genotypeC = "AC"
        elif (genotypeC == "GA"):
            genotypeC = "AG"
        elif (genotypeC == "GC"):
            genotypeC = "CG"
        elif (genotypeC == "TA"):
            genotypeC = "AT"
        elif (genotypeC == "TC"):
            genotypeC = "CT"
        elif (genotypeC == "TG"):
            genotypeC = "GT"



        if(chr_id == TargetChr):
            report_SNP(chr_id, curr_chr_number, SNP_position, genotypeA, genotypeB, genotypeC, rsidA, FFvs23A+FFvs23B+FFvs23C)
            SNP_cnt = SNP_cnt + 1


        prev_chr_number = curr_chr_number
        prev_SNP_position = SNP_position
        line_noA = line_noA + 1
        line_noB = line_noB + 1
        line_noC = line_noC + 1
    #// end HUGE while

sys.stdout.write("\n")
tmpout = "%d SNPs were processed for Chromosome %s\n" %(SNP_cnt, TargetChr)
sys.stdout.write(tmpout)
sys.stdout.write("Processing Completed.\n<p>")
