import web3storagepy

w3s = web3storagepy

# uploads the file and stores in the web3.storage IPFS system
upload = w3s.upload("text.txt", "eyJhbGci[REDACTED]pXVCJ9.eyJzdWIiOiJkaWQ6ZXRoc[REDACTED]FiZDdkMDVlZDgwMEI5RUIiL{REDACTED}3JhZ2UiLCJpYXQiOjE2Njk1N[REDACTED]ZDHKqSUZ8_k2C0NwQn0Oc")
print(upload)

# check status of the uploaded file using the CID and the token
status = w3s.status("[cid comes here]", "eyJhbGci[REDACTED]pXVCJ9.eyJzdWIiOiJkaWQ6ZXRoc[REDACTED]FiZDdkMDVlZDgwMEI5RUIiL{REDACTED}3JhZ2UiLCJpYXQiOjE2Njk1N[REDACTED]ZDHKqSUZ8_k2C0NwQn0Oc")
print(status)

# list previous uploads
all_uploads = w3s.user_uploads("eyJhbGci[REDACTED]pXVCJ9.eyJzdWIiOiJkaWQ6ZXRoc[REDACTED]FiZDdkMDVlZDgwMEI5RUIiL{REDACTED}3JhZ2UiLCJpYXQiOjE2Njk1N[REDACTED]ZDHKqSUZ8_k2C0NwQn0Oc")
print(all_uploads)

# retrieve an uploaded file with CID
get_file = w3s.get_upload("[cid comes here]")
print(get_file)

