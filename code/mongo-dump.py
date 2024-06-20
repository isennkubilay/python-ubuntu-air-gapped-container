import subprocess
import os

# Create a client connection to your MongoDB instance
uri = 'mongodb://admin:12345@192.168.1.1:27017/deneme'

# Define your database name, and output directory
database_name = 'deneme'
output_dir = '/media/py'

# Construct the mongodump command
command = f'mongodump --uri {uri} --db {database_name} --out {output_dir}'
# command2 = f"mongodump --uri '${uri}' --gzip --archive=${output_dir}/mongodump-$(date '+%Y-%m-%d-%H-%M').gz"

# Run the command
os.system(command)
