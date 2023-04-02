#221RDB412 Kārlis Rūdolfs Birznieks


class Query:
    def __init__(self, query):
        self.type = query[0]
        self.number = int(query[1])
        if self.type == 'add':
            self.name = query[2]

class phone_book:
    size = 1000
    multiplier = 13

    def __init__(self):
        self.array = [None] * self.size

    def get_hash(self, key):
        hash = (key * self.multiplier) % self.size

        return hash
    
    def add(self, number, name):
        hash = self.get_hash(number)

        self.array[hash] = name

    def delete(self, number):
        hash = self.get_hash(number)

        self.array[hash] = None

    def find(self, number):
        hash = self.get_hash(number)

        if self.array[hash] == None:
            return 'not found'
        
        return self.array[hash]


def read_queries():
    n = int(input())
    return [Query(input().split()) for i in range(n)]

def write_responses(result):
    print('\n'.join(result))

def process_queries(queries):
    result = []
    
    contacts = phone_book()
    for cur_query in queries:
        if cur_query.type == 'add':
        
            contacts.add(cur_query.number, cur_query.name)
        elif cur_query.type == 'del':
            
            contacts.delete(cur_query.number)
        else:
            
            result.append(contacts.find(cur_query.number))
    return result

if __name__ == '__main__':
    write_responses(process_queries(read_queries()))
