def get_function(seq):
    m = seq[0]
    n = seq[1] - m
    if any(s != n*x+m for x, s in enumerate(seq)):
        return "Non-linear sequence"
    return "f(x) = {}{}{}{}{}{}".format(
        "-"         * (n < 0),
        str(abs(n)) * (abs(n) > 1),
        "x"         * (n != 0),
        " + "       * (m > 0 and n != 0),
        " - "       * (m < 0),
        str(abs(m)) * (m != 0 or n == 0)
    )

# Calculate the function f(x) for a simple linear sequence (Easy)
# [1,4,7,10,13]