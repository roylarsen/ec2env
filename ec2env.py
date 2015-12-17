import boto.ec2, boto.ec2.elb
#it's going to be ugly, but it'll work

#returns ec2 connection
def init_ec2_conn():
    conn = boto.ec2.connect_to_region('us-east-1')
    return conn

#returns elb connection
def init_elb_conn():
    elb = boto.ec2.elb.onnect_to_region('us-east-1')
    return elb

#creates amount of EC2 instances
def create_ec2_instance(ec2, number):
    ec2.run_instances('ami-60b6c60a',key_name='aws_do_key',instance_type='t2.micro',max_count=number,security_groups=['do-ssh'])

#creates load balancer for EC2 instances
def create_load_balancer(elb, instances):
    pass
#returns names of EC2 instances
def get_instances(ec2):
    instances = ec2.get_all_reservations()
    return instances[0].instances

#Main PRogram flow
if __name__ == '__main__':
    ec2 = init_ec2_conn()
    elb = init_elb_conn()
    create_ec2_instance(ec2, 2)
    instances = get_instances(ec2)
