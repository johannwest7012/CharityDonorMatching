class Donor:
    def __init__(self, symbol, money, preferences = {}):
        self.symbol = symbol
        self.money = money
        self.preferences = preferences
        self.moneyspent = []
        self.ranking = 0



class Charity:
    def __init__(self, symbol, capacity, preferences = {}):
        self.symbol = symbol
        #total capactiy of funding
        self.capacity = capacity
        #current received funding
        self.funding = 0
        self.preferences = preferences


def loop(donor_list, charity_list, num_charities):
    # charities 1 takes all 1:1's (donor_ranking, charity_ranking), then takes 1:2's, so on

    #transaction report (money will move, this keeps track of the moves)
    transaction_report = []

    best_ranking = 1
    while best_ranking <= num_charities:
        #start with looking for 1 rankings
        for charity in charity_list:
            #on a current charity

            ranked_donors = []

            for donor in donor_list:
                if donor.preferences[charity.symbol] == best_ranking:
                    ranked_donors.append(donor)

            #currently have all the donor's whose preference is the current charity
            #now must sort these donor's in order of the charities preference

            for i in ranked_donors:
                i.ranking = charity.preferences[i.symbol]
            ranked_donors.sort(key=lambda x: x.ranking)


            #recon
            print("Sorted")
            for i in ranked_donors:
                print(i.symbol)
            print('----------------')

            #now that a list of the most preferred donors for this charity has been made
            #must fill the charity with money until budget is met
            #and fill out the transaction report

            while charity.capacity < 0:
                for i in donor_list:

                    #if the donor has more money than the capacity
                    if (i.money + charity.capacity > 0):
                        donation = charity.capacity * -1
                        i.money = i.money - donation
                        charity.capacity = 0
                        charity.funding += donation

                        transaction_report.append(i.symbol + " donates the amount of " + str(donation) + " to " + charity.symbol)

                    else:
                        donation = i.money
                        charity.capacity = charity.capacity + donation
                        i.money = 0
                        charity.funding += donation

                        transaction_report.append(i.symbol + " donates the amount of " + str(donation) + " to " + charity.symbol)

                    if charity.capacity == 0:
                        break







        best_ranking += 1
    print("Transaction report", transaction_report)
    for i in charity_list:
        print(i.symbol, i.funding)


def test1():
    donor1pref = {"A": 1, "B": 2,"C": 3}
    donor2pref = {"A": 1, "B": 3, "C": 2}
    donor3pref = {"A": 3, "B": 2, "C": 1}

    charityApref = {"1": 1, "2": 2, "3": 3}
    charityBpref = {"1": 2, "2": 1, "3": 3}
    charityCpref = {"1": 1, "2": 3, "3": 2}

    donor1 = Donor("1",40, donor1pref)
    donor2 = Donor("2",25, donor2pref)
    donor3 = Donor("3",10, donor3pref)

    charA = Charity("A",-30, charityApref)
    charB = Charity("B",-30, charityBpref)
    charC = Charity("C",-15, charityCpref)

    dlist = [donor1,donor2,donor3]
    clist = [charA,charB,charC]

    loop(dlist,clist, 3)


def prompt():

    dlist = []
    clist = []
    while True:
        yesno = input("Would you like to add a donor? (Y/N)")
        if yesno == 'Y' or yesno == 'y' or yesno == 'yes':
            #yes
            symbol = str(input("What is the donor name or symbol"))
            money = int(input("How much funds does donor " + symbol +" have?"))

            new_don = Donor(symbol,money)
            dlist.append(new_don)
            print("Donor successfully added")
        else:
            break

    while True:
        yesno = input("Would you like to add a charity? (Y/N)")
        if yesno == 'Y' or yesno == 'y' or yesno == 'yes':
            # yes
            symbol = str(input("What is the charity name or symbol"))
            money = int(input("How much funds is charity " + symbol + " accepting in donations?"))
            new_charity = Charity(symbol, money)
            clist.append(new_charity)

        else:
            break

    num_donors = len(dlist)
    num_chars = len(clist)
    for i in dlist:
        pref = {}
        for j in range(1,num_donors + 1):
            sym = input("What is the name or symbol of donor " + i.symbol + " # " + str(j) + " preference?")
            pref[sym] = j

        i.preferences = pref

    for i in clist:
        pref = {}
        for j in range(1,num_chars + 1):
            sym = input("What is the name or symbol of charity " + i.symbol + " # " + str(j) + " preference?")
            pref[sym] = j

        i.preferences = pref

    loop(dlist,clist,num_chars)



def main():
    #prompt()
    test1()
    print()


if __name__ == '__main__':
    main()
