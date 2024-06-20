def print_to_table(data, symbol, interval):
    currentPrice = data.get("currentPrice")
    levels = data.get("levels")
    table_string = f"Fibonacci levels for {symbol} {interval}\n"
    table_string += f"Current Price: {currentPrice:.2f}\n"  # Format the current price to two decimal places
    table_string += "```\n"  # Start of code block
    table_string += "| Level    | Value           |\n"
    table_string += "|----------|-----------------|\n"
    for level, value in levels.items():
        formatted_value = f"{value:.8f}" if value < 1 else f"{value:,.2f}"  # Format small numbers with 8 decimal places, larger numbers with commas
        table_string += f"| {level:>8} | {formatted_value:>15} |\n"  # Right-align the text in the columns
    table_string += "```"  # End of code block
    return table_string