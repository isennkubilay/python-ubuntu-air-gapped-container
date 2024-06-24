import subprocess
import os

def backup_postgresql_db(db_name, username, password, host, port, backup_file):
    # Set the environment variable for the PostgreSQL password
    os.environ['PGPASSWORD'] = password

    # Construct the pg_dump command
    pg_dump_command = [
        'pg_dump',
        '-U', username,
        '-h', host,
        '-p', str(port),
        db_name
    ]

    # Construct the gzip command
    gzip_command = ['gzip']

    # Open the backup file in write mode
    with open(backup_file, 'wb') as f_out:
        # Create the pg_dump subprocess
        pg_dump_process = subprocess.Popen(pg_dump_command, stdout=subprocess.PIPE)
        
        # Create the gzip subprocess
        gzip_process = subprocess.Popen(gzip_command, stdin=pg_dump_process.stdout, stdout=f_out)

        # Close pg_dump stdout to allow gzip to receive EOF
        pg_dump_process.stdout.close()

        # Wait for the processes to complete
        pg_dump_process.wait()
        gzip_process.wait()

    # Clean up the environment variable
    del os.environ['PGPASSWORD']

    print(f'Backup of database "{db_name}" completed successfully to {backup_file}')

# Example usage
backup_postgresql_db(
    db_name='postgres',
    username='postgres',
    password='12345',
    host='localhost',
    port=5432,
    backup_file='backup.sql.gz'
)
