from dao.i_policy_service import IPolicyService
from entity.policy import Policy
from util.db_connection import DBConnection
from exception.policy_exception import PolicyNotFoundException


class InsuranceServiceImpl(IPolicyService):
    def __init__(self):
        self.connection = DBConnection.getConnection() 

    def createPolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()

            query = """INSERT INTO Policy (policyId, policyName, premiumAmount, coverageAmount)
                       VALUES (?, ?, ?, ?)"""
            cursor.execute(query, (policy.get_policyId(), policy.get_policyName(),
                                   policy.get_premiumAmount(), policy.get_coverageAmount()))

            self.connection.commit()
            return True

        except Exception as e:
            print(f"Error while creating policy: {e}")
            return False

    def getPolicy(self, policyId: int):
        try:
            cursor = self.connection.cursor()

            query = """SELECT * FROM Policy WHERE policyId = ?"""
            cursor.execute(query, (policyId,))
            row = cursor.fetchone()

            if row:
                policy = Policy(row[0], row[1], row[2], row[3])
                return policy
            else:
                raise PolicyNotFoundException(f"Policy with ID {policyId} not found.")

        except PolicyNotFoundException as e:
            print(e)
            return None

        except Exception as e:
            print(f"Error while fetching policy: {e}")
            return None

    def getAllPolicies(self):
        try:
            cursor = self.connection.cursor()

            query = """SELECT * FROM Policy"""
            cursor.execute(query)
            rows = cursor.fetchall()

            policies = []
            for row in rows:
                policy = Policy(row[0], row[1], row[2], row[3])
                policies.append(policy)

            return policies

        except Exception as e:
            print(f"Error while fetching all policies: {e}")
            return []

    def updatePolicy(self, policy: Policy):
        try:
            cursor = self.connection.cursor()

            query = """UPDATE Policy
                       SET policyName = ?, premiumAmount = ?, coverageAmount = ?
                       WHERE policyId = ?"""
            cursor.execute(query, (policy.get_policyName(), policy.get_premiumAmount(),
                                   policy.get_coverageAmount(), policy.get_policyId()))

            self.connection.commit()
            return True

        except Exception as e:
            print(f"Error while updating policy: {e}")
            return False

    def deletePolicy(self, policyId: int):
        try:
            cursor = self.connection.cursor()

            query = """DELETE FROM Policy WHERE policyId = ?"""
            cursor.execute(query, (policyId,))

            self.connection.commit()
            return True

        except Exception as e:
            print(f"Error while deleting policy: {e}")
            return False
