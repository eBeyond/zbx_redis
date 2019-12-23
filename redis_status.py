#!/usr/bin/python3
import requests
import click
import json
import redis

@click.group()
@click.pass_context
@click.argument('host')
@click.option('-p', '--port', default=6379)
def main(ctx, host, port):
  ctx.obj = redis.Redis(host=host, port=port, db=0)

  
@main.command()
@click.pass_obj
@click.argument('database')
@click.argument('metric')
def database(db, database, metric):
  info = db.info()
  for key, value in info.items() :
    if key == database:
      for subkey, subvalue in value.items():
        if subkey == metric:
          print(subvalue)


if __name__ == "__main__":
  main()