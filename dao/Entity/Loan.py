class Loan:
    def __init__(self,loanID, customerID, principalAmount, interestRate, loanTerm, loanType, loanStatus) -> None:
        self.loanID=loanID
        self.customerID=customerID
        self.principalAmount=principalAmount
        self.interestRate=interestRate
        self.loanTerm=loanTerm
        self.loanType=loanType
        self.loanStatus=loanStatus
        
    class HomeLoan:
        def __init__(self,propertyAddress,propertyValue) -> None:
            self.propertyAddress=propertyAddress
            self.propertyValue=propertyValue
    class CarLoan:
        def __init__(self,carModel,carValue):
            self.carModel=carModel
            self.carValue=carValue
