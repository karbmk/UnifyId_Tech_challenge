import sys
import random

script,filename = sys.argv

words = open(filename).read().split()

result_key = "-----BEGIN RSA PUBLIC KEY-----\n" #start of an RSA public key

for i in range(len(words)):
    result_key = result_key + words[i] + random.choice(['/','+','&','-','\n'])#embedding the random alphanumerics generated into the RSA format

result_key = result_key + "\n-----END RSA PUBLIC KEY-----"# ending a RSA public key

f = open('id_rsa.pub', 'w')
f.write(result_key)
f.close()
