import redis


class database_redit():
    def __init__(self,redis_cli):
        self.redis_cli = redis_cli


    def print_keys(self):
        for i in self.redis_cli.keys():
            print(i)
   
    def hset_value(self,value):
        try:
            self.redis_cli.hset(value[0], mapping={
            'url': value[1],
            "text": value[2],
            "date": value[3]
            })
        except Exception as e:
            print(f"Error: {e}")
        

    def hgetall(self,key):
        items = self.redis_cli.hgetall(key).items()

        if(len(items) !=0):
            print(key)
            for keys,values in items:
                print(keys + ": " + values)
        else:
            print("Nieznaleziono klucza")
        
    def delete_key(self,key):
        self.redis_cli.delete(key)

    def save_database_to_file(self):
        self.redis_cli.bgsave("C:/Users/niewi/Desktop/bazydanychprojekt/dump")
        while True:
            if self.redis_cli.info('persistence')['rdb_bgsave_in_progress'] == 0:
                break


