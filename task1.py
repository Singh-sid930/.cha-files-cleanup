

def file_cleanup():
    print("this is a test run of the program, the output.txt file contains the extracted portions of the children's speech and output2.txt file contains the cleaned speech portions of the transcript")
    f=open('test script.txt' , 'r')
    file=f.read()
    cstart=[]
    cend=[]
    clean_file=[]
    for i in range(len(file)):  #loop to check for the portions of transcript with children's speech
        if file[i]=='*' and file[i+1]=='C' and file[i+2]=='H':
            cstart.append(i+1)
            d=i
            while (file[d]!='%'):
                d+=1

            cend.append(d)


    for n in range (len(cend)): #loop to create a string list having children's speech
        clean_file.append(file[cstart[n]:cend[n]])

    #print (file)
    #print(clean_file)
    fn=open("output.txt","w")
    to_write=''.join(clean_file) #writing portions of the child's speech in a file named output
    fn.write(to_write)
    f.close()
    fn.close()


    new_clean_file=[]
    for t in range(len(clean_file)): #loop to access every string (portion of child's speech

            j=clean_file[t].split()
            ln=len(j)

            i=0
            while(i<ln):  #loop to remove &words and +words
                if j[i][0]=='&':
                    del(j[i])
                elif j[i][0]=='+':
                    del(j[i])
                i+=1
                ln=len(j)
            l=0
            while(l<ln): #loop to remove [] words and reatain [//] [*] [/]
                lo=len(j[l])
                if j[l][0]=='[':
                    if j[l]=='[/]' or j[l]=='[//]' or j[l]=='[*]':
                        break
                    else:
                        del(j[l])




                ln=len(j)
                l+=1
            k=0
            while(k<ln): #loop to remove < > ( )
               lp=len(j[k])

               if j[k][0]=='<' and j[k][lp-1]=='>':
                   j[k]=j[k][1:lp-1]
               elif j[k][0]=='<' and j[k][lp-1]!='>':
                   j[k]=j[k][1:lp]
               elif j[k][0]!='<' and j[k][lp-1]=='>':
                   j[k]=j[k][0:lp-1]
               t=0
               lu=len(j[k])
               while (t<lu):
                   if j[k][t]=='(' and j[k][t+1]!='.':
                       j[k]=j[k][0:t]+j[k][t+1:len(j[k])]
                   elif j[k][t]==')' and j[k][t-1]!='.':
                       j[k]=j[k][0:t]+j[k][t+1:len(j[k])]
                   lu=len(j[k])
                   t+=1
               k+=1
               ln=len(j)

            new_clean_file.append(j)

    new2_to_write=[]
    ft=open('output2.txt','w')
    #print(new_clean_file)
    for q in range(len(new_clean_file)): #loop for converting list of lists into list of strings
        new_to_write=' '.join(new_clean_file[q])
        new2_to_write.append(new_to_write)
        new2_to_write.append('\n')
    new3_to_write=' '.join(new2_to_write) #converting list to strings
    #print (new3_to_write)
    ft.write(new3_to_write) #printing file to ouput file
    ft.close()




file_cleanup()


