from langserve import RemoteRunnable

remote_chain = RemoteRunnable("http://localhost:8000/chain/")
result = remote_chain.invoke({"language": "roadman english", "text": "hello my dear friend i've known since I was very young"})
print(result)
