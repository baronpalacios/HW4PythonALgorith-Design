# takes as input the list of n people and the list of pairs who know each other, and outputs the best choice of party invitees.
def partyInvitees(people,pairs):
    output=[]
    known=[]
    #take a person and calculate that how many people he/she knows.
    for i in range (len(people)):
        count=0#reset count
        for j in range(len(pairs)):#search this person in pairs
            if(people[i] in pairs[j]):#if this person is in  pair[j] ,increase count by 1
                count=count+1
        known.append(count)#append 'count' into the array known.(this person is in the ith index and known[i] represents the number of people whohe/she knows)
    for i in range(len(people)):#Take a person and make a decision to invite this person to the party or not
        #if this person should have at least five other people whom they know
        #and five other people whom they don't know,add this person into the array output .
        if(known[i]>=5 and (len(people)+1 -known[i]) >=5):
            output.append(people[i])#this array includes people who will ne inviteed to the party.
    return output

#Standard form for people
people=["a","b","c","d","e","f","g","h","i","j","k","l","m"]

#standard form for pairs
pairs=[
    ("a","b"),("a","d"),("a","e"),("a","f"),("a","m"),
    ("b","d"),("b","e"),("b","f"),("c","e"),("c","h"),
    ("d","e"),("d","k"),("d","h"),("e","f"),("e","h"),
    ("f","h"),("f","i"),("g","i"),("h","i"),("h","j"),
    ("h","l"),("i","j"),("i","k"),("i","m"),("j","k"),
    ("j","l"),("j","m"),("k","l"),("k","m"),("l","m")
      ]

print(partyInvitees(people,pairs))
