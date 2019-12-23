#!/usr/bin/python3
import requests
import click
import json
import redis

@click.group()
@click.pass_context
@click.argument('host')
@click.argument('port')
@click.option('-p', '--port', default=6379)
def main(ctx, host, port):
  ctx.obj = redis.Redis(host=host, port=port, db=0)

  
@main.command()
@click.pass_obj
def databases(r):
  info = r.info()
  databases = []
  for key, value in info.items() :
    if key.startswith("db"):
      databases.append({ "name": key, "values": value })
  print(json.dumps(databases))

if __name__ == "__main__":
  main()