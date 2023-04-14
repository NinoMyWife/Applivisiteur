from hashlib import sha512

mdp = 'azerty'

mdp = mdp.encode()

mdp_sign = sha512(mdp).hexdigest()

print (mdp_sign)