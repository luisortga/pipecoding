from rich.table import Table
from rich.console import Console
# orteg

class Style:

    def __init__(self):
        pass

    def __view__(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p,q,r):
        """
        funcion para crear la tabla y el diseño
        """

        table = Table()
        table.add_column("[yellow]Information👽")
        table.add_column("Answer🧪")

        table.add_row(a, b)
        table.add_row(c, d)
        table.add_row(e, f)
        table.add_row(g, h)
        table.add_row(i, j)
        table.add_row(k, l)
        table.add_row(m, n)
        table.add_row(o, p)
        table.add_row(q, r)


        console = Console()
        console.print(table)

    def view_less(self,a,b,c,d,e,f,g,h,i,j,k,l,m,n,o,p):
        """
        funcion para crear la tabla y el diseño
        """

        table = Table()
        table.add_column("[yellow]Information👽")
        table.add_column("Answer🧪")

        table.add_row(a, b)
        table.add_row(c, d)
        table.add_row(e, f)
        table.add_row(g, h)
        table.add_row(i, j)
        table.add_row(k, l)
        table.add_row(m, n)
        table.add_row(o, p)


        console = Console()
        console.print(table)

    def view_error(self, alfa, e= "Excepcion: "):
        """
        funcion para crear la tabla y diseño si esta en blanco el texto
        """

        table = Table()
        table.add_column("[yellow]Information👽")
        table.add_column("Answer🧪")

        table.add_row(e, alfa)
        console = Console()
        console.print(table)
