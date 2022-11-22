import json
#author: arvind lavania

def searchReplacer(str, custom = False, params = {'search': '', 'replace': ''}):

    predefinedRules = {
        'Oracle': 'Oracle©',
        'Google': 'Google©',
        'Microsoft': 'Microsoft©',
        'Ibm': 'Ibm©',
        'Azure': 'Azure©',
        'Deloitte': 'Deloitte©',
        'DigitalOcean': 'DigitalOcean©',
    }

    finalStr = str

    if not custom:
        for key in predefinedRules.keys():
            finalStr = finalStr.replace(key + ' Cloud', key + ' Cloud©')
    else:
        finalStr = finalStr.replace(params['search'],params['replace'])

    return finalStr

def lambda_handler(event, context):
    if not event['body']:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "status": "error",
                "message": "Client Error: Request body is required",
            }),
        }

    reqBody = json.loads(event['body'])

    if 'target' not in reqBody or not reqBody['target']:
        return {
            "statusCode": 400,
            "body": json.dumps({
                "status": "error",
                "message": "Client Error: Missing fields",
                "fieldErrors": {
                    "target": '"target" field is required'
                }
            }),
        }

    if 'custom' not in reqBody or not reqBody['custom']:
        replacedString = searchReplacer(reqBody['target'])
    else:
        errorBody = {}
        if 'target' not in reqBody or not reqBody['target']:
            errorBody['target'] = '"target" field is required'
        if 'customSearchTerm' not in reqBody or not reqBody['customSearchTerm']:
            errorBody['customSearchTerm'] = '"customSearchTerm" field is required'
        if 'customReplaceTerm' not in reqBody or not reqBody['customReplaceTerm']:
            errorBody['customReplaceTerm'] = '"customReplaceTerm" field is required'

        if errorBody:
            return {
                "statusCode": 400,
                "body": json.dumps({
                    "status": "error",
                    "message": "Client Error: Missing fields",
                    "fieldErrors": errorBody
                }),
            }

        replacedString = searchReplacer(reqBody['target'],True,{'search': reqBody['customSearchTerm'], 'replace': reqBody['customReplaceTerm']})

    return {
        "statusCode": 200,
        "body": json.dumps({
            "status": "success",
            "response": {
                "replacedString": replacedString
            }
        })
    }
