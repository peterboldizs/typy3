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
