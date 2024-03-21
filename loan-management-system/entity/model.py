from abc import ABC, abstractmethod

class Customer:
    def __init__(self, customer_id, name, email, phone_number, address, credit_score):
        self.customer_id = customer_id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.address = address
        self.credit_score = credit_score

    def __str__(self):
        return f"Customer ID: {self.customer_id}\nName: {self.name}\nEmail: {self.email}\nPhone Number: {self.phone_number}\nAddress: {self.address}\nCredit Score: {self.credit_score}"

class Loan(ABC):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, loan_type, loan_status):
        self.loan_id = loan_id
        self.customer_id = customer_id
        self.principal_amount = principal_amount
        self.interest_rate = interest_rate
        self.loan_term_months = loan_term_months
        self.loan_type = loan_type
        self.loan_status = loan_status

    @abstractmethod
    def calculate_interest(self):
        pass

    @abstractmethod
    def calculate_emi(self):
        pass

    @abstractmethod
    def loan_repayment(self, amount):
        pass

class HomeLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, property_address, property_value):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term_months, "HomeLoan", "Pending")
        self.property_address = property_address
        self.property_value = property_value

    def calculate_interest(self):
        return (self.principal_amount * self.interest_rate * self.loan_term_months) / 12

    def calculate_emi(self):
        R = self.interest_rate / 12 / 100
        N = self.loan_term_months
        EMI = (self.principal_amount * R * (1+R)**N) / ((1+R)**N - 1)
        return EMI

    def loan_repayment(self, amount):
        no_of_emi = amount / self.calculate_emi()
        return int(no_of_emi)

class CarLoan(Loan):
    def __init__(self, loan_id, customer_id, principal_amount, interest_rate, loan_term_months, car_model, car_value):
        super().__init__(loan_id, customer_id, principal_amount, interest_rate, loan_term_months, "CarLoan", "Pending")
        self.car_model = car_model
        self.car_value = car_value

    def calculate_interest(self):
        return (self.principal_amount * self.interest_rate * self.loan_term_months) / 12

    def calculate_emi(self):
        R = self.interest_rate / 12 / 100
        N = self.loan_term_months
        EMI = (self.principal_amount * R * (1+R)**N) / ((1+R)**N - 1)
        return EMI

    def loan_repayment(self, amount):
        no_of_emi = amount / self.calculate_emi()
        return int(no_of_emi)