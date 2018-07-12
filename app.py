import jenkins
import devCreds

server = jenkins.Jenkins(devCreds.jenkins_url, username=devCreds.username, password=devCreds.password)

user = server.get_whoami()
version = server.get_version()

all_jobs = server.get_jobs()
job_count = server.jobs_count()

print(job_count)