import uvicorn


if __name__ == '__main__':
    uvicorn.run('Api.Api:app', host='localhost', port=78)
