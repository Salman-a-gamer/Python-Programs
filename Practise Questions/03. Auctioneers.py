print('Welcome to auction program! '.center(40, '*'))
auctioneers = {}
end = True
while end:
    auctioneers[input('Whats your name?')] = int(input('What is your bid?'))
    choice = input("Enter 'yes' to add new auctioneer/ 'no' to end ".lower())
    if choice == 'yes':
        print('\n' * 10)
        continue
    else:
        break
max = 0
winner = ''
for k,v in auctioneers.items():
    if v > max:
        max = v
        winner += k
print('Congrats' , k, 'won the auction by bidding', v, 'Dirhams')

# we can use max(auctioneers, key = auctioneers.get) to get key of max value

