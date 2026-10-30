from pydantic import BaseModel, HttpUrl
from fastapi import FastAPI, Request
from fastapi.responses import RedirectResponse
from hashing import URLHash

class URL(BaseModel):
    url: HttpUrl

url_hash = URLHash()
app = FastAPI()

@app.post("/shorten")
def shorten_a_url(request: Request,url: URL = None):
    print(url)
    url = url.url
    encode = url_hash.generate_hash(str(url))
    output = {"key":encode,"long_url": url,"short_url": f'{str(request.base_url)}{encode}'}
    return output

@app.get("/{hsh}")
def redirect_url(hsh:str):
    url = url_hash.get_url_from_hash(hsh)
    if url:
        return RedirectResponse(url)
    return "not a valid URL."

@app.delete("/{hsh}")
def remove_mapping(hsh:str):
    url_hash.remove_hash_db_cache(hsh)
    return "mapping removed."

