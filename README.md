SQL Schemas

CREATE DATABASE InsuranceManagementSystem; USE InsuranceManagementSystem;

CREATE TABLE Users (userId INT PRIMARY KEY,username VARCHAR(85),password VARCHAR(85),role VARCHAR(20));

CREATE TABLE Policy (policyId INT PRIMARY KEY,policyName VARCHAR(85),premiumAmount DECIMAL(12, 2),coverageAmount DECIMAL(12, 2));

CREATE TABLE Client (
    clientId INT PRIMARY KEY,clientName VARCHAR(120),contactInfo VARCHAR(120),policyId INT);

CREATE TABLE Claim (
    claimId INT PRIMARY KEY,claimNumber VARCHAR(85),dateFiled DATE,claimAmount DECIMAL(12, 2),status VARCHAR(20),policyId VARCHAR(85),clientId INT,CONSTRAINT FK_Claim_Client FOREIGN KEY (clientId) REFERENCES Client(clientId));

CREATE TABLE Payment (
    paymentId INT PRIMARY KEY,paymentDate DATE,paymentAmount DECIMAL(10, 2),clientId INT,CONSTRAINT FK_Payment_Client FOREIGN KEY (clientId) REFERENCES Client(clientId));

  REFERENCE SCREENSHOTS :

1. Creating Policy

![image](https://github.com/user-attachments/assets/92ce6626-ff56-4963-9e6e-bfd4c3dff88e)
![image](https://github.com/user-attachments/assets/cf69c096-5d80-40d6-a374-b344fb2c9166)

2. Get Policy by ID
   
![image](https://github.com/user-attachments/assets/cf9c0a97-72df-4693-a43d-f8f3e3f2d162)
![image](https://github.com/user-attachments/assets/bd27e33d-22dc-4fd5-be40-d3db3a3f44d3)

3. Get All Policies
   
![image](https://github.com/user-attachments/assets/8766bc6c-7cd8-40d9-b693-0e0c8c0f7835)
![image](https://github.com/user-attachments/assets/ebc30b37-a8d1-4736-b2d1-fa58588136d0)

4. Updating Policy
   
![image](https://github.com/user-attachments/assets/ce8e3edb-40a5-457b-846a-1b78cee97576)
![image](https://github.com/user-attachments/assets/df71fb4a-94ea-406a-9707-8bd589a8c579)

5. Deleting Policy

![image](https://github.com/user-attachments/assets/dff59299-60ce-4d02-9061-a643bd399a77)
![image](https://github.com/user-attachments/assets/4075b992-1e32-42fe-8a5e-4f5e49e31095)

6. Policy Not Found Exception

![image](https://github.com/user-attachments/assets/f2c51d94-1673-4259-a0e5-75d43d20b9cd)

7. Exit
    
![image](https://github.com/user-attachments/assets/5c4eb1fb-ed31-4dee-bbf1-7fcb12014434)











