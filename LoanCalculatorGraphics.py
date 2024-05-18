#importing th required libraries

from PyQt5.QtWidgets import *
from PyQt5 import QtCore, QtGui
from PyQt5.QtCore import *
from PyQt5.QtGui import *

import sys


#main class

class Window(QMainWindow):
	#constructor method
	def __init__(self):
		#inheriting the super class methods QMainWindow
		super().__init__()
		#setting the tittle of the window
		self.setWindowTitle("LOAN CALCULATOR ")
		# setting the geomtery of the app
		self.width = 400
		self.height = 800
		self.setGeometry(100,100 , self.width ,self.height)
		self.UIComponents()  # Call the UIComponents method to create the UI
		#showing the window
		self.show()

	#function to add widgets
	def UIComponents(self):
		# head label 
		head = QLabel("LOAN CALCULATOR\n",self)
		head.setGeometry(0,10,400,60)
		font = QFont('Times',15)
		font.setBold(True)
		head.setFont(font)
		head.setAlignment(Qt.AlignCenter)
		color = QGraphicsColorizeEffect(self)
		color.setColor(Qt.darkBlue)
		head.setGraphicsEffect(color)


		#amount label 
		a_label = QLabel("Loan amount (DH)"  , self)
		# properties of the amount label
		a_label.setAlignment(Qt.AlignCenter)
		a_label.setGeometry(20,100,170,40)
		a_label.setStyleSheet( "QLabel" "{" 
											"border : 2px solid black ;"
											"background : rgba(70,70,70,35);"
											"}")
		a_label.setFont(QFont('Times',9))

		#input field for the amount  
		self.amount = QLineEdit(self)
		#for the validation in the input
		onlyInt = QIntValidator()
		self.amount.setValidator(onlyInt)
			#setting the properties of the input
		self.amount.setGeometry(200,100,180,40) #X = 200 Y = 100 width = 180 height = 40
		self.amount.setAlignment(Qt.AlignCenter)
		self.amount.setFont(QFont('Times',9))



		#--------------------------------------#

		# interest label
		i_label = QLabel("Loan interest  "  , self)
		# properties of the interest label
		i_label.setAlignment(Qt.AlignCenter)
		i_label.setGeometry(20,200,170,40)
		i_label.setStyleSheet( "QLabel" "{" 
											"border : 2px solid black ;"
											"background : rgba(70,70,70,35)"
											"}")
		i_label.setFont(QFont('Times',9))
	

		#input field for the interest rate
		self.rate = QLineEdit(self)
			#setting the properties of the input
		self.rate.setGeometry(200,200,180,40) #X = 200 Y = 100 width = 180 height = 40
		self.rate.setAlignment(Qt.AlignCenter)
		self.rate.setFont(QFont('Times',9))

		#--------------------------------------#
      
	  	# loan term label
		term_label = QLabel("Loan term (months) "  , self)
		# properties of the loan term label
		term_label.setAlignment(Qt.AlignCenter)
		term_label.setGeometry(20,300,170,40)
		term_label.setStyleSheet( "QLabel" "{" 
											"border : 2px solid black ;"
											"background : rgba(70,70,70,35)"
											"}")
		term_label.setFont(QFont('Times',9))
	

		#input field for loan term rate
		self.term = QLineEdit(self)
			#for the validation in the input
		onlyInt = QIntValidator()
		self.term.setValidator(onlyInt)
			#setting the properties of the input
		self.term.setGeometry(200,300,180,40) #X = 200 Y = 100 width = 180 height = 40
		self.term.setAlignment(Qt.AlignCenter)
		self.term.setFont(QFont('Times',9))


		#--------------------Calculating payment ------------------#
		# button that calculate the payement 
		calculate  =  QPushButton("Calculate payment", self)
		# set geometry
		calculate.setGeometry(125,400,150,40)
		#add action to calculate button
		calculate.clicked.connect(self.calculate_action)


		#-------------------Resetting----------------------------#
		# button that calculate the payement 
		reset  =  QPushButton("reset", self)
		# set geometry
		reset.setGeometry(125,450,150,40)
		#add action to calculate button
		reset.clicked.connect(self.reset_action)
		
		#-----------Output widgets------------------------
		#monthly payement 
		self.m_payement = QLabel(self)
		# properties of the payement
		self.m_payement.setAlignment(Qt.AlignCenter)
		self.m_payement.setGeometry(50,500,300,60)
		self.m_payement.setStyleSheet( "QLabel" "{" 
											"border : 3px solid black ;"
											"background :white"
											"}")
		self.m_payement.setFont(QFont('Times',11))

		#yearly payement 
		self.y_payement = QLabel(self)
		# properties of the payement
		self.y_payement.setAlignment(Qt.AlignCenter)
		self.y_payement.setGeometry(50,600,300,60)
		self.y_payement.setStyleSheet( "QLabel" "{" 
											"border : 3px solid black ;"
											"background :white"
											"}")
		self.y_payement.setFont(QFont('Times',11))

	def calculate_action(self):

		loan_interest_rate = self.rate.text()
			
		#check if the fields are empty
		if len(loan_interest_rate) == 0 or loan_interest_rate == '0' :
			QMessageBox.critical(self,"Alert!","Fill the loan interest ")
		
			
		loan_amount = self.amount.text()
		if len(loan_amount) == 0 or loan_amount == '0' :
			QMessageBox.critical(self,"Alert!","Fill the loan amount")

		
		loan_term = self.term.text()
		if len(loan_term) == 0 or loan_term == '0' :
			QMessageBox.critical(self,"Alert!","Fill the loan term")

		loan_interest_rate =float(loan_interest_rate)
		loan_amount  = int(loan_amount)
		loan_term = int(loan_term)

		loan_interest = loan_interest_rate / 100
		#Calculate the monthly payement
		monthly_payment =  (loan_amount * loan_interest_rate / 12) / (1 - (1 + loan_interest / 12) ** -loan_term)
		#Define the format of the monthly payemenr
		monthly_payement = "{:.2f}".format(monthly_payment)
		# add text to monthly payement and 
		self.m_payement.setText("Monthly payement : " + str(monthly_payement) + "DH")

		# yearly_payement = monthly_payement * 12
		# yearly_payement = "{:.2f}".format(yearly_payement)
		# self.y_payement.setText("Yearly payement : " + str(yearly_payement) + "DH")


		yearly_payment = monthly_payment * 12
		yearly_payment = "{:.2f}".format(yearly_payment)
		self.y_payement.setText("Yearly payment : " + str(yearly_payment) + " DH")

	def reset_action(self):
		self.amount.clear()
		self.rate.clear()
		self.term.clear()
		self.m_payement.clear()
		self.y_payement.clear()


		

# Create app object 
App = QApplication(sys.argv)  # this command calls the c++ constructor and passes the argv arguments in it to initialize the Qtapp  

#instantiate the window class
window = Window()

#start the app
sys.exit(App.exec())  # this starts the event loop and blocks everything else


