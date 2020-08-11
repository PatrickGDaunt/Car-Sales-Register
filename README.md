# Car Sales Register App

## Table of contents
* [General Info](#general-info)
* [Technologies](#technologies)
* [Setup](#setup)

## General info
* Records car sales and relevant data (make, model, year, sales person, sale price) to a local SQL database

## Technologies
* Project is created with:
	* Python 3.7
 	* Requests package
 	* mySQL package

## Setup
* Install XAMPP (https://www.apachefriends.org/download.html). 
	* XAMPP provides local access to PHPMyAdmin.
	* PHPAdmin is a data administration tool
* Run XAMPP
	* Start the Apache and MySQL modules
	* Enter "http://localhost/phpmyadmin" in your local web browser
* Create a new SQL database called "c4v"
* Select the SQL tab and copy the following line:
	* CREATE TABLE assignment4 (carMake TEXT, carModel TEXT, carYear TEXT, salesPerson TEXT, salesPrice TEXT, timestamp TIMESTAMP, PRIMARY KEY(timestamp));
	* click the "go" button
* Run CarSalesRegister.exe within the dist file
