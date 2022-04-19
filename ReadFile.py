import json

bankFile= open('./jsonFiles/bankDetail.json','r')
bankData=bankFile.read()
print(bankData)
#lods convert json data to dictionary object
bank_object=json.loads(bankData)
print(bank_object)
print(bank_object['BankDetail'])
print(bank_object['BankDetail']['Currency'])

bank_object['BankDetail']["name"]="Gurmeet singh"
bank_object['BankDetail']['Currency']="Dollar"
#lods convert dictioanry data to dictionary json
bank_object_json=json.dumps(bank_object)
print(bank_object_json)
bankFile.close()
bankupdatedFile=open('./jsonFiles/bankDetailupdated.json','w')
json.dump(bank_object,bankupdatedFile)
bankupdatedFile.close()

