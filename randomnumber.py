import random
import uuid
def genunique(email=""):
    email=email.split("@")
    email=email[0]
    if len(email)<2:
        for num in range(2-len(email)):
            email+=str(num)
            num+=1
    email=email[:2]
    unique_id=email+str(random.randrange(100,999))
    unique_id="DEVFEST-"+unique_id+"-GDGDGP23"
    return unique_id


def genuuid(name=None):
    return str(uuid.uuid4())