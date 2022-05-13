
import json


def Remove_JsonElement(ele):

    with open('test_payload.json') as f1:
        obj = json.load(f1)
  
    if ele == 'planselect_1' or ele == 'retdt' or ele == 'appdate' or ele == 'statecode' or ele == 'deptdt':
        print("i ma here")
        for key in obj['inParams']:
             
            if key == ele:
                obj['inParams'].pop(key)
                break


    if ele == 'spreadsheetName' or ele == 'outParams' or ele == 'sessionId' or ele == 'inParams':
    
        for key in obj:
        
            if key == ele:
                obj.pop(key)
                break
        

            
    with open('output_payload.json', 'w') as fp:
        json.dump(obj, fp)


if __name__ == '__main__':

    val = input("enter element you want remove from json,EX : outParams,appdate:" )
    Remove_JsonElement(val)
    
