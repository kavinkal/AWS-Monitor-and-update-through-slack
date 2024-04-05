# Designing an Automatic Data Collection and Storage System with AWS Lambda and Slack Integration for Server Availability Monitoring and Slack Notification

1. created the AWS lambda function to fetch the data from API and stored in RDS.
2. For automatic data collection from API. Trigger the lambda function with cloudwatch event for every 15 seconds. (cloud watch 
   event(rule creation))(setting alarm if the threashold value is set to 0 )
3. created one more lambda function to send notification through slack.
4. used slack webhook api to communicate with lambda function.
5. created rule to check the threshold of the event in lambda function then,trigger the lambda function if the value matches.
6. Integrating the alarm with Amazon SNS to send a message through slack if server goes down.
7. Finally, if the lambda function face any issue every 15 seconds. In slack notification would trigger based on the cloud watch event.



