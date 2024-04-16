from typing import List, Any

from models import Author, Quote


def find_by_author(author: str) -> list[list[Any]]:
    print(f"Find by: {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result


def find_by_tag(tag: str) -> list[str | None]:
    print(f"Find by {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [e.to_json() for e in quotes]
    return result


def find_by_tags(tags: str) -> list[str | None]:
    print(f"Find by {tags}")
    quotes = Quote.objects(tags__in=tags)
    result = [e.to_json() for e in quotes]
    return result
