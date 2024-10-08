SQL Schemas

CREATE DATABASE InsuranceManagementSystem; USE InsuranceManagementSystem;

CREATE TABLE Users (userId INT PRIMARY KEY, username VARCHAR(85), password VARCHAR(85), role VARCHAR(20));

CREATE TABLE Policy (policyId INT PRIMARY KEY, policyName VARCHAR(85), premiumAmount DECIMAL(12, 2), coverageAmount DECIMAL(12, 2));

CREATE TABLE Client (
    clientId INT PRIMARY KEY, clientName VARCHAR(120), contactInfo VARCHAR(120), policyId INT);

CREATE TABLE Claim (
    claimId INT PRIMARY KEY, claimNumber VARCHAR(85), dateFiled DATE, claimAmount DECIMAL(12, 2), status VARCHAR(20), policyId VARCHAR(85), clientId INT, CONSTRAINT FK_Claim_Client FOREIGN KEY (clientId) REFERENCES Client(clientId));

CREATE TABLE Payment (
    paymentId INT PRIMARY KEY, paymentDate DATE, paymentAmount DECIMAL(10, 2), clientId INT, CONSTRAINT FK_Payment_Client FOREIGN KEY (clientId) REFERENCES Client(clientId));

  REFERENCE SCREENSHOTS :

1. Creating Policy

![Screenshot 2024-10-08 154232](https://github.com/user-attachments/assets/af9f40de-8a71-42fc-bd2f-b61a3f45c4f3)
![image](https://github.com/user-attachments/assets/cf69c096-5d80-40d6-a374-b344fb2c9166)

2. Get Policy by ID

![Screenshot 2024-10-08 154329](https://github.com/user-attachments/assets/0c74196e-d519-49b5-bbc0-54ff78c7adb9)
![image](https://github.com/user-attachments/assets/6ad0d2b9-875d-4bd9-b2e1-6c8b435ee4b5)

3. Get All Policies

![Screenshot 2024-10-08 154357](https://github.com/user-attachments/assets/dedcf303-cfa6-4295-8349-01a7135d1bf5)
![image](https://github.com/user-attachments/assets/67bcc0cb-a916-4764-b958-4da42737348c)

4. Updating Policy
   
![Screenshot 2024-10-08 154638](https://github.com/user-attachments/assets/d1f1c968-769a-47d3-ba57-c391ddce4c6d)
![image](https://github.com/user-attachments/assets/df71fb4a-94ea-406a-9707-8bd589a8c579)

5. Deleting Policy

![Screenshot 2024-10-08 154710](https://github.com/user-attachments/assets/b65769b0-1a51-4fb8-974f-105c8cff8031)
![image](https://github.com/user-attachments/assets/4075b992-1e32-42fe-8a5e-4f5e49e31095)

6. Policy Not Found Exception

![Screenshot 2024-10-08 154802](https://github.com/user-attachments/assets/c4ffdae9-2b8b-45d3-b698-0bb429b86f70)

7. Exit
    
![Screenshot 2024-10-08 154850](https://github.com/user-attachments/assets/66f6df61-4ee9-442e-a6dc-81ae6aae0ec5)












