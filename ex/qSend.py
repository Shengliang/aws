
import json
import argparse
import boto3
from botocore.exceptions import NoCredentialsError, PartialCredentialsError

def send_message_to_sqs(json_file_path, queue_url, seq_number=None):
    # Create SQS client
    sqs = boto3.client('sqs')

    try:
        # Read the JSON file
        with open(json_file_path, 'r') as file:
            message_body = json.load(file)

        # Update SeqNumber if provided
        if seq_number is not None:
            message_body['SeqNumber'] = seq_number

        # Send message to SQS queue
        response = sqs.send_message(
            QueueUrl=queue_url,
            MessageBody=json.dumps(message_body)
        )

        print(f"Message sent to SQS with ID: {response['MessageId']}")

    except FileNotFoundError:
        print(f"The file '{json_file_path}' was not found.")
    except json.JSONDecodeError:
        print(f"The file '{json_file_path}' does not contain valid JSON.")
    except NoCredentialsError:
        print("AWS credentials not available.")
    except PartialCredentialsError:
        print("Incomplete AWS credentials provided.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="Send a JSON message to an SQS queue.")
    parser.add_argument('-j', '--json', required=True, help="Path to the JSON message file.")
    parser.add_argument('-q', '--queue_url', required=True, help="SQS queue URL.")
    parser.add_argument('-s', '--seq_number', type=int, help="Sequence number to update in the JSON message.")
    args = parser.parse_args()

    # Call the function with provided arguments
    send_message_to_sqs(args.json, args.queue_url, args.seq_number)

