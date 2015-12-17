
import boto
#it's going to be ugly, but it'll work

def init_ec2_conn():
def init_elb_conn():
def create_ec2_instance(ec2, number):
def create_load_balancer(ec2):
def get_instances(ec2):
    instances = ec2.get_all_reservatons()
    for instance in instances:
        print instance.name
if __name__ == '__main__':
    
