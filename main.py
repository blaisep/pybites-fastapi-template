def generate_xmas_tree(rows=10):
    """Generate a xmas tree of stars (*) for given rows (default 10).
       Each row has row_number*2-1 stars, simple example: for rows=3 the
       output would be like this (ignore docstring's indentation):
         *
        ***
       *****"""
    star = "*"
    max_width = rows*2 - 1
    star_list = []
    for i in range(1, rows + 1):
        num_stars = i * 2 - 1
        star_list.append(f"{num_stars * star:^{max_width}}")
    return "\n".join(star_list)

