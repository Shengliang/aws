SN=${1:-42}
Q=https://sqs.us-east-1.amazonaws.com/586893569188/test
F=msg.json
python3 qSend.py -j $F -q $Q -s $SN



