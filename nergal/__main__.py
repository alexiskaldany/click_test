import click
import yfinance as yf
import pandas as pd
import time
from datetime import date 

# @click.group()
# def single():
#     ticker = ticker()
#     start = start()
#     end = end()
#     save_path = save_path()
#     pd.DataFrame(yahoo_finance.get_data_yahoo(ticker, interval='d', start=start, end=end)).to_csv(save_path)
#     pass

# @click.command()
# @click.option('-ticker', '--ticker', prompt='The stock ticker', help='Ticker of the stock')
# def ticker(ticker):
#     return ticker

# @click.command()
# @click.option('-start', '--start_date', prompt='Start date', help='Start date')
# def start(start_date):
#     return start_date
# @click.command()
# @click.option('-end', '--end_date', prompt='End date', help='End date')
# def end(end_date):
#     return end_date

# @click.command()
# @click.option('-path', '--save_path', type=click.Path(exists=False),prompt='Output file', help='Output file')
# def path(save_path):
#     return save_path

# single.add_command(ticker)
# single.add_command(start)
# single.add_command(end)
# single.add_command(path)
@click.command()
@click.option('-ticker', '--ticker', prompt='The stock ticker', help='Ticker of the stock')
def single(ticker):
    path = "./nergal/test.csv"
    yf.download(ticker, start="2000-01-01", end=date.isoformat(date.today())).to_csv(path)
    click.echo('Saved data to {}'.format(path))
    
# def main(ticker,start_date, end_date ,save_path):
#     """
#     Simple CLI application to save a yahoo-finance csv to the desired save path
#     """

#     dataframe = pd.DataFrame(yahoo_finance.get_data_yahoo(ticker, interval='d', start=start_date, end=end_date))
#     dataframe.to_csv(save_path)
#     return


