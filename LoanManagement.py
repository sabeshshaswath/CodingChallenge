from dao.Entity import Loan
from dao import ILoanRepositoryImpl

def mainmenu():
    print("1. Apply loan")
    print("2. Calculate Interest")
    print("3. calculate Emi")
    print("4. loanRepayment")
    print("5. getAllLoan")
    print("6. getLoanByID")
    print("7. Exit")
while True:
    mainmenu()
    loanservice=ILoanRepositoryImpl()
    choice=int(input("Enter your choice: "))
    if choice==1:
        loanID = input("Enter Loan ID: ")
        customerID = input("Enter Customer ID: ")
        principalAmount = float(input("Enter Principal Amount: "))
        interestRate = float(input("Enter Interest Rate: "))
        loanTerm = int(input("Enter Loan Term (in months): "))
        loanType = input("Enter Loan Type: ")
        loanStatus = input("Enter Loan Status: ")
        
        loan = Loan(loanID, customerID, principalAmount, interestRate, loanTerm, loanType, loanStatus)
        loanservice.applyLoan(loan)
    elif choice==2:
        loneid=int(input("Enter the loneID: "))
        loanservice.calculateInterest(loneid)
    elif choice==3:
        loneid=int(input("Enter the loneID: "))
        loanservice.calculateEMI(loneid)
    elif choice==4:
        loneid=int(input("Enter the loneID: "))
        loanservice.loanRepayment(loneid)
    elif choice==5:
        loanservice.getAllLoan()
    elif choice==6:
        loneid=int(input("Enter the loneID: "))
        loanservice.getLoanById(loneid)
    elif choice==7:
        loanservice.close()
        break
    else:
        print("Please enter the choice within range")
