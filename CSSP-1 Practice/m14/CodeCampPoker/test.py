hand = ['2D' ,'3S' ,'5S' ,'4C' ,'6D']
value_dict = {
'2' : 0 , '3' : 1, '4' : 2, '5' : 3 , '6' : 4, 
'7' : 5, '8' : 6, '9' : 7, 'T' : 8,
'J' : 9 , 'Q' : 10 , 'K' : 11 , 'A' : 12 
}

sub_stng_value= []
sub_stng_score = 0

for i in hand:
    print(i)
    sub_stng_value.append(i[0])
    sub_stng_score += value_dict.get(i[0])

print(sub_stng_value)
print(sub_stng_score)