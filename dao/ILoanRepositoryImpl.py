from  .ILoanRepository import ILoanRepository
from .Util import DBConnutil,Db_prop
from .Exception import ApplyLoneException,calculateEMIException,InvalidLoanException,RetriveloanException,calculateInterestException
from tabulate import tabulate


class ILoanRepositoryImpl(ILoanRepository):

    def __init__(self) -> None:
        self.connection=DBConnutil.get_connectionOBJ(Db_prop.getconstring())
        self.cursor=self.connection.cursor()

    def applyLoan(self, Loan):
        try:
            self.cursor.execute("INSERT INTO  Loan (loanID, customerID, principalAmount, interestRate, loanTerm, loanType, loanStatus) VALUES (?,?,?,?,?,?,?)",
                                (Loan.loanID,Loan.customerID, Loan.principalAmount, Loan.interestRate, Loan.loanTerm, Loan.loanType, Loan.loanStatus))
            self.connection.commit()
        except Exception as e:
            self.connection.rollback()
            raise ApplyLoneException("Could'nt apply loan check CustomerId")
        
    def calculateInterest(self, LoanID):
        try:
            self.cursor.execute("Select principalAmount,interestRate,loanTerm from Loan where LoanID=?",
                                (LoanID))
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                principalAmount, interestRate, loanTerm = result
                interest = (principalAmount * interestRate * loanTerm) / 12
                print(f"The interest is {round(interest,2)}")
            else:
                raise calculateInterestException("Loan not found")
        except Exception as e:
            self.connection.rollback()
            raise calculateInterestException("Couldn't calculate interest. Error: {}".format(str(e)))
        
    def loanStatus(self, loanId):
        try:
            self.cursor.execute("Select credit_score from Loan l inner join  Customer c on c.customerID=l.customerID where loanID=?;",(loanId))
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                credit_score = result[0]
                if credit_score>650:
                    print("Approved")
                    self.cursor.execute("update Loan set loanStatus='Approved' where loanID=?;",(loanId))
                    self.connection.commit()
                else:
                    print("Rejected")
                    self.cursor.execute("update Loan set loanStatus='Rejected' where loanID=?;",(loanId))
                    self.connection.commit()
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            self.connection.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
        
    def calculateEMI(self, loneId):
        try:
            self.cursor.execute("Select principalAmount,interestRate,loanTerm from Loan where LoanID=?",
                                (loneId))            
            result=self.cursor.fetchone()
            if result:
                ##self.calculateInterest(result[0],result[1],result[2])
                principalAmount, interestRate, loanTerm = result
                R = interestRate / (12 * 100)
                emi=(principalAmount*R*(1+R)**loanTerm)/((1+R)**loanTerm-1)
                print(f"The emi is {round(emi,2)}")
                return emi
            else:
                raise InvalidLoanException("Loan not found")
        except Exception as e:
            self.connection.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
        
    def loanRepayment(self,loneId,amount):
        try:
            emi=self.calculateEMI(loneId)
            loanRepaymentcount=0
            if emi:
                if emi>amount:
                    raise InvalidLoanException(f"Payment rejected amount {amount} is letter than emi {emi}")
                ##self.calculateInterest(result[0],result[1],result[2])
                else:
                    while amount>0:
                        amount=amount/emi
                        loanRepaymentcount+=1
                print(f"The total number of emi payed by amount {amount} is {loanRepaymentcount}")
            else:
                raise calculateEMIException("Loan not found")
        except Exception as e:
            self.connection.rollback()
            raise InvalidLoanException("Couldn't find customer/loan. Error: {}".format(str(e)))
                
    def getAllLoan(self):
        try:
            self.cursor.execute("Select * from Loan")
            print(tabulate(self.cursor.fetchall()))
        except Exception as e:
            self.connection.rollback()
            raise InvalidLoanException("No loan available")
        
    def getLoanById(self, loanId):
        try:
            self.cursor.execute("Select * from Loan where loanID=?",(loanId))
            result=self.cursor.fetchall()
            if result:
                print(tabulate(result))
            else:
                raise RetriveloanException("Id not found")
        except Exception as e:
            self.connection.rollback()
            raise InvalidLoanException("No loan available")
    def close(self):
        self.cursor.close()
        self.connection.close()
               
        ##overloadingcode
    # def calculateInterest(self,principalAmount, interestRate, loanTerm):
    #     try:
    #         interest=(principalAmount*interestRate*loanTerm)/12
    #         print(f"The interest is {interest}")
    #     except Exception as e:
    #         raise calculateInterestException("Error")

