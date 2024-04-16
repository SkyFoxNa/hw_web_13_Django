import random
from openai import OpenAI
from django.conf import settings
from ..models import Author, Tag, Quote


client = OpenAI(api_key=settings.OPEN_AI_KEY)


def ask_gpt(user_prompt: str) -> str:
    completion = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a writer-journalist. Write a quote from a famous person."},
            {"role": "user", "content": user_prompt}
        ]
    )
    return completion.choices[0].message.content


def generate_random_quote(user):
    print("Quote generator is started")
    all_authors = Author.objects.all()
    if all_authors:
        random_author: Author = random.choice(all_authors)
        user_prompt = f"Write a quote on behalf of {random_author.fullname}, the quote must be in English."
        quote = ask_gpt(user_prompt)
        print(quote)

        tags_list = []
        rfind_index = quote.rfind('"')
        lfind_index = quote.find('"')
        clear_quote = quote[lfind_index + 1:rfind_index]
        tag_count = random.randint(3, 5)
        all_words = [word for word in clear_quote.split() if word.isalpha() and 4 <= len(word) <= 12]
        random.shuffle(all_words)
        target_tags = all_words[:tag_count]
        for tag in target_tags:
            t, *_ = Tag.objects.get_or_create(name=tag)
            tags_list.append(t)

        # quote_obj = Quote.objects.create(quote=clear_quote, author=random_author)
        quote_obj = Quote.objects.create(quote = clear_quote, author = random_author, user = user)
        for tag in tags_list:
            quote_obj.tags.add(tag)

        print("Quote has been added successfully")
        return True
    else:
        return False
