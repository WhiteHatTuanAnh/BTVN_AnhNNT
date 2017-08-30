infile = open('alice_story.txt', 'r')
text = infile.read()
text1 = text.split()
infile.close()

outfile = open('alice_words.txt', 'w')

dict1 = {}
for symbol in text1:
    symbol = symbol.replace("'",'').replace('_', '').replace('"', '').replace(',', '').replace('.', '').replace(':', '').replace('[', '').replace(';', '').replace('-', '').replace('?', '').replace('!', '').replace("'", '').replace('(', '').replace(')', '').replace(']', '')
    symbol = symbol.lower()
    if symbol != " ":
        dict1[symbol] = dict1.get(symbol, 0) + 1

short_keys = sorted( dict1.keys() )

outfile.write( "%-20s%s \n" % ("Character", "Count") )
outfile.write( "========================= \n" )
for key in short_keys :
    outfile.write( "%-20s%d \n" % (key, dict1[key ]) )
outfile.close()

count_alice = dict1['alice']
print ("Số chữ alice là:", count_alice)
