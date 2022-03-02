import subprocess

from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = (
        " Create a simple backup file for the database."
    )

    def handle(self, **options):
        self.prepare()
        self.main()
        self.finalize()

    def prepare(self):
        pass

    def main(self):
        subprocess.run(["bash", "backup_db.sh"])

    def finalize(self):
        pass