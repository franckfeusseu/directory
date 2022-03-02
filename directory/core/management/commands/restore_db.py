from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = (
        "Restore the database ."
        "Expects database backup file -)"
    )

    def add_arguments(self, parser):
        parser.add_argument("file_path", nargs=1, type=str)

    def handle(self, **options):
        self.file_path = options["file_path"][0]
        self.prepare()
        self.main()
        self.finalize()

    def prepare(self):
        pass

    def main(self):
        pass

    def finalize(self):
        pass