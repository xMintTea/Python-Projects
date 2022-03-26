import requests, json,os
from rich.console import Console

console = Console()

def USD(ping):
    data = ping.json()
    current = data.get("Valute").get("USD").get("Value")
    prev = data.get("Valute").get("USD").get("Previous")
    if prev < current:
        console.print(f"$USD: [bold green]{prev}[/bold green] => [bold red]{current}[/bold red]")

    elif prev > current:
        console.print(f"$USD: [bold red]{prev}[/bold red] => [bold green]{current}[/bold green]")

    else:
        console.print(f"$USD: [bold yellow]{prev}[/bold yellow] => [bold yellow]{current}[/bold yellow]")


def EUR(ping):
    data = ping.json()
    current = data.get("Valute").get("EUR").get("Value")
    prev = data.get("Valute").get("EUR").get("Previous")
    if prev < current:
        console.print(f"€EUR: [bold green]{prev}[/bold green] => [bold red]{current}[/bold red]")

    elif prev > current:
        console.print(f"€EUR: [bold red]{prev}[/bold red] => [bold green]{current}[/bold green]")

    else:
        console.print(f"€EUR: [bold yellow]{prev}[/bold yellow] => [bold yellow]{current}[/bold yellow]")

def KZT(ping):
    data = ping.json()
    current = data.get("Valute").get("KZT").get("Value")
    prev = data.get("Valute").get("KZT").get("Previous")
    if prev < current:
        console.print(f"₸KZT: [bold green]{prev}[/bold green] => [bold red]{current}[/bold red]")

    elif prev > current:
        console.print(f"₸KZT: [bold red]{prev}[/bold red] => [bold green]{current}[/bold green]")

    else:
        console.print(f"₸KZT: [bold yellow]{prev}[/bold yellow] => [bold yellow]{current}[/bold yellow]")

def GBP(ping):
    data = ping.json()
    current = data.get("Valute").get("GBP").get("Value")
    prev = data.get("Valute").get("GBP").get("Previous")
    if prev < current:
        console.print(f"£GBP: [bold green]{prev}[/bold green] => [bold red]{current}[/bold red]")

    elif prev > current:
        console.print(f"£GBP: [bold red]{prev}[/bold red] => [bold green]{current}[/bold green]")

    else:
        console.print(f"£GBP: [bold yellow]{prev}[/bold yellow] => [bold yellow]{current}[/bold yellow]")

def UAH(ping):
    data = ping.json()
    current = data.get("Valute").get("UAH").get("Value")
    prev = data.get("Valute").get("UAH").get("Previous")
    if prev < current:
        console.print(f"₴UAH: [bold green]{prev}[/bold green] => [bold red]{current}[/bold red]")

    elif prev > current:
        console.print(f"₴UAH: [bold red]{prev}[/bold red] => [bold green]{current}[/bold green]")

    else:
        console.print(f"₴UAH: [bold yellow]{prev}[/bold yellow] => [bold yellow]{current}[/bold yellow]")



while 1:
    link = "https://www.cbr-xml-daily.ru/daily_json.js"
    ping = requests.get(link)
    if ping.status_code == 200:
        USD(ping)
        EUR(ping)
        KZT(ping)
        GBP(ping)
        UAH(ping)
    input("Нажмите Enter, чтобы продолжить...")
    os.system("cls")