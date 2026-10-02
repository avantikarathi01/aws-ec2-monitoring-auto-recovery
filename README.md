# aws-ec2-monitoring-auto-recovery
AWS EC2 monitoring, CloudWatch alerting, SNS email notification, and Lambda-based automated recovery project.
# AWS EC2 Monitoring & Automated Recovery

A hands-on AWS project for monitoring an EC2 instance, detecting high CPU usage, sending email alerts, and automatically recovering the instance using AWS Lambda.

## Architecture

EC2
↓
CloudWatch Agent
↓
Amazon CloudWatch
↓
CloudWatch Alarm (>70% CPU)
↓
┌───────────────┬────────────────────┐
↓               ↓
SNS Email       AWS Lambda
Alert            ↓
                 EC2 Reboot

## AWS Services Used

- Amazon EC2
- Amazon CloudWatch
- CloudWatch Agent
- Amazon SNS
- AWS Lambda
- AWS IAM

## Project Workflow

1. An Ubuntu EC2 instance is launched.
2. CloudWatch Agent is installed on the EC2 instance.
3. The agent sends CPU, memory and disk metrics to CloudWatch.
4. A CloudWatch Alarm monitors CPU utilization.
5. If CPU usage goes above 70%, the alarm enters the `In Alarm` state.
6. Amazon SNS sends an email notification.
7. AWS Lambda is invoked automatically.
8. Lambda initiates an EC2 reboot for automated recovery.

## Monitoring

The CloudWatch Agent collects:

- CPU usage
- Memory usage
- Disk usage

Custom CloudWatch namespace:

`AWS/EC2/MonitoringProject`

## Alert Configuration

CloudWatch Alarm:

- Alarm Name: `EC2-High-CPU`
- Statistic: Average
- Period: 1 minute
- Threshold: CPU > 70%
- Datapoints: 1 out of 1

## Lambda Auto Recovery

The Lambda function uses the AWS SDK (`boto3`) to initiate an EC2 reboot.

The public version of the Lambda code uses a placeholder for the EC2 instance ID to avoid exposing infrastructure details.

## Testing

The monitoring and recovery workflow was tested by generating CPU load on the EC2 instance.

The test successfully triggered:

- CloudWatch Alarm
- SNS email notification
- Lambda execution
- EC2 reboot/recovery

## Repository Structure

```text
aws-ec2-monitoring-auto-recovery/
│
├── README.md
│
├── lambda/
│   └── ec2_auto_recovery.py
│
├── cloudwatch/
│   └── agent-config.json
│
├── architecture/
│   └── aws-architecture.png
│
└── screenshots/
    ├── cloudwatch-metrics.png
    ├── alarm-triggered.png
    ├── sns-email.png
    ├── lambda-success.png
    └── ec2-recovery.png

Security
- No AWS access keys or secret keys are stored in this repository.
- Infrastructure-specific information should be removed from public screenshots.
- IAM permissions should follow the principle of least privilege where possible.
Key Concepts Learned
- EC2 monitoring
- CloudWatch custom metrics
- CloudWatch Alarms
- SNS notifications
- AWS Lambda
- IAM roles and permissions
- Event-driven automation
- Automated EC2 recovery
