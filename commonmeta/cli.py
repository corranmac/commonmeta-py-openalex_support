import click
import pydash as py_

from commonmeta import Metadata # __version__
from commonmeta.api_utils import update_ghost_post_via_api
from commonmeta.doi_utils import validate_prefix
from commonmeta.utils import encode_doi, decode_doi
from commonmeta.readers.json_feed_reader import (
    get_json_feed_unregistered,
    get_json_feed_updated,
    get_json_feed_item_uuid,
)


@click.group()
@click.option("--show-errors", default=False)
def cli(show_errors):
    if show_errors:
        click.echo("Show errors mode is on")


@cli.command()
@click.argument("input", type=str, required=True)
@click.option("--via", "-f", type=str, default=None)
@click.option("--to", "-t", type=str, default="commonmeta")
@click.option("--style", "-s", type=str, default="apa")
@click.option("--locale", "-l", type=str, default="en-US")
@click.option("--doi", type=str)
@click.option("--depositor", type=str)
@click.option("--email", type=str)
@click.option("--registrant", type=str)
def convert(input, via, to, style, locale, doi, depositor, email, registrant):
    metadata = Metadata(
        input,
        via=via,
        style=style,
        locale=locale,
        doi=doi,
        depositor=depositor,
        email=email,
        registrant=registrant,
    )
    output = metadata.write(to=to)
    click.echo(output)


@cli.command()
@click.argument("prefix", type=str, required=True)
def encode(prefix):
    if validate_prefix(prefix) is None:
        return None
    output = encode_doi(prefix)
    click.echo(output)


@cli.command()
@click.argument("doi", type=str, required=True)
def decode(doi):
    output = decode_doi(doi)
    click.echo(output)


@cli.command()
@click.argument("slug", type=str, required=True)
def encode_by_slug(slug):
    if validate_prefix(prefix) is None:
        return None
    output = encode_doi(prefix)
    click.echo(output)


@cli.command()
@click.argument("filter", type=str, required=True, default="unregistered")
@click.option("--id", type=str)
def json_feed(filter, id=None):
    if filter == "unregistered":
        output = get_json_feed_unregistered()
    elif filter == "updated":
        output = get_json_feed_updated()
    elif filter == "blog_slug" and id is not None:
        post = get_json_feed_item_uuid(id)
        output = py_.get(post, "blog.slug", "no slug found")
    else:
        output = "no filter specified"
    click.echo(output)


@cli.command()
@click.argument("id", type=str, required=True)
@click.option("--api-key", "-k", type=str, required=True)
@click.option("--api-url", "-u", type=str, required=True)
def update_ghost_post(id, api_key, api_url):
    output = update_ghost_post_via_api(id, api_key, api_url)
    click.echo(output)


if __name__ == "__main__":
    cli()
