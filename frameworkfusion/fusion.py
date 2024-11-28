import typer
import pandas as pd
from opencre_lib.compare import Map
from rich.console import Console
from rich.markdown import Markdown
from rich.table import Table

console = Console()
app = typer.Typer(help="FrameworkFusion")
bases = Map(primary="CWE", secundary="ASVS").bases

def print_bases():
    num = 0
    table = Table(title="Base Standards")

    table.add_column("ID Argument", justify="right", style="cyan", no_wrap=True)
    table.add_column("Name Base", style="magenta")
    for base in bases:
        table.add_row(str(num), base)
        num += 1
    console.print(table)

@app.command()
def example():
    text = """```shell
    framework-fusion --primary 2 --secundary 4
    """
    md = Markdown(text)
    console.print(md)
    console.print("[bold green][+] [white]This command will do correlation between CWE and controls of ISO 27001\n\n")
    print_bases()

@app.command()
def compare(primary: int = typer.Option(help="Primary framework to compare, based in table EXAMPLE"), secundary: int = typer.Option(help="Secundary framework to compare, based in table EXAMPLE"), output: str = typer.Option(help="Output file name format XLSX.", default="output.xlsx")):
    map = Map(primary=bases[primary], secundary=bases[secundary]).generate_table()
    table = Table(title=f"Compare Between {bases[primary]} and {bases[secundary]}")
    table.add_column("Score", justify="right", style="cyan", no_wrap=True)
    table.add_column("Base", style="magenta")
    table.add_column("Standard that Match", style="magenta")
    for item in map:
        table.add_row(str(item.get('score_relationship')), item.get('base'), item.get('standard_match'))
    
    console.print(table)
    if output != "output.xlsx":
        pd.DataFrame(map).to_excel(output, sheet_name="COMPARE", index=False)
        console.print(f'[green bold][+] [white]Output file created: [blink]{output}')
        

if __name__ == "__main__":
    app()

# @app.command()
# def cli(primary: str)