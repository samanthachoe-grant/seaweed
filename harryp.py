gryffindor = 0
ravenclaw = 0
hufflepuff = 0
slytherin = 0 

print('Q1. Do you like dawn or dusk?')
print('1. Dawn')
print('2. Dusk')

score = int(input('Enter 1 or 2: '))

if score == 1:
    gryffindor += 1
    ravenclaw += 1
elif score == 2:
    hufflepuff += 1
    slytherin += 1 
else:
    print('Invalid input. Please enter 1 or 2.')

print('Q2. Which of the following would you most hate people to call you?')
print('1. Ordinary')
print('2. Ignorant')
print('3. Cowardly')
print('4. Selfish')

score = int(input('Enter 1, 2, 3, or 4: '))

if score == 1:
    ravenclaw += 1
elif score == 2:
    slytherin += 1
elif score == 3:
    gryffindor += 1
elif score == 4:
    hufflepuff += 1
else:
    print('Invalid input. Please enter 1, 2, 3, or 4.')

print('Q3. Moon or stars?')
print('1. Moon')
print('2. Stars')

score = int(input('Enter 1 or 2: '))

if score == 1:
    hufflepuff += 2
    ravenclaw += 2
elif score == 2:
    gryffindor += 2
    slytherin += 2
else:
    print('Invalid input. Please enter 1 or 2.')

print('Q4. How would you like to be known to history?')
print('1. The Brave')
print('2. The Wise')
print('3. The Loyal')
print('4. The Cunning')

score = int(input('Enter 1, 2, 3, or 4: '))

if score == 1:
    gryffindor += 2
elif score == 2:
    ravenclaw += 2
elif score == 3:
    hufflepuff += 2
elif score == 4:
    slytherin += 2
else:
    print('Invalid input. Please enter 1, 2, 3, or 4.')

print('Q5. Heads or tails?')
print('1. Heads')
print('2. Tails')

score = int(input('Enter 1 or 2: '))

if score == 1:
    gryffindor += 3
    hufflepuff += 3
elif score == 2:
    ravenclaw += 3
    slytherin += 3
else:
    print('Invalid input. Please enter 1 or 2.')

print('Q6. Forest or river?')
print('1. Forest')
print('2. River')

score = int(input('Enter 1 or 2: '))

if score == 1:
    gryffindor += 3
    hufflepuff += 3
elif score == 2:
    ravenclaw += 3
    slytherin += 3
else:
    print('Invalid input. Please enter 1 or 2.')

print(gryffindor, ravenclaw, hufflepuff, slytherin)

print(max(gryffindor, ravenclaw, hufflepuff, slytherin))