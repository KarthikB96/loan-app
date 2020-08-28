Camino Financial Backend Take Home Challenge

The Objective of the project was to create two api calls, one for accepting the input json and create a new loan application for that company and second to check the status of that application.

loanapp api: For LoanApp API, the following models were created
  1. Address
  2. Owners
  3. Business
  4. Application
  
In loanapp api we parse the json string and check if that business has already applied if so we update the values else we create a new record and add it to our database. if updated, the update field in business is set to true.

In status api, i am assuming that the filter_id field in the json is unique. I get the application from the database and return the status field and the upated field along with the loan amount of that application

Finally, dockerfile is created to create the container for the project.
