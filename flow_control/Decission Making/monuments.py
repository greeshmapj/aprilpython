#accept any city from the user and display the monument of that city.
#delhi-red fort
#agra- taj mahal
#jaipur- jal mahal            #== present, int not present

city=(input("enter any city="))

if(city=='delhi'):
    print("red fort")
elif(city=='agra'):
    print("taj mahal")
elif(city=='jaipur'):
    print("jal mahal")
else:
    print("invalid input")