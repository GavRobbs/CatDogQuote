from .models import Quote

def populate_quotes():
    print("Going to populate the database with the quotes from the file")
    with open('quotes.txt') as quotefile:
        for line in quotefile.readlines():
            [qtext, author] = line.split('~')
            added_quote = Quote(text=qtext.rstrip(), author=author.rstrip())
            added_quote.save()

def delete_quotes():
    print("Deleting all the quotes in the database")
    Quote.objects.all().delete()