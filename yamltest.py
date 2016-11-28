__author__ = 'fnxuser'
import yaml

with open("config.yml", 'r') as ymlfile:
    cfg = yaml.load(ymlfile)

for section in cfg:
    print(section)

print(cfg['queue_manager'])
print(cfg['queue_manager']['name'])
print(cfg['queue_manager']['host'])
print(cfg['mq_user'])
print(cfg['query_queue'])

print("service config:")
with open('be-services.yml', 'r') as ymlfile:
    scfg = yaml.load(ymlfile)

print(scfg['javabackend']['name'])
print(scfg['javabackend']['user'])
print(scfg['javabackend']['passwd'])

java = scfg['javabackend']
for p in java:
    print(p)

jser = scfg['javabackend']['service']
for s in jser:
    print(s)

baseurl = scfg['javabackend']['service']['base']
op_allcust = scfg['javabackend']['service']['ops']['allcust']
print("url:")
print(baseurl + op_allcust)
