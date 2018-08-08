#read a sqs receive messsage
import boto3
import json
client = boto3.client('sqs')
response = client.receive_message(QueueUrl='https://sqs.us-west-1.amazonaws.com/112367390792/s3-to-sns-emailsqs')
print(response)
print(type(response))
for messages in response["Messages"]:
    print("msg_body:", messages['Body'])
    msg=messages['Body']
    #print(type(msg))
    receive_msg=json.loads(msg)
    print("Message is:",receive_msg)
    print(type(receive_msg))
    print(receive_msg['Message'])

#download' the s3 object uploaded:
    client2 = boto3.client('s3')
    message=receive_msg['Message']
    print(type(message))
    s3=json.loads(message)['Records'][0]['s3']
    print("s3:",s3)
    #print(type(s3))
    bucket=s3['bucket']['name']
    key=s3['object']['key']
    print(bucket,key)
    res = client2.download_file(bucket, key, '/home/ec2-user/key')
    print(res)

# receive message is deleted:
    message = response['Messages'][0]
    receipt_handle = message['ReceiptHandle']
    r2 = client.delete_message(QueueUrl='https://sqs.us-west-1.amazonaws.com/112367390792/s3-to-sns-emailsqs',ReceiptHandle=receipt_handle)
    print(r2)

