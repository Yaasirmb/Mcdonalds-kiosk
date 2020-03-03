from tabulate import tabulate

menu_items = [
    ["Menu Items","Price"],
    ['Bacon BBQ Burger'.title(), 3.19],
    ['Double Bacon BBQ Burger'.title(), 4.50],
    ['big mac'.title(), 3.99],
    ['quarter pounder with cheese'.title(), 3.79],
    ['quarter pounder with cheese delux'.title(), 5],
    ['double_quarter_pounder_with_cheese'.title(), 4.25],
    ['quarter pounder with cheese bacon'.title(), 4.25],
    ['double cheeseburger'.title(), 1.69],
    ['McDouble', 1.39],
    ['Cheeseburger', 1],
    ['hamburger'.title(), 1],
    ['10 Piece Mcnuggets'.title(), 4.49],
    ['20 Piece Mcnuggets'.title(), 5],
    ['40 Piece Mcnuggets'.title(), 8.99],
    ['buttermilk crispy tenders'.title(), 4],
    ['artisan grilled chicken sandwich'.title(), 4.39],
    ['buttermilk crispy chicken sandwich'.title(), 4.39],
    ['mcchicen'.title(), 1],
    ['filet o fish'.title(), 3.79],
    ['Bacon Ranch Salad with Buttermilk Crispy Chicken'.title(), 4.59],
    ['Bacon_Ranch_Grilled_Chicken_Salad'.title(), 4.59],
    ['Southwest_Buttermilk_Crispy_Chicken_Salad'.title(), 4.79],
    ['Southwest_Grilled_Chicken_Salad'.title(), 4.79],
    ['donut sticks'.title(), 2.49],
    ['small fries'.title(), 1],
    ['medium fries'.title(), 1.50],
    ['large fries'.title(), 2],
    ['apple slices'.title(), 1],
    ['Go Gurt'.title(), 1],
    ['side salad'.title(), 1.59],
    ['yogurt_parfait'.title(), 1],
    ['vanilla cone'.title(), 1],
    ['hot fudge sundae'.title(), 1.29],
    ['M&m Mcflurry'.title(), 2.39],
    ['Kids Cone'.title(), 1],
    ['hot caramel sundae'.title(), 1.29],
    ['strawberry sundae'.title(), 1.29],
    ['oreo mcflurry'.title(), 2.39],
    ['Apple Pie', .70],
    ['Cookie', 1]
]


drinks = [
    ['coke'.title(),1.23],
    ['water'.title(), 0],
    ['sprite'.title(), 1.38],
    ['dr pepper'.title(), 1.31],
    ['hi c'.title(), 1.3],
    ['diet coke'.title(),1.21],
    ['diet dr pepper'.title(),1.53],
    ['strawberry shake'.title(), 2.19],
    ['sweet peach slushie'.title(), 1.25],
    [' fruit punch slushie'.title(), 1.25],
    ['blue rasberry slushi'.title(), 1.25],
    ['SnickerDoodle mcflurry'.title(), 2.09],
    ['chocolate shake'.title(), 2.19],
    ['vanilla shake'.title(), 2.19]
]


display = (tabulate(menu_items,headers = "firstrow" ))

logo = """
                  | |                 | |   | |
 _ __ ___   ___ __| | ___  _ __   __ _| | __| |
| '_ ` _ \ / __/ _` |/ _ \| '_ \ / _` | |/ _` |
| | | | | | (_| (_| | (_) | | | | (_| | | (_| |
|_| |_| |_|\___\__,_|\___/|_| |_|\__,_|_|\__,_|
                                               """

print(logo + '\n' + "Hello welcome to McDonalds, here are our menu choices: \n" + display)