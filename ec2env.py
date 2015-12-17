
import boto
#it's going to be ugly, but it'll work

#returns ec2 connection
def init_ec2_conn():
    conn = boto.ec2.connect_to_region('us-east-1')
    return conn
#returns elb connection
def init_elb_conn():
#creates amount of EC2 instances
def create_ec2_instance(ec2, number):
    ec2.run_instance('ami-60b6c60a',key_name='aws_do_key',instance_type='t2.micro',max_count=number)
#creates load balancer for EC2 instances
def create_load_balancer(ec2):
#returns names of EC2 instances
def get_instances(ec2):
    instances = ec2.get_all_reservatons()
    for instance in instances:
        print instance.name

if __name__ == '__main__':
    
