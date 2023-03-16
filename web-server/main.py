import store 
from fastapi import FastApi

app = FastApi()

@app.get('/')
def get_list():
    return [1,2,3]

@app.get('/contact')
def get_list():
    return {'name': 'Platzi'}


def run():
    store.get_categories()

if __name__ == '__main__':
    run()   