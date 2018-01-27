# Author: <hanye han>
# Recitation: <101 # Richard Tillquist>

# Assignment4
def compute_census(List_rates, Curr_population):
    total_sec=365*24*60*60;#to calculate the total seconds per year
    tot_birth=total_sec//List_rates[0];#to calculate the total births per year
    tot_death=total_sec//List_rates[1];#to calculate the total deaths per year
    tot_immig=total_sec//List_rates[2];#to calculate the total immigrants per year
    total=tot_birth + tot_immig - tot_death;#to calculate the total population
    return (total + Curr_population);#return the result

def convert_seconds():
	s = int(input())
    #Calculating remainder seconds
	s_rem = s%86400
    #Calculating dys
	d = s//86400
    #Calculting remianding hours
	h_rem = s_rem%3600
   #calcuting hours
	h = s_rem//3600
    #calculating remainder minutes
	m_rem = h_rem%60
    #calcuating minuts
	m = h_rem//60
    #calculating remainder seconds
	s_rem = m_rem%60
    #calcuting seconds
	S = m_rem%60
    #display output
	print s,"corresponds to:",d,"days,",h,"hours,",m,"minutes,",S,"seconds."

def generate_story(list_to_story):
	size=1
	while (size<len(list_to_story)):
		list_to_story[size]=raw_input(list_to_story[size])#user input
		size=size+2
	return (' '.join(list_to_story))#print the hole list






def similarity_score(seq1,seq2):#funcion to return similarity score
	if len(seq1)!=len(seq2): #if lengths are uneqal
		return 0
	else:
		j=0
		count=0
		for i in seq1:
			if i!=seq2[j]: #counting the number of mismatches
				count=count+1
			j=j+1
		return (len(seq1)-count)/float(len(seq1)) #returning score

def best_match(s1,s2):#function to return best match
	i=0
	score=0#min score for start
	g=0
	while i<=len(s1):#iterating through second string
		if similarity_score(s1[i:i+len(s2)],s2) >score: #calcualting score and checkign if its more than existing score
			score=similarity_score(s1[i:i+len(s2)],s2)
			g=i
		i=i+1
	return (g)

#def calc_stats(List_of_numbers):
#	List_of_numbers.sort()
	#average=float(sum(List_of_numbers)/len(List_of_numbers))
	#number=len(List_of_numbers)
	#if number % 2 == 0:   
#		median = (List_of_numbers[number//2]+List_of_numbers[number//2-1])/2
	#elif number % 2 == 1:
	#	median = List_of_numbers[(number)/2]
#	result=[average,median]
#	return (result)
def calc_stats(l):#function to return stats of list
	l.sort()#sorting the list
	sum=0
	for i in l:
		sum=sum+i#calculating the sum
	mean=sum/float(len(l))#mean=sum/count
	if len(l)%2==0:#if even numbers are present
		median=float((l[len(l)//2-1]+l[len(l)//2]))/2 #median is average of middle 2 numbers
	else:
		median= l[len(l)//2] # median is the middle element
	result=[mean,median]
	return (result)

def parse_ratings(filename):
	f=open(filename)
    # list to store the list of name, ratings
	res=[]
    # reading through every line in the file
	for line in f:
        # removing the spaces
		line=line.strip()
        # splitting line by 'comma'
		data=line.split(',')
        # getting the name
		name=data[0]
        # getting the ratings
		ratings=data[1].split()
        # temporary list to store the name, and ratings
		t=[]
        # adding the name to the list
		t.append(name)
        # another temporary list to store the ratings
		t2=[]
        # adding the ratings to the list
		for r in ratings:
			t2.append(int(r))
        # adding the temporary list t2 to t
		t.append(t2)
        # adding the temporary list t to res
		res.append(t)
    # returning the final list
	return res

if __name__=="__main__":
 birth_rate=8
 death_rate=12
 new_immigrants_rate=33
 List_of_rates=[birth_rate,death_rate,new_immigrants_rate]
 Curr_population = 1000000
 print (compute_census(List_of_rates, Curr_population))
    
 convert_seconds()

 str1="I went skiing to "
 str2=" it was really crowded and I stayed in line for "
 str3=" hours"
 prompt1="Enter a location"
 prompt2="Enter numbers of hour:"
 list_to_story = [str1, prompt1, str2, prompt2, str3]
 print(generate_story(list_to_story))
 List_of_numbers=[1,2.5,3,8,10.6,5]
 print(calc_stats(List_of_numbers))
 
 print(parse_ratings('data.txt'))
 
 print (similarity_score('CCGCCGCCGA','CCTCCTCGCTA'))
 print ('best match at: ',best_match('CGN','JJJ'))



    
    
    
