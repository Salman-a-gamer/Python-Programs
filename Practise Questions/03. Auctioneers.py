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
for k,v in auctioneers.items():
    if v > max:
        max = v
for k,v in auctioneers.items():
    if v == max:
        print('Congrats' , k, 'won the auction by bidding', v, 'Dirhams')

