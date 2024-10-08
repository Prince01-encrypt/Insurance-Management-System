from dao.insurance_service_impl import InsuranceServiceImpl
from entity.policy import Policy
from exception.policy_exception import PolicyNotFoundException

class PolicyManagement :
    def __init__(self) :
        self.insurance_service = InsuranceServiceImpl()

    def menu(self) :
        while True :
            print("\n===== Policy Management System Menu =====")
            print("1. Create Policy")
            print("2. Get Policy by ID")
            print("3. Get All Policies")
            print("4. Update Policy")
            print("5. Delete Policy")
            print("6. Exit")

            choice = input("Enter your choice : ")

            if choice == '1':
                self.createPolicy()
            elif choice == '2':
                self.getPolicy()
            elif choice == '3':
                self.getAllPolicies()
            elif choice == '4':
                self.updatePolicy()
            elif choice == '5':
                self.deletePolicy()
            elif choice == '6':
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")

    def createPolicy(self):
        try:
            policy_id = int(input("Enter policy ID : "))
            policy_name = input("Enter policy name : ")
            premium_amount = float(input("Enter premium amount : "))
            coverage_amount = float(input("Enter coverage amount : "))

            policy = Policy(policy_id, policy_name, premium_amount, coverage_amount)
            result = self.insurance_service.createPolicy(policy)
            if result:
                print("Policy created successfully.")
            else:
                print("Failed to create policy.")
        except Exception as e:
            print(f"Error while creating policy : {e}")

    def getPolicy(self):
        try:
            policy_id = int(input("Enter policy ID : "))
            policy = self.insurance_service.getPolicy(policy_id)
            if policy:
                print(policy)
        except Exception as e:
            print(f"Error while fetching policy : {e}")

    def getAllPolicies(self):
        try:
            policies = self.insurance_service.getAllPolicies()
            if policies:
                print("\nAll Policies:")
                for policy in policies:
                    print(policy)
            else:
                print("No policies found.")
        except Exception as e:
            print(f"Error while fetching all policies : {e}")

    def updatePolicy(self):
        try:
            policy_id = int(input("Enter policy ID to update : "))
            policy = self.insurance_service.getPolicy(policy_id)
            if policy:
                print("Current policy details :", policy)

                # Updating fields
                new_name = input(f"Enter new policy name (current: {policy.get_policyName()}) : ") or policy.get_policyName()
                new_premium = float(input(f"Enter new premium amount (current: {policy.get_premiumAmount()}) : ") or policy.get_premiumAmount())
                new_coverage = float(input(f"Enter new coverage amount (current: {policy.get_coverageAmount()}) : ") or policy.get_coverageAmount())

                # Updating object
                policy.set_policyName(new_name)
                policy.set_premiumAmount(new_premium)
                policy.set_coverageAmount(new_coverage)

                result = self.insurance_service.updatePolicy(policy)
                if result:
                    print(f"Policy {policy_id} updated successfully.")
                else:
                    print("Failed to update policy.")
            else:
                print(f"Policy with ID {policy_id} not found.")
        except Exception as e:
            print(f"Error while updating policy : {e}")

    def deletePolicy(self):
        try:
            policy_id = int(input("Enter policy ID to delete : "))
            result = self.insurance_service.deletePolicy(policy_id)
            if result:
                print(f"Policy {policy_id} deleted successfully.")
            else:
                print(f"Failed to delete policy with ID {policy_id}.")
        except Exception as e:
            print(f"Error while deleting policy : {e}")

def main():
    policy_management = PolicyManagement()
    policy_management.menu()

if __name__ == "__main__" :
    main()