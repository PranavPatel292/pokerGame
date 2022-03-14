lcount = 0

def pair(hashmap, key):
	
	for k in key:

		if hashmap[k] == 2:
			return True, 2

	return False

def twoPair(hashmap, key):

	countTwoPair = 0

	for k in key:

		if hashmap[k] == 2:
			countTwoPair += 1

	return True if countTwoPair == 2 else False

def straight(hashmap, key):

	startValue = 0

	for k in key:

		if hashmap[k] > 0:
			startValue = int(k)
			break

	if (startValue + 4) <= 14:
		if hashmap[str(startValue)] > 0 and hashmap[str(startValue + 1)] > 0 and hashmap[str(startValue + 2)] and hashmap[str(startValue + 3)] and hashmap[str(startValue + 4)]:
			return True

	return False


def flush(hashmap):

	if hashmap['D'] == 5 or hashmap['S'] == 5 or hashmap['H'] == 5 or hashmap['C'] == 5:
		return True

	return False

def threeAKind(hashmap, key):

	for k in key:

		if hashmap[k] == 3:
			return True, 4

	return False

def fullHouse(hashmap, key):

	if threeAKind(hashmap, key) and pair(hashmap, key):
		return True

	return False

def fourOfKind(hashmap, key):
	for k in key:

		if hashmap[k] == 4:
			return True

	return False

def straightFlush(hashmap, key):

	startValue = 0

	for k in key:
		if hashmap[k] > 0:
			startValue = int(k)
			break


	if (startValue + 4) <= 14:
		if flush(hashmap) and hashmap[str(startValue)] > 0 and hashmap[str(startValue + 1)] and hashmap[str(startValue + 2)] and hashmap[str(startValue + 3)] and hashmap[str(startValue + 4)]:
			return True

	return False

def royalFlush(hashmap):

	if flush(hashmap) and hashmap['10'] > 0 and hashmap['11'] > 0 and hashmap['12'] > 0 and hashmap['13'] > 0 and hashmap['14'] > 0:
		return True

	return False


def rank(player, key):

	if royalFlush(player):
		return 10, 'royalFlush'
	elif straightFlush(player, key):
		return 9, 'straightFlush'
	elif fourOfKind(player, key):
		return 8, 'fourOfKind'
	elif fullHouse(player, key):
		return 7, 'fullHouse'
	elif flush(player):
		return 6, 'flush'
	elif straight(player, key):
		return 5, 'straight'
	elif threeAKind(player, key):
		return 4, 'threeAKind'
	elif twoPair(player, key):
		return 3, 'twoPair'
	elif pair(player, key):
		return 2, 'pair'
	else:
		return 1, 'highCard'



def hashmapEntry(arr, hashmap):

	for i in arr:

		if i[0] == 'T':
			hashmap['10'] += 1

		elif i[0] == 'J':
			hashmap['11'] += 1

		elif i[0] == 'Q':
			hashmap['12'] += 1

		elif i[0] == 'K':
			hashmap['13'] += 1

		elif i[0] == 'A':
			hashmap['14'] += 1
			
		else:
			hashmap[i[0]] += 1

		hashmap[i[1]] += 1

	return hashmap

# Michelle Carlin (Poker game: Monday)
# Michael O'Sullivan (Moroku Game: Tuesday)

# here the flag value determines whether the rank is: Pair, HighCard, threeOfKind, 

def highestInPairs(p1, p2, key, table, flag, count):
	player1Max = 0
	player2Max = 0

	if flag == 'fullHouse':

		player1Max1 = 0
		player2Max2 = 0

		for k in key:
			if k == "D":
				break

			if p1[k] == 3:
				player1Max = max(player1Max, int(k))

			if p1[k] == 2:
				player1Max1 = max(player1Max1, int(k))

			if p2[k] == 3:
				player2Max = max(player2Max, int(k))

			if p2[k] == 2:
				player2Max2 = max(player2Max2, int(k))

		if player1Max == player2Max:

			if player1Max1 > player2Max2:
				table['player1'] += 1
			else:
				winnerPoker['player2'] += 1
		elif player1Max > player2Max:
			table['player1'] += 1
		else:
			table['player2'] += 1

	elif flag == 'pair' or flag == 'twoPair':

		player1Max1 = 0
		player2Max2 = 0

		for k in key:
			if k == "D":
				break

			if p1[k] == 2:
				player1Max = max(player1Max, int(k))

			if p1[k] != 0 and p1[k] != 2:
				player1Max1 = max(player1Max1, int(k))

			if p2[k] == 2:
				player2Max = max(player2Max, int(k))

			if p2[k] != 0 and p2[k] != 2:
				player2Max2 = max(player2Max2, int(k))

		if player1Max == player2Max:
			if player1Max1 > player2Max2:
				table['player1'] += 1
			else:
				table['player2'] += 1
		elif player1Max > player2Max:
			table['player1'] += 1
		else:
			table['player2'] += 1

	else:

		deleteKey1 = ['None']
		deleteKey2 = ['None']
		for k in key:
			if k == 'D':
				break

			if (flag == 'highCard') or (flag == 'threeAKind' and (p1[k] == 3 or p2[k] == 3)) or (flag == 'fourOfKind' and (p1[k] == 4 or p2[k] == 4)):
				if p1[k] != 0:
					deleteKey1[0] = k
					player1Max = int(k)
				if p2[k] != 0:
					deleteKey2[0] = k
					player2Max = int(k)



		if player1Max > player2Max:
			table['player1'] += 1

		elif player1Max < player2Max:
			table['player2'] += 1
		else:
			
			while player1Max == player2Max:

				del p1[deleteKey1[0]]
				del p2[deleteKey2[0]]

				key1 = p1.keys()

				key2 = p2.keys()

				
				for k in key1:

					if k == 'D':
						break

					if p1[k] != 0:
						deleteKey1[0] = k
						player1Max =  int(k)

				
				for k in key2:

					if k == 'D':
						break

					if p2[k] != 0:
						deleteKey2[0] = k
						player2Max =  int(k)

			if player1Max > player2Max:
				table['player1'] += 1
			else:
				table['player2'] += 1

# this function takes a hashmap created from both the array

def slove(player1, player2, key, table, count):

	count[0] += 1

	
	score1, state = rank(player1, key)

	score2, state = rank(player2, key)



	if score1 > score2:
		
		table['player1']  += 1
		

	elif score1 < score2:
		
		table['player2'] += 1
		

	else:
		# pair, two pair, threeOfKind, full house, highCard, fourOfKind
		if state == 'pair':
			highestInPairs(player1, player2, key, table, 'pair', count)

		elif state == 'twoPair':
			highestInPairs(player1, player2, key, table, 'twoPair', count)

		elif state == 'threeAKind':
			highestInPairs(player1, player2, key, table, 'threeAKind', count)

		elif state == 'fullHouse':
			highestInPairs(player1, player2, key, table, 'fullHouse', count)

		elif state == 'fourOfKind':
			highestInPairs(player1, player2, key, table, 'fourOfKind', count)

		else: # High Card, Straight, Flush and Straight Flush
			highestInPairs(player1, player2, key, table, 'highCard', count)

def winnerPoker(str, table, count):

	
	arr = str.split(" ")



	player1 = arr[:5]
	player2 = arr[5:]

	keys = ['2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14']

	hash_hashmap_player1 = {'2' : 0,'3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0,'8' : 0,'9' : 0,'10' : 0, '11' : 0,
	'12' : 0, '13' : 0,'14' : 0, 'D' : 0, 'C' : 0, 'S' : 0, 'H' : 0}

	hash_hashmap_player2 =  {'2' : 0,'3' : 0,'4' : 0,'5' : 0,'6' : 0,'7' : 0,'8' : 0,'9' : 0,'10' : 0, '11' : 0,
	'12' : 0, '13' : 0,'14' : 0, 'D' : 0, 'C' : 0, 'S' : 0, 'H' : 0}

	
	hashmapEntry(player1, hash_hashmap_player1)

	hashmapEntry(player2, hash_hashmap_player2)

	slove(hash_hashmap_player1, hash_hashmap_player2, keys, table, count)



# main function

winnerTable  = {'player1' : 0, 'player2' : 0}

test_file_for_input = open('./data/poker-hands.txt', 'r')

count = [0]

lines = []

with test_file_for_input as file:
    lines = [line.rstrip('\n') for line in file]

for i in lines:
	winnerPoker(i, winnerTable, count)

print('Player 1: ', winnerTable['player1'])
print('Player 2: ', winnerTable['player2'])