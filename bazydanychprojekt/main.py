import json
from redditapi import get_data_from_reddit_url
from redis_database import database_redit
import redis
import os

try:
    redis_cli = redis.Redis(
        host='localhost',
        port=6379,
        charset="utf-8",
        decode_responses=True
        )

    if(redis_cli.ping()):
        redis_connection = database_redit(redis_cli)

        x=0
        while x!="6":
            print("Wybierz działanie")
            print("1.Dodaj post do bazy danych")
            print("2.Wyswietl wszystkie klucze")
            print("3.Wyswietl post dla podanego klucza")
            print("4.Usuń post dla podanego klucza")
            print("5.Kliknij aby zapisać bazę danych")
            print("6.Kliknij aby wyłączyć program")
            x=input()
            if x=="1":
                plik = get_data_from_reddit_url(str(input("Podaj link: ")))
                redis_connection.hset_value(plik)
                
            elif x=="2":
                redis_connection.print_keys()
            elif x== "3":
                redis_connection.hgetall(input("Podaj klucz: "))
            elif x=="4":
                redis_connection.delete_key(input("Podaj klucz: "))
            elif x=="5":
                redis_connection.save_database_to_file()
         
    else:
        print("Nie udało się połączyć z bazą danych.")

except redis.ConnectionError:
    print("Błąd, nie można nawiązać połączenia z kontenerem")