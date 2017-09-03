import numpy as np
import matplotlib.pyplot as plt
import plotly as py
def statistics():
    f=open('output2.txt' , 'r')
    file=f.read()
    length_trascript=len(file)#reading from cleaned file
    #print (file)
    ln=length_trascript
    #print(ln)
    unique_words=0
    grammar_error=0
    retracing=0
    repetition=0
    pauses=0
    for t in range(ln): #calculating number of unique words
        if file[t]==' ':
            if file[t+1]=='C' or file[t+1]=='(' or file[t+1]=='.' or file[t+1]=='[' or file[t+1]=='(':
                continue
            else:
                unique_words+=1

    for r in range(ln):
        if file[r:r+3]=='[*]': #calculating number of grammatical errors
            #print(file[r:r+3])
            grammar_error+=1
        elif file[r:r+3]=='[/]': #calculating number of repetitions
            repetition+=1
            #print(file[r:r+3])
        elif file[r:r+4]=='[//]': #calculating number of retracings
            retracing+=1
            #print(file[r:r+4])

    for q in range(ln): #calculating number of pauses
        if file[q]=='(':
            pauses+=1
    #print(unique_words)
    #print(grammar_error)
    #print(retracing)
    #print(repetition)
    #print(pauses)
    data=[str(unique_words),str(grammar_error),str(retracing),str(repetition),str(pauses)]
    titles=['unique_words','grammar_error','retracing','repetition','pauses']
    list=[titles,data]
    table=np.array(list)
    print("this is a test run of the program. This program reads the clean output.txt file generated from task 1 to read data and generate statistics")
    print("The following table shows the statistics required and the table shows the same data in tabular format")
    print(table) #printing table of statistics
    objects = titles
    y_pos = np.arange(len(titles))
    performance = [unique_words,grammar_error,retracing,repetition,pauses]

    plt.bar(y_pos, performance, align='center', alpha=0.5)
    plt.xticks(y_pos, objects)
    plt.ylabel('frequency')
    plt.title('statistic type')
    plt.show()



statistics()
