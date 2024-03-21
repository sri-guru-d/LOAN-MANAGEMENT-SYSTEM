import pyodbc
import uuid
from entity.model import CarLoan, HomeLoan
from dao import iloanrepository
from abc import ABC, abstractmethod
from exceptions.exceptions import InvalidLoanException
from util import db_conn_util


class LoanManagement:
    @staticmethod
    def main():
        loan_repo = iloanrepository.ILoanRepositoryImpl()
        loancount=101
        while True:
            print("\nLoan Management System")
            print("Menu:")
            print("0. Display Customer Details")
            print("1. Apply for Loan")
            print("2. Calculate Interest")
            print("3. Check Loan Status")
            print("4. Calculate EMI")
            print("5. Loan Repayment")
            print("6. Get All Loans")
            print("7. Get Loan by ID")
            print("8. Exit")

            choice = input("Enter your choice: ")

            if choice == "0":
                print("Display Customer Details")
                loan_repo.customer_details()

            elif choice == "1":

                
                
                # Apply for Loan
                print("\nApplying for Loan:")
                customer_id = input("Enter Customer ID: ")
                principal_amount = float(input("Enter Principal Amount: "))
                interest_rate = float(input("Enter Interest Rate: "))
                loan_term_months = int(input("Enter Loan Term (in months): "))
                loan_type = input("Enter Loan Type (HomeLoan/CarLoan): ")
                property_address = input("Enter Property Address: ") if loan_type.lower() == "homeloan" else None
                property_value = float(input("Enter Property Value: ")) if loan_type.lower() == "homeloan" else None
                car_model = input("Enter Car Model: ") if loan_type.lower() == "carloan" else None
                car_value = float(input("Enter Car Value: ")) if loan_type.lower() == "carloan" else None
                if loan_type.lower() == "homeloan":
                    loan = HomeLoan(str(loancount), customer_id, principal_amount, interest_rate, loan_term_months, property_address, property_value)
                    loancount=loancount+1
                elif loan_type.lower() == "carloan":
                    loan = CarLoan(str(loancount), customer_id, principal_amount, interest_rate, loan_term_months, car_model, car_value)
                    loancount=loancount+1
                else:
                    print("Invalid loan type.")
                    continue
                loan_repo.apply_loan(loan)

            elif choice == "2":
                # Calculate Interest
                loan_id = input("Enter Loan ID: ")
                interest = loan_repo.calculate_interest(loan_id)
                print(f"Interest Amount: {interest}")

            elif choice == "3":
                # Check Loan Status
                loan_id = input("Enter Loan ID: ")
                loan_repo.loan_status(loan_id)

            elif choice == "4":
                # Calculate EMI
                loan_id = input("Enter Loan ID: ")
                emi = loan_repo.calculate_emi(loan_id)
                print(f"EMI Amount: {emi}")

            elif choice == "5":
                # Loan Repayment
                loan_id = input("Enter Loan ID: ")
                amount = float(input("                Enter Amount for Repayment: "))
                loan_repo.loan_repayment(loan_id, amount)

            elif choice == "6":
                # Get All Loans
                loan_repo.get_all_loan()

            elif choice == "7":
                # Get Loan by ID
                loan_id = input("Enter Loan ID: ")
                loan_repo.get_loan_by_id(loan_id)

            elif choice == "8":
                # Exit
                print("Exiting Loan Management System.")
                break
            
            else:
                print("Invalid choice. Please try again.")

if __name__ == "__main__":
    LoanManagement.main()