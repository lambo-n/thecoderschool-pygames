def formatNumber(number):
    suffixes = ["", "K", "M", "B", "T", "Qa", "Qi"]
    index = 0
    # bump up to the next suffix every time we pass 1000
    while number >= 1000 and index < len(suffixes) - 1:
        number /= 1000
        index += 1
    if index == 0:
        # small numbers stay as whole numbers
        return f"{int(number)}"
    # show one decimal place, e.g. 1.5K
    return f"{number:.1f}{suffixes[index]}"