#Opens a file in read mode  
file = open("data.txt", "r")  

#example for racial slurs
racialSlurs= ["hello", "how"]

#Gets each line till end of file is reached  
for line in file:  
    #Splits each line into sentence to find all sentence 
    allline = line.split(".");
    # we get every sentence from file not we have to count how many slurs are present in everyline
    for everline in allline:
        # find every word from a sentence 
        words=everline.split(' ');
        wordscount = 0;
        slur=0;
        for word in words:
            slur+=racialSlurs.count(word)
            wordscount=wordscount+1
        #change in to precentage using total word and slur words
        percentage=int((slur*100)/wordscount); 
        if percentage!=0:
            print(percentage)
        
        
file.close();  
