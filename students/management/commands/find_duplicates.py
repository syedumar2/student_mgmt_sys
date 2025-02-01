from django.core.management.base import BaseCommand
from students import Student

class Command(BaseCommand):
    help = 'Find duplicate USN values'

    def handle(self, *args, **kwargs):
        from django.db.models import Count

        duplicates = Student.objects.values('usn').annotate(usn_count=Count('usn')).filter(usn_count__gt=1)
        if duplicates:
            self.stdout.write("Duplicate USN values found:")
            for item in duplicates:
                self.stdout.write(f"USN: {item['usn']} - Count: {item['usn_count']}")
        else:
            self.stdout.write("No duplicate USN values found.")
