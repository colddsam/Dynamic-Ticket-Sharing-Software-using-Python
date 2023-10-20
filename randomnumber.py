import random
import uuid
email='dassamratkumar772@gmail.com'
def genunique(email):
    email=email.split("@")
    email=email[0]
    if len(email)<4:
        for num in range(4-len(email)):
            email+=str(num)
            num+=1
    email=email[:4]
    unique_id=email+str(random.randrange(1000,9999))
    return unique_id


def genuuid(name=None):
    return str(uuid.uuid4())