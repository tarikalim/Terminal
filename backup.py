import subprocess
from datetime import datetime

def yedek_al():
    try:
        user = ''
        password = ''
        host = ''
        database = ''

        yedek_tarih = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
        yedek_dosya = f"db_backup_{yedek_tarih}.sql"

        mysqldump_command = f"/usr/bin/mysqldump -u {user} -p{password} -h {host} {database} > {yedek_dosya}"

        subprocess.run(mysqldump_command, shell=True, check=True)

    except subprocess.CalledProcessError as err:
        print(f"Hata: {err}")

if __name__ == "__main__":
    yedek_al()
