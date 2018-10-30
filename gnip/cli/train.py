import click
from gnip.models import architecture
from gnip.models.dataset import get_data_from_type
from gnip.models.store import load_model


@click.command('train')
@click.argument('type', type=int)
def train(type):
    df = get_data_from_type(type)
    model_name = str(type) + '.pkl'

    score = architecture.compile(df, ['X'], ['y'], model_name)

    click.echo(score)


@click.command('test')
@click.argument('filename')
@click.option('--xx', '-x', type=float)
@click.option('--yy', '-y', type=float)
def test(filename, xx, yy):
    model = load_model(filename)
    y_hat = model.predict([[xx]])

    click.echo(yy)

    click.echo(y_hat[0][0])


@click.group()
def cli():
    pass


cli.add_command(train)
cli.add_command(test)
