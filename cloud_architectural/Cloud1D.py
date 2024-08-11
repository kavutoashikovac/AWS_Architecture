from diagrams import Diagram, Cluster
from diagrams.aws.compute import EC2Instance, AutoScaling
from diagrams.aws.database import RDS
from diagrams.aws.network import ELB, Route53, VPC, CloudFront
from diagrams.aws.security import FMS, WAF
from diagrams.aws.storage import S3

with Diagram("GameNook AWS Architecture", show=False):

    with Cluster("Region"):
        with Cluster("VPC"):
            igw = Route53("Internet Gateway")
            nat = AutoScaling("NAT Gateway")
            fw = FMS("Firewall")
            sub1 = VPC("Public Subnet")
            sub2 = VPC("Private Subnet")

            igw >> sub1 >> [ELB("Load Balancer"), fw]
            sub2 >> [EC2Instance("Web Server 1"), EC2Instance("Web Server 2")]

            with Cluster("Database"):
                db = RDS("Database Server")
                db >> S3("Game Data Storage")

